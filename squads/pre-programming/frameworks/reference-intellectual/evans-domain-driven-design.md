# Evans: Domain-Driven Design

## Título e Propósito

Framework baseado no trabalho de **Eric Evans** (*Domain-Driven Design*). A tese central: **o software deve refletir o domínio de negócio em sua estrutura, linguagem e fronteiras**. O propósito é aplicar os princípios de DDD na pré-programação para que a arquitetura do sistema espelhe a realidade do negócio, facilitando comunicação e evolução.

## Quando Usar

- Em domínios complexos onde a lógica de negócio é o diferencial
- Na definição de fronteiras entre módulos, serviços ou equipes
- Quando a equipe e os stakeholders usam termos diferentes para as mesmas coisas
- Ao decompor um monolito em bounded contexts
- Em projetos onde entender o domínio é mais desafiador que a tecnologia

## Conceitos-Chave

1. **Linguagem Ubíqua**: Um vocabulário compartilhado entre devs e negócio. O mesmo termo significa a mesma coisa para todos. No código, nas conversas, nos documentos.
2. **Bounded Context**: Fronteira dentro da qual um modelo de domínio é consistente. "Cliente" em vendas pode ser diferente de "Cliente" em suporte — e tudo bem.
3. **Aggregate**: Cluster de entidades tratadas como unidade para mudanças de dados. Define fronteira transacional.
4. **Context Map**: Mapa de como bounded contexts se relacionam: shared kernel, customer-supplier, anti-corruption layer.
5. **Strategic Design vs. Tactical Design**: Strategic define bounded contexts e relações. Tactical define entidades, value objects, aggregates dentro de um contexto.

## Processo / Passos

### Passo 1 — Construir Linguagem Ubíqua
Reúna devs e domain experts. Defina termos-chave do domínio. Documente em glossário. Use esses termos no código.

### Passo 2 — Identificar Bounded Contexts
Onde os termos mudam de significado? Onde modelos diferentes são necessários? Cada bounded context é um módulo/serviço potencial.

### Passo 3 — Criar o Context Map
Mapeie relações entre contextos: quem consome de quem? Como se comunicam? Quais adaptações são necessárias?

### Passo 4 — Definir Aggregates
Para cada contexto, identifique aggregates: unidades de consistência transacional. Limites de aggregate definem limites de transação.

### Passo 5 — Projetar Anti-Corruption Layers
Onde bounded contexts interagem, projete ACLs para que um contexto não contamine o modelo do outro.

## Perguntas de Ativação

- "Quando o negócio diz 'pedido', significa a mesma coisa que o código chama de 'pedido'?"
- "Essas duas partes do sistema usam o termo X com significados diferentes?"
- "Qual é a fronteira transacional aqui? O que precisa ser consistente junto?"
- "Se eu mostrar o código para o domain expert, ele reconheceria o vocabulário?"
- "Onde bounded contexts precisam de tradução entre seus modelos?"

## Output Esperado

Glossário de linguagem ubíqua, mapa de bounded contexts com relações, aggregates identificados por contexto, anti-corruption layers projetadas.

## Armadilhas Comuns

1. **DDD sem domain experts**: Aplicar DDD sem envolver quem entende o negócio gera modelo que reflete suposições dos devs, não a realidade.
2. **Bounded context = microserviço**: Nem todo bounded context precisa ser um serviço separado. Módulos dentro de um monolito são válidos.
3. **Linguagem ubíqua ignorada**: Definir o glossário e não usar no código. Se o código usa termos diferentes, a comunicação quebra.
4. **DDD para CRUD**: Se o domínio é simples (CRUD), DDD adiciona complexidade sem valor. Use DDD onde a lógica de negócio justifica.
5. **Aggregates grandes demais**: Aggregates que incluem entidades demais geram contention e transações longas.
