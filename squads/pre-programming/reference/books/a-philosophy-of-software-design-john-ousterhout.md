# A Philosophy of Software Design

## Informações Gerais

- **Titulo:** A Philosophy of Software Design
- **Autor:** John Ousterhout
- **Ano:** 2018

## Tese Central

A complexidade é o maior inimigo do desenvolvimento de software. Ela se acumula incrementalmente por meio de decisões aparentemente pequenas, e a principal tarefa de um projetista de software é minimizar a complexidade dos sistemas ao longo do tempo. A complexidade se manifesta em três formas: amplificação de mudanças, carga cognitiva e desconhecidos desconhecidos (unknown unknowns).

## Conceitos-Chave para Pre-Programacao

### 1. Complexidade Incremental
A complexidade nunca surge de uma unica decisao catastrofica. Ela se acumula por meio de centenas de pequenas escolhas de design. Na pre-programacao, cada decisao de interface, cada contrato de API e cada dependencia adicionada contribui para a complexidade total do sistema.

### 2. Modulos Profundos vs. Rasos
Modulos profundos oferecem interfaces simples que escondem implementacoes complexas. Modulos rasos expoe complexidade desnecessaria. Durante a fase de design, preferir interfaces estreitas e profundas reduz a complexidade global do sistema.

### 3. Information Hiding e Information Leakage
Information hiding e o principio mais importante para alcancar modulos profundos. Information leakage ocorre quando conhecimento de design que deveria estar encapsulado em um modulo se espalha por outros. Na pre-programacao, identificar vazamentos de informacao nos contratos entre servicos e essencial.

### 4. Design It Twice
Sempre considerar pelo menos duas abordagens diferentes antes de escolher uma. Isso previne vieses cognitivos e frequentemente leva a solucoes melhores. No squad de pre-programacao, isso se traduz em exigir alternativas explicitamente nos design docs.

### 5. Definir Erros Fora de Existencia (Define Errors Out of Existence)
Projetar interfaces de modo que condicoes de erro nao possam existir, em vez de adicionar tratamento de excecoes em cascata. Isso simplifica tanto a implementacao quanto a compreensao do sistema.

### 6. Camadas de Abstracao
Cada camada de abstracao deve fornecer uma visao diferente e mais simples do sistema. Camadas que simplesmente repassam chamadas (pass-through) adicionam complexidade sem valor. Na pre-programacao, avaliar se cada camada proposta realmente simplifica o entendimento.

## Como Aplicar no Squad

### Na Avaliacao de Design Docs
- Verificar se cada modulo proposto e "profundo" — interface simples, funcionalidade rica.
- Identificar information leakage entre componentes e servicos.
- Exigir a secao "Alternativas Consideradas" com pelo menos duas opcoes genuinas.
- Avaliar se as camadas de abstracao propostas realmente simplificam o sistema.

### Na Definicao de Contratos e APIs
- Preferir APIs com poucas operacoes poderosas em vez de muitas operacoes granulares.
- Aplicar o principio de "definir erros fora de existencia" nos contratos.
- Verificar se detalhes de implementacao estao vazando pelas interfaces.

### Nos Criterios de Readiness
- Incluir checklist de complexidade: "O design foi avaliado quanto a information leakage?"
- Verificar se o principio "Design It Twice" foi aplicado em decisoes arquiteturais criticas.
- Avaliar se a complexidade total do sistema e proporcional ao problema sendo resolvido.

### Na Estimativa de Esforco
- Reconhecer que complexidade escondida e a principal causa de estimativas erradas.
- Usar a profundidade/rasura dos modulos como heuristica para estimar dificuldade de implementacao.

## Citacoes Importantes

> "Complexity is anything related to the structure of a software system that makes it hard to understand and modify the system."

> "The most important technique for achieving deep modules is information hiding."

> "If a system has a clean and simple design, then it will be easy to modify and extend. If it is complex, it will be difficult and expensive to make changes."

> "The best modules are those whose interfaces are much simpler than their implementations."

> "Complexity is incremental: you have to sweat the small stuff."

> "If you're not making the design better, you are probably making it worse."

## Relacao com Outros Livros de Referencia

- **Clean Architecture (Martin):** Complementa com princípios SOLID, mas Ousterhout critica a granularidade excessiva de classes que pode criar modulos rasos.
- **DDD (Evans):** Os bounded contexts de DDD alinham-se com o conceito de modulos profundos quando bem definidos.
- **Fundamentals of Software Architecture:** A avaliacao de trade-offs arquiteturais se beneficia do framework de complexidade de Ousterhout.
