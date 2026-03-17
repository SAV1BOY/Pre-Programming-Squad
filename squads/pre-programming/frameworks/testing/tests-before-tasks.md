# Tests Before Tasks

## Título e Propósito

O **Tests Before Tasks** é um framework que inverte a ordem tradicional: define os testes que provarão que o trabalho está completo antes de definir as tarefas de implementação. O propósito é garantir que cada tarefa tenha critérios de verificação objetivos desde o início — porque se você não sabe como vai testar, você não entendeu o que precisa construir.

## Quando Usar

- No refinamento de histórias de usuário e tarefas técnicas
- Quando critérios de aceite estão vagos ou ausentes
- Para alinhar entendimento entre devs, QA e produto sobre "pronto"
- Quando a equipe frequentemente entrega features que não passam na revisão
- Como prática padrão de pré-programação antes de iniciar qualquer implementação

## Conceitos-Chave

1. **Test-First Thinking**: Pensar em como verificar antes de pensar em como construir. O teste é a especificação executável.
2. **Critério de Aceite Verificável**: Condição objetiva que qualquer pessoa pode avaliar como verdadeira ou falsa. "Deve ser rápido" não é verificável. "Resposta em < 200ms (p95)" é.
3. **Prova de Completude**: Conjunto mínimo de testes que, se todos passarem, prova que o trabalho está completo.
4. **Cenário de Teste**: Combinação de precondição, ação e resultado esperado que verifica um aspecto do requisito.
5. **Coverage de Requisitos**: Todo requisito mapeado para pelo menos um teste. Todo teste justificado por um requisito.

## Processo / Passos

### Passo 1 — Ler o Requisito
Leia o requisito, história de usuário ou tarefa. Identifique o que está claro e o que é ambíguo.

### Passo 2 — Escrever os Testes de Aceite
Para cada comportamento esperado, escreva um teste no formato: "DADO [precondição], QUANDO [ação], ENTÃO [resultado esperado]."

### Passo 3 — Incluir Cenários Negativos
Não teste apenas o happy path. Inclua: dados inválidos, permissões insuficientes, concorrência, timeout, estado inconsistente.

### Passo 4 — Validar com Stakeholder
Apresente os testes ao PO/stakeholder: "Se todos esses testes passarem, o trabalho está completo?" Se não, há requisitos faltando.

### Passo 5 — Derivar Tarefas dos Testes
Agora sim, decomponha em tarefas de implementação. Cada tarefa deve contribuir para fazer pelo menos um teste passar.

### Passo 6 — Estimar com Base nos Testes
A complexidade real está nos testes que precisam passar, não na descrição da feature. Use os testes para informar a estimativa.

### Passo 7 — Implementar e Verificar
Implemente as tarefas. Use os testes definidos como checklist de completude.

## Perguntas de Ativação

- "Como vamos saber que isso está funcionando corretamente?"
- "Se eu te desse o sistema implementado, que teste faria para verificar?"
- "O que acontece quando o input é inválido? Nulo? Vazio? Enorme?"
- "Se esse teste passasse e todos os outros falhassem, diríamos que está completo?"
- "Quais cenários o QA vai testar que não listamos ainda?"
- "Se o PO olhasse esses testes, concordaria que cobrem o pedido?"

## Output Esperado

```
HISTÓRIA: Como usuário, quero filtrar produtos por faixa de preço para encontrar itens no meu orçamento.

TESTES DE ACEITE (definidos ANTES das tarefas):

Happy Path:
- DADO catálogo com produtos de R$10 a R$1000
  QUANDO filtro por R$50-R$200
  ENTÃO vejo apenas produtos com preço entre R$50 e R$200, ordenados por relevância

- DADO filtro de preço aplicado
  QUANDO removo o filtro
  ENTÃO vejo todos os produtos novamente

Cenários Negativos:
- DADO valor mínimo maior que máximo (min=200, max=50)
  QUANDO aplico o filtro
  ENTÃO vejo mensagem de erro "Valor mínimo deve ser menor que máximo"

- DADO nenhum produto na faixa de preço selecionada
  QUANDO aplico o filtro
  ENTÃO vejo mensagem "Nenhum produto encontrado nessa faixa de preço"

- DADO filtro com valor negativo
  QUANDO tento aplicar
  ENTÃO o campo não aceita valores negativos

Performance:
- DADO catálogo com 100.000 produtos
  QUANDO aplico filtro de preço
  ENTÃO resultado aparece em < 500ms

TAREFAS DERIVADAS (definidas DEPOIS dos testes):
1. Adicionar índice de preço na tabela de produtos
2. Implementar endpoint GET /produtos?preco_min=X&preco_max=Y
3. Implementar validação de input (min < max, valores positivos)
4. Implementar componente de UI com slider de preço
5. Implementar estado "nenhum resultado"
```

## Armadilhas Comuns

1. **Testes vagos**: "Deve funcionar corretamente" não é teste. Seja específico: input, ação, resultado esperado.
2. **Apenas happy path**: Ignorar cenários negativos e de borda é descobri-los em produção.
3. **Testes derivados da implementação**: Definir testes olhando para o código, não para os requisitos. Isso testa implementação, não comportamento.
4. **Excesso de testes**: Listar 50 cenários para uma feature simples paralisa. Foque nos que provam completude.
5. **Testes sem validação do stakeholder**: Definir testes que a engenharia acha relevantes mas que não cobrem o que o PO espera.
6. **Não atualizar quando requisitos mudam**: Requisito mudou mas os testes ficaram os mesmos. Sempre sincronize.
