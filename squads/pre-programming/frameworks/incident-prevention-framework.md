# Incident Prevention Framework

## Propósito
Antecipar e prevenir incidentes em produção durante a fase de pré-programação, transformando o aprendizado de incidentes passados em design defensivo.

## Problema que Resolve
A maioria dos incidentes em produção era previsível. Database sem failover cai. API sem timeout trava. Deploy sem rollback exige hotfix manual. Este framework força a pensar em cenários de falha antes do código existir.

## Quando Usar
- Durante a fase de Risk Review (obrigatório)
- Quando Failure Analyst mapeia failure modes
- Em projetos que tocam infraestrutura crítica
- Em projetos com dependências externas (APIs de terceiros)

## Categorias de Incidente Prevenível

| Categoria | Exemplo | Prevenção |
|-----------|---------|-----------|
| **Disponibilidade** | Database única sem replica cai | Failover automático, read replicas |
| **Performance** | Query N+1 em listagem com 100k registros | Query analysis em design review |
| **Dados** | Migration sem rollback corrompe schema | Migration + rollback script testados |
| **Integração** | API de terceiro fora do ar por 4h | Circuit breaker, fallback, retry com backoff |
| **Segurança** | SQL injection em endpoint público | Input validation, parameterized queries |
| **Operacional** | Deploy em sexta às 18h sem rollback plan | Deploy policy, rollback automático |

## Processo

### Passo 1 — Estudar Incidentes Históricos
Consultar:
- Post-mortems internos de projetos similares
- `archive/failures/` do squad
- Incidentes de empresas similares no setor
- OWASP Top 10, NIST common vulnerabilities

### Passo 2 — Pre-Mortem
Imaginar que o projeto já falhou em produção. Perguntar:
- "O que causou o incidente?"
- "Que sinais havia antes do incidente?"
- "O que poderíamos ter prevenido no design?"

### Passo 3 — Mapear Defesas por Categoria
Para cada categoria aplicável ao projeto:

| Defesa | Implementação | Custo | Impacto |
|--------|--------------|-------|---------|
| Circuit breaker em API de pagamento | Resilience4j / Polly | Baixo | Alto |
| Retry com exponential backoff | Config de HTTP client | Baixo | Alto |
| Feature flag para rollback instantâneo | LaunchDarkly / custom | Médio | Crítico |
| Health check em todos os serviços | /health endpoint | Baixo | Alto |
| Alertas proativos (latência, error rate) | Datadog / Grafana | Médio | Alto |

### Passo 4 — Incluir no Architecture Sketch
Defesas não são "nice to have" — são componentes de arquitetura. Incluir no architecture sketch como decisão documentada.

### Passo 5 — Validar com Failure Analyst
O Failure Analyst revisa o mapa de defesas e questiona:
- "E se [defesa X] falhar?"
- "Qual é o modo de degradação?"
- "O rollback funciona sem intervenção manual?"

## Heurísticas
1. **Se depende de terceiro, precisa de circuit breaker** — Sempre
2. **Se tem database, precisa de failover** — Para sistemas críticos
3. **Se tem deploy, precisa de rollback** — Feature flags ou blue-green
4. **Se processa dados financeiros, precisa de idempotência** — Retry não pode duplicar transação
5. **Se tem fila, precisa de dead letter queue** — Mensagens que falham precisam de destino

## Armadilhas
- **"Nunca aconteceu, não vai acontecer"** → Normalcy bias — os piores incidentes são os que nunca aconteceram antes
- **Monitoramento só reativo** → Alertas devem disparar antes do impacto ao usuário
- **Design sem fallback** → Todo componente crítico precisa de degradation mode
- **Rollback "manual"** → Se precisa de SSH para fazer rollback, não é rollback
