# V1 Architecture Lens

## Título e Propósito

O **V1 Architecture Lens** é um framework para projetar a primeira versão de uma arquitetura que seja simples o suficiente para entregar rápido e flexível o suficiente para evoluir. O propósito é combater dois extremos: o over-engineering da v1 (projetar para 10 milhões de usuários quando há 100) e o under-engineering (código descartável que se torna permanente).

## Quando Usar

- Ao projetar a arquitetura inicial de um novo produto ou serviço
- Quando há pressão para entregar rápido mas preocupação com sustentabilidade
- Em projetos greenfield onde as decisões arquiteturais são todas novas
- Quando a equipe debate entre "fazer simples" e "fazer direito"
- Para calibrar o nível correto de investimento arquitetural na v1

## Conceitos-Chave

1. **Boa o Suficiente para Agora**: A arquitetura v1 não precisa ser perfeita — precisa resolver o problema atual sem criar dívida técnica insustentável.
2. **Pontos de Extensão**: Locais no design onde sabemos que mudanças serão necessárias. Projetar para extensibilidade nesses pontos, simplicidade nos demais.
3. **Decisões Adiáveis**: Decisões que não precisam ser tomadas na v1 e que se beneficiam de mais informação. Adie-as.
4. **Arquitetura Evolutiva**: Design que pode evoluir incrementalmente sem rewrite completo.
5. **Fronteiras Certas, Implementação Simples**: Acerte os limites entre módulos/serviços/camadas. A implementação interna pode ser simples e refatorada depois.

## Processo / Passos

### Passo 1 — Definir Requisitos da V1
O que a v1 precisa fazer? Quantos usuários, que volume de dados, que nível de disponibilidade? Use números reais, não aspiracionais.

### Passo 2 — Identificar Decisões que Podem ser Adiadas
Quais decisões arquiteturais podem esperar até termos mais informação? Cache distribuído, event sourcing, CQRS — precisa agora?

### Passo 3 — Identificar Decisões que Devem ser Tomadas Agora
Fronteiras entre serviços, modelo de dados principal, padrão de autenticação — difíceis de mudar depois.

### Passo 4 — Projetar Fronteiras
Defina os limites entre módulos/serviços com contratos claros. Fronteiras erradas custam caro; implementação interna barata de refatorar.

### Passo 5 — Escolher Simplicidade como Default
Para cada componente, pergunte: "Qual é a solução mais simples que funciona para a v1?" Monolito antes de microsserviços. Banco relacional antes de NoSQL. Sincrôno antes de assíncrono.

### Passo 6 — Marcar Pontos de Extensão
Identifique onde a complexidade vai crescer: integração com novos parceiros, novos tipos de usuário, novos canais. Deixe esses pontos extensíveis.

### Passo 7 — Documentar a Estratégia de Evolução
Descreva como a v1 evolui para v2: quais componentes serão refatorados, quais extraídos, quais substituídos.

## Perguntas de Ativação

- "Estamos projetando para os 100 usuários que temos ou para os 10 milhões que sonhamos?"
- "Essa decisão precisa ser tomada agora ou pode esperar?"
- "Qual é a solução mais simples que resolve o problema da v1?"
- "Se precisarmos mudar isso em 6 meses, quanto vai custar?"
- "Estamos adicionando complexidade por necessidade real ou por 'boas práticas'?"
- "As fronteiras entre módulos estão nos lugares certos?"

## Output Esperado

```
ARQUITETURA V1 — [Projeto]

REQUISITOS V1: [volume, usuários, SLAs reais]

DECISÕES TOMADAS AGORA:
- Monolito modular (não microsserviços) — Razão: time de 3, simplicidade operacional
- PostgreSQL — Razão: transações ACID, equipe experiente
- REST para APIs — Razão: maturidade, tooling, familiaridade

DECISÕES ADIADAS:
- Cache distribuído — Quando reavaliar: se latência p95 > 500ms
- Fila de mensagens — Quando reavaliar: se processamento assíncrono necessário
- Separação em serviços — Quando reavaliar: se equipe crescer para 8+

PONTOS DE EXTENSÃO:
- Interface de pagamento (novos gateways virão)
- Provider de notificação (email agora, SMS/push depois)
- Motor de regras (regras vão crescer em complexidade)

FRONTEIRAS DEFINIDAS:
- Módulo de Pedidos: [interface pública]
- Módulo de Catálogo: [interface pública]
- Módulo de Usuários: [interface pública]

ESTRATÉGIA DE EVOLUÇÃO V1 → V2:
- Se volume > X: adicionar cache + read replica
- Se equipe > 8: considerar extração de serviço de pedidos
- Se latência > Y: otimizar queries, adicionar índices, depois considerar CQRS
```

## Armadilhas Comuns

1. **Over-engineering**: Microsserviços, Kafka, Kubernetes para um MVP com 50 usuários. Comece simples.
2. **Under-engineering**: "É só um MVP" — e o código descartável vira a base do produto por 3 anos.
3. **Fronteiras erradas**: Acertar a implementação interna mas errar os limites entre módulos custa caro para corrigir.
4. **Não planejar evolução**: V1 sem visão de como evolui para v2 tende a exigir rewrite completo.
5. **Decidir tudo agora**: Tomar decisões que poderiam esperar, desperdiçando informação futura.
6. **Copiar arquitetura**: Replicar a arquitetura do projeto anterior sem considerar que o contexto é diferente.
