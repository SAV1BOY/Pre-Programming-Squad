# KPI-Driven Planning Framework

## Propósito
Orientar o pipeline de pré-programação com base em 17 KPIs mensuráveis organizados em 4 categorias, garantindo que decisões são baseadas em dados e que o squad melhora continuamente.

## Problema que Resolve
Sem métricas, o squad não sabe se está melhorando. Checklists passam mas bugs escapam. Templates são preenchidos mas handoffs causam retrabalho. KPIs transformam "achamos que está bom" em "os dados mostram que melhoramos 30%".

## Quando Usar
- **Início de projeto:** Selecionar KPIs relevantes para o tipo/porte
- **Em cada gate transition:** Verificar se métricas estão dentro do target
- **Pós-handoff:** Coletar métricas de resultado
- **RalphLoop retro (mensal):** Analisar tendências e ajustar targets

## Os 17 KPIs do Squad

### Categoria 1: Planning Quality (5 KPIs)
| KPI | Fórmula | Target | Coleta |
|-----|---------|--------|--------|
| Ambiguity Burndown Rate | perguntas_resolvidas / perguntas_totais | >80% antes de scope | Assumptions log |
| Missed Requirement Rate | requisitos_pós_handoff / requisitos_totais | <5% | Feedback do coding squad |
| Missed Edge Case Rate | edge_cases_pós_handoff / edge_cases_totais | <10% | Defect origin analysis |
| Defect Origin in Requirements | defeitos_de_requisito / defeitos_totais | <15% | Bug tracking |
| Assumption Validation Rate | suposições_validadas / suposições_totais | >90% | Assumptions log |

### Categoria 2: Efficiency (4 KPIs)
| KPI | Fórmula | Target | Coleta |
|-----|---------|--------|--------|
| Readiness Cycle Time | data_readiness - data_intake | <7d (M), <14d (G) | Pipeline tracking |
| Planning to Delivery Ratio | tempo_planning / tempo_total | 15-25% | Time tracking |
| Rework Reduction Rate | 1 - (rework_atual / rework_baseline) | >30% | Rework reports |
| Pre-prod Defect Escape Rate | defeitos_prod / defeitos_totais | <3% | Bug tracking |

### Categoria 3: Architecture (4 KPIs)
| KPI | Fórmula | Target | Coleta |
|-----|---------|--------|--------|
| Architecture Reversal Rate | decisões_revertidas / decisões_totais | <10% | ADR tracking |
| Build vs Buy Savings | custo_evitado_por_decisão | Documentado | Decision log |
| Dependency Surprise Rate | deps_não_previstas / deps_totais | <5% | Post-handoff analysis |
| Test Readiness Score | score_SPG_testes | >85/100 | Readiness formula |

### Categoria 4: Operational (4 KPIs)
| KPI | Fórmula | Target | Coleta |
|-----|---------|--------|--------|
| Handoff Clarity Score | média_avaliação_dev | >8/10 | Survey pós-handoff |
| Rollback Readiness Score | rollback_plans / deploys | >90% | Checklist tracking |
| Production Incident Prevented | incidentes_prevenidos | Documentado | Incident review |
| Readiness Gate Pass Rate | gates_1ª_tentativa / gates_totais | >75% | Gate log |

## Processo de Uso

### Passo 1 — Selecionar KPIs por Porte
- **P (Pequeno):** 4 KPIs essenciais (Missed Requirement, Handoff Clarity, Cycle Time, Gate Pass)
- **M (Médio):** 10 KPIs core (todos os essenciais + Architecture + Rework)
- **G/XG (Grande):** Todos os 17 KPIs

### Passo 2 — Definir Baselines
Na primeira execução, coletar dados sem targets. Após 5 projetos, definir baselines realistas.

### Passo 3 — Instrumentar Coleta
Cada KPI tem fonte de dados definida. Garantir que registries e feedback loops estão configurados.

### Passo 4 — Revisar em Gates
Em cada gate transition, verificar KPIs relevantes:
- Discovery → Scope: Ambiguity Burndown Rate >80%?
- Architecture → Risk: Architecture quality adequate?
- Readiness → Handoff: All operational KPIs within target?

### Passo 5 — Analisar em RalphLoop
Mensalmente:
1. Consolidar KPIs de todos os projetos do mês
2. Identificar top 3 KPIs fora do target
3. Root cause analysis para cada um
4. Definir ação corretiva (ajustar checklist, template, processo)
5. Medir impacto no mês seguinte

## Armadilhas Comuns (Goodhart's Law)
- **Medir tudo sem foco** → Selecionar KPIs por porte, não usar todos sempre
- **Usar KPIs como punição** → KPIs servem para aprendizado, não para blame
- **Gaming de métricas** → Se gate pass rate sobe mas bugs também, o gate está fraco
- **Não atualizar targets** → Targets devem evoluir com maturidade do squad
- **Confundir leading com lagging** → Ambiguity Burndown é leading; Defect Rate é lagging. Ambos importam.

## Exemplo Real
```
Projeto: Migração de Gateway de Pagamento (porte G)
Mês: Março 2024

Planning Quality:
  - Ambiguity Burndown: 92% ✅ (target >80%)
  - Missed Requirements: 3% ✅ (target <5%)
  - Missed Edge Cases: 8% ✅ (target <10%)

Efficiency:
  - Cycle Time: 11 dias ✅ (target <14d para G)
  - Rework Rate: -35% vs baseline ✅ (target >30%)

Architecture:
  - Reversal Rate: 5% ✅ (target <10%)
  - Test Readiness: 88/100 ✅ (target >85)

Operational:
  - Handoff Clarity: 9.2/10 ✅ (target >8)
  - Gate Pass Rate: 87% ✅ (target >75%)

Score Final: 9/9 KPIs dentro do target → GOLD
```
