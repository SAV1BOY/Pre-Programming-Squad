# Nygard: Design for Production

## Título e Propósito

Framework baseado no trabalho de **Michael Nygard** (*Release It!*). A tese central: **a maioria dos problemas de software ocorrem em produção, não em desenvolvimento** — e sistemas devem ser projetados para sobreviver ao ambiente hostil de produção desde o design. O propósito é incorporar pensamento de produção na pré-programação.

## Quando Usar

- Em design de sistemas que precisam rodar 24/7 em produção
- Ao projetar integrações com serviços externos
- Na definição de estratégias de resiliência (circuit breaker, bulkhead, timeout)
- Quando incidentes de produção revelam fragilidades de design
- Ao projetar deployment, operação e monitoramento

## Conceitos-Chave

1. **Stability Patterns**: Circuit Breaker (para quando dependência falha), Bulkhead (isolar falhas), Timeout (não esperar para sempre), Retry com backoff.
2. **Anti-patterns de Estabilidade**: Integration points (toda integração é ponto de falha), Cascading failures, Blocked threads, Self-denial attacks.
3. **Design for Operations**: O sistema deve ser operável: observável, diagnosticável, configurável em runtime.
4. **Capacity Planning**: O sistema deve aguentar o pico, não apenas a média. E ter degradação graciosa além do pico.
5. **Zero-Downtime Deployment**: Deploys não devem causar indisponibilidade. Blue-green, canary, rolling update.

## Processo / Passos

### Passo 1 — Identificar Integration Points
Liste toda dependência externa. Cada uma é ponto potencial de falha.

### Passo 2 — Projetar Stability Patterns
Para cada integration point: timeout, retry com backoff, circuit breaker. Para componentes críticos: bulkhead.

### Passo 3 — Projetar para Capacity
Estimar pico de carga. Projetar para 2x o pico. Definir degradação graciosa para além disso.

### Passo 4 — Projetar para Operações
Logs estruturados, métricas, tracing, feature flags, configuração em runtime, health checks.

### Passo 5 — Projetar Deploy
Zero-downtime deployment, rollback rápido, canary release para mudanças de risco.

## Perguntas de Ativação

- "Esse sistema foi projetado para sobreviver a falhas de dependências?"
- "Temos timeout em toda chamada externa?"
- "Se o tráfego dobrar amanhã, o sistema degrada graciosamente ou colapsa?"
- "Podemos fazer deploy sem downtime?"
- "As equipes de operações têm as ferramentas para diagnosticar problemas?"

## Output Esperado

Mapa de integration points com stability patterns definidos, capacity planning, estratégia de deploy, checklist de operabilidade.

## Armadilhas Comuns

1. **Desenvolvimento como produção**: Projetar assumindo condições ideais (rede confiável, dependências disponíveis, carga previsível).
2. **Sem timeout**: Chamadas que esperam para sempre, acumulando threads bloqueadas até o sistema travar.
3. **Cascading failures**: Uma dependência falha, sobrecarrega as outras, e o sistema inteiro cai.
4. **Deploy como evento de risco**: Se deploy causa medo, o processo está quebrado. Deve ser rotina.
5. **Sistema inoperável**: Funciona em desenvolvimento mas é impossível de diagnosticar e operar em produção.
