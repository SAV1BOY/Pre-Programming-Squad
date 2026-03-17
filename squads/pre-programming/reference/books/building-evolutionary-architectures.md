# Building Evolutionary Architectures

## Informações Gerais

- **Titulo:** Building Evolutionary Architectures: Support Constant Change
- **Autores:** Neal Ford, Rebecca Parsons, Patrick Kua
- **Ano:** 2017

## Tese Central

Arquiteturas de software devem ser projetadas para evoluir, nao para serem finalizadas. Em vez de tentar prever o futuro e criar a arquitetura "perfeita" antecipadamente (big design upfront), devemos criar mecanismos que guiem a evolucao arquitetural ao longo do tempo. Fitness functions arquiteturais sao o mecanismo principal para proteger caracteristicas importantes enquanto o sistema evolui.

## Conceitos-Chave para Pre-Programacao

### 1. Fitness Functions Arquiteturais
Funcoes objetivas que avaliam se uma caracteristica arquitetural esta sendo mantida. Podem ser automatizadas (testes de performance, metricas de acoplamento) ou manuais (reviews periodicos). Na pre-programacao, definir fitness functions para cada caracteristica critica.

### 2. Tipos de Fitness Functions
- **Atomicas:** Testam uma unica caracteristica (ex: latencia de resposta < 200ms).
- **Holisticas:** Testam interacao entre caracteristicas (ex: seguranca + performance).
- **Triggered:** Executadas em resposta a evento (ex: no pipeline de CI).
- **Continuous:** Monitoramento constante (ex: alertas de producao).
- **Static:** Resultado fixo (ex: analise de dependencias).
- **Dynamic:** Resultado varia (ex: teste de carga sob condicoes reais).

### 3. Incremental Change
Mudancas pequenas e frequentes sao mais seguras e faceis de reverter que mudancas grandes e infrequentes. A arquitetura deve suportar entrega incremental.

### 4. Guided Change vs. Unguided Change
Sem fitness functions, mudancas sao desguiadas — a arquitetura degrada ao longo do tempo (technical debt). Com fitness functions, mudancas sao guiadas — degradacoes sao detectadas automaticamente.

### 5. Acoplamento Apropriado
Nem todo acoplamento e ruim. O objetivo e acoplamento apropriado: forte coesao dentro de componentes, baixo acoplamento entre componentes. Fitness functions de acoplamento medem e protegem essa propriedade.

### 6. Sacrificial Architecture
Aceitar que partes do sistema serao substituidas no futuro. Projetar para que a substituicao seja facil, nao para que o componente dure para sempre.

## Como Aplicar no Squad

### Na Definicao de Fitness Functions
- Para cada caracteristica arquitetural critica, definir pelo menos uma fitness function.
- Automatizar fitness functions no pipeline de CI/CD quando possivel.
- Definir thresholds claros (ex: tempo de resposta p99 < 500ms, cobertura de testes > 80%).
- Incluir fitness functions nos criterios de readiness.

### Na Avaliacao de Evolvabilidade
- Verificar se o design permite evolucao incremental.
- Avaliar se componentes podem ser substituidos independentemente.
- Identificar pontos de acoplamento que dificultariam mudancas futuras.
- Planejar migrations paths para decisoes que podem mudar.

### Na Estrategia de Entrega
- Exigir que designs suportem entrega incremental.
- Rejeitar designs que requerem "big-bang" releases.
- Planejar feature flags e mecanismos de rollback.
- Definir estrategia de canary/blue-green deploy.

### Nos Criterios de Readiness
- "Fitness functions estao definidas para caracteristicas arquiteturais criticas?"
- "O design suporta evolucao incremental?"
- "Sacrificial components estao identificados e preparados para substituicao?"
- "Mecanismos de deteccao de degradacao arquitetural estao planejados?"

## Citacoes Importantes

> "An evolutionary architecture supports guided, incremental change across multiple dimensions."

> "A fitness function is any mechanism that provides an objective integrity assessment of some architecture characteristic."

> "The best architecture is one that can evolve, not one that is perfect on day one."

> "If you can't measure it, you can't protect it."

> "Architecture is not a phase — it is a continuous activity."

## Relacao com Outros Livros de Referencia

- **Fundamentals of Software Architecture:** Richards/Ford introduzem fitness functions; este livro as detalha completamente.
- **Continuous Delivery:** A entrega continua e pre-requisito para evolucao arquitetural incremental.
- **Accelerate:** As metricas DORA podem ser vistas como fitness functions organizacionais.
