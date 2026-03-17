# Vies de Otimismo em Timelines

## Vies/Efeito

**Vies de Otimismo (Optimism Bias):** A tendencia de acreditar que eventos positivos sao mais provaveis para nos do que para outros, e que eventos negativos sao menos provaveis. Identificado por Weinstein (1980), e considerado um dos vieses mais consistentes e robustos em psicologia.

## Descricao

Diferente do overconfidence (excesso de confianca na precisao do julgamento), o vies de otimismo e sobre a direcao do julgamento: sistematicamente acreditamos que as coisas irao melhor do que a evidencia sugere. Estudos mostram que 80% das pessoas se consideram "acima da media" em habilidade de direcao — uma impossibilidade estatistica.

## Como se Manifesta em Pre-Programacao

### Em Timelines
- **"Vamos terminar no prazo."** Baseado em desejo, nao em dados. Historicamente, a equipe atrasa em 70% dos projetos.
- **"A integracao vai ser rapida."** Integracoes sao historicamente a parte mais imprevisivel de qualquer projeto.
- **"O terceiro trimestre e possivel."** Sem decompor em semanas de trabalho real, descontar ferias, feriados, suporte, reunioes, e trabalho nao planejado.

### Em Suposicoes sobre Dependencias
- **"A API do parceiro vai estar pronta quando precisarmos."** Sem confirmacao formal, sem plano B.
- **"A equipe de infra vai provisionar o ambiente rapidamente."** Sem SLA, sem prioridade confirmada.
- **"O design ja esta validado, nao vai mudar."** Designs sempre mudam quando encontram a realidade da implementacao.

### Em Suposicoes sobre a Equipe
- **"Ninguem vai sair durante o projeto."** Rotatividade acontece. E se o key contributor sair?
- **"Nao vai ter trabalho nao planejado."** Sempre ha: bugs urgentes, suporte, incidentes, reunioes inesperadas.
- **"Todo mundo vai estar focado 100% neste projeto."** Context switching e reunioes consomem 30-50% do tempo.

### Em Suposicoes sobre Tecnologia
- **"Nao vamos encontrar bugs na biblioteca."** Toda biblioteca tem bugs. A questao e quando e como serao descobertos.
- **"A performance vai ser suficiente."** Sem benchmark, sem dados, so esperanca.
- **"A migracao vai ser smooth."** Migracoes de dados sempre revelam surpresas.

## Como Mitigar

### 1. Planejamento Pessimista Deliberado
Para cada suposicao otimista, perguntar: "E se isso der errado? Qual e o plano B?" Ter plano B nao significa que sera usado — significa que a equipe esta preparada.

### 2. Fator de Disponibilidade Realista
Desenvolvedores nao codam 8h/dia. Fator de disponibilidade realista:
- Tempo produtivo de codigo: 4-5h/dia.
- Reunioes, code review, comunicacao: 2-3h/dia.
- Trabalho nao planejado: 10-20% do tempo.
- Feriados e ferias: ~15% do ano.

### 3. Buffer por Categoria de Incerteza
| Nivel de Incerteza | Exemplo | Buffer |
|---|---|---|
| Baixa | Tarefa ja feita antes, requisitos claros | +20% |
| Media | Tarefa nova, tecnologia conhecida | +50% |
| Alta | Tecnologia nova, integracao com terceiros | +100% |
| Desconhecida | "Nunca fizemos nada parecido" | Spike primeiro, estimar depois |

### 4. Historico como Bussola
Manter registro de estimativas vs. duracao real. Calcular o fator de otimismo medio da equipe. Aplicar automaticamente.

### 5. Cenarios em vez de Pontos
Apresentar timelines como cenarios, nao como datas:
- **Otimista (10% de chance):** 8 semanas — se tudo der certo.
- **Provavel (60% de chance):** 12 semanas — com problemas tipicos.
- **Pessimista (90% de chance):** 16 semanas — com problemas significativos.

### 6. Comprometer com Ranges, nao Datas
"Entregaremos entre marco e maio" em vez de "Entregaremos em abril." Ranges comunicam incerteza honestamente.

## Exemplo Real

**Contexto:** Equipe planeja construir feature de recomendacao de produtos com ML.

**Timeline otimista apresentada:**
- Semana 1-2: Coleta de dados e feature engineering.
- Semana 3-4: Treinamento do modelo.
- Semana 5-6: API de serving.
- Semana 7-8: Integracao com frontend e testes.
- **Total: 8 semanas. "Entregar ate final de abril."**

**O que realmente aconteceu (20 semanas):**
- Semanas 1-4: Dados estavam sujos. 2 semanas extras de limpeza.
- Semanas 5-8: Modelo inicial com accuracy insatisfatoria. Iteracao.
- Semana 9: Descoberta de que o volume de dados e insuficiente. Coleta adicional.
- Semanas 10-12: Modelo aceitavel apos 3 iteracoes.
- Semanas 13-14: API de serving. Latencia inaceitavel (200ms target, 800ms real).
- Semanas 15-16: Otimizacao de serving com caching e quantizacao.
- Semanas 17-18: Integracao com frontend. A/B test setup.
- Semanas 19-20: A/B test, ajustes, lancamento gradual.

**O que deveria ter acontecido na pre-programacao:**
- Cenarios: 8 semanas (otimista), 14 semanas (provavel), 20 semanas (pessimista).
- Spike de 1 semana para avaliar qualidade dos dados antes de estimar.
- Plano B se dados forem insuficientes.
- Buffer explicito para iteracao de modelo (nunca funciona na primeira tentativa).
