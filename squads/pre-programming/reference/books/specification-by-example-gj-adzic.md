# Specification by Example

## Informações Gerais

- **Titulo:** Specification by Example: How Successful Teams Deliver the Right Software
- **Autor:** Gojko Adzic
- **Ano:** 2011

## Tese Central

Especificacoes executaveis — exemplos concretos que servem simultaneamente como requisitos, testes de aceitacao e documentacao viva — sao a forma mais eficaz de alinhar negocio e desenvolvimento. Equipes de sucesso colaboram para derivar exemplos concretos de regras de negocio, automatizam esses exemplos como testes e os mantém como documentacao viva do sistema.

## Conceitos-Chave para Pre-Programacao

### 1. Exemplos Concretos como Especificacao
Em vez de escrever requisitos abstratos ("o sistema deve validar CPF"), usar exemplos concretos ("dado CPF 123.456.789-09, o resultado deve ser valido; dado CPF 111.111.111-11, o resultado deve ser invalido"). Exemplos eliminam ambiguidade e sao verificaveis.

### 2. Especificacoes Executaveis
Exemplos que podem ser executados automaticamente como testes. Ferramentas como Cucumber, SpecFlow ou FitNesse transformam especificacoes em suites de testes. Na pre-programacao, definir especificacoes executaveis garante que requisitos sao verificaveis.

### 3. Documentacao Viva (Living Documentation)
Especificacoes executaveis que passam nos testes sao, por definicao, documentacao atualizada do comportamento do sistema. Eliminam o problema de documentacao desatualizada.

### 4. Refinamento Colaborativo de Exemplos
O processo de derivar exemplos deve envolver negocio, desenvolvimento e QA (os "Three Amigos"). A conversa e tao valiosa quanto os exemplos resultantes — ela alinha entendimento.

### 5. Key Examples (Exemplos-Chave)
Nem todo exemplo e igualmente valioso. Exemplos-chave sao aqueles que ilustram regras de negocio criticas, fronteiras (boundary conditions) e cenarios excepcionais. Na pre-programacao, identificar exemplos-chave e uma habilidade critica.

### 6. Automacao sem Mudanca de Processo
A automacao deve se encaixar no processo existente da equipe, nao exigir uma revolucao. Comecar automatizando os exemplos mais criticos e expandir gradualmente.

## Como Aplicar no Squad

### Na Definicao de Requisitos
- Exigir exemplos concretos para cada regra de negocio antes de considerar o requisito "pronto".
- Conduzir sessoes de "Three Amigos" para derivar exemplos colaborativamente.
- Usar formato Given-When-Then para estruturar exemplos.
- Identificar exemplos-chave que cobrem regras criticas e boundary conditions.

### Na Avaliacao de Readiness
- Verificar se cada user story tem exemplos concretos suficientes.
- Avaliar se os exemplos cobrem: cenario feliz, cenarios de erro, boundary conditions.
- Confirmar que exemplos sao verificaveis e nao-ambiguos.
- Checar se exemplos foram validados com stakeholders de negocio.

### Na Estrategia de Testes
- Planejar automacao de especificacoes como testes de aceitacao.
- Definir quais exemplos serao automatizados vs. testados manualmente.
- Escolher ferramentas de automacao de especificacoes na fase de pre-programacao.
- Planejar pipeline de execucao de especificacoes executaveis.

### Na Documentacao
- Usar especificacoes executaveis como fonte de verdade para documentacao.
- Planejar geração automatica de documentacao a partir de especificacoes.
- Eliminar necessidade de documentacao de requisitos separada.

## Citacoes Importantes

> "The biggest value of Specification by Example is that the team gets a shared understanding of what needs to be delivered."

> "Concrete examples are the best way to eliminate ambiguity from requirements."

> "Specifications are not just tests — they are living documentation of the system's behavior."

> "The conversation is more valuable than the resulting artifact."

> "Key examples should illustrate business rules, not test the implementation."

## Relacao com Outros Livros de Referencia

- **TDD by Example (Beck):** SbE estende TDD para o nivel de requisitos de negocio.
- **DDD (Evans):** A linguagem ubiqua de DDD e o vocabulario usado nas especificacoes.
- **Inspired (Cagan):** Especificacoes por exemplo complementam product discovery com verificacao concreta.
