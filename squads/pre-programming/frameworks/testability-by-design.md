# Testability by Design

## Título e Propósito

O **Testability by Design** é um framework para incorporar testabilidade como critério de design desde o início, não como preocupação tardia. O propósito é garantir que o sistema seja projetado de forma que testes automatizados, manuais e exploratórios possam ser escritos e executados com facilidade — porque código difícil de testar é código difícil de manter.

## Quando Usar

- Durante decisões de arquitetura e design
- Quando a equipe reclama que "é difícil testar" componentes existentes
- Ao projetar interfaces entre módulos, serviços ou camadas
- Antes de definir padrões e convenções de código do projeto
- Quando testes são lentos, frágeis ou difíceis de escrever

## Conceitos-Chave

1. **Observabilidade Interna**: A capacidade de inspecionar o estado interno do sistema durante e após a execução. Sem observabilidade, testes são caixas-pretas.
2. **Controlabilidade**: A capacidade de colocar o sistema em qualquer estado desejado para teste. Sem controlabilidade, setup de testes é pesadelo.
3. **Isolamento**: A capacidade de testar componentes independentemente de suas dependências.
4. **Determinismo**: Mesma entrada, mesma saída. Testes flaky geralmente indicam falta de determinismo no design.
5. **Seam (Costura)**: Ponto no código onde comportamento pode ser alterado sem modificar o código em si — interfaces, injeção de dependência, configuração.

## Processo / Passos

### Passo 1 — Identificar Componentes Críticos
Liste os componentes do sistema que mais precisam de testes: lógica de negócio, integrações, transformações de dados, fluxos de estado.

### Passo 2 — Avaliar Testabilidade Atual
Para cada componente, avalie (1-5): Observabilidade, Controlabilidade, Isolamento, Determinismo. Componentes com score baixo precisam de redesign.

### Passo 3 — Projetar Seams
Para cada componente com baixa testabilidade, identifique onde adicionar costuras: interfaces para injeção de dependência, ports/adapters, event hooks.

### Passo 4 — Definir Contratos Testáveis
Cada interface entre componentes deve ter contrato claro e testável: inputs válidos, outputs esperados, efeitos colaterais documentados.

### Passo 5 — Planejar Estratégia de Teste por Camada
Defina: unitários para lógica isolada, integração para contratos entre componentes, E2E para fluxos críticos. A pirâmide de testes começa no design.

### Passo 6 — Eliminar Fontes de Não-Determinismo
Identifique e isole: relógio do sistema, geradores de ID, chamadas externas, estado compartilhado. Torne injetáveis.

### Passo 7 — Validar com um Teste Real
Escreva pelo menos um teste para cada componente crítico antes de implementar. Se o teste for difícil de escrever, o design precisa mudar.

## Perguntas de Ativação

- "Se eu quisesse testar esse componente isoladamente, o que me impediria?"
- "Consigo colocar o sistema no estado necessário para esse teste sem depender de outros componentes?"
- "Esse teste vai ser determinístico ou vai falhar aleatoriamente?"
- "Onde estão as costuras (seams) nesse design?"
- "Se mudarmos a implementação interna, os testes quebram?"
- "Quanto tempo leva para escrever um teste para esse componente?"

## Output Esperado

| Componente | Observabilidade | Controlabilidade | Isolamento | Determinismo | Score | Ação Necessária |
|---|---|---|---|---|---|---|
| Motor de regras de preço | 3 | 2 | 1 | 4 | 10 | Extrair interface, injetar dependências |
| API Gateway | 4 | 4 | 3 | 4 | 15 | Adicionar mock para serviços downstream |
| Job de sincronização | 2 | 1 | 1 | 2 | 6 | Redesenhar: injetar clock, isolar I/O |
| Componente de UI: formulário | 4 | 4 | 4 | 5 | 17 | OK — design testável |

**Padrões definidos**: Injeção de dependência via construtor, interfaces para todos os I/O, clock injetável, IDs gerados via factory.

## Armadilhas Comuns

1. **Testabilidade como afterthought**: "Depois a gente testa" geralmente significa redesenhar depois para poder testar.
2. **Testes acoplados à implementação**: Se mudar código interno (sem mudar comportamento) quebra testes, o design tem acoplamento excessivo.
3. **Mocks demais**: Excesso de mocks indica que o componente tem dependências demais — simplifique o design.
4. **Testes lentos por design**: Se o teste precisa subir banco, fila e 3 serviços, o design não permite isolamento.
5. **Não-determinismo ignorado**: Testes que passam "quase sempre" são sinais de design com fontes de aleatoriedade não controladas.
6. **Confundir testabilidade com cobertura**: Design testável não garante bons testes — mas é pré-requisito para eles.
