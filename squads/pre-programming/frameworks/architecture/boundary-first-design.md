# Boundary-First Design

## Título e Propósito

O **Boundary-First Design** é um framework que prioriza a definição de fronteiras (boundaries) entre componentes como a primeira e mais importante decisão de design. O propósito é garantir que os limites entre módulos, serviços, equipes e domínios estejam nos lugares certos — porque fronteiras erradas geram acoplamento desnecessário, comunicação excessiva e impossibilidade de evolução independente.

## Quando Usar

- No design inicial de qualquer sistema com múltiplos componentes
- Quando uma equipe está crescendo e precisa de independência entre subequipes
- Ao decompor um monolito em módulos ou serviços
- Na definição de contratos de API entre sistemas
- Quando componentes que deveriam ser independentes estão fortemente acoplados

## Conceitos-Chave

1. **Fronteira**: O limite onde um componente termina e outro começa. Define o que é "dentro" e "fora".
2. **Contrato**: O acordo sobre como os dois lados da fronteira se comunicam: formato, protocolo, semântica, versionamento.
3. **Encapsulamento**: O que está dentro da fronteira é detalhe interno. O que cruza a fronteira é contrato público.
4. **Coesão**: Coisas que mudam juntas devem estar dentro da mesma fronteira.
5. **Acoplamento**: Dependências que cruzam fronteiras. Quanto menos e mais estreitas, melhor.
6. **Bounded Context**: Conceito do DDD — contexto onde termos, modelos e regras têm significado específico e consistente.

## Processo / Passos

### Passo 1 — Identificar Domínios
Mapeie os domínios de negócio envolvidos: pedidos, pagamentos, catálogo, usuários, logística. Cada domínio é candidato a fronteira.

### Passo 2 — Aplicar o Teste de Coesão
Para cada agrupamento proposto, pergunte: "Essas coisas mudam juntas? São modificadas pelas mesmas razões? Pela mesma equipe?" Se sim, pertencem à mesma fronteira.

### Passo 3 — Aplicar o Teste de Acoplamento
Para cada fronteira proposta, pergunte: "Quantas dependências cruzam esse limite? Os dois lados podem evoluir independentemente?" Muitas dependências indicam fronteira no lugar errado.

### Passo 4 — Definir Contratos
Para cada fronteira, defina o contrato: quais operações são expostas, quais dados cruzam, que formato, que protocolo.

### Passo 5 — Minimizar Superfície de Contato
Reduza o contrato ao mínimo necessário. Cada ponto de contato é ponto de acoplamento e potencial ponto de falha.

### Passo 6 — Validar com Cenários
Teste as fronteiras contra cenários reais: "Se eu mudar X dentro da fronteira A, preciso mudar algo na fronteira B?" Se sim frequentemente, a fronteira está errada.

### Passo 7 — Documentar Fronteiras e Contratos
Registre as fronteiras, seus contratos, a justificativa para a posição de cada fronteira e as responsabilidades de cada lado.

## Perguntas de Ativação

- "Se esse módulo mudar internamente, algo fora dele quebra?"
- "Essas duas funcionalidades realmente pertencem ao mesmo componente?"
- "Duas equipes diferentes precisariam coordenar para mudar isso?"
- "Qual é o mínimo que precisa cruzar essa fronteira?"
- "Se separássemos isso, a comunicação entre as partes seria simples ou complexa?"
- "Essa fronteira está alinhada com um bounded context de negócio?"

## Output Esperado

```
MAPA DE FRONTEIRAS:

┌─────────────┐     contrato: API REST     ┌──────────────┐
│  Catálogo   │ ◄─────────────────────────► │   Pedidos    │
│             │  GET /produtos/{id}         │              │
│  - Produtos │  {id, nome, preço}          │  - Carrinho  │
│  - Categorias│                            │  - Checkout  │
│  - Busca    │                             │  - Histórico │
└─────────────┘                             └──────┬───────┘
                                                   │
                                    contrato: Eventos
                                    pedido.criado {id, itens, total}
                                                   │
                                            ┌──────▼───────┐
                                            │  Pagamentos  │
                                            │              │
                                            │  - Cobrança  │
                                            │  - Estorno   │
                                            │  - Conciliação│
                                            └──────────────┘

JUSTIFICATIVA:
- Catálogo x Pedidos: domínios distintos, equipes distintas, ciclos de mudança distintos
- Pedidos x Pagamentos: regras de negócio independentes, integração via eventos para desacoplamento

CONTRATOS DEFINIDOS:
- Catálogo → Pedidos: REST síncrono (consulta de preço no checkout)
- Pedidos → Pagamentos: Evento assíncrono (pedido.criado)
```

## Armadilhas Comuns

1. **Fronteiras por tecnologia**: Separar "frontend" e "backend" como fronteiras em vez de domínios de negócio.
2. **Fronteiras cedo demais**: Separar em microsserviços antes de entender onde as fronteiras naturais estão.
3. **Fronteiras de conveniência**: Separar onde é fácil, não onde é correto. A fronteira deve estar onde o acoplamento é naturalmente baixo.
4. **Contratos informais**: Fronteira sem contrato explícito é fronteira que vai ser violada.
5. **Dados compartilhados cruzando fronteiras**: Compartilhar banco de dados entre componentes elimina a independência que a fronteira deveria criar.
6. **Fronteiras estáticas**: À medida que o domínio evolui, fronteiras podem precisar ser ajustadas. Não trate como permanentes.
