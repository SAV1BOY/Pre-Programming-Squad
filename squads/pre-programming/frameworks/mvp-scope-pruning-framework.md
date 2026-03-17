# MVP Scope Pruning Framework

## Título e Propósito

O **MVP Scope Pruning Framework** é um sistema disciplinado para podar o escopo de um projeto até o mínimo viável que entrega valor real. O propósito é combater a tendência natural de equipes de adicionar "só mais uma coisinha" até que o MVP se torne um produto completo disfarçado — eliminando a vantagem de velocidade e aprendizado que o MVP deveria proporcionar.

## Quando Usar

- Quando o escopo do MVP está crescendo além do razoável
- No planejamento inicial de qualquer produto ou feature nova
- Quando a equipe não consegue concordar sobre o que é "mínimo" e o que é "viável"
- Quando stakeholders continuam adicionando requisitos "essenciais"
- Antes de estimar prazo e esforço — escopar primeiro, estimar depois

## Conceitos-Chave

1. **Mínimo**: O menor conjunto de funcionalidades. Menos que isso e não há produto.
2. **Viável**: Suficiente para entregar valor real a um usuário real. Menos que isso e não há aprendizado.
3. **Feature Essencial vs. Desejável**: Essencial = sem ela o MVP não faz sentido. Desejável = melhora a experiência mas não é necessária para validar a hipótese.
4. **Hipótese de Valor**: A aposta que o MVP está testando. Toda feature deve servir para testar essa hipótese ou não pertence ao MVP.
5. **Custo de Inclusão vs. Custo de Exclusão**: Incluir uma feature custa tempo. Excluir pode custar aprendizado. O trade-off precisa ser explícito.

## Processo / Passos

### Passo 1 — Declarar a Hipótese de Valor
Escreva em uma frase: "Acreditamos que [público] vai [ação] porque [razão], e saberemos que funcionou quando [métrica]."

### Passo 2 — Listar Todas as Features Propostas
Colete tudo que foi sugerido, sem filtro. Registre quem sugeriu e a justificativa.

### Passo 3 — Aplicar o Teste da Hipótese
Para cada feature, pergunte: "Essa feature é necessária para testar nossa hipótese de valor?" Se não, mova para a lista "Depois do MVP".

### Passo 4 — Aplicar o Teste de Viabilidade
Para as features restantes, pergunte: "Sem essa feature, o produto ainda entrega valor mínimo?" Se sim, ela é desejável, não essencial.

### Passo 5 — Aplicar o Teste de Custo
Para cada feature essencial, estime o custo relativo. Se uma feature essencial custa mais que 30% do esforço total do MVP, questione se há uma versão simplificada.

### Passo 6 — Poda Final
Revise a lista final e aplique a regra: "Se tivermos dúvida, cortamos." Dúvida sobre se é essencial = não é essencial.

### Passo 7 — Criar a Lista "Depois do MVP"
Todas as features removidas vão para uma lista priorizada para iterações futuras. Nada se perde — apenas se sequencia.

## Perguntas de Ativação

- "Se tivéssemos apenas 2 semanas, o que construiríamos?"
- "Essa feature testa nossa hipótese ou é 'nice to have'?"
- "Um usuário real usaria o produto sem essa feature?"
- "Qual é a versão mais simples possível dessa feature que ainda entrega valor?"
- "Estamos adicionando isso por medo ou por evidência?"
- "Se cortarmos isso, o que de pior acontece?"

## Output Esperado

```
Hipótese de Valor: [declaração]

FEATURES DO MVP (Essenciais):
1. [Feature] — Justificativa: [por que é essencial para a hipótese]
2. [Feature] — Justificativa: [...]

DEPOIS DO MVP (Desejáveis):
1. [Feature] — Prioridade: Alta/Média/Baixa — Justificativa para exclusão: [...]
2. [Feature] — Prioridade: [...]

DESCARTADAS:
1. [Feature] — Razão: [não serve à hipótese / custo desproporcional / ...]

Custo estimado do MVP podado: [X semanas com Y pessoas]
```

## Armadilhas Comuns

1. **MVP que não é mínimo**: Incluir tudo "essencial" segundo cada stakeholder resulta em um projeto de 6 meses chamado de MVP.
2. **MVP que não é viável**: Cortar demais e entregar algo que ninguém consegue usar ou que não testa a hipótese.
3. **Ausência de hipótese**: Sem hipótese de valor clara, não há critério para decidir o que fica e o que sai.
4. **Poda emocional**: Manter features por apego ou por medo de decepcionar stakeholders, não por lógica.
5. **"Só mais uma feature"**: A adição incremental que parece pequena mas que, acumulada, dobra o escopo.
6. **Não criar a lista "Depois"**: Sem ela, stakeholders sentem que suas features foram ignoradas, não priorizadas.
