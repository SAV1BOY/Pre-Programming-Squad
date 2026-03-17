# Domain-Driven Design

## Informações Gerais

- **Titulo:** Domain-Driven Design: Tackling Complexity in the Heart of Software
- **Autor:** Eric Evans
- **Ano:** 2003

## Tese Central

A complexidade real do software esta no dominio de negocio, nao na tecnologia. O sucesso de um projeto depende de construir um modelo de dominio rico, desenvolvido iterativamente em colaboracao entre desenvolvedores e especialistas do dominio, usando uma linguagem ubiqua compartilhada. O design estrategico (bounded contexts, context maps) e tao importante quanto o design tatico (entidades, value objects, aggregates).

## Conceitos-Chave para Pre-Programacao

### 1. Linguagem Ubiqua (Ubiquitous Language)
Um vocabulario rigoroso e compartilhado entre desenvolvedores e especialistas do dominio. Cada termo tem um significado preciso, usado consistentemente no codigo, documentacao e conversas. Na pre-programacao, estabelecer a linguagem ubiqua e a primeira atividade.

### 2. Bounded Contexts
Um limite explicito dentro do qual um modelo de dominio se aplica. O mesmo termo pode ter significados diferentes em contexts diferentes (ex: "conta" em faturamento vs. "conta" em autenticacao). Na pre-programacao, mapear bounded contexts e essencial.

### 3. Context Mapping
Padroes de relacionamento entre bounded contexts: Partnership, Shared Kernel, Customer-Supplier, Conformist, Anticorruption Layer, Open Host Service, Published Language, Separate Ways. Na pre-programacao, definir como contexts se comunicam.

### 4. Aggregates
Um cluster de entidades e value objects tratados como uma unidade de consistencia. Cada aggregate tem um root entity e um limite de transacao. Na pre-programacao, definir aggregates determina as fronteiras transacionais do sistema.

### 5. Entidades vs. Value Objects
Entidades tem identidade e ciclo de vida. Value objects sao definidos por seus atributos e sao imutaveis. Distinguir corretamente entre eles na pre-programacao simplifica enormemente o design.

### 6. Domain Events
Algo que aconteceu no dominio que os especialistas se importam. Domain events sao a base para comunicacao assincrona entre bounded contexts e para event sourcing.

### 7. Anticorruption Layer (ACL)
Uma camada de traducao que protege um bounded context de ser contaminado pelo modelo de outro. Essencial quando integrando com sistemas legados ou de terceiros.

### 8. Destilacao do Dominio
Identificar o Core Domain (a parte mais valiosa e diferenciadora do negocio) e distingui-lo de Supporting Subdomains e Generic Subdomains. Na pre-programacao, isso direciona onde investir esforco de design.

## Como Aplicar no Squad

### Na Fase de Discovery de Dominio
- Conduzir sessoes de Event Storming para mapear o dominio.
- Estabelecer a linguagem ubiqua como glossario vivo do projeto.
- Identificar bounded contexts e seus relacionamentos.
- Destinar tempo explicito para conversas com especialistas do dominio.

### Na Definicao de Boundaries de Servico
- Usar bounded contexts como guia para definir limites de microsservicos.
- Definir context maps explicitamente: como cada context se relaciona com os demais.
- Identificar onde anticorruption layers sao necessarias.
- Nao forcar um modelo unico para todo o sistema.

### Na Modelagem de Dados e Agregados
- Definir aggregates como unidades de consistencia transacional.
- Identificar invariantes de negocio que determinam os limites dos aggregates.
- Preferir aggregates pequenos que encapsulam uma unica invariante.
- Definir domain events para comunicacao entre aggregates.

### Nos Criterios de Readiness
- "A linguagem ubiqua esta documentada e validada com especialistas do dominio?"
- "Os bounded contexts estao identificados e mapeados?"
- "O core domain foi identificado e priorizado?"
- "Os aggregates tem invariantes de negocio claras?"
- "O context map mostra como os contexts se integram?"

## Citacoes Importantes

> "The heart of software is its ability to solve domain-related problems for its user."

> "If the design, or some central part of it, does not map to the domain model, that model is of little value."

> "When you are not making progress, step back and find a context boundary."

> "The model is distilled knowledge. It is not just any knowledge — it is the most relevant knowledge about the problem domain."

> "Software that lacks a unifying model will grow into a Big Ball of Mud."

> "Explicitly define the context within which a model applies. Keep the model consistent within these bounds."

## Relacao com Outros Livros de Referencia

- **Implementing DDD (Vernon):** Vernon fornece a implementacao pratica dos conceitos de Evans.
- **Clean Architecture (Martin):** A Regra de Dependencia de Martin protege o modelo de dominio de Evans.
- **Team Topologies:** Bounded contexts frequentemente alinham-se com stream-aligned teams.
- **Specification by Example (Adzic):** A linguagem ubiqua de DDD se traduz naturalmente em especificacoes executaveis.
