# Modo Auditoria

## Nível de Detalhe

Estruturado, formal e rastreável. Cada item é verificável com critério binário (atende/não atende). Inclui evidência para cada verificação, responsável pela evidência e data da verificação. O documento serve como registro formal e pode ser usado em auditorias internas, compliance e post-mortems.

**Proporção alvo:** 10% contexto, 80% checklist com evidências, 10% sumário de conformidade.

## Quando Usar

- **Pré-checks obrigatórios** — security review, performance review, compliance check
- **Gate reviews** — go/no-go antes de releases ou migrações
- **Auditorias internas** — verificação periódica de padrões e processos
- **Readiness assessments** — validação de que um sistema está pronto para produção
- **Compliance** — verificação de aderência a normas (LGPD, SOC 2, PCI-DSS)
- **Handoff formal** — quando a transferência de responsabilidade precisa de registro

**Não usar quando:**
- A situação exige discussão exploratória (use standard ou deep-dive)
- O contexto é informal e iterativo (use conciso)
- Não há critérios objetivos definidos previamente

## Extensão Esperada

- **Pre-check de segurança:** 15-30 itens, 1-3 páginas
- **Gate review:** 10-20 itens por área, 2-4 páginas com sumário
- **Readiness assessment:** 20-50 itens categorizados, 3-5 páginas
- **Total:** Variável conforme checklist, mas sempre com estrutura tabular

## Exemplo

```
## Auditoria de Readiness — Serviço de Pagamentos v3.0

### Metadata
- **Data:** 10/mar/2025
- **Auditor:** Carlos Lima (Security Lead)
- **Escopo:** Prontidão para produção do Serviço de Pagamentos v3.0
- **Veredicto geral:** 🔶 APROVADO COM CONDIÇÕES (ver itens 2.3 e 4.1)

---

### 1. Segurança

| # | Critério | Status | Evidência | Verificado por |
|---|---|---|---|---|
| 1.1 | Autenticação em todos os endpoints | ✅ Atende | Relatório OWASP ZAP scan #487 | @carlos 08/mar |
| 1.2 | Autorização granular (RBAC) | ✅ Atende | Matriz de permissões em /docs/rbac.md, testes em /tests/auth/ | @carlos 08/mar |
| 1.3 | Dados sensíveis encriptados at-rest | ✅ Atende | KMS key configurada, verificado em terraform plan | @ana 07/mar |
| 1.4 | Dados sensíveis encriptados in-transit | ✅ Atende | TLS 1.3 enforced, certificado válido até dez/2025 | @carlos 08/mar |
| 1.5 | Secrets em vault (não em código) | ✅ Atende | Scan com gitleaks: 0 findings | @carlos 09/mar |
| 1.6 | Logs sem dados sensíveis (PII/PCI) | ✅ Atende | Log sanitizer implementado, audit em 500 log entries | @carlos 09/mar |
| 1.7 | Rate limiting configurado | ✅ Atende | 100 req/min por API key, 429 testado | @pedro 08/mar |
| 1.8 | Penetration test realizado | ✅ Atende | Relatório pentest CyberSec #2025-031, 0 críticos, 0 altos | @carlos 10/mar |

**Subtotal Segurança:** 8/8 ✅

---

### 2. Performance

| # | Critério | Status | Evidência | Verificado por |
|---|---|---|---|---|
| 2.1 | Load test com 2x tráfego esperado | ✅ Atende | k6 report: 2000 RPS sustentado por 30min, p99 < 500ms | @julia 09/mar |
| 2.2 | Sem memory leaks em teste de 24h | ✅ Atende | Grafana: heap estável em 512MB por 24h | @julia 09/mar |
| 2.3 | Database connection pool dimensionado | 🔶 Parcial | Pool atual: 20 conexões. Sob 2x carga, saturou em 85%. Recomendação: subir para 40. | @julia 09/mar |
| 2.4 | Cache hit rate > 80% para queries frequentes | ✅ Atende | Redis metrics: 87% hit rate em load test | @julia 09/mar |
| 2.5 | CDN configurada para assets estáticos | ✅ Atende | CloudFront distribution ativa, cache-control headers corretos | @pedro 08/mar |

**Subtotal Performance:** 4/5 ✅, 1 condicional

---

### 3. Observabilidade

| # | Critério | Status | Evidência | Verificado por |
|---|---|---|---|---|
| 3.1 | Métricas RED (Rate, Errors, Duration) | ✅ Atende | Dashboard Grafana "payments-v3-red" configurado | @maria 08/mar |
| 3.2 | Distributed tracing habilitado | ✅ Atende | Jaeger trace IDs propagados em todos os endpoints | @maria 08/mar |
| 3.3 | Alertas configurados para SLOs | ✅ Atende | PagerDuty: 4 alertas (latência, erro rate, saturation, availability) | @maria 09/mar |
| 3.4 | Runbook atualizado | ✅ Atende | /docs/runbooks/payments-v3.md revisado em 09/mar | @maria 09/mar |
| 3.5 | Log aggregation funcionando | ✅ Atende | Logs em Elasticsearch, retenção de 30 dias confirmada | @maria 08/mar |

**Subtotal Observabilidade:** 5/5 ✅

---

### 4. Operação

| # | Critério | Status | Evidência | Verificado por |
|---|---|---|---|---|
| 4.1 | Rollback testado e documentado | 🔶 Parcial | Rollback de código testado; rollback de schema NÃO testado (migration irreversível em tabela X) | @pedro 10/mar |
| 4.2 | Feature flags para funcionalidades novas | ✅ Atende | LaunchDarkly: 3 flags configuradas, kill-switch global funcional | @pedro 09/mar |
| 4.3 | Backup e recovery testados | ✅ Atende | Backup RDS a cada 6h, recovery testado em 10/mar (RTO: 15min) | @pedro 10/mar |
| 4.4 | Scaling automático configurado | ✅ Atende | HPA: min 3, max 10 pods, CPU target 70% | @pedro 09/mar |
| 4.5 | Documentação de on-call atualizada | ✅ Atende | Escalonamento definido, contatos atualizados em PagerDuty | @maria 10/mar |

**Subtotal Operação:** 4/5 ✅, 1 condicional

---

### Sumário de Conformidade

| Área | Atende | Parcial | Não Atende |
|---|---|---|---|
| Segurança | 8 | 0 | 0 |
| Performance | 4 | 1 | 0 |
| Observabilidade | 5 | 0 | 0 |
| Operação | 4 | 1 | 0 |
| **Total** | **21** | **2** | **0** |

### Condições para Aprovação Final
1. **Item 2.3** — Aumentar connection pool para 40 e retestar sob carga.
   Owner: @julia. Prazo: 12/mar. Bloqueante: Não (pode ir para
   produção com pool atual, mas ajustar antes do pico previsto).

2. **Item 4.1** — Documentar procedimento de rollback de schema e
   testar em staging. Owner: @pedro. Prazo: 13/mar. Bloqueante: Sim.
   Não aprovar deploy em produção sem esta validação.

### Aprovações

| Papel | Nome | Aprovação | Data |
|---|---|---|---|
| Security Lead | Carlos Lima | ✅ Aprovado | 10/mar |
| Tech Lead | Pedro Santos | 🔶 Aprovado com condição (4.1) | 10/mar |
| SRE Lead | Maria Oliveira | ✅ Aprovado | 10/mar |
| Engineering Manager | João Fernandes | ⏳ Pendente | — |
```
