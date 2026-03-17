# Martin Fowler — Fonte de Referência

## Fonte

**Autor**: Martin Fowler
**Prática**: Padrões de arquitetura, refactoring, entrega contínua, design de software
**Referências Principais**:
- martinfowler.com — Blog com centenas de artigos sobre arquitetura e design
- "Patterns of Enterprise Application Architecture" (Livro, 2002)
- "Refactoring: Improving the Design of Existing Code" (Livro, 2a edição, 2018)
- Bliki (Blog+Wiki) com padrões catalogados

## URL de Referência

- https://martinfowler.com/
- https://martinfowler.com/architecture/
- https://martinfowler.com/bliki/

---

## O que Aprender

### Padrões de Arquitetura

Martin Fowler catalogou padrões fundamentais que toda equipe de pré-programação deve conhecer:

- **Strangler Fig Application**: Migração gradual de sistemas legados substituindo funcionalidades uma a uma
- **Branch by Abstraction**: Técnica para fazer mudanças de larga escala em sistemas ativos sem feature branches longas
- **Event-Driven Architecture**: Quando usar e quando não usar comunicação baseada em eventos
- **Microservices Prerequisites**: O que uma organização precisa ter ANTES de adotar microsserviços

### Refactoring como Prática Contínua

O trabalho de Fowler sobre refactoring ensina que:
- Refactoring não é reescrita — é melhoria incremental preservando comportamento
- Code smells são heurísticas para identificar oportunidades de melhoria
- Refactoring seguro depende de testes — sem testes, refactoring é aposta

### Decisões Reversíveis vs Irreversíveis

Fowler categoriza decisões arquiteturais em:
- **Reversíveis**: Podem ser mudadas facilmente depois (escolha de library, formatação, estrutura de pastas)
- **Irreversíveis**: Custam muito para mudar (linguagem, protocolo de comunicação, modelo de dados core)

A pré-programação deve focar em acertar as irreversíveis.

### Sacrificial Architecture

O conceito de que a melhor maneira de planejar é aceitar que o primeiro sistema será substituído. Isso libera para decisões pragmáticas em vez de tentar criar a "arquitetura perfeita".

---

## Práticas Relevantes para Pré-Programação

1. **Classificar decisões por reversibilidade**: No ADR, marcar se a decisão é reversível ou irreversível. Gastar mais tempo de análise em decisões irreversíveis.

2. **Strangler Fig como padrão de migração**: Para todo projeto que substitui um sistema existente, avaliar strangler fig como abordagem padrão. Documentar a sequência de funcionalidades a serem migradas.

3. **Microservices Prerequisites checklist**: Antes de decidir por microsserviços, verificar: CI/CD automatizado? Monitoring robusto? DevOps culture? Provisionamento rápido? Se não, começar com monolito modular.

4. **Evolutionary Architecture**: Projetar sistemas que possam evoluir em vez de tentar prever o futuro. Pontos de extensão, contratos bem definidos e modularidade são mais importantes que "arquitetura definitiva".

5. **Technical debt como conceito de planejamento**: Incluir dívida técnica conhecida no registro de riscos. Fowler distingue debt prudente (consciente) de imprudente (ignorância), deliberada de inadvertente.

6. **Two Pizza Team como restrição de design**: Se o componente precisa de mais de um "time de duas pizzas" para ser mantido, provavelmente é grande demais e precisa ser dividido.

7. **YAGNI (You Aren't Gonna Need It)**: Durante o design, questionar cada componente com "precisamos disso AGORA ou estamos planejando para um futuro hipotético?". Manter no design apenas o que tem justificativa concreta.
