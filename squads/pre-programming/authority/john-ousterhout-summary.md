# John Ousterhout — Resumo de Autoridade

## Autor

**Nome**: John Ousterhout
**Afiliação**: Professor de Ciência da Computação, Stanford University
**Obra Principal**: "A Philosophy of Software Design" (2018, 2a edição 2021)
**Área de Expertise**: Design de software, complexidade de sistemas, interfaces de módulos

---

## Tese Central

A maior causa de degradação de software ao longo do tempo é a **complexidade acumulada** — e a complexidade surge de duas fontes: **dependências** (quando um módulo não pode ser entendido isoladamente) e **obscuridade** (quando informação importante não é óbvia). O papel do designer de software é combater a complexidade implacavelmente, fazendo escolhas de design que minimizam ambas.

A abordagem de Ousterhout é diametralmente oposta ao dogma de "classes/funções pequenas": ele argumenta que **módulos profundos** (interfaces simples escondendo implementação complexa) são superiores a **módulos rasos** (interfaces complicadas escondendo implementação trivial).

---

## Conceitos-Chave

### 1. Complexidade como Inimigo Principal
Complexidade é qualquer coisa que torna o software difícil de entender ou modificar. Manifesta-se como: amplificação de mudanças (uma mudança requer alterações em muitos lugares), carga cognitiva (quanta informação o dev precisa manter na cabeça) e incógnitas desconhecidas (o que você não sabe que não sabe).

### 2. Módulos Profundos vs Rasos
Um módulo profundo tem interface simples mas implementação rica — como um sistema de arquivos Unix (open, read, write, close servem para qualquer dispositivo de storage). Um módulo raso tem interface complexa que não esconde muita funcionalidade — como uma classe Java com getters e setters para cada campo.

### 3. Information Hiding
Cada módulo deve encapsular conhecimento sobre decisões de design. Quando essa informação "vaza" para outros módulos, cria dependências que amplificam mudanças.

### 4. Design It Twice
Para decisões de design importantes, projetar pelo menos duas alternativas antes de escolher. A comparação revela trade-offs que uma única proposta esconde.

### 5. Comentários como Design
Comentários não são luxo — são ferramenta de design. Escrever o comentário antes do código (comment-first approach) força clareza de pensamento.

---

## Aplicação ao Squad

- **Revisão de interfaces no design doc**: Avaliar se as interfaces propostas são "profundas" — interface simples, implementação rica. Rejeitar designs com interfaces complexas que expõem detalhes internos.

- **"Design It Twice" como prática**: Para toda decisão de arquitetura significativa, o squad exige pelo menos duas propostas antes de decidir. ADRs sem alternativas são devolvidos para complementação.

- **Avaliação de complexidade em readiness reviews**: Perguntar para cada componente: "Qual é a carga cognitiva para um dev novo entender e modificar isso?" Se a resposta é alta, o design precisa ser simplificado.

- **Comment-first nos contratos de API**: Escrever a documentação da API antes de especificar os endpoints. Se a documentação é difícil de escrever, a API é difícil de usar.

---

## Citações Relevantes

> "The most fundamental problem in computer science is problem decomposition: how to take a complex problem and divide it up into pieces that can be solved independently."

> "Modules should be deep. The best modules are those whose interfaces are much simpler than their implementations."

> "Complexity is incremental: it's not one particular thing that makes a system complicated, but the accumulation of dozens or hundreds of small things."

> "If a system has a clean and simple design, it will be easier to modify, debug, and test. In contrast, every increment of complexity makes the system harder to work with."

> "The most important thing is to design interfaces that are simple and clear, even if that makes the implementation more complex."
