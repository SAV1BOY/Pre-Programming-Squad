# Data Shape Before Code

## Título e Propósito

O **Data Shape Before Code** é um framework que prioriza a definição da forma dos dados (estrutura, relacionamentos, ciclo de vida, invariantes) como primeira atividade de design, antes de pensar em código, APIs ou UI. O propósito é reconhecer que dados são o ativo mais durável de um sistema — código muda, interfaces mudam, mas dados e suas relações persistem e são os mais caros de migrar.

## Quando Usar

- No início do design de qualquer sistema que persiste dados
- Quando modelos de dados de sistemas diferentes precisam ser integrados
- Antes de definir APIs — a API deveria refletir o modelo de dados, não o contrário
- Quando decisões de schema impactam performance, integridade ou evolução futura
- Em projetos de migração ou modernização onde dados legados precisam ser transformados

## Conceitos-Chave

1. **Forma dos Dados (Data Shape)**: A estrutura, tipos, relacionamentos, cardinalidade e invariantes dos dados. Responde "como os dados se parecem?"
2. **Ciclo de Vida dos Dados**: Criação, leitura, atualização, arquivamento, deleção. Cada fase tem requisitos diferentes.
3. **Invariante de Dados**: Regra que deve ser verdadeira em todo momento. Exemplo: "todo pedido tem pelo menos um item". Invariantes violados = dados corrompidos.
4. **Modelo de Leitura vs. Escrita**: Dados otimizados para escrita (normalizado) vs. para leitura (denormalizado). Reconhecer qual padrão domina.
5. **Gravidade dos Dados**: Dados atraem mais dados, código e integrações. Quanto mais dados em um sistema, mais difícil mover ou mudar.

## Processo / Passos

### Passo 1 — Identificar as Entidades Principais
Liste as entidades centrais do domínio. Use linguagem de negócio, não técnica. Exemplo: Pedido, Cliente, Produto — não "tabela_pedidos".

### Passo 2 — Definir Atributos e Tipos
Para cada entidade, liste atributos essenciais com tipos. Inclua: obrigatoriedade, valor padrão, formato, restrições.

### Passo 3 — Mapear Relacionamentos e Cardinalidade
Como as entidades se relacionam? 1:1, 1:N, N:N? Quais relacionamentos são obrigatórios? Quais são opcionais?

### Passo 4 — Definir Invariantes
Quais regras sobre os dados devem ser verdadeiras em todo momento? Documente cada invariante e onde ele será enforçado (DB, aplicação, ambos).

### Passo 5 — Mapear Ciclo de Vida
Para cada entidade: como é criada? Quem cria? Quanto tempo vive? É atualizada? Como é arquivada ou deletada? Há requisitos legais de retenção?

### Passo 6 — Identificar Padrões de Acesso
Como os dados serão lidos e escritos predominantemente? Isso informa escolha de banco, indexação e estrutura.

### Passo 7 — Projetar para Evolução
Como o schema evolui quando requisitos mudam? Quais migrações serão necessárias? Dados existentes são afetados?

## Perguntas de Ativação

- "Quais são as 5 entidades mais importantes do sistema?"
- "Se eu olhasse para os dados sem ver o código, a estrutura faria sentido de negócio?"
- "Quais invariantes de dados, se violados, causariam problemas sérios?"
- "Esses dados são lidos 100x mais do que escritos, ou o contrário?"
- "Como esse schema evolui quando adicionarmos [feature futura conhecida]?"
- "Quais dados precisam ser consistentes imediatamente e quais podem ser eventualmente consistentes?"

## Output Esperado

```
MODELO DE DADOS — [Projeto]

ENTIDADES:
┌─────────────┐       1:N        ┌─────────────┐
│   Cliente    │ ────────────────►│   Pedido     │
│             │                   │              │
│ - id (UUID) │       N:N        │ - id (UUID)  │
│ - nome      │  ┌──────────────►│ - status     │
│ - email (UK)│  │               │ - total      │
│ - cpf (UK)  │  │               │ - criado_em  │
└─────────────┘  │               └──────┬───────┘
                 │                      │ 1:N
           ┌─────┴───────┐      ┌──────▼───────┐
           │  Produto     │◄─────│ Item Pedido  │
           │              │ N:1  │              │
           │ - id (UUID)  │      │ - quantidade │
           │ - nome       │      │ - preço_unit │
           │ - preço      │      └──────────────┘
           │ - estoque    │
           └──────────────┘

INVARIANTES:
1. Todo pedido tem pelo menos 1 item — Enforcement: aplicação + constraint DB
2. Estoque nunca é negativo — Enforcement: check constraint + lógica de negócio
3. Email de cliente é único — Enforcement: unique constraint
4. Preço do item no pedido é imutável após confirmação — Enforcement: aplicação

CICLO DE VIDA:
- Pedido: criado → confirmado → pago → enviado → entregue → [cancelado em qualquer estado]
- Produto: criado → ativo → inativo → arquivado (nunca deletado)

PADRÕES DE ACESSO:
- Leitura dominante: catálogo de produtos (cache agressivo)
- Escrita dominante: criação de pedidos (transacional, ACID)
- Analítico: relatórios de vendas (read replica ou data warehouse)
```

## Armadilhas Comuns

1. **Código primeiro, dados depois**: Projetar APIs e UI antes do modelo de dados resulta em schema que serve ao código mas não ao domínio.
2. **Invariantes não documentados**: Regras sobre dados que vivem apenas no código. Quando o código muda, os invariantes se perdem.
3. **Schema que não evolui**: Projetar como se o schema nunca fosse mudar. Toda migração futura é mais fácil se considerada no design inicial.
4. **Normalização excessiva**: Normalizar tudo gera joins complexos. Denormalizar demais gera inconsistência. Encontre o equilíbrio para o padrão de acesso.
5. **Ignorar volume e crescimento**: Schema que funciona com 1.000 registros pode ser insustentável com 10 milhões.
6. **Dados como reflexo do UI**: Modelar dados pela tela em vez do domínio cria schema acoplado à interface que quebra quando a UI muda.
