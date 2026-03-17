# Test-Driven Development by Example

## Informações Gerais

- **Titulo:** Test-Driven Development: By Example
- **Autor:** Kent Beck
- **Ano:** 2002

## Tese Central

O desenvolvimento guiado por testes (TDD) e uma tecnica de design, nao apenas de testes. O ciclo Red-Green-Refactor — escrever um teste que falha, fazer o teste passar com o codigo mais simples possivel, refatorar — produz codigo limpo, bem projetado e com cobertura de testes automatica. TDD muda fundamentalmente como pensamos sobre design de software.

## Conceitos-Chave para Pre-Programacao

### 1. O Ciclo Red-Green-Refactor
1. **Red:** Escrever um teste que falha, definindo o comportamento esperado.
2. **Green:** Escrever o codigo mais simples possivel para fazer o teste passar.
3. **Refactor:** Melhorar o design sem mudar o comportamento.

Na pre-programacao, pensar em termos de testes durante o design melhora a qualidade das especificacoes.

### 2. Testes como Especificacao
Testes definem precisamente o que o sistema deve fazer. Na pre-programacao, escrever criterios de aceitacao no formato de testes (Given-When-Then) elimina ambiguidade.

### 3. Baby Steps
Avançar em passos muito pequenos e verificaveis. Cada passo e seguro porque o teste anterior garante que nada foi quebrado. Na pre-programacao, dividir entregas em incrementos verificaveis segue o mesmo principio.

### 4. Triangulação
Quando nao esta claro como generalizar, adicione mais exemplos (testes) ate que o padrao emerja. Na pre-programacao, quando requisitos sao ambiguos, pedir mais exemplos concretos resolve a ambiguidade.

### 5. Fake It Till You Make It
Comece com implementacoes fake e substitua gradualmente por implementacoes reais. Na pre-programacao, prototipos e mocks servem ao mesmo proposito.

### 6. Obvious Implementation
Quando a implementacao e obvia, implemente diretamente. TDD nao proibe conhecimento previo — ele fornece uma rede de seguranca para validar suposicoes.

### 7. Testabilidade como Qualidade de Design
Codigo dificil de testar geralmente tem problemas de design (acoplamento, dependencias escondidas). Se durante a pre-programacao o design parece dificil de testar, e um sinal de alerta.

## Como Aplicar no Squad

### Na Definicao de Criterios de Aceitacao
- Escrever criterios de aceitacao no formato Given-When-Then.
- Cada criterio deve ser verificavel por um teste automatizado.
- Usar exemplos concretos em vez de descricoes abstratas.
- Aplicar triangulacao: fornecer multiplos exemplos para eliminar ambiguidade.

### Na Estrategia de Testes
- Definir a estrategia de testes na fase de pre-programacao.
- Especificar quais tipos de testes sao necessarios para cada componente.
- Identificar o que pode ser testado com unit tests vs. integration tests vs. e2e tests.
- Planejar mocks e stubs necessarios para isolar componentes.

### Na Avaliacao de Testabilidade do Design
- Incluir "testabilidade" como criterio de avaliacao em design reviews.
- Verificar se o design permite injecao de dependencias.
- Avaliar se interfaces sao facilmente mockáveis.
- Alertar quando o design torna testes dificeis — provavelmente ha problemas de acoplamento.

### Nos Criterios de Readiness
- "Criterios de aceitacao estao escritos no formato Given-When-Then?"
- "A estrategia de testes esta definida (tipos, cobertura, ferramentas)?"
- "O design foi avaliado quanto a testabilidade?"
- "Exemplos concretos foram fornecidos para cada requisito?"

## Citacoes Importantes

> "Clean code that works — that's the goal of test-driven development."

> "Write a failing test before you write production code."

> "Make it work, make it right, make it fast — in that order."

> "If you can't write a test for it, you don't understand the requirement well enough."

> "The tests are a canary in a coal mine revealing by their distress the presence of evil design."

## Relacao com Outros Livros de Referencia

- **Specification by Example (Adzic):** Estende TDD para o nivel de requisitos de negocio com especificacoes executaveis.
- **Working Effectively with Legacy Code (Feathers):** Mostra como aplicar TDD em sistemas que nao foram construidos com testes.
- **Clean Architecture (Martin):** A testabilidade e uma consequencia natural da Clean Architecture.
