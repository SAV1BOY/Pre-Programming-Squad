# Meadows: Pontos de Alavancagem em Sistemas

## Título e Propósito

Framework baseado no trabalho de **Donella Meadows** (*Thinking in Systems*, "Leverage Points: Places to Intervene in a System"). A tese central: **em sistemas complexos, há pontos onde uma pequena mudança produz grande impacto — e a maioria das pessoas intervém nos pontos errados**. O propósito é identificar onde intervir no sistema para obter máximo resultado com mínimo esforço.

## Quando Usar

- Quando o sistema tem problemas recorrentes que "correções" não resolvem
- Ao priorizar onde investir esforço de engenharia para máximo impacto
- Em análise de causa raiz de problemas sistêmicos
- Quando mudanças técnicas não produzem os resultados esperados
- Para entender por que certas melhorias têm impacto desproporcional

## Conceitos-Chave

1. **Ponto de Alavancagem**: Local no sistema onde uma mudança pequena produz efeito grande. Meadows lista 12, do menos ao mais poderoso.
2. **Feedback Loops**: Loops de reforço (amplificam) e balanceamento (estabilizam). Mudar a estrutura dos loops é mais poderoso que mudar parâmetros.
3. **Stocks e Flows**: O estado do sistema (stock) e o que o muda (flow). Buffer é stock. Processing rate é flow.
4. **Regras do Sistema**: Quem define as regras tem mais poder que quem opera dentro delas. Mudar regras é intervenção de alta alavancagem.
5. **Paradigma**: O mindset que gera as regras. Mudar o paradigma é o ponto de alavancagem mais poderoso — e mais difícil.

## Processo / Passos

### Passo 1 — Mapear o Sistema
Identifique: stocks (estados, filas, caches), flows (processos, taxa de mudança), feedback loops (métricas que influenciam ações).

### Passo 2 — Identificar Onde a Equipe Intervém Hoje
Quais mudanças a equipe faz tipicamente? Parâmetros (configs, thresholds)? Buffers (cache, filas)? Regras (lógica de negócio)?

### Passo 3 — Subir na Escada de Alavancagem
Pergunte: "Estamos mudando parâmetros quando deveríamos mudar estrutura? Estamos otimizando fluxos quando deveríamos mudar feedback loops?"

### Passo 4 — Identificar os Pontos de Maior Alavancagem
Onde uma mudança pequena teria efeito desproporcional? Exemplos: mudar como métricas são definidas, como feedback chega à equipe, como decisões são tomadas.

### Passo 5 — Intervir no Ponto Certo
Foque esforço nos pontos de alta alavancagem em vez de distribuir uniformemente.

## Perguntas de Ativação

- "Estamos tratando sintomas (parâmetros) ou causas estruturais (feedback loops, regras)?"
- "Se pudéssemos mudar apenas uma coisa no sistema, o que teria mais impacto?"
- "Quais feedback loops estão amplificando problemas?"
- "As regras do sistema incentivam o comportamento que queremos?"
- "Estamos intervindo onde é fácil ou onde é eficaz?"

## Output Esperado

Mapa do sistema com stocks, flows e feedback loops; pontos de alavancagem identificados e ranqueados; recomendação de onde intervir para máximo impacto.

## Armadilhas Comuns

1. **Intervir nos parâmetros**: Ajustar números (timeouts, thresholds) quando a estrutura é o problema.
2. **Ignorar feedback loops**: Não perceber que uma métrica (ex: "velocity") cria incentivo perverso (inflar story points).
3. **Alavancagem reversa**: Intervir no ponto certo mas na direção errada. Exemplo: adicionar mais processo para resolver problema causado por excesso de processo.
4. **Resistência do sistema**: Sistemas complexos resistem a mudanças. Intervenções de alta alavancagem encontram mais resistência.
5. **Foco no técnico**: Às vezes o ponto de alavancagem é organizacional (como equipes se comunicam), não técnico.
