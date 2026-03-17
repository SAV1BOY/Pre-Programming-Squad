# Architectural Option Comparison

## Título e Propósito

O **Architectural Option Comparison** é um framework para avaliar e comparar opções arquiteturais de forma estruturada e transparente. O propósito é substituir debates de opinião ("eu acho que microsserviços é melhor") por análise baseada em critérios explícitos, pesos justificados e trade-offs documentados.

## Quando Usar

- Quando há duas ou mais opções arquiteturais viáveis
- Em decisões que afetam a estrutura fundamental do sistema
- Quando a equipe está polarizada entre abordagens diferentes
- Antes de comprometer-se com padrões, tecnologias ou topologias
- Em revisões de arquitetura para avaliar alternativas ao design atual

## Conceitos-Chave

1. **Opção Arquitetural**: Uma abordagem distinta para resolver o problema. Deve ser genuinamente diferente, não variação cosmética.
2. **Critério de Avaliação**: Dimensão pela qual as opções são comparadas. Deve ser relevante, mensurável e independente.
3. **Peso do Critério**: A importância relativa de cada critério no contexto específico do projeto.
4. **Trade-off Explícito**: Para cada opção, o que se ganha e o que se perde. Não existe almoço grátis.
5. **Risco Residual**: Riscos que permanecem após a escolha e que precisam ser monitorados ou mitigados.

## Processo / Passos

### Passo 1 — Definir o Problema Arquitetural
Descreva o que precisa ser decidido em termos de capacidades, não de tecnologias. "Como vamos lidar com processamento assíncrono?" não "Kafka ou RabbitMQ?"

### Passo 2 — Gerar Opções Genuínas
Liste pelo menos 3 opções realmente diferentes. Inclua sempre a opção "não fazer nada / manter como está" como baseline.

### Passo 3 — Definir Critérios de Avaliação
Selecione critérios relevantes para o contexto. Exemplos: complexidade operacional, performance, escalabilidade, custo, curva de aprendizado, extensibilidade, maturidade, ecossistema.

### Passo 4 — Atribuir Pesos
Pondere cada critério de 1 (pouco importante) a 5 (crítico). Justifique os pesos com base no contexto do projeto.

### Passo 5 — Avaliar Cada Opção
Para cada opção × critério, atribua uma nota de 1 (ruim) a 5 (excelente) com justificativa breve.

### Passo 6 — Calcular e Comparar
Multiplique nota × peso para cada célula. Some por opção. O maior score não é automaticamente o vencedor — é o ponto de partida para discussão.

### Passo 7 — Analisar Trade-offs
Para a opção preferida, liste explicitamente o que se perde comparado às alternativas. A equipe aceita esses trade-offs?

### Passo 8 — Documentar a Decisão
Registre a escolha, os critérios, os trade-offs aceitos e as condições que justificariam revisitar a decisão.

## Perguntas de Ativação

- "Estamos comparando opções realmente diferentes ou variações da mesma ideia?"
- "Quais critérios são mais importantes para este projeto específico?"
- "O que perdemos com a opção que estamos preferindo?"
- "Há uma opção que ninguém mencionou porque parece simples demais?"
- "Estamos avaliando com dados ou com preferências pessoais?"
- "Sob que condições mudaríamos de ideia?"

## Output Esperado

| Critério | Peso | Opção A: Monolito Modular | Opção B: Microsserviços | Opção C: Serverless |
|---|---|---|---|---|
| Complexidade operacional | 5 | 4 (simples) = 20 | 2 (alta) = 10 | 3 (média) = 15 |
| Escalabilidade | 3 | 3 (vertical) = 9 | 5 (granular) = 15 | 5 (automática) = 15 |
| Custo inicial | 4 | 5 (baixo) = 20 | 2 (alto) = 8 | 4 (médio) = 16 |
| Curva de aprendizado | 3 | 4 (familiar) = 12 | 2 (complexa) = 6 | 3 (nova) = 9 |
| **Total** | | **61** | **39** | **55** |

**Decisão**: Opção A — Monolito Modular
**Trade-offs aceitos**: Escalabilidade limitada a vertical no curto prazo
**Condição de revisão**: Se atingirmos 10x o volume atual

## Armadilhas Comuns

1. **Opções falsas**: Apresentar uma opção claramente ruim para fazer a preferida parecer melhor.
2. **Critérios enviesados**: Escolher critérios que favorecem a opção que alguém já decidiu.
3. **Pesos uniformes**: Dar peso igual a tudo é o mesmo que não ponderar. Priorize.
4. **Notas sem justificativa**: "Dei 4 porque me parece bom" não é avaliação — é opinião sem fundamento.
5. **Análise como teatro**: Fazer a análise para justificar uma decisão já tomada em vez de para informar a decisão.
6. **Ignorar a opção "não fazer nada"**: Às vezes, a melhor decisão é manter o que já funciona.
