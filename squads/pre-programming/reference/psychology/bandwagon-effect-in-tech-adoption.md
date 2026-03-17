# Efeito Bandwagon na Adoção de Tecnologia

## Viés/Efeito

**Efeito Bandwagon (Bandwagon Effect):** A tendência de adotar tecnologias, frameworks ou padrões arquiteturais porque "todo mundo está usando" — sem avaliar se são adequados para o contexto específico do projeto. Também conhecido como "hype-driven development".

## Descrição

O efeito bandwagon em tecnologia é amplificado por: conference talks, blog posts, Twitter, e o medo de ficar "para trás". Quando o Google usa microservices para escalar para bilhões de usuários, times de 5 pessoas concluem que também precisam de microservices. Quando Netflix usa chaos engineering, startups com 3 serviços adotam Chaos Monkey.

O problema não é que a tecnologia é ruim — é que o contexto é diferente. Kubernetes resolve problemas reais para empresas com centenas de serviços. Para uma startup com 3 APIs, é overhead operacional que rouba tempo de desenvolvimento.

## Como se Manifesta em Pré-Programação

### Na Escolha de Stack
- **"Todo mundo está usando Rust, devíamos migrar"** — Time de 4 devs Python quer migrar para Rust porque viu palestra no YouTube. Custo de learning curve: 6 meses. Benefício de performance: irrelevante para app com 500 req/min.
- **"Precisamos de GraphQL"** — REST simples atende 100% dos casos de uso, mas GraphQL é "moderno". Custo de complexidade: schema management, caching mais difícil, N+1 queries.

### Na Arquitetura
- **"Microservices desde o dia 1"** — Startup com product-market fit não validado adota 12 microservices. Resultado: 60% do tempo gasto em infra, não em produto.
- **"Event sourcing para tudo"** — Time adota event sourcing para CRUD simples porque "é o futuro". Resultado: complexidade 10x para benefício zero.

### Em Ferramentas e Processos
- **"Kubernetes é o padrão"** — 3 containers em produção, custo de K8s cluster: $500/mês + 1 person-month de setup. Docker Compose faria o mesmo.
- **"Precisamos de observability stack completo"** — Projeto com 2 serviços adota Jaeger + Prometheus + Grafana + Loki + Tempo antes de ter um único alerta definido.

## Como Mitigar

### 1. Perguntar: "Qual problema isso resolve PARA NÓS?"
Não "qual problema isso resolve no Google" — mas no nosso contexto, com nosso time, nosso volume, nosso budget.

**Implementação prática:**
- Em toda proposta de tecnologia nova, exigir: problema específico que resolve + alternativa mais simples avaliada
- Use o framework Build vs Buy com critérios objetivos

### 2. Avaliar Custo Total de Adoção
Não apenas custo de licença. Incluir: learning curve, operational overhead, debugging complexity, hiring impact, vendor lock-in.

**Implementação prática:**
- Template: "Para adotar X, precisamos de: Y horas de learning, Z horas de setup, W horas/mês de manutenção"
- Comparar com alternativa: "Se usarmos a solução simples, economizamos A horas"

### 3. Buscar Anti-Cases, Não Apenas Cases
Para cada tecnologia hyped, buscar: "Quem adotou e se arrependeu? Por quê?"

### 4. Reference Class: Empresas do Mesmo Porte
Não comparar com FAANG. Buscar: "Empresas do nosso porte/indústria, o que usam? O que funcionou?"

## Referências
- ThoughtWorks Technology Radar (avaliação criteriosa de tecnologias)
- Basecamp — "Choose Boring Technology" (Dan McKinley)
- DORA metrics (o que realmente correlaciona com performance)
