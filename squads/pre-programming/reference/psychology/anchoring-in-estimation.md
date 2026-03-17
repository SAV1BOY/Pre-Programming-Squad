# Ancoragem em Estimativas

## Vies/Efeito

**Ancoragem (Anchoring Bias):** A tendencia de depender excessivamente da primeira informacao recebida (a "ancora") ao tomar decisoes, mesmo quando a ancora e irrelevante ou arbitraria.

## Descricao

Demonstrado por Tversky e Kahneman (1974), o efeito de ancoragem mostra que numeros iniciais — mesmo completamente arbitrarios — influenciam estimativas subsequentes. Em um experimento classico, girar uma roleta antes de estimar a porcentagem de paises africanos na ONU influenciou significativamente as respostas, mesmo sendo completamente irrelevante.

## Como se Manifesta em Pre-Programacao

### Na Estimativa de Esforco
- **Ancora do stakeholder:** "Isso deve levar umas 2 semanas, ne?" — a equipe ajusta a partir de 2 semanas em vez de estimar independentemente.
- **Ancora do projeto anterior:** "O ultimo projeto similar levou 3 meses" — sem considerar que o contexto e completamente diferente.
- **Ancora da solucao simples:** Pensar primeiro na implementação mais simples e subestimar a complexidade real.
- **Ancora do prazo:** "Precisamos entregar ate marco" — a equipe estima para caber no prazo em vez de estimar realisticamente.

### Na Estimativa de Capacidade
- **Ancora do benchmark:** "O Redis processa 100k ops/segundo" — sem considerar latencia de rede, tamanho dos dados, pattern de acesso.
- **Ancora do marketing:** "O servico managed suporta auto-scaling infinito" — sem considerar custos e limites reais.

### Na Avaliacao de Risco
- **Ancora de probabilidade:** Se alguem diz "a chance de falha e 5%", o grupo ajusta a partir de 5% em vez de avaliar independentemente.
- **Ancora de severidade:** A primeira avaliacao de severidade de um risco ancora todas as subsequentes.

## Como Mitigar

### 1. Estimativa Independente (Planning Poker)
Cada membro da equipe estima independentemente ANTES de revelar estimativas. Isso previne ancoragem pela primeira estimativa verbalizada.

### 2. Estimativa em Tres Pontos
Estimar otimista, mais provavel e pessimista. Calculo: (O + 4M + P) / 6. Forca a equipe a considerar a amplitude da incerteza.

### 3. Analogias Multiplas
Em vez de ancorar em um unico projeto similar, buscar 3-5 analogias com resultados variados. A media de multiplas analogias e mais confiavel.

### 4. Estimativa Bottom-Up
Decompor em tarefas pequenas e somar. Mais trabalhoso mas menos susceptivel a ancoragem em numero unico.

### 5. Sem Numeros na Pergunta
Nunca perguntar "Isso leva mais ou menos X?" Perguntar "Quanto tempo leva?" Nunca compartilhar deadlines desejados antes da estimativa tecnica.

### 6. Reference Class Forecasting
Usar dados historicos de projetos REAIS (nao memorias seletivas) como base. Banco de dados de estimativas vs. realizacoes.

## Exemplo Real

**Contexto:** PM pergunta ao tech lead: "O CTO mencionou que a integracao com o parceiro deve ser simples, talvez 2-3 sprints. O que voces acham?"

**Manifestacao da ancoragem:**
- O numero "2-3 sprints" se torna a ancora implicita.
- A equipe estima 4 sprints (ajuste insuficiente a partir da ancora).
- Ninguem verifica a complexidade real da API do parceiro.
- A documentacao da API do parceiro e descoberta mais tarde como incompleta.
- O projeto real leva 8 sprints.

**O que deveria ter acontecido:**
- PM apresenta o escopo sem mencionar numeros: "Precisamos integrar com a API do parceiro. Quais informacoes voces precisam para estimar?"
- Equipe faz spike de 2 dias para entender a API.
- Cada membro estima independentemente (planning poker).
- Estimativas vao de 4 a 10 sprints — o range amplo sinaliza incerteza.
- Equipe negocia escopo ou timeline com dados reais.
