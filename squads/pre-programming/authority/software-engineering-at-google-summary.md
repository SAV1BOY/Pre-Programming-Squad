# Software Engineering at Google — Resumo de Autoridade

## Autor

**Autores**: Titus Winters, Tom Manshreck, Hyrum Wright (editores)
**Obra**: "Software Engineering at Google: Lessons Learned from Programming Over Time" (O'Reilly, 2020)
**Contexto**: Compilação de práticas de engenharia de software do Google, escritas por engenheiros que as vivenciam diariamente

---

## Tese Central

Software engineering é programação integrada ao longo do tempo. A diferença entre "programar" e "fazer engenharia de software" é considerar a sustentabilidade da base de código ao longo de anos e décadas. Decisões que parecem eficientes no curto prazo podem ser desastrosas no longo prazo, e vice-versa. A escala do Google (bilhões de linhas de código, dezenas de milhares de engenheiros) amplia tanto os benefícios de boas práticas quanto os custos de más decisões.

---

## Conceitos-Chave

### 1. Hyrum's Law
"Com um número suficiente de usuários de uma API, todo comportamento observável do sistema será dependido por alguém." Implicação: qualquer mudança pode quebrar algum consumidor, mesmo que esteja dentro do contrato. APIs devem ser desenhadas para minimizar a superfície de comportamento observável.

### 2. Beyoncé Rule
"Se você gostou, deveria ter colocado um teste." Se uma propriedade do sistema é importante, ela deve ser testada. Se não é testada, pode ser alterada por qualquer outra mudança.

### 3. Shift Left
Mover atividades de validação para o mais cedo possível no processo. Encontrar bugs em design review é mais barato que em code review, que é mais barato que em produção. A pré-programação é o shift-left definitivo.

### 4. Monorepo e Large-Scale Changes
Google mantém todo o código em um único repositório (monorepo) com ferramentas que permitem mudanças atômicas em milhares de arquivos. Isso demonstra que escala não requer repositórios separados — requer ferramentas adequadas.

### 5. Code Review como Prática Cultural
No Google, 100% do código passa por review. Review não é sobre encontrar bugs — é sobre compartilhar conhecimento, manter padrões e criar ownership coletivo.

### 6. Testing Culture
Testes automatizados são obrigatórios. O Google classifica testes em: pequenos (unitários, < 100ms), médios (integração, < 300s) e grandes (e2e, tempo variável). A grande maioria deve ser pequena.

---

## Aplicação ao Squad

- **Hyrum's Law no design de APIs**: Ao definir contratos de API, considerar que consumidores dependerão de qualquer comportamento, mesmo não documentado. Minimizar superfície observável. Documentar comportamento indefinido explicitamente.

- **"Shift Left" como missão do squad**: O Pre-Programming Squad é a materialização do shift-left. Encontrar problemas antes do código ser escrito é literalmente a razão de existir do squad.

- **Classificação de testes no plano de testes**: Usar a classificação Google (pequenos/médios/grandes) em vez de rótulos vagos. Definir limites de tempo para cada nível.

- **Code review do design**: Não apenas code review — design review. Design docs revisados por peers com a mesma seriedade que código.

- **Beyoncé Rule aplicada a premissas**: Se uma premissa é importante para o projeto, ela deve ser validada (testada). Premissa "importante mas não validada" é contradição.

---

## Citações Relevantes

> "Software engineering is programming integrated over time."

> "With a sufficient number of users of an API, it does not matter what you promise in the contract: all observable behaviors of your system will be depended on by somebody." (Hyrum's Law)

> "If you liked it, you should have put a test on it." (Beyoncé Rule)

> "The cost of a bug grows exponentially the later it is found in the development cycle."

> "Knowledge is half the battle. The other half is establishing processes that help people do the right thing by default."
