# Qualidade de User Stories

## O que e uma User Story de Qualidade

Uma user story de qualidade nao e apenas um ticket com formato "Como [persona], quero [acao], para [beneficio]". E um artefato de comunicacao que expressa uma necessidade do usuario, complementado por criterios de aceitacao verificaveis, exemplos concretos e contexto suficiente para que a equipe entenda o problema e possa propor a melhor solucao.

## Criterios INVEST

Bill Wake definiu os criterios INVEST para avaliar a qualidade de user stories:

### I - Independent (Independente)
A story pode ser desenvolvida e entregue independentemente de outras.
**Na pre-programacao:** Verificar se a story tem dependencias ocultas que bloqueiam a implementacao. Se duas stories devem ser implementadas juntas, considere combina-las.

### N - Negotiable (Negociavel)
A story e um convite para conversa, nao um contrato fixo. Os detalhes sao negociados entre equipe e stakeholders.
**Na pre-programacao:** Se a story prescreve a solucao tecnica em vez de descrever o problema, ela nao e negociavel. Questionar: "Existe outra forma de resolver isso?"

### V - Valuable (Valiosa)
A story entrega valor mensuravel para o usuario ou negocio.
**Na pre-programacao:** Se nao conseguimos articular o valor de negocio, a story nao deveria existir. Perguntar: "Qual metrica melhora com esta entrega?"

### E - Estimable (Estimavel)
A equipe consegue estimar o esforco com razoavel confianca.
**Na pre-programacao:** Se a equipe nao consegue estimar, faltam informacoes. Identificar lacunas e resolver antes de comprometer a equipe.

### S - Small (Pequena)
A story pode ser completada em menos de uma sprint.
**Na pre-programacao:** Stories que levam mais de uma sprint geralmente escondem complexidade. Quebrar em stories menores que entregam valor incrementalmente.

### T - Testable (Testavel)
Existe uma forma clara de verificar se a story foi completada corretamente.
**Na pre-programacao:** Criterios de aceitacao devem ser especificos o suficiente para gerar testes automatizados.

## Anatomia de uma User Story Completa

```markdown
## Story: [Titulo curto e descritivo]

### Narrativa
Como [persona com contexto],
quero [acao especifica],
para que [beneficio mensuravel].

### Contexto
[Por que essa story e importante agora? Que problema ela resolve?
Dados que justificam a prioridade.]

### Criterios de Aceitacao

#### Cenario 1: [Nome do cenario]
Dado [pre-condicao]
Quando [acao do usuario]
Entao [resultado esperado]

#### Cenario 2: [Nome do cenario]
Dado [pre-condicao]
Quando [acao do usuario]
Entao [resultado esperado]

### Cenarios de Erro
#### Quando [condicao de erro]
Entao [comportamento esperado]

### Requisitos Nao-Funcionais
- Performance: [metrica]
- Seguranca: [requisito]
- Acessibilidade: [requisito]

### Fora de Escopo
- [O que nao esta incluido nesta story]

### Dependencias
- [Outras stories ou sistemas]

### Metricas de Sucesso
- [Como medir se a story atingiu o objetivo]
```

## Exemplos de Boa vs. Ma Qualidade

### Exemplo 1: Busca de Produtos

**Ma qualidade:**
```
Como usuario, quero buscar produtos para encontrar o que preciso.
```
Problemas: Persona generica, acao vaga, sem criterios de aceitacao, nao testavel, nao estimavel.

**Boa qualidade:**
```
Story: Busca por nome de produto com tolerancia a erros de digitacao

Como comprador frequente do app mobile,
quero encontrar produtos mesmo quando erro a digitacao,
para que eu nao precise adivinhar a grafia exata do produto.

Criterios de Aceitacao:

Cenario 1: Busca com erro de 1 caractere
Dado que o produto "Samsung Galaxy S25" existe no catalogo
Quando eu busco por "Samsnug Galaxy"
Entao o resultado inclui "Samsung Galaxy S25" nos primeiros 5 resultados

Cenario 2: Busca sem resultados
Dado que nenhum produto corresponde a busca
Quando eu busco por "xyzabc123"
Entao vejo a mensagem "Nenhum produto encontrado"
E vejo sugestoes de categorias populares

Cenario de Erro: Busca vazia
Quando eu envio uma busca com campo vazio
Entao vejo os produtos mais populares

Requisitos Nao-Funcionais:
- Latencia de busca: p99 < 300ms
- Resultados: maximo 50 por pagina com paginacao

Fora de Escopo:
- Busca por imagem (story separada)
- Autocomplete (story separada)

Metricas: Reduzir taxa de "busca sem resultado" de 23% para <10%.
```

## Checklist de Qualidade para Pre-Programacao

### Clareza
- [ ] A persona e especifica (nao "usuario generico")?
- [ ] O problema e claro (nao apenas a solucao)?
- [ ] Os criterios de aceitacao sao especificos e verificaveis?
- [ ] Cenarios de erro estao descritos?
- [ ] O escopo negativo esta definido (fora de escopo)?

### Completude
- [ ] Requisitos nao-funcionais estao quantificados?
- [ ] Dependencias estao identificadas?
- [ ] Metricas de sucesso estao definidas?
- [ ] Edge cases foram considerados?
- [ ] Ha exemplos concretos para cada criterio?

### Viabilidade Tecnica
- [ ] A equipe consegue estimar com confianca?
- [ ] As dependencias tecnicas estao resolvidas?
- [ ] A story pode ser entregue em uma sprint?
- [ ] O design tecnico e conhecido ou precisa de spike?

### Valor
- [ ] O valor de negocio e claro e mensuravel?
- [ ] A priorizacao e justificada por dados?
- [ ] A story resolve um problema real de usuarios?

## Anti-Padroes em User Stories

### A Story Tecnica
"Como desenvolvedor, quero refatorar o modulo de pagamento."
**Problema:** Nao expressa valor para o usuario final.
**Correcao:** Vincular ao problema de negocio: "Para reduzir o tempo de deploy do modulo de pagamento de 4h para 30min, permitindo correcoes mais rapidas."

### A Story Gigante (Epic Disfarçado)
"Como admin, quero gerenciar todos os usuarios do sistema."
**Problema:** Muito grande, impossivel de estimar ou entregar em uma sprint.
**Correcao:** Quebrar em stories menores: listar usuarios, criar usuario, editar permissoes, desativar usuario.

### A Story Prescritiva
"Como usuario, quero um dropdown com opcoes A, B e C na tela X."
**Problema:** Prescreve a solucao, nao descreve o problema.
**Correcao:** "Como usuario, quero filtrar resultados por categoria para encontrar itens relevantes mais rapido."

### A Story Ambigua
"O sistema deve ser rapido e facil de usar."
**Problema:** Impossivel de testar ou implementar.
**Correcao:** "Latencia p99 < 200ms. Taxa de conclusao de tarefa > 90% em teste de usabilidade."
