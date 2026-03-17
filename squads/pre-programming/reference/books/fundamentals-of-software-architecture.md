# Fundamentals of Software Architecture

## Informações Gerais

- **Titulo:** Fundamentals of Software Architecture: An Engineering Approach
- **Autores:** Mark Richards, Neal Ford
- **Ano:** 2020

## Tese Central

Arquitetura de software e sobre trade-offs — tudo em arquitetura e um trade-off. Nao existe uma solucao "melhor", apenas solucoes que equilibram diferentes qualidades arquiteturais (as chamadas "-ilidades") de acordo com o contexto. O papel do arquiteto e analisar trade-offs explicitamente e tomar decisoes informadas, documentando as razoes por tras de cada escolha.

## Conceitos-Chave para Pre-Programacao

### 1. Primeira Lei da Arquitetura de Software
"Tudo em arquitetura de software e um trade-off." Nao existe decisao arquitetural sem custo. Na pre-programacao, cada decisao deve ter seus trade-offs explicitamente documentados.

### 2. Segunda Lei da Arquitetura de Software
"Por que e mais importante do que como." A razao por tras de uma decisao arquitetural e mais valiosa que a decisao em si, porque contextos mudam mas a documentacao do raciocinio permite reavaliar decisoes futuras.

### 3. Caracteristicas Arquiteturais (-ilidades)
Qualidades como escalabilidade, disponibilidade, performance, seguranca, testabilidade, deployability, simplicidade. Cada sistema precisa priorizar um subconjunto — nao e possivel maximizar todas simultaneamente.

### 4. Estilos Arquiteturais
- **Monolito layered:** Simples, bom para equipes pequenas.
- **Modular monolith:** Melhor separacao sem complexidade distribuida.
- **Microservices:** Maximo desacoplamento, alta complexidade operacional.
- **Event-driven:** Bom para processamento assincrono e desacoplamento temporal.
- **Space-based:** Para alta elasticidade e escalabilidade extrema.

Cada estilo favorece diferentes caracteristicas arquiteturais.

### 5. Fitness Functions Arquiteturais
Mecanismos objetivos e automatizados para validar que caracteristicas arquiteturais estao sendo mantidas. Exemplos: testes de performance automatizados, verificacoes de acoplamento, metricas de complexidade ciclomatica.

### 6. Quantum Arquitetural
A menor unidade deployavel independentemente que inclui todos os componentes estruturais necessarios para funcionar. Determina a granularidade real do sistema e e fundamental para avaliar acoplamento.

### 7. Analise de Trade-offs com ADRs
Architecture Decision Records documentam decisoes, contexto, alternativas e consequencias. Sao a ferramenta principal para rastrear o raciocinio arquitetural ao longo do tempo.

## Como Aplicar no Squad

### Na Identificacao de Caracteristicas Arquiteturais
- Para cada projeto, identificar as 3-5 caracteristicas arquiteturais mais importantes.
- Priorizar explicitamente (nao e possivel ter tudo).
- Usar a matriz de caracteristicas vs. estilos arquiteturais para orientar a escolha de estilo.
- Documentar quais caracteristicas foram sacrificadas e por que.

### Na Avaliacao de Design Docs
- Verificar se os trade-offs estao explicitamente documentados.
- Confirmar que ADRs acompanham decisoes arquiteturais significativas.
- Avaliar se o estilo arquitetural escolhido suporta as caracteristicas priorizadas.
- Verificar se fitness functions foram definidas para caracteristicas criticas.

### Na Selecao de Estilos Arquiteturais
- Nao escolher microservices por default — avaliar se a complexidade adicional e justificada.
- Considerar modular monolith como ponto de partida para muitos projetos.
- Avaliar o quantum arquitetural necessario para os requisitos de deploy e escala.

### Nos Criterios de Readiness
- Checklist: "As 3-5 caracteristicas arquiteturais prioritarias foram identificadas?"
- Checklist: "O estilo arquitetural foi justificado com base nos trade-offs?"
- Checklist: "ADRs foram criados para decisoes arquiteturais significativas?"
- Checklist: "Fitness functions foram definidas para caracteristicas criticas?"

## Citacoes Importantes

> "Everything in software architecture is a trade-off."

> "Why is more important than how."

> "There are no best practices in software architecture — only trade-offs."

> "An architect who cannot code is like a general who has never been on a battlefield."

> "Never shoot for the best architecture, but rather the least worst architecture."

> "If you think you have discovered something that isn't a trade-off, it just means you haven't identified the trade-off yet."

## Relacao com Outros Livros de Referencia

- **Clean Architecture (Martin):** Martin foca em principios (SOLID, dependencias), Richards/Ford focam em trade-offs e estilos — sao complementares.
- **Building Evolutionary Architectures:** Expande o conceito de fitness functions introduzido aqui.
- **A Philosophy of Software Design (Ousterhout):** A "complexidade" de Ousterhout e uma das caracteristicas arquiteturais que devem ser minimizadas.
