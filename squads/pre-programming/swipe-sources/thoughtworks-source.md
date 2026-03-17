# ThoughtWorks — Fonte de Referência

## Fonte

**Organização**: ThoughtWorks
**Prática**: Technology Radar, entrega contínua, práticas ágeis avançadas, consultoria de engenharia
**Referências Principais**:
- ThoughtWorks Technology Radar (publicação semestral)
- "Building Evolutionary Architectures" (Livro, Neal Ford, Rebecca Parsons, Patrick Kua)
- "Continuous Delivery" (Livro, Jez Humble & David Farley)
- ThoughtWorks Insights (thoughtworks.com/insights)

## URL de Referência

- https://www.thoughtworks.com/radar
- https://www.thoughtworks.com/insights
- https://www.thoughtworks.com/books

---

## O que Aprender

### Technology Radar

O Technology Radar da ThoughtWorks é publicado semestralmente e classifica tecnologias, ferramentas, plataformas e técnicas em quatro anéis:

- **Adopt**: Recomendamos adotar com confiança
- **Trial**: Vale a pena explorar com objetivo de entender como se aplica
- **Assess**: Vale a pena pesquisar para entender como pode afetar sua organização
- **Hold**: Proceda com cautela ou evite

O Radar é recurso valioso para decisões de stack na pré-programação.

### Entrega Contínua

ThoughtWorks é berço do conceito de Continuous Delivery (Jez Humble):

- Deploy deve ser rotineiro, não evento especial
- Pipeline automatizada: commit -> build -> test -> stage -> production
- Feature flags para separar deploy de release
- Trunk-based development em vez de feature branches longas

### Arquiteturas Evolucionárias

O conceito de fitness functions — testes automatizados que validam propriedades arquiteturais:

- Fitness function de performance: Latência p99 < Xms
- Fitness function de acoplamento: Nenhum módulo com mais de N dependências
- Fitness function de segurança: Zero vulnerabilidades críticas em scan
- Executadas no CI — a arquitetura é testada continuamente

### ADR como Prática Organizacional

ThoughtWorks foi uma das primeiras consultoras a adotar e evangelizar ADRs como prática padrão em todos os projetos de consultoria.

---

## Práticas Relevantes para Pré-Programação

1. **Technology Radar como input para pesquisa de stack**: Consultar o Radar mais recente antes de decisões de stack. Tecnologias em "Hold" devem ser evitadas sem justificativa muito forte.

2. **Fitness functions no plano de testes**: Definir fitness functions durante a pré-programação que serão implementadas como testes automatizados no CI. Exemplos: tempo de build < 5min, cobertura > 80%, zero dependências circulares.

3. **Pipeline de CI/CD como artefato de pré-programação**: Definir a estrutura da pipeline antes de codificar. Quais gates existem? Quais testes rodam em cada stage? Qual é o tempo máximo aceitável de pipeline?

4. **Feature flags no design**: Planejar quais features serão protegidas por feature flags desde o design doc. Não é decisão pós-implementação.

5. **Trunk-based development como premissa**: Se o time vai usar trunk-based, o design deve suportar mudanças incrementais. Se vai usar feature branches, o design deve suportar merges complexos. Decidir na pré-programação.

6. **Propriedades arquiteturais mensuráveis**: Para cada atributo de qualidade desejado (performance, segurança, manutenibilidade), definir uma fitness function mensurável que será monitorada continuamente.

7. **Quadrante de técnicas**: Usar o quadrante "Techniques" do Radar para identificar práticas de engenharia que o squad deveria adotar ou evitar.
