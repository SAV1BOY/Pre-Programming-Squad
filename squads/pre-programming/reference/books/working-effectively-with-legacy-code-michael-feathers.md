# Working Effectively with Legacy Code

## Informações Gerais

- **Titulo:** Working Effectively with Legacy Code
- **Autor:** Michael Feathers
- **Ano:** 2004

## Tese Central

Codigo legado e codigo sem testes. A principal barreira para modificar sistemas existentes com seguranca e a falta de testes automatizados. O livro fornece tecnicas praticas para colocar codigo existente sob teste, quebrando dependencias de forma segura e criando "costuras" (seams) que permitem isolar e testar componentes individualmente.

## Conceitos-Chave para Pre-Programacao

### 1. Definicao de Codigo Legado
Codigo sem testes e codigo legado, independentemente de sua idade. Na pre-programacao, quando o projeto envolve modificacao de codigo existente, a primeira pergunta e: "tem testes?"

### 2. O Dilema do Legado
Para mudar codigo com seguranca, precisamos de testes. Para colocar testes, precisamos mudar o codigo. Feathers fornece tecnicas para quebrar esse ciclo com mudancas seguras e minimamente invasivas.

### 3. Seams (Costuras)
Um seam e um ponto no codigo onde o comportamento pode ser alterado sem modificar o codigo em si. Tipos: object seams, preprocessing seams, link seams. Na pre-programacao, identificar seams existentes guia a estrategia de modificacao.

### 4. Characterization Tests
Testes que documentam o comportamento atual do sistema, nao o comportamento desejado. Sao a rede de seguranca antes de qualquer mudanca. Na pre-programacao de modificacoes em legado, planejar characterization tests primeiro.

### 5. Sprout Method / Sprout Class
Quando precisa adicionar funcionalidade nova em codigo legado, criar um novo metodo ou classe testavel em vez de modificar o existente. Na pre-programacao, essa estrategia permite entrega incremental sem reescritas.

### 6. Wrap Method / Wrap Class
Envolver codigo existente com nova funcionalidade sem modifica-lo. Decorator pattern aplicado a legado. Na pre-programacao, definir estrategia de wrapping quando o codigo existente e intocavel.

### 7. Strangler Fig Pattern
Substituir gradualmente um sistema legado construindo o novo sistema ao redor dele, redirecionando funcionalidades uma a uma. Na pre-programacao, planejar a migracaoincremental com milestones claros.

### 8. Quebrando Dependencias
Tecnicas como Extract Interface, Parameterize Constructor, Extract and Override, Introduce Instance Delegator. Na pre-programacao, identificar dependencias que precisam ser quebradas e planejar a sequencia.

## Como Aplicar no Squad

### Na Avaliacao de Projetos com Legado
- Avaliar a cobertura de testes existente antes de planejar mudancas.
- Identificar seams disponiveis para injecao de testes.
- Estimar o esforco de "tornar testavel" como parte do esforco total.
- Planejar characterization tests como primeira fase do trabalho.

### Na Estrategia de Migracao
- Aplicar Strangler Fig Pattern para substituicoes graduais.
- Definir milestones de migracao com rollback points.
- Preferir Sprout Method/Class sobre modificacao de codigo legado.
- Planejar coexistencia entre novo e legado durante a transicao.

### Na Estimativa de Esforco
- Incluir o custo de colocar codigo sob teste nas estimativas.
- Reconhecer que trabalhar com legado e inerentemente mais lento.
- Planejar tempo para entender comportamento existente (characterization).
- Incluir margem para surpresas — legado sempre tem comportamento inesperado.

### Nos Criterios de Readiness
- "A cobertura de testes existente foi mapeada?"
- "Seams foram identificados para injecao de testes?"
- "A estrategia de migracaoincremental esta definida com milestones?"
- "Characterization tests estao planejados como primeira fase?"
- "O Strangler Fig Pattern foi considerado para substituicoes?"

## Citacoes Importantes

> "To me, legacy code is simply code without tests."

> "In the end, it comes down to this: we can be effective at changing code, or we can be unafraid to change code, but rarely both at the same time without good tools."

> "When we change code, we should have tests in place. To put tests in place, we often have to change code."

> "A seam is a place where you can alter behavior in your program without editing in that place."

> "The first step in working with legacy code is to get it under test."

## Relacao com Outros Livros de Referencia

- **TDD by Example (Beck):** Feathers mostra como aplicar TDD em codigo que nao foi construido para testes.
- **Clean Architecture (Martin):** Clean Architecture previne a criacao de legado futuro; Feathers ajuda a lidar com o legado presente.
- **Release It! (Nygard):** Ambos lidam com a realidade de sistemas em producao vs. idealizacoes de design.
