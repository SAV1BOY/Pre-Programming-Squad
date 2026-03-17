# Go/No-Go Decision Framework

## Título e Propósito

O **Go/No-Go Decision Framework** é um sistema estruturado para tomar a decisão binária de prosseguir ou não com um projeto, deploy, lançamento ou migração. O propósito é transformar uma decisão frequentemente política ou emocional em uma avaliação baseada em critérios pré-definidos, com responsabilidades claras e documentação do racional.

## Quando Usar

- Antes de iniciar implementação de um projeto aprovado
- Antes de deploys em produção de mudanças de alto impacto
- Em gates de lançamento de produto
- Antes de migrações de dados ou infraestrutura
- Quando há dúvida se é seguro prosseguir

## Conceitos-Chave

1. **Critério Go**: Condição que deve ser verdadeira para prosseguir. Definida antes da avaliação.
2. **Critério No-Go**: Condição que, se verdadeira, impede prosseguir independente de outros fatores.
3. **Critério Condicional**: Condição que permite prosseguir com ressalvas ou mitigações adicionais.
4. **Decisor**: Pessoa com autoridade para tomar a decisão final. Deve ser definida antes da reunião.
5. **Registro de Decisão**: Documentação do resultado, critérios avaliados, riscos aceitos e responsável pela decisão.

## Processo / Passos

### Passo 1 — Definir Critérios Antecipadamente
Antes de qualquer avaliação, defina: quais critérios Go são obrigatórios? Quais critérios No-Go são eliminatórios? Quais são condicionais?

### Passo 2 — Definir o Decisor
Quem tem autoridade final? Essa pessoa deve estar presente na avaliação e assumir responsabilidade pela decisão.

### Passo 3 — Coletar Evidências
Para cada critério, colete dados que comprovem o estado atual. Evidência > opinião.

### Passo 4 — Avaliar Cada Critério
Para cada critério, marque: **Atendido**, **Parcialmente Atendido**, **Não Atendido**. Parcial requer explicação.

### Passo 5 — Verificar No-Gos
Se qualquer critério No-Go está ativo, a decisão é No-Go. Não há negociação.

### Passo 6 — Avaliar Critérios Condicionais
Se há critérios parcialmente atendidos, defina mitigações específicas e verifique se são aceitáveis.

### Passo 7 — Tomar e Registrar a Decisão
O decisor declara Go, No-Go ou Go-Condicional. Registre: decisão, critérios, riscos aceitos, mitigações, data, responsável.

## Perguntas de Ativação

- "Todos os critérios Go estão atendidos com evidência?"
- "Há algum critério No-Go ativo que estamos tentando ignorar?"
- "Quem é responsável por essa decisão e está confortável em assumi-la?"
- "Se der errado, vamos poder dizer que tomamos uma decisão informada?"
- "Estamos prosseguindo porque é seguro ou porque o prazo está pressionando?"
- "Quais riscos estamos aceitando conscientemente?"

## Output Esperado

```
DECISÃO GO/NO-GO: [projeto/deploy/lançamento]
DATA: [data]
DECISOR: [nome e cargo]

CRITÉRIOS GO (obrigatórios):
[✓] Testes automatizados passando — Evidência: CI pipeline verde
[✓] Plano de rollback testado — Evidência: executado em staging ontem
[✗] Performance validada em carga — Evidência: teste de carga não executado

CRITÉRIOS NO-GO (eliminatórios):
[✗] Vulnerabilidade de segurança crítica aberta — Status: Nenhuma
[✗] Perda de dados possível sem rollback — Status: Rollback seguro

CRITÉRIOS CONDICIONAIS:
[~] Documentação de operação — Status: 80% completa — Mitigação: completar até amanhã

DECISÃO: NO-GO
RAZÃO: Teste de carga não executado (critério Go obrigatório não atendido)
PRÓXIMOS PASSOS: Executar teste de carga, reagendar avaliação para [data]
```

## Armadilhas Comuns

1. **Critérios definidos depois da avaliação**: Definir critérios que justifiquem a decisão já tomada. Critérios devem ser definidos antes.
2. **Pressão para ignorar No-Gos**: "É só dessa vez" — critérios No-Go existem exatamente para momentos de pressão.
3. **Go por inércia**: "Já investimos tanto..." (sunk cost fallacy). O investimento passado não muda o risco presente.
4. **Decisor ausente**: Ninguém quer assumir a responsabilidade pela decisão. Sem decisor definido, a decisão é tomada por omissão.
5. **Avaliação sem evidência**: "Acho que os testes passam" não é evidência. Verifique antes da reunião.
6. **Registro ausente**: Decisão Go sem documentação. Quando der problema, ninguém lembra por que foi aprovado.
