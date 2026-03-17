# Kent Beck — Resumo de Autoridade

## Autor

**Nome**: Kent Beck
**Afiliação**: Engenheiro de software, criador do XP e do TDD
**Obras Principais**: "Extreme Programming Explained" (1999, 2a ed. 2004), "Test Driven Development: By Example" (2002), "Tidy First?" (2023)
**Área de Expertise**: Metodologias ágeis, TDD, design de software, padrões de implementação

---

## Tese Central

Software excelente é construído através de **feedback rápido**, **simplicidade**, **comunicação** e **coragem**. O design emerge da prática disciplinada de escrever testes antes do código (TDD), refatorar continuamente e manter o código limpo. A chave não é prever o futuro perfeito, mas criar sistemas que sejam fáceis de mudar quando o futuro chegar.

Em "Tidy First?", Beck refina: antes de adicionar funcionalidade, faça pequenos arrumações (tidyings) no código que tornem a mudança mais fácil. Separar arrumação de comportamento é fundamental.

---

## Conceitos-Chave

### 1. Test-Driven Development (TDD)
Ciclo Red-Green-Refactor:
- **Red**: Escreva um teste que falha
- **Green**: Escreva o código mínimo para o teste passar
- **Refactor**: Melhore o código mantendo os testes verdes

TDD não é sobre testes — é sobre design. Escrever o teste primeiro força pensar na interface antes da implementação.

### 2. Simplicidade (YAGNI e KISS)
- Faça a coisa mais simples que pode funcionar
- Não adicione funcionalidade que não é necessária agora
- Complexidade prematura é tão perigosa quanto otimização prematura

### 3. Valores de XP
- **Comunicação**: Código é comunicação entre humanos, não instrução para máquinas
- **Simplicidade**: Faça o que é necessário, nada mais
- **Feedback**: Quanto mais rápido, melhor
- **Coragem**: Faça as mudanças difíceis necessárias
- **Respeito**: Toda contribuição tem valor

### 4. Tidyings (Arrumações)
Pequenas melhorias no código que precedem mudanças comportamentais:
- Extrair helper
- Reordenar declarações
- Remover dead code
- Renomear para clareza

Separar commits de tidying de commits de comportamento mantém histórico limpo.

### 5. Make the Change Easy, Then Make the Easy Change
Primeiro, refatore para que a mudança desejada seja simples. Depois, faça a mudança simples. Duas etapas pequenas são mais seguras que uma grande.

---

## Aplicação ao Squad

- **TDD no plano de testes**: Os cenários de teste definidos na pré-programação são os "Red" do TDD. O time de desenvolvimento recebe os testes como especificação — implementa até ficarem verdes.

- **Simplicidade como critério de revisão**: Em readiness reviews, questionar: "Existe uma forma mais simples de resolver isso?" Design que requer explicação longa provavelmente é complexo demais.

- **Feedback loops curtos no processo**: O squad não espera semanas para validar premissas. Valida no mesmo dia, se possível. Sprint de pré-programação não deve exceder 1 semana para features normais.

- **"Make the Change Easy" na análise de legado**: Ao planejar integração com legado, primeiro identificar que refatorações no legado facilitariam a integração. Separar o "tornar fácil" do "fazer a mudança".

---

## Citações Relevantes

> "I'm not a great programmer; I'm just a good programmer with great habits."

> "Optimism is an occupational hazard of programming; feedback is the treatment."

> "Make the change easy (warning: this may be hard), then make the easy change."

> "Do the simplest thing that could possibly work."

> "Any fool can write code that a computer can understand. Good programmers write code that humans can understand."

> "First make the change easy, then make the easy change. To do those things in the opposite order is folly."
