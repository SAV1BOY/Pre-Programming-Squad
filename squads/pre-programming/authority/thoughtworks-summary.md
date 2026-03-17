# ThoughtWorks — Resumo de Autoridade

## Autor

**Organização**: ThoughtWorks
**Contribuidores Notáveis**: Martin Fowler (Chief Scientist), Neal Ford, Rebecca Parsons, Jez Humble, Sam Newman
**Obras Coletivas**: Technology Radar, "Building Evolutionary Architectures", "Continuous Delivery", "Building Microservices"
**Área de Expertise**: Consultoria de engenharia de software, práticas ágeis, entrega contínua, arquiteturas evolucionárias

---

## Tese Central

Software excelente é produto de **práticas de engenharia disciplinadas**, aplicadas por **times multidisciplinares** em **ciclos curtos de feedback**. A ThoughtWorks defende que a excelência técnica e as práticas ágeis não são opostas — são complementares. Entrega contínua, testes automatizados, pair programming e evolutionary architecture não são overhead — são investimentos que pagam dividendos exponenciais ao longo do tempo.

---

## Conceitos-Chave

### 1. Technology Radar
Publicação semestral que classifica tecnologias em Adopt/Trial/Assess/Hold. Princípios do Radar:
- Baseado em experiência prática de projetos reais, não hype
- Cobre Técnicas, Ferramentas, Plataformas e Linguagens/Frameworks
- Serve como input para decisões de stack informadas

### 2. Evolutionary Architecture
Arquiteturas que suportam mudança guiada e incremental ao longo de múltiplas dimensões:
- **Fitness Functions**: Testes automatizados que validam propriedades arquiteturais
- **Incremental Change**: Mudanças pequenas e frequentes em vez de redesign completo
- **Appropriate Coupling**: Acoplamento consciente — nem tudo precisa ser desacoplado

### 3. Continuous Delivery
Pipeline que leva cada commit até produção de forma automatizada e confiável:
- Commit -> Build -> Test -> Stage -> Production
- Deploy é rotina, não evento especial
- Qualquer commit verde pode ir para produção a qualquer momento
- Feature flags separam deploy de release

### 4. Lean Software Development
Eliminar desperdício:
- Código não usado é desperdício
- Funcionalidade não validada é desperdício
- Handoff sem contexto é desperdício
- Espera por aprovação é desperdício

### 5. DevOps como Cultura
DevOps não é ferramenta ou cargo — é cultura de responsabilidade compartilhada entre desenvolvimento e operações. "You build it, you run it" é a expressão máxima dessa cultura.

---

## Aplicação ao Squad

- **Technology Radar como input trimestral**: Revisar o Radar mais recente a cada trimestre. Atualizar recomendações de stack do squad baseado nas mudanças.

- **Fitness functions definidas na pré-programação**: Para cada atributo de qualidade (performance, segurança, manutenibilidade), definir uma fitness function mensurável que será implementada no CI.

- **Pipeline de CD como artefato do squad**: A estrutura da pipeline de CI/CD (stages, gates, testes) deve ser definida durante a pré-programação, não improvisada pelo time de dev.

- **Eliminação de desperdício no processo**: O squad deve constantemente questionar: "Este artefato é necessário?" "Este processo adiciona valor?". Documentação que ninguém lê é desperdício.

- **Prática de pair/mob para design**: Decisões de arquitetura complexas devem ser tomadas em pair ou mob session, não por uma pessoa isolada. Diversidade de perspectivas melhora a qualidade.

---

## Citações Relevantes

> "If it hurts, do it more frequently, and bring the pain forward." (sobre Continuous Integration)

> "An evolutionary architecture supports guided, incremental change across multiple dimensions."

> "The goal of continuous delivery is to make deployments — whether of a large-scale distributed system, a complex production environment, an embedded system, or an app — predictable, routine affairs."

> "The biggest risk is not taking any risk. In a world that's changing really quickly, the only strategy that is guaranteed to fail is not taking risks."

> "Software delivery performance matters. High performers deploy more frequently, with shorter lead times, lower failure rates, and faster recovery times."
