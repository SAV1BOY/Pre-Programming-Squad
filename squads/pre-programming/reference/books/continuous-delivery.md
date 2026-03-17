# Continuous Delivery

## Informações Gerais

- **Titulo:** Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation
- **Autores:** Jez Humble, David Farley
- **Ano:** 2010

## Tese Central

O software deve estar sempre em estado deployavel. O deployment pipeline — uma sequencia automatizada de build, teste e deploy — e o mecanismo central para garantir que cada mudanca pode ser liberada para producao com confianca e a qualquer momento. A entrega continua reduz risco, custo e tempo de feedback, permitindo entregas frequentes e confiaveis.

## Conceitos-Chave para Pre-Programacao

### 1. O Deployment Pipeline
Uma sequencia automatizada de estagios: commit stage (build + unit tests), acceptance tests, staging, producao. Cada estagio aumenta a confianca de que a mudanca e segura. Na pre-programacao, o pipeline deve ser planejado como parte do design.

### 2. Manter Software Sempre Deployavel
O trunk/main deve estar sempre em estado deployavel. Isso requer: integracao continua, feature flags, branch by abstraction. Na pre-programacao, o design deve viabilizar deploys frequentes sem coordenacao complexa.

### 3. Configuration Management
Toda configuracao — infraestrutura, aplicacao, ambiente — deve ser versionada e automatizada. Ambientes devem ser reproduziveis. Na pre-programacao, planejar estrategia de configuracao.

### 4. Automacao de Testes em Multiplos Niveis
- Testes unitarios: rapidos, isolados, executados em todo commit.
- Testes de aceitacao: validam requisitos de negocio automaticamente.
- Testes de capacidade: validam performance sob carga.
- Testes exploratórios: manuais, criativos, para descobrir problemas inesperados.

### 5. Gerenciamento de Dados
Migrations de banco de dados automatizadas, versionadas e reversiveis. Na pre-programacao, definir estrategia de migration e evolucao de schema.

### 6. Zero-Downtime Deployment
Tecnicas: blue-green deployment, canary releases, rolling updates, dark launching. Na pre-programacao, a estrategia de deploy deve ser definida e o design deve suporta-la.

### 7. Feedback Loops
Quanto mais rapido o feedback, mais rapida a correcao. O pipeline deve dar feedback em minutos, nao horas. Na pre-programacao, projetar para feedback rapido.

## Como Aplicar no Squad

### No Design do Pipeline
- Incluir definicao do deployment pipeline nos design docs.
- Especificar estagios do pipeline e criterios de passagem.
- Planejar automacao de testes em cada estagio.
- Definir estrategia de rollback em cada estagio.

### Na Estrategia de Deploy
- Definir estrategia de zero-downtime deployment.
- Planejar feature flags para desacoplamento de deploy e release.
- Especificar estrategia de canary/blue-green deploy.
- Definir criterios automatizados de promoção entre ambientes.

### Na Evolucao de Schema
- Planejar estrategia de migration de banco de dados.
- Exigir backward-compatible schema changes quando possivel.
- Definir processo de rollback de migrations.
- Planejar expand-and-contract para mudancas incompativeis.

### Nos Criterios de Readiness
- "O deployment pipeline esta definido com todos os estagios?"
- "A estrategia de zero-downtime deploy esta especificada?"
- "Feature flags estao planejadas para funcionalidades que precisam de rollout gradual?"
- "A estrategia de migration de banco esta definida?"
- "Criterios automatizados de rollback estao definidos?"

## Citacoes Importantes

> "If it hurts, do it more frequently, and bring the pain forward."

> "The goal of continuous delivery is to make deployments — whether of a large-scale distributed system, a complex production environment, an embedded system, or an app — predictable, routine affairs."

> "Done means released."

> "Every change should trigger the deployment pipeline. Every change that passes the pipeline should be a release candidate."

> "Releasing software should be as easy as pressing a button."

## Relacao com Outros Livros de Referencia

- **Accelerate:** Accelerate fornece evidencia empirica de que as praticas de Continuous Delivery impulsionam performance organizacional.
- **The DevOps Handbook:** Complementa com o contexto cultural e organizacional.
- **Release It! (Nygard):** Nygard foca na estabilidade em producao; Humble/Farley focam no caminho ate a producao.
