# Implementing Domain-Driven Design

## Informações Gerais

- **Titulo:** Implementing Domain-Driven Design
- **Autor:** Vaughn Vernon
- **Ano:** 2013

## Tese Central

DDD nao e apenas um conjunto de padroes taticos — e uma abordagem completa para alinhar software ao negocio. O livro preenche a lacuna entre a teoria de Eric Evans e a implementacao pratica, fornecendo guias concretos para aplicar bounded contexts, aggregates, domain events e outros padroes em projetos reais, incluindo integracao com arquiteturas modernas como CQRS e Event Sourcing.

## Conceitos-Chave para Pre-Programacao

### 1. Aggregates na Pratica
Regras praticas para design de aggregates: prefira aggregates pequenos, referencie outros aggregates por identidade (nao por objeto), use consistencia eventual entre aggregates. Na pre-programacao, essas regras guiam a modelagem de limites transacionais.

### 2. CQRS (Command Query Responsibility Segregation)
Separar o modelo de leitura do modelo de escrita. O lado de comando aplica regras de negocio e persiste estado. O lado de consulta serve dados otimizados para leitura. Na pre-programacao, decidir se CQRS e necessario e onde aplica-lo.

### 3. Event Sourcing
Persistir o estado como uma sequencia de eventos em vez de snapshots. Permite reconstruir estado historico, auditoria completa e projecoes multiplas dos mesmos dados. Na pre-programacao, avaliar custo-beneficio: poder vs. complexidade.

### 4. Domain Events entre Bounded Contexts
Domain events como mecanismo de integracao entre contexts. Padroes de publicacao e subscricao. Garantias de entrega (at-least-once, exactly-once). Na pre-programacao, definir contratos de eventos com cuidado.

### 5. Repositories e Persistence
O repository e a abstracao que isola o dominio da infraestrutura de persistencia. Vernon detalha como implementar repositories que respeitem os limites do aggregate. Na pre-programacao, a definicao do repository inclui o contrato de busca e persistencia.

### 6. Application Services vs. Domain Services
Application services orquestram use cases e coordenam objetos de dominio. Domain services encapsulam logica de negocio que nao pertence naturalmente a uma entidade ou value object. Na pre-programacao, distinguir responsabilidades evita camadas inchadas.

### 7. Integracao de Bounded Contexts
Estrategias praticas: REST, messaging, RPC. Padroes: Published Language, Open Host Service, Anticorruption Layer. Na pre-programacao, a escolha do mecanismo de integracao afeta latencia, acoplamento e confiabilidade.

## Como Aplicar no Squad

### Na Modelagem de Aggregates
- Aplicar a regra de aggregates pequenos: um aggregate = uma invariante de negocio.
- Referenciar outros aggregates por ID, nao por referencia direta.
- Definir limites de consistencia: forte dentro do aggregate, eventual entre aggregates.
- Documentar invariantes de negocio explicitamente no design doc.

### Na Decisao sobre CQRS/Event Sourcing
- Avaliar se a complexidade de CQRS/ES e justificada pelo dominio.
- Usar CQRS quando padroes de leitura e escrita sao fundamentalmente diferentes.
- Usar Event Sourcing quando historico completo e auditoria sao requisitos de negocio.
- Documentar o custo operacional adicional dessas escolhas.

### Na Integracao entre Servicos
- Definir contratos de eventos com schema evolution em mente.
- Escolher mecanismo de integracao (sincrono vs. assincrono) com base em requisitos de latencia e acoplamento.
- Planejar anticorruption layers para integracao com sistemas legados.
- Definir estrategia de idempotencia para consumers de eventos.

### Nos Criterios de Readiness
- "Aggregates estao dimensionados corretamente (uma invariante por aggregate)?"
- "A estrategia de consistencia (forte vs. eventual) esta definida por boundary?"
- "Contratos de eventos entre contexts estao especificados?"
- "Se CQRS/ES foi escolhido, o custo operacional esta documentado?"

## Citacoes Importantes

> "Design each Aggregate with a single-transaction consistency boundary."

> "Reference other Aggregates by identity, not by direct object reference."

> "Use eventual consistency between Aggregates. This is often overlooked."

> "A Bounded Context is an explicit boundary within which a domain model exists."

> "The model is the code, and the code is the model."

## Relacao com Outros Livros de Referencia

- **DDD (Evans):** Vernon implementa os conceitos de Evans com exemplos concretos e codigo.
- **DDIA (Kleppmann):** Kleppmann fornece a base teorica de consistencia e distribuicao que fundamenta as decisoes de Vernon.
- **Release It! (Nygard):** Complementa com padroes de estabilidade para os mecanismos de integracao de Vernon.
