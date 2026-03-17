# Evolução do Pre-Programming Squad: v1 para v2

## Objetivo

Documentar a evolução do Pre-Programming Squad da versão 1 (inicial) para a versão 2 (madura), incluindo lições aprendidas, mudanças de processo e métricas de melhoria.

---

## V1 — O Início (Primeiros 6 Meses)

### Estrutura Original
- **Agentes:** 3 agentes genéricos (Analista, Revisor, Coordenador)
- **Processo:** Linear e sequencial — cada agente executava em ordem fixa
- **Foco:** Gerar documentação antes do código
- **Output:** Um documento único ("Pre-Programming Report") entregue ao time de desenvolvimento

### Problemas Identificados na V1

1. **Agentes genéricos demais** — O "Analista" tentava cobrir requisitos, arquitetura, riscos e testes em uma única passada. Profundidade era sacrificada por amplitude.

2. **Processo rígido** — Sequência fixa não se adaptava ao tipo de projeto. Bugfix crítico passava pelas mesmas 8 etapas que feature nova de 3 meses.

3. **Output monolítico** — Documento único de 30+ páginas que ninguém lia completamente. Informação crítica se perdia no meio de texto genérico.

4. **Sem feedback loop** — Output era entregue e esquecido. Nenhum mecanismo para medir se a pré-programação realmente preveniu problemas.

5. **Checklists estáticos** — Mesmos checklists para todo tipo de projeto. Itens irrelevantes eram marcados como "N/A" sem questionamento.

### Métricas da V1
- Taxa de retrabalho pós-handoff: 35%
- Tempo médio de pré-programação: 5 dias (independente do tamanho)
- Satisfação do time de desenvolvimento: 5.2/10
- Bugs encontrados em pré-programação que teriam chegado a produção: ~12%

---

## Transição V1 → V2 (Meses 7-9)

### Catalisadores da Mudança

1. **Incidente do Caso Pagamentos** — Bug de race condition em produção que custou R$85K. O Pre-Programming Report mencionava "considerar concorrência" sem profundidade. Time de dev disse: "se a pré-programação tivesse sido específica, teríamos implementado locking."

2. **Feedback do Retro Trimestral** — Desenvolvedores: "O relatório é muito genérico. Precisamos de guidance específica por domínio, não conselhos gerais."

3. **Benchmark externo** — Análise de squads similares em empresas de referência mostrou que especialização de agentes reduzia retrabalho em 40-60%.

### Decisões-Chave da Transição

| Decisão | Motivo | Impacto |
|---------|--------|---------|
| Especializar agentes por domínio | Profundidade > amplitude | 6 agentes especializados |
| Adaptar processo por tipo de projeto | Nem todo projeto é igual | 9 tipos de projeto com fases adaptadas |
| Fragmentar output | Documentos menores e focados | 8 outputs por fase em vez de 1 monolítico |
| Criar feedback loop | Medir eficácia | Métricas de retrabalho e bugs prevenidos |
| Evoluir checklists continuamente | Aprender com falhas | Checklists atualizados a cada incidente |

---

## V2 — Maturidade (Mês 10+)

### Estrutura Evoluída
- **Agentes:** Especializados por domínio (Requisitos, Escopo, Arquitetura, Riscos, Testes, Readiness)
- **Processo:** Adaptativo por tipo de projeto — fases podem ser abreviadas ou expandidas
- **Foco:** Prevenir problemas específicos, não gerar documentação
- **Output:** Artefatos modulares por fase, consumíveis independentemente

### Melhorias Específicas

#### 1. Agentes Especializados
**Antes (V1):** Agente genérico "Analista" cobria tudo superficialmente.
**Depois (V2):** Agente de Requisitos faz deep-dive em ambiguidades. Agente de Riscos foca exclusivamente em blast radius e rollback. Agente de Testes desenha estratégia de teste antes do código.

#### 2. Processo Adaptativo
**Antes (V1):** Bugfix crítico passava por 8 fases em 5 dias.
**Depois (V2):** Bugfix crítico tem fast-track: intake, blast radius, fix scope, rollback plan — em horas, não dias.

#### 3. Archive de Falhas
**Antes (V1):** Não existia.
**Depois (V2):** Cada falha alimenta o archive e atualiza checklists. Squad aprende com erros de forma estruturada.

#### 4. Gates de Qualidade
**Antes (V1):** Gate único no final ("relatório está pronto?").
**Depois (V2):** Gate em cada fase com critérios específicos e mensuráveis.

### Métricas da V2
- Taxa de retrabalho pós-handoff: 12% (redução de 66%)
- Tempo médio de pré-programação: varia por tipo (2h para bugfix, 5 dias para feature complexa)
- Satisfação do time de desenvolvimento: 8.1/10
- Bugs encontrados em pré-programação que teriam chegado a produção: ~38%

---

## Lições da Evolução

### O Que Funcionou
1. **Especialização > Generalização** — Agentes especializados encontram problemas que generalistas perdem
2. **Adaptação por tipo de projeto** — Respeitar a natureza do projeto reduz overhead e aumenta relevância
3. **Feedback loop contínuo** — Medir o impacto da pré-programação justifica o investimento e guia melhorias
4. **Archive de falhas** — Aprender estruturadamente com erros é mais valioso que qualquer framework

### O Que Não Funcionou
1. **Tentar automatizar tudo de uma vez** — Automação prematura de decisões complexas gerou outputs genéricos
2. **Métricas de vaidade** — "Número de documentos gerados" não mede valor. "Retrabalho prevenido" sim
3. **Processo uniforme** — Forçar o mesmo processo para todo tipo de projeto é desperdício

### Princípios para V3
1. Integrar feedback de produção (bugs que passaram → atualizar processo)
2. Expandir archive com exemplos icônicos (não só falhas)
3. Criar modelo de maturidade para auto-avaliação contínua
4. Explorar colaboração entre agentes (não apenas sequência)
