# Paralisia por Análise

## Viés/Efeito

**Paralisia por Análise (Analysis Paralysis):** A incapacidade de tomar decisões quando confrontado com muitas opções, informação excessiva ou medo de escolher errado. Em pré-programação, manifesta-se como semanas de avaliação sem conclusão, reuniões intermináveis de arquitetura, e ciclos de "precisamos de mais informação" que nunca terminam.

## Descrição

A paralisia por análise é distinta da diligência. Diligência é analisar até ter informação suficiente para decidir. Paralisia é continuar analisando depois que a informação já é suficiente — motivada por medo de errar, perfeccionismo ou falta de framework de decisão.

Jeff Bezos distingue decisões Type 1 (irreversíveis, merecem análise profunda) de Type 2 (reversíveis, devem ser decididas rápido com 70% de certeza). A maioria das decisões em software é Type 2, mas times as tratam como Type 1.

## Como se Manifesta em Pré-Programação

### Na Escolha de Tecnologia
- Semanas avaliando 8 frameworks quando 3 atendem o requisito
- Planilhas comparativas intermináveis sem critérios de corte
- "Precisamos fazer mais um POC" quando os dois primeiros já mostraram resultado claro
- **Custo real:** Enquanto o time avalia, o deadline se aproxima e a decisão é tomada às pressas no final

### Em Design Reviews
- Reuniões de 2h que terminam com "vamos pensar mais"
- Mesma decisão de arquitetura rediscutida em 3 sessões diferentes
- Ninguém quer ser o primeiro a propor porque "e se estiver errado?"
- **Custo real:** Time desengaja, decisões são tomadas por inércia ou pelo mais vocal

### Na Definição de Escopo
- "Precisamos de mais informação do stakeholder" usado como desculpa para não definir
- Escopo muda a cada reunião porque ninguém fecha
- MVP vira "fazemos tudo" porque cortar é decidir e decidir dá medo
- **Custo real:** Escopo cresce até ser irrealizável

## Como Mitigar

### 1. Classificar Decisões (Type 1 vs Type 2)
Antes de analisar, perguntar: "Se escolhermos errado, qual o custo de reverter?"
- **Type 1 (irreversível):** Database principal, linguagem core → análise profunda justificada
- **Type 2 (reversível):** Library de logging, formato de config → decidir em 30 minutos

**Implementação prática:**
- No início de cada design review, classificar as decisões pendentes
- Type 2: timebox de 30min, decidir com 70% de certeza
- Type 1: deep work session dedicada, máximo 2 por dia

### 2. Definir Critérios de Corte Antes de Pesquisar
Antes de avaliar opções, definir: "O que faz uma opção ser descartada?"
Se a opção não atende os critérios de corte, eliminar antes de analisar.

**Implementação prática:**
- Máximo 3 opções na análise final (eliminar antes de comparar)
- Critérios de corte: must-have vs nice-to-have definidos antes da pesquisa

### 3. Timeboxing Rigoroso
Toda decisão tem deadline. Se o deadline chega sem decisão, o Chief decide com a informação disponível.

**Implementação prática:**
- Type 2: 1-2 horas de análise, máximo
- Type 1: 1-3 dias de análise, máximo
- Se mais tempo for necessário, é spike (pesquisa com deliverable)

### 4. Bias para Ação
Em caso de empate entre opções, escolher qualquer uma e seguir. A maioria das decisões reversíveis tem custo de reversão menor que custo de atraso.

"A paralisia custa mais que uma decisão subótima que pode ser corrigida."

## Referências
- Bezos, J. — 2016 Letter to Shareholders (Type 1 vs Type 2 decisions)
- Schwartz, B. — The Paradox of Choice
- Ousterhout, J. — A Philosophy of Software Design (complexity and simplicity of decision)
