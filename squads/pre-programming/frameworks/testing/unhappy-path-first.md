# Unhappy Path First

## Título e Propósito

O **Unhappy Path First** é um framework que prioriza o design e teste de cenários de erro, falha e exceção antes dos cenários de sucesso. O propósito é combater o viés natural de projetar para o caso feliz e tratar erros como exceção — quando, em produção, o unhappy path é frequentemente o caminho mais percorrido e o menos preparado.

## Quando Usar

- No design de fluxos que envolvem entrada de dados do usuário
- Ao projetar integrações com sistemas externos
- Em features que envolvem transações financeiras ou dados críticos
- Quando bugs em produção são majoritariamente em cenários de erro
- Durante definição de critérios de aceite e planos de teste

## Conceitos-Chave

1. **Happy Path**: O fluxo onde tudo dá certo — inputs válidos, serviços disponíveis, dados consistentes.
2. **Unhappy Path**: Tudo que pode dar errado — inputs inválidos, timeouts, dados corrompidos, concorrência, permissões insuficientes.
3. **Viés do Happy Path**: A tendência de projetar, implementar e testar o caso feliz primeiro e tratar erros como detalhe posterior.
4. **Erro Gracioso**: O sistema falha de forma controlada, comunicando claramente ao usuário o que aconteceu e o que fazer.
5. **Cenário de Recuperação**: O que o sistema faz após um erro para voltar a um estado consistente.

## Processo / Passos

### Passo 1 — Descrever o Happy Path
Primeiro, entenda o fluxo de sucesso. Não pule — é a referência para identificar desvios.

### Passo 2 — Listar Tudo que Pode Dar Errado
Para cada passo do happy path, pergunte: "O que pode falhar aqui?" Categorize: input inválido, falha de dependência, estado inconsistente, concorrência, timeout, permissão.

### Passo 3 — Priorizar Unhappy Paths
Classifique por: probabilidade × impacto. Trate primeiro os mais prováveis e mais impactantes.

### Passo 4 — Projetar Tratamento de Cada Unhappy Path
Para cada cenário, defina: o que o usuário vê? O que o sistema faz internamente? Como recuperar?

### Passo 5 — Definir Testes para Unhappy Paths Primeiro
Escreva os testes de cenários de erro antes dos testes de sucesso. Se o unhappy path está coberto, o happy path geralmente é mais fácil.

### Passo 6 — Implementar Tratamento de Erros Junto (Não Depois)
O tratamento de erros é parte da feature, não adição posterior. Implemente junto com a lógica principal.

### Passo 7 — Revisar Mensagens de Erro
Cada mensagem de erro deve: explicar o que aconteceu, sugerir o que fazer, não expor detalhes internos.

## Perguntas de Ativação

- "O que acontece se o usuário clicar Submit duas vezes rapidamente?"
- "E se a API externa retornar erro? E se demorar 30 segundos? E se retornar dados errados?"
- "Se dois usuários tentarem a mesma ação simultaneamente, o que acontece?"
- "O que o usuário vê quando dá erro? É útil ou críptico?"
- "Se o banco estiver fora do ar, o que acontece com os dados que o usuário acabou de enviar?"
- "Dos últimos 20 bugs em produção, quantos eram no happy path vs. unhappy path?"

## Output Esperado

```
FEATURE: Checkout e Pagamento

HAPPY PATH: Usuário seleciona itens → informa dados → confirma → pagamento aprovado → pedido criado

UNHAPPY PATHS (priorizados):

1. [ALTA PROB × ALTO IMPACTO] Pagamento recusado pela operadora
   - Usuário vê: "Pagamento não aprovado. Verifique os dados do cartão ou tente outro meio."
   - Sistema: Log do motivo, não salva dados do cartão, permite retry
   - Recuperação: Usuário tenta novamente ou escolhe outro meio
   - Teste: DADO cartão com saldo insuficiente QUANDO confirmo ENTÃO vejo mensagem + posso tentar novamente

2. [MÉDIA PROB × ALTO IMPACTO] Timeout na gateway de pagamento
   - Usuário vê: "Estamos processando seu pagamento. Você receberá confirmação por email."
   - Sistema: Marca pedido como "processando", inicia polling/webhook para verificar
   - Recuperação: Webhook confirma ou timeout + conciliação manual
   - Teste: DADO timeout de 30s na gateway QUANDO confirmo ENTÃO vejo mensagem de processamento

3. [BAIXA PROB × CRÍTICO IMPACTO] Cobrança dupla por double-submit
   - Usuário vê: Botão desabilitado após primeiro clique
   - Sistema: Idempotency key por pedido, rejeita duplicata
   - Recuperação: Se cobrou duas vezes, estorno automático
   - Teste: DADO dois clicks em < 1s QUANDO confirmo ENTÃO apenas uma cobrança

4. [ALTA PROB × MÉDIO IMPACTO] CEP inválido
   - Usuário vê: "CEP não encontrado. Verifique o número digitado."
   - Sistema: Validação em tempo real, fallback para segunda API de CEP
   - Recuperação: Usuário corrige ou preenche endereço manualmente
   - Teste: DADO CEP "00000-000" QUANDO preencho ENTÃO vejo mensagem de erro
```

## Armadilhas Comuns

1. **"Depois tratamos os erros"**: Erros tratados depois são tratados mal ou esquecidos completamente.
2. **Mensagens genéricas**: "Ocorreu um erro" não ajuda ninguém. Mensagens devem ser específicas e orientar ação.
3. **Erros que expõem internos**: Stack traces, IDs de transação interna ou SQL no frontend — risco de segurança.
4. **Apenas validação client-side**: Validar no frontend e confiar. Toda validação deve existir no backend.
5. **Não considerar concorrência**: "Funciona quando testo sozinho" mas falha com 10 usuários simultâneos.
6. **Recovery não testado**: O sistema tem código de recuperação de erros que nunca foi exercitado.
