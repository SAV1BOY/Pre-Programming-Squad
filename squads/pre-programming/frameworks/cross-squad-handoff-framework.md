# Cross-Squad Handoff Framework

## Propósito
Estruturar handoffs bidirecionais entre o Pre-Programming Squad e outros 9 squads do MMOS, garantindo que artefatos, contratos e expectativas estejam alinhados antes de qualquer transferência de responsabilidade.

## Problema que Resolve
Handoffs informais entre squads geram: contexto perdido, retrabalho por mal-entendido, dependências não rastreadas e finger-pointing quando algo dá errado. Este framework transforma handoff de "enviar email" em processo formal com aceite.

## Quando Usar
- Ao enviar qualquer artefato para outro squad (outbound)
- Ao receber input ou validação de outro squad (inbound)
- Em sincronizações periódicas cross-squad
- Quando uma dependência entre squads é identificada

## Conceitos-Chave

### 1. Handoff ≠ Dump
Handoff não é enviar documentos. É transferir **responsabilidade com contexto suficiente para ação**. O receptor deve conseguir agir sem voltar a perguntar.

### 2. Protocolo de Aceite
Todo handoff formal requer:
- **Entrega:** Squad emissor envia artefatos completos
- **Verificação:** Squad receptor confirma que artefatos são suficientes
- **Aceite:** Squad receptor assume responsabilidade formalmente
- **Registro:** Handoff registrado no `data/registries/cross-squad-handoff-registry.yaml`

### 3. SLA de Resposta
| Prioridade | Tempo de resposta | Tempo de resolução |
|------------|------------------|-------------------|
| Crítico (bloqueio ativo) | 4h | 24h |
| Alto (path crítico) | 24h | 3 dias úteis |
| Médio (planejado) | 48h | 5 dias úteis |
| Baixo (informacional) | 5 dias | Best-effort |

## Processo

### Passo 1 — Identificar Tipo de Handoff
Classificar: `input_request` | `review_request` | `handoff_delivery` | `escalation`

### Passo 2 — Preparar Pacote
Para cada squad receptor, montar pacote com:
- **Contexto:** Por que este handoff existe (1-2 parágrafos)
- **Pedido específico:** O que é esperado do receptor
- **Artefatos:** Documentos, schemas, contratos incluídos
- **Impacto:** O que acontece se o handoff atrasar
- **Timeline:** Prazo esperado para resposta
- **Ponto de contato:** Pessoa responsável no emissor

### Passo 3 — Enviar via Canal Formal
Não enviar por chat informal. Usar:
1. Registro no handoff registry
2. Notificação para o squad chief do receptor
3. Follow-up em 24h se não houver confirmação de recebimento

### Passo 4 — Verificação e Aceite
O receptor verifica:
- [ ] Artefatos estão completos e legíveis
- [ ] Contexto é suficiente para entender o pedido
- [ ] Prazo é realista
- [ ] Não há dependências ocultas

Se incompleto → devolve com lista de gaps.
Se completo → aceita formalmente e assume responsabilidade.

### Passo 5 — Registrar e Rastrear
```yaml
# data/registries/cross-squad-handoff-registry.yaml
- handoff_id: "HO-2024-042"
  date: "2024-03-15"
  source: pre-programming
  target: coding
  type: handoff_delivery
  artifacts: [implementation-package, test-design, risk-register]
  status: accepted
  acceptance_date: "2024-03-16"
  sla_met: true
```

### Passo 6 — Feedback Loop
Após conclusão do trabalho pelo receptor:
1. Coletar feedback sobre qualidade do handoff
2. Registrar rework causado por gaps no handoff
3. Alimentar `data/metrics/cross-squad-handoff-quality.yaml`
4. Ajustar processo no próximo RalphLoop retro

## Mapa de Handoffs por Squad

| Squad | Outbound (enviamos) | Inbound (recebemos) |
|-------|---------------------|---------------------|
| **Coding** | Implementation package, DoD | Feedback de implementação, rework reports |
| **Design** | UX requirements, interaction contracts | Wireframes, UX constraints |
| **Data** | Metric definitions, observability reqs | Data model constraints, benchmarks |
| **Cybersecurity** | Security review request | Security assessment, requirements |
| **DeepResearch** | Research requests, uncertainty questions | Research findings, tech evaluations |
| **C-Level** | Irreversible decisions, strategic trade-offs | Strategic context, budget decisions |
| **Advisory Board** | Strategic technical decisions | Strategic guidance |
| **Traffic** | Tracking requirements | Channel constraints |
| **Storytelling** | Feature narrative | User journey insights |

## Armadilhas Comuns
- **Assumir que o outro squad já sabe o contexto** → Sempre incluir contexto completo
- **Enviar artefatos incompletos esperando que o receptor complete** → Handoff deve ser self-contained
- **Não definir SLA de resposta** → Sempre acordar prazo antes de enviar
- **Ignorar dependências cíclicas** → Mapear bi-direcionalidade antes de iniciar
- **Usar chat como canal oficial** → Chat é para follow-up, não para handoff formal

## Métricas de Qualidade
- **Acceptance rate sem retrabalho:** >90% target
- **SLA de resposta cumprido:** >85% target
- **Feedback score do receptor:** >8/10 target
