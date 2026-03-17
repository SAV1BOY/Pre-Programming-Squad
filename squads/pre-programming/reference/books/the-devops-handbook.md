# The DevOps Handbook

## Informações Gerais

- **Titulo:** The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations
- **Autores:** Gene Kim, Jez Humble, Patrick Debois, John Willis
- **Ano:** 2016

## Tese Central

DevOps nao e um cargo ou ferramenta — e um conjunto de principios e praticas que unificam desenvolvimento e operacoes para entregar valor mais rapido e com mais confiabilidade. Os Tres Caminhos — Flow (fluxo rapido do desenvolvimento a producao), Feedback (feedback rapido de producao para desenvolvimento) e Aprendizado Continuo (experimentacao e aprendizado organizacional) — formam a base de toda transformacao DevOps.

## Conceitos-Chave para Pre-Programacao

### 1. O Primeiro Caminho: Flow
Acelerar o fluxo de trabalho do desenvolvimento a producao. Reduzir batch sizes, limitar WIP (Work in Progress), eliminar handoffs desnecessarios. Na pre-programacao, projetar para flow significa projetar para deploys pequenos e frequentes.

### 2. O Segundo Caminho: Feedback
Criar loops de feedback rapidos e amplificados. Telemetria, monitoramento, alertas, postmortems blameless. Na pre-programacao, planejar observabilidade e mecanismos de feedback desde o design.

### 3. O Terceiro Caminho: Aprendizado Continuo
Criar uma cultura de experimentacao e aprendizado. Reservar tempo para melhorias, conduzir game days, praticar chaos engineering. Na pre-programacao, incorporar aprendizado de incidentes passados.

### 4. Infraestrutura como Codigo
Toda infraestrutura deve ser definida em codigo, versionada e testada. Ambientes devem ser reproduziveis e descartaveis. Na pre-programacao, a estrategia de IaC deve ser parte do design.

### 5. Telemetria e Observabilidade
Instrumentar tudo: metricas de negocio, metricas de aplicacao, metricas de infraestrutura. Na pre-programacao, definir quais metricas monitorar e quais alertas configurar.

### 6. Seguranca Integrada (Shifting Left Security)
Seguranca deve ser integrada em todo o pipeline, nao adicionada no final. Analise de vulnerabilidades automatizada, security reviews no design. Na pre-programacao, incluir requisitos de seguranca no design doc.

### 7. Arquitetura de Baixo Risco
Arquiteturas que suportam deploys independentes por equipe, com contratos bem definidos e baixo acoplamento. Na pre-programacao, a arquitetura deve viabilizar praticas DevOps.

## Como Aplicar no Squad

### No Design para Flow
- Verificar se o design permite deploys independentes por equipe.
- Avaliar se o design suporta entrega incremental (small batch sizes).
- Identificar pontos de handoff que podem gerar gargalos.
- Planejar automacao do pipeline desde o design.

### No Design para Feedback
- Incluir estrategia de observabilidade nos design docs.
- Definir metricas de negocio e tecnicas a serem monitoradas.
- Planejar alertas e dashboards como parte do design.
- Definir runbooks para cenarios de falha conhecidos.

### No Design para Seguranca
- Incluir threat modeling nos design docs.
- Definir requisitos de seguranca (autenticacao, autorizacao, encriptacao, auditoria).
- Planejar security scanning automatizado no pipeline.
- Avaliar compliance requirements na fase de pre-programacao.

### Nos Criterios de Readiness
- "O design suporta deploys independentes e frequentes?"
- "A estrategia de observabilidade esta definida (metricas, logs, traces, alertas)?"
- "Requisitos de seguranca estao documentados e o threat model foi revisado?"
- "O pipeline de CI/CD esta planejado?"

## Citacoes Importantes

> "Any improvements made anywhere besides the bottleneck are an illusion."

> "Instead of a culture of fear, we have a high-trust, collaborative culture."

> "Everyone needs to feel safe to talk about problems so that they can be resolved."

> "Done means running in production and delivering value to customers."

> "If it hurts, do it more often."

## Relacao com Outros Livros de Referencia

- **Accelerate:** Fornece a evidencia empirica para as praticas prescritas neste handbook.
- **Continuous Delivery (Humble/Farley):** O DevOps Handbook expande CD com dimensoes culturais e organizacionais.
- **SRE (Google):** Perspectivas complementares sobre confiabilidade e operacao.
- **Release It! (Nygard):** Complementa com padroes praticos de estabilidade.
