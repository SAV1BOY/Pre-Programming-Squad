# Beck: TDD como Ferramenta de Design

## Título e Propósito

Framework baseado no trabalho de **Kent Beck** (*Test-Driven Development: By Example*). A tese central: **TDD não é apenas sobre testes — é uma ferramenta de design** que força interfaces limpas, acoplamento baixo e código testável. O propósito é aplicar o pensamento TDD na pré-programação: definir como verificar antes de definir como construir.

## Quando Usar

- Na definição de critérios de aceite e planos de teste antes da implementação
- Quando o design de interfaces e contratos precisa ser refinado
- Para revelar complexidade oculta em requisitos aparentemente simples
- Ao ensinar a equipe a pensar em verificabilidade desde o design
- Em revisões de design para avaliar testabilidade

## Conceitos-Chave

1. **Red-Green-Refactor**: Escreva um teste que falha (red), faça-o passar da forma mais simples (green), melhore o código (refactor). O ciclo força incrementalidade.
2. **Test como Especificação**: O teste é a especificação executável do comportamento esperado. Se o teste não expressa claramente o requisito, o requisito não está claro.
3. **Design Emergente**: O design emerge dos testes em vez de ser planejado centralmente. Cada teste adiciona uma responsabilidade e revela a interface necessária.
4. **Coragem para Mudar**: Com boa cobertura de testes, a equipe pode refatorar sem medo. Sem testes, mudanças são arriscadas.
5. **Simplicidade Forçada**: TDD força a implementação mais simples que faz o teste passar. Complexidade só é adicionada quando um teste a exige.

## Processo / Passos

### Passo 1 — Antes de Projetar, Perguntar "Como Vamos Testar?"
Para cada componente, pergunte: "Como vou verificar que funciona?" Se a resposta for difícil, o design precisa mudar.

### Passo 2 — Escrever Critérios de Aceite como Testes
Transforme cada critério de aceite em formato DADO-QUANDO-ENTÃO. Se não conseguir, o critério está ambíguo.

### Passo 3 — Usar Testes para Refinar Interfaces
A dificuldade de escrever um teste revela problemas de design: dependências demais, interface complexa, estado oculto.

### Passo 4 — Projetar para Testabilidade
Injeção de dependência, interfaces abstratas, separação de concerns — são consequências naturais de projetar para testabilidade.

### Passo 5 — Definir a Pirâmide de Testes na Fase de Design
Decidir quais componentes terão testes unitários, de integração e E2E antes de implementar.

## Perguntas de Ativação

- "Se eu tivesse que escrever um teste para isso agora, o que testaria?"
- "A dificuldade em escrever esse teste indica um problema no design?"
- "Esse componente pode ser testado isoladamente ou tem dependências demais?"
- "O teste expressa o comportamento esperado de forma clara?"
- "Se esse teste passasse, eu teria confiança de que funciona?"

## Output Esperado

Critérios de aceite em formato de testes, avaliação de testabilidade por componente, pirâmide de testes definida, decisões de design influenciadas por testabilidade.

## Armadilhas Comuns

1. **TDD dogmático**: Insistir em TDD para todo código, incluindo protótipos exploratórios onde flexibilidade é mais importante.
2. **Testes acoplados**: Testes que verificam implementação interna em vez de comportamento externo. Quebram com refactors legítimos.
3. **Testar trivialidades**: Getter/setter, construtores, wrappers. Foque em lógica de negócio e integrações.
4. **Ignorar o "Refactor"**: Fazer Red-Green mas pular Refactor. O teste passa mas o código acumula dívida.
5. **Confundir cobertura com qualidade**: 100% de cobertura com testes ruins dá falsa segurança.
