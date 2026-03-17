# SRE e DevOps — Fonte de Referência

## Fonte

**Organizações**: Google (SRE), Comunidade DevOps
**Prática**: Site Reliability Engineering, DevOps, observabilidade, gestão de incidentes
**Referências Principais**:
- "Site Reliability Engineering" (Livro, Google/O'Reilly, 2016) — o "SRE Book"
- "The Site Reliability Workbook" (Google/O'Reilly, 2018)
- "Accelerate" (Nicole Forsgren, Jez Humble, Gene Kim, 2018)
- "The DevOps Handbook" (Gene Kim et al., 2016)

## URL de Referência

- https://sre.google/books/
- https://sre.google/sre-book/table-of-contents/
- https://cloud.google.com/blog/products/devops-sre

---

## O que Aprender

### Error Budgets

Conceito central de SRE: se o SLO é 99.9% de disponibilidade, o time tem um "budget de erros" de 0.1% (43.8 minutos/mês). Enquanto dentro do budget, o time pode assumir riscos e lançar features. Se exceder o budget, foco muda para confiabilidade.

- Alinha incentivos: velocidade de features vs estabilidade
- Cria linguagem comum entre produto e engenharia
- Permite decisões baseadas em dados, não em medo

### SLIs, SLOs e SLAs

- **SLI (Service Level Indicator)**: Métrica que mede qualidade do serviço (latência p99, taxa de erro, throughput)
- **SLO (Service Level Objective)**: Meta interna para o SLI (latência p99 < 200ms)
- **SLA (Service Level Agreement)**: Compromisso externo com consequências (99.9% uptime ou crédito)

A distinção é crucial: SLOs devem ser mais rigorosos que SLAs para criar margem de segurança.

### Toil e Automação

Toil é trabalho manual, repetitivo, automatizável, que não gera valor duradouro. SRE tem como meta manter toil abaixo de 50% do tempo do engenheiro. O restante é investido em automação e melhoria de sistemas.

### Observabilidade

Os três pilares: logs, métricas e traces. Sistemas observáveis permitem responder perguntas que não foram antecipadas. Não basta monitorar — precisa ser possível investigar problemas novos.

### Postmortems Sem Culpa

Análise estruturada de incidentes focada em:
- Linha do tempo factual do incidente
- Causa raiz (frequentemente múltipla)
- O que funcionou, o que não funcionou
- Action items com responsáveis e prazos
- Sem atribuição de culpa individual

---

## Práticas Relevantes para Pré-Programação

1. **Definir SLIs/SLOs no design doc**: Antes de codificar, definir quais indicadores medem a saúde do serviço e quais são as metas. Isso influencia decisões de arquitetura, caching, redundância.

2. **Error budget no planejamento de release**: Verificar o error budget atual antes de planejar releases arriscados. Se o budget está quase esgotado, priorizar confiabilidade sobre features.

3. **Observabilidade como requisito não-funcional**: Incluir nos critérios de readiness review: logs estruturados definidos, métricas de negócio planejadas, traces entre serviços configurados, dashboards desenhados.

4. **Toil assessment na pré-programação**: Identificar processos manuais atuais que o novo sistema deveria automatizar. Quantificar horas de toil economizadas como métrica de sucesso do projeto.

5. **Runbook como artefato de handoff**: Todo serviço entregue ao time de dev deve ter runbook básico: como fazer deploy, como verificar saúde, como interpretar alertas, como fazer rollback.

6. **Postmortem template no squad**: Quando premissas falham ou riscos se materializam, usar formato de postmortem sem culpa para aprender e melhorar o processo.

7. **Capacity planning no design**: Estimar load esperado (requests/segundo, dados/mês, usuários concorrentes) e dimensionar a arquitetura. Incluir plano de escala para 10x o volume atual.

8. **On-call readiness como critério de go/no-go**: O sistema está pronto para ser operado? Alertas configurados? Runbooks escritos? Escala de plantão definida?
