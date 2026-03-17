# Clean Architecture

## Informações Gerais

- **Titulo:** Clean Architecture: A Craftsman's Guide to Software Structure and Design
- **Autor:** Robert C. Martin (Uncle Bob)
- **Ano:** 2017

## Tese Central

A arquitetura de um sistema de software deve maximizar a quantidade de decisoes que podem ser adiadas. Separando regras de negocio de detalhes de implementacao (frameworks, bancos de dados, UI), criamos sistemas flexiveis, testaveis e independentes de tecnologia. A direcao das dependencias deve sempre apontar para dentro, em direcao as politicas de nivel mais alto.

## Conceitos-Chave para Pre-Programacao

### 1. A Regra de Dependencia
Dependencias de codigo-fonte devem apontar apenas para dentro, em direcao as politicas de nivel mais alto. Camadas externas (frameworks, drivers, UI) dependem de camadas internas (entidades, use cases), nunca o contrario.

### 2. Principios SOLID
- **S - Single Responsibility:** Um modulo deve ter um, e apenas um, motivo para mudar.
- **O - Open/Closed:** Aberto para extensao, fechado para modificacao.
- **L - Liskov Substitution:** Subtipos devem ser substituiveis por seus tipos base.
- **I - Interface Segregation:** Clientes nao devem depender de interfaces que nao usam.
- **D - Dependency Inversion:** Depender de abstracoes, nao de implementacoes concretas.

### 3. Entidades e Use Cases
Entidades encapsulam regras de negocio criticas e independentes de aplicacao. Use cases encapsulam regras de negocio especificas da aplicacao. Na pre-programacao, identificar claramente essa separacao.

### 4. Boundaries (Limites Arquiteturais)
Linhas que separam componentes de software e protegem cada lado de saber sobre o outro. Na pre-programacao, definir onde estao os limites arquiteturais e o que cruza cada limite.

### 5. Gritando Arquitetura (Screaming Architecture)
A arquitetura de um sistema deve gritar o proposito do sistema, nao os frameworks utilizados. Um sistema de saude deveria gritar "saude", nao "Spring Boot" ou "React".

### 6. Humildade quanto a Frameworks
Frameworks sao detalhes, nao a arquitetura. O design deve permitir trocar frameworks sem reescrever regras de negocio. Na pre-programacao, evitar que decisoes de framework contaminem o modelo de dominio.

## Como Aplicar no Squad

### Na Definicao de Limites Arquiteturais
- Mapear os limites entre dominio de negocio e infraestrutura tecnica.
- Verificar que a direcao das dependencias esta correta (de fora para dentro).
- Identificar onde inversao de dependencia e necessaria.
- Proteger o modelo de dominio de contaminacao por detalhes de framework.

### Na Avaliacao de Design Docs
- Verificar se o design "grita" o dominio do problema, nao a stack tecnologica.
- Avaliar se entidades e use cases estao claramente separados de adaptadores e frameworks.
- Confirmar que principios SOLID foram considerados na definicao de interfaces.
- Checar se decisoes de framework podem ser adiadas ou revertidas.

### Na Definicao de Contratos entre Camadas
- Definir interfaces claras nos limites arquiteturais.
- Aplicar Interface Segregation: clientes nao devem conhecer metodos que nao usam.
- Usar Dependency Inversion para desacoplar camadas.

### Nos Criterios de Readiness
- "O modelo de dominio esta livre de dependencias de framework?"
- "A direcao das dependencias esta correta em todas as camadas?"
- "Entidades e use cases estao claramente identificados e separados?"
- "Decisoes de tecnologia (BD, framework, UI) podem ser alteradas sem reescrever o dominio?"

## Citacoes Importantes

> "The goal of software architecture is to minimize the human resources required to build and maintain the required system."

> "A good architecture allows major decisions to be deferred."

> "The architecture should scream the use cases of the system."

> "Good architectures are centered on use cases so that architects can safely describe the structures that support those use cases without committing to frameworks, tools, and environments."

> "Your architectures should tell readers about the system, not about the frameworks you used in your system."

## Relacao com Outros Livros de Referencia

- **DDD (Evans):** Clean Architecture fornece a estrutura de camadas; DDD fornece as tecnicas para modelar o dominio dentro dessas camadas.
- **A Philosophy of Software Design (Ousterhout):** Ousterhout critica a granularidade excessiva do SOLID, argumentando que muitas classes pequenas podem criar modulos rasos.
- **Fundamentals of Software Architecture:** Richards/Ford contextualizam Clean Architecture como um dos muitos estilos possiveis, nao como a unica resposta.
