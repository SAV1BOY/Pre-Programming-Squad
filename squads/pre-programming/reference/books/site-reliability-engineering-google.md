# Site Reliability Engineering

## Informações Gerais

- **Titulo:** Site Reliability Engineering: How Google Runs Production Systems
- **Autores:** Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (editores)
- **Ano:** 2016

## Tese Central

SRE e o que acontece quando voce pede a um engenheiro de software para projetar uma funcao de operacoes. Em vez de tratar operacoes como atividade separada e reativa, SRE aplica principios de engenharia de software a problemas de infraestrutura e operacoes. O conceito central e o error budget: a quantidade de downtime aceitavel determina quanto risco a equipe pode assumir em mudancas, criando um equilibrio natural entre velocidade e confiabilidade.

## Conceitos-Chave para Pre-Programacao

### 1. SLIs, SLOs e SLAs
- **SLI (Service Level Indicator):** Metrica que mede um aspecto do nivel de servico (ex: latencia p99, taxa de erros).
- **SLO (Service Level Objective):** Target para um SLI (ex: latencia p99 < 200ms em 99.9% do tempo).
- **SLA (Service Level Agreement):** Contrato com consequencias por violacao de SLO.

Na pre-programacao, definir SLIs e SLOs e fundamental para alinhar expectativas.

### 2. Error Budget
A diferenca entre 100% de confiabilidade e o SLO define o error budget. Se o SLO e 99.9%, o error budget e 0.1% de downtime (~43 minutos/mes). Enquanto ha budget, a equipe pode assumir riscos com mudancas. Quando o budget esgota, foco em confiabilidade.

### 3. Toil (Trabalho Operacional Repetitivo)
Trabalho manual, repetitivo, automatizavel, reativo e sem valor duradouro. SRE busca eliminar toil por meio de automacao. Na pre-programacao, projetar sistemas que minimizem toil futuro.

### 4. Monitoring e Alerting
Monitoramento deve gerar alertas acionaveis, nao ruido. Quatro sinais dourados: latencia, trafego, erros, saturacao. Na pre-programacao, definir os sinais dourados de cada servico.

### 5. Capacity Planning
Planejamento de capacidade baseado em projecoes de crescimento, com margem de seguranca. Incluir testes de carga regulares. Na pre-programacao, estimar capacidade necessaria e planejar escalabilidade.

### 6. Postmortems Blameless
Apos incidentes, conduzir postmortems focados em aprendizado, nao em culpa. Documentar timeline, impacto, causa raiz, acoes corretivas. Na pre-programacao, incorporar aprendizados de postmortems passados.

### 7. Release Engineering
O processo de build, test e deploy deve ser reproduzivel, automatizado e auditavel. Na pre-programacao, definir o processo de release como parte do design.

## Como Aplicar no Squad

### Na Definicao de SLIs/SLOs
- Para cada servico, definir SLIs relevantes (latencia, disponibilidade, throughput, corretude).
- Estabelecer SLOs realistas baseados em necessidades de negocio.
- Calcular error budgets e definir politicas quando esgotados.
- Incluir SLIs/SLOs nos design docs como requisitos nao-funcionais.

### Na Analise de Capacidade
- Incluir estimativas de capacidade nos design docs.
- Planejar testes de carga como parte da estrategia de validacao.
- Definir estrategia de escalabilidade (horizontal/vertical) com triggers.
- Estimar custos operacionais baseados nas projecoes de capacidade.

### No Design para Operabilidade
- Definir os quatro sinais dourados para cada servico.
- Planejar dashboards e alertas como parte do design.
- Projetar sistemas que minimizem toil operacional.
- Incluir runbooks para cenarios de falha conhecidos.

### Nos Criterios de Readiness
- "SLIs e SLOs estao definidos para cada servico?"
- "Error budgets foram calculados e politicas definidas?"
- "Os quatro sinais dourados estao definidos e serao monitorados?"
- "Estimativas de capacidade estao documentadas?"
- "O design minimiza toil operacional futuro?"

## Citacoes Importantes

> "Hope is not a strategy."

> "100% is the wrong reliability target for virtually everything."

> "Monitoring should never require a human to interpret any part of the alerting domain."

> "The price of reliability is the pursuit of the utmost simplicity."

> "SRE is what happens when you ask a software engineer to design an operations function."

> "An error budget provides a clear, objective metric that determines how unreliable the service is allowed to be."

## Relacao com Outros Livros de Referencia

- **Release It! (Nygard):** Ambos focam em confiabilidade de producao, com perspectivas complementares.
- **The DevOps Handbook:** DevOps e SRE compartilham principios, com implementacoes diferentes.
- **Accelerate:** MTTR (metrica DORA) alinha-se diretamente com praticas de SRE.
- **DDIA (Kleppmann):** Fundamentos de confiabilidade distribuida que SRE aplica operacionalmente.
