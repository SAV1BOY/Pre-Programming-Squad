# Exemplos de Architecture Decision Records (ADRs)

## O que e um ADR

Um Architecture Decision Record (ADR) e um documento curto que captura uma decisao arquitetural significativa junto com seu contexto e consequencias. ADRs criam um registro historico do raciocinio por tras das decisoes, permitindo que equipes futuras entendam por que o sistema e como e.

## Template Padrao (Formato Michael Nygard)

```markdown
# ADR-[NUMERO]: [TITULO DA DECISAO]

**Data:** [YYYY-MM-DD]
**Status:** Proposto | Aceito | Depreciado | Substituido por ADR-[N]

## Contexto
[Descreva as forcas em jogo: requisitos tecnicos, restricoes de negocio,
limitacoes da equipe, pressoes de prazo. Seja factual e neutro.]

## Decisao
[Descreva a decisao tomada de forma clara e direta.
"Nos decidimos [fazer X] porque [razao]."]

## Consequencias
[Descreva as consequencias positivas e negativas da decisao.
Inclua trade-offs aceitos conscientemente.]
```

## Exemplo 1: Escolha de Banco de Dados

```markdown
# ADR-001: Usar PostgreSQL como banco de dados principal

**Data:** 2025-01-15
**Status:** Aceito

## Contexto
O servico de gestao de pedidos precisa de um banco de dados que suporte:
- Transacoes ACID para garantir consistencia de pedidos.
- Queries complexas com joins para relatorios operacionais.
- Tipos de dados JSON para armazenar metadados flexiveis de produtos.
- Volume estimado: 50M registros no primeiro ano, crescimento de 30% ao ano.

A equipe tem experiencia forte em PostgreSQL e MySQL. Nao temos DBA dedicado.

## Decisao
Usaremos PostgreSQL 16 hospedado no Amazon RDS.

Razoes:
- Suporte nativo a JSONB atende a necessidade de metadados flexiveis.
- Recursos avancados de indexacao (GIN, GiST) suportam queries complexas.
- RDS elimina overhead operacional de gerenciamento de instancias.
- A equipe ja tem experiencia com PostgreSQL em 3 servicos existentes.

## Consequencias

### Positivas
- Modelo relacional bem adequado para dominio de pedidos com entidades relacionadas.
- JSONB permite flexibilidade sem sacrificar queries estruturadas.
- Ecossistema maduro de ferramentas (pgAdmin, pg_dump, Flyway).
- Read replicas no RDS para separar carga OLTP e relatorios.

### Negativas
- Custo de RDS maior que self-hosted (~$800/mes para instancia db.r6g.xlarge).
- Escalabilidade horizontal limitada comparada a bancos NoSQL.
- Se volume exceder 500M registros, avaliar particionamento ou sharding.

### Riscos Aceitos
- Lock-in em RDS (mitigacao: uso padrao de SQL, sem features proprietarias da AWS).
- Limite de conexoes simultaneas (mitigacao: connection pooling com PgBouncer).
```

## Exemplo 2: Padrao de Comunicacao entre Servicos

```markdown
# ADR-002: Comunicacao assincrona via eventos para integracao entre dominios

**Data:** 2025-02-01
**Status:** Aceito

## Contexto
Os servicos de Pedidos, Estoque e Faturamento precisam se comunicar.
Atualmente usam chamadas REST sincronas, o que causa:
- Cascading failures: se Estoque esta fora, Pedidos falha.
- Acoplamento temporal: todos os servicos devem estar online simultaneamente.
- Latencia somada: pedido leva 800ms porque encadeia 3 chamadas sincronas.

Volume: ~5.000 pedidos/hora em pico.

## Decisao
Adotaremos comunicacao assincrona via eventos usando Amazon SQS com SNS
para fan-out. Cada dominio publica eventos de dominio; consumers processam
de forma independente.

Razoes:
- Desacoplamento temporal: servicos podem processar eventos em ritmo proprio.
- Resiliencia: falha em um consumer nao bloqueia o producer.
- SQS/SNS e gerenciado, sem overhead operacional de Kafka para nosso volume.

## Consequencias

### Positivas
- Eliminacao de cascading failures entre dominios.
- Latencia de pedido reduzida de 800ms para ~200ms (so processamento local).
- Cada dominio evolui independentemente.

### Negativas
- Consistencia eventual entre dominios (aceito: pedido pode aparecer em
  faturamento com delay de ate 30s).
- Complexidade de debugging distribuido (mitigacao: correlation IDs e tracing).
- Necessidade de idempotencia em todos os consumers (SQS garante at-least-once).

### Riscos Aceitos
- Mensagens fora de ordem (mitigacao: consumers devem tolerar reordenacao).
- Dead letter queue para mensagens que falham apos 3 retries.
```

## Exemplo 3: Estrategia de Autenticacao

```markdown
# ADR-003: Adotar JWT com refresh tokens para autenticacao de API

**Data:** 2025-02-20
**Status:** Aceito

## Contexto
O sistema atualmente usa sessoes server-side armazenadas em Redis.
Com a migracaoepara arquitetura de microsservicos, cada servico
precisaria consultar Redis para validar sessoes, criando um ponto
unico de falha e gargalo de performance.

Requisitos:
- Autenticacao stateless para microsservicos.
- Revogacao de acesso em ate 15 minutos.
- Suporte a multiplos clientes (web, mobile, API partners).

## Decisao
Adotaremos JWT (RS256) com access tokens de curta duracao (15 minutos)
e refresh tokens opacos armazenados no banco de dados.

## Consequencias

### Positivas
- Validacao stateless: cada servico verifica JWT localmente com chave publica.
- Elimina Redis como dependencia critica para autenticacao.
- Padrao amplamente suportado por bibliotecas e frameworks.

### Negativas
- Revogacao nao e imediata (ate 15 minutos de delay).
- Tamanho do JWT em cada request (~800 bytes vs. ~40 bytes de session ID).
- Complexidade de rotacao de chaves de assinatura.

### Riscos Aceitos
- Window de 15 minutos onde um token revogado ainda e valido
  (aceitavel para nosso perfil de risco; operacoes criticas verificam
  adicionalmente no banco).
```

## Exemplo 4: Decisao de Substituicao

```markdown
# ADR-004: Migrar de REST para gRPC para comunicacao interna

**Data:** 2025-03-10
**Status:** Proposto — Substituindo ADR-002 parcialmente

## Contexto
A comunicacao sincrona entre servicos dentro do mesmo dominio usa REST.
Com o crescimento de 5 para 15 servicos internos, os problemas de REST
tornaram-se evidentes:
- Serializacao/desserializacao JSON representa 30% da latencia intra-servico.
- Falta de schema forte causa incompatibilidades silenciosas.
- Geração manual de clientes HTTP e propensa a erros.

Nota: comunicacao entre dominios continua assincrona (ADR-002).

## Decisao
Para comunicacao sincrona INTRA-dominio, adotaremos gRPC com Protocol
Buffers. Comunicacao INTER-dominio permanece assincrona via eventos.

## Consequencias

### Positivas
- Reducao de 60-70% na latencia de serializacao.
- Contratos fortemente tipados via .proto files.
- Geração automatica de clientes em multiplas linguagens.
- Streaming bidirecional quando necessario.

### Negativas
- Curva de aprendizado para equipe (2-3 sprints estimados).
- Debugging mais complexo que REST (ferramentas como grpcurl, Postman gRPC).
- Load balancers precisam suportar HTTP/2.
```

## Boas Praticas para ADRs

### Quando Criar um ADR
- Decisoes que afetam multiplos componentes ou equipes.
- Decisoes dificeis de reverter.
- Decisoes onde havia debate significativo.
- Escolhas de tecnologia, padroes ou frameworks.

### O que NAO e um ADR
- Decisoes triviais de implementacao.
- Escolhas de estilo de codigo (use linters).
- Decisoes temporarias de debug.

### Governanca
- ADRs sao numerados sequencialmente.
- ADRs nunca sao deletados — sao marcados como "Depreciado" ou "Substituido".
- Manter um indice (index.md) com todos os ADRs e seus status.
- Armazenar ADRs no repositorio de codigo, nao em wikis externas.
