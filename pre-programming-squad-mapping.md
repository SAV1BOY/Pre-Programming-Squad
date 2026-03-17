
# 🗺️ MAPEAMENTO COMPLETO — PRE-PROGRAMMING SQUAD (Tech / MMOS)

## O Pre-Programming Squad mais completo, pragmático e executável possível (18 agentes | Gold Standard / SOTA / HRM)

> **Objetivo:** Mapear TODOS os arquivos necessários para criar um squad de **pré-programação / pre-coding / solution readiness**
> de nível mundial dentro do MMOS, cobrindo tudo o que precisa acontecer **antes da primeira linha de código**:
> descoberta, entendimento do problema, alinhamento, escopo, arquitetura inicial, modelagem, avaliação de risco,
> design de testes, preparação de ambiente, decisão de stack, handoff para implementação e governança de prontidão.

---

## 🧠 NOTAS DE ARQUITETURA (OBRIGATÓRIO)

### O que separa "planejamento bonito" de "pré-programação que muda o jogo"

Pré-programação vira **SOTA** quando vira **sistema operacional executável**:

**Task → Agents → Frameworks → Checklists → Templates → Registries → Metrics → Aprendizado (RalphLoop)**

Não basta gerar checklist de requisitos.
Não basta escrever PRD.
Não basta desenhar arquitetura.

O squad só é realmente **gold standard** quando consegue:

1. **descobrir o problema real antes da solução**;
2. **transformar ambiguidade em escopo operacional**;
3. **traduzir contexto de negócio em decisões técnicas**;
4. **antecipar falhas antes de elas virarem bugs**;
5. **desenhar testes antes do código**;
6. **saber exatamente quando já é hora de implementar**.

### O que alguém 100x mais inteligente faria?

Criaria o **`config.yaml` como cérebro de roteamento**:

- para cada tipo de projeto/tarefa:
  - **quais agentes chamar**;
  - **em qual ordem**;
  - **quais frameworks são obrigatórios**;
  - **quais checklists precisam passar**;
  - **quais templates geram o output**;
  - **onde registrar** em `data/registries/`;
  - **quais métricas** em `data/metrics/` provam que o planejamento foi bom;
  - **quais handoffs cross-squad** são obrigatórios antes de liberar desenvolvimento.

E criaria também o **`ARCHITECTURE.md` como a constituição**:

- como o squad pensa;
- como qualifica prontidão;
- como conflitos são resolvidos;
- como riscos são escalados;
- como decisões irreversíveis são tratadas;
- como o squad aprende com falhas de planejamento.

### Princípio central

**Pedido → Descoberta → Escopo → Decomposição → Arquitetura → Riscos → Testes → Prontidão → Handoff → Memória**

---

## 📐 ESTRUTURA RAIZ DO SQUAD

```text
squads/pre-programming/
├── agents/
├── archive/
├── authority/
├── checklists/
│   ├── chief/
│   ├── discovery/
│   ├── scope/
│   ├── business/
│   ├── architecture/
│   ├── domain/
│   ├── data/
│   ├── api/
│   ├── testing/
│   ├── risk/
│   ├── security/
│   ├── performance/
│   ├── operations/
│   ├── estimation/
│   ├── readiness/
│   ├── handoff/
│   ├── ai-systems/
│   ├── legacy/
│   └── cross-squad/
├── data/
│   ├── research/
│   ├── registries/
│   ├── metrics/
│   ├── readiness-reviews/
│   ├── decision-memos/
│   ├── assumptions/
│   ├── risks/
│   ├── test-designs/
│   ├── architecture-notes/
│   └── project-briefs/
├── docs/
├── frameworks/
├── lib/
│   ├── components/
│   ├── patterns/
│   ├── utilities/
│   └── taxonomies/
├── phrases/
├── projects/
├── reference/
│   ├── books/
│   ├── papers/
│   ├── engineering/
│   ├── architecture/
│   ├── testing/
│   ├── product/
│   ├── operations/
│   ├── ai/
│   ├── psychology/
│   └── industries/
├── scripts/
├── swipe/
├── swipe-sources/
├── tasks/
├── templates/
├── voice/
├── workflows/
├── ARCHITECTURE.md
├── config.yaml
├── README.md
└── swipe.config
```

---

# 1. 🤖 AGENTS/ — 18 Agentes do Pre-Programming Squad

Cada arquivo `.md` contém: tese central, princípios, frameworks favoritos, heurísticas de decisão,
anti-padrões, padrões de output, checklists de revisão e prompt de ativação.

## 1.1 Comando e orquestração

```text
agents/
├── pre-programming-chief.md            # Orquestrador: escopo, prioridade, governança, win condition, go/no-go
├── readiness-gatekeeper.md             # Decide se o projeto está pronto para implementação ou não
```

## 1.2 Descoberta e entendimento do problema

```text
agents/
├── problem-framer.md                   # Delimita o problema real, separa sintoma vs causa, define boundaries
├── requirements-clarifier.md           # Esclarece requisitos explícitos/implícitos e remove ambiguidades
├── business-translator.md              # Traduz objetivos de negócio em critérios técnicos e operacionais
├── stakeholder-mapper.md               # Mapeia stakeholders, dependências, donos, alinhamentos e conflitos
```

## 1.3 Solução e arquitetura inicial

```text
agents/
├── system-architect.md                 # Arquitetura inicial, módulos, responsabilidades, boundaries
├── domain-modeler.md                   # Entidades, relações, regras de negócio, invariantes e estados
├── interface-designer.md               # APIs, contratos, eventos, integrações, inputs/outputs
├── decomposition-engineer.md           # Quebra o problema em partes implementáveis e ordenáveis
```

## 1.4 Qualidade, risco e testabilidade

```text
agents/
├── failure-analyst.md                  # Edge cases, unhappy paths, rollback, consistência, falhas previsíveis
├── test-strategist.md                  # Testes antes do código: unit, integration, contract, e2e, load
├── security-and-trust-reviewer.md      # Segurança, privacidade, authn/authz, misuse cases
├── performance-capacity-planner.md     # Performance, escala, gargalos, custo computacional, latência
```

## 1.5 Implementabilidade e entrega

```text
agents/
├── build-vs-buy-analyst.md             # Reusar vs construir, stack, dependências, custo de manutenção
├── legacy-impact-auditor.md            # Compatibilidade com legado, impactos laterais, migração
├── estimation-planner.md               # Esforço, fatiamento, milestones, sequencing, risco de prazo
├── handoff-orchestrator.md             # Gera pacote de handoff para squad de implementação / coding squad
```

## 1.6 Regras anti-caos

- **Pre-Programming Chief** define a `win condition`, prioriza e protege o rigor.
- **Readiness Gatekeeper** tem poder de veto: sem passar no gate, não começa implementação.
- **Problem Framer** manda em **problema real** e impede solução prematura.
- **Requirements Clarifier** mata ambiguidade antes que ela vire retrabalho.
- **Business Translator** garante que técnica sirva negócio — não o contrário.
- **System Architect** manda em **estrutura**, boundaries e trade-offs.
- **Domain Modeler** protege a integridade da lógica do domínio.
- **Interface Designer** impede contratos vagos ou integrações improvisadas.
- **Failure Analyst** obriga o time a pensar no que dá errado antes do happy path.
- **Test Strategist** transforma requisitos em verificação objetiva antes do código.
- **Security Reviewer** evita que segurança vire retrofit caro.
- **Performance Planner** impede soluções inocentemente lentas/caras.
- **Build vs Buy Analyst** protege simplicidade, velocidade e foco.
- **Legacy Impact Auditor** evita quebrar produção por ignorar contexto existente.
- **Estimation Planner** transforma ambição em execução realista.
- **Handoff Orchestrator** garante que o dev receba um pacote claro e completo.

**Total de Agents: 18 arquivos**

---

# 2. ✅ CHECKLISTS/ — Quality Gates (Pre-Programming)

> Regra: **nada entra em desenvolvimento** sem passar pelos gates certos.

## 2.1 Checklists macro por entregável

```text
checklists/
├── project-brief-quality.md                     # Problema, objetivo, stakeholders, restrições, sucesso
├── discovery-quality.md                         # Sintoma vs causa, contexto, escopo, perguntas abertas
├── requirements-quality.md                      # Requisitos claros, explícitos, implícitos, ambiguidades
├── scope-definition-quality.md                  # In-scope/out-of-scope, MVP, cortes, prioridades
├── solution-options-quality.md                  # Alternativas, trade-offs, motivo da escolha
├── architecture-sketch-quality.md               # Módulos, fluxo, boundaries, responsabilidades
├── domain-model-quality.md                      # Entidades, invariantes, estados, ciclos de vida
├── api-contract-quality.md                      # Endpoints, payloads, versionamento, erros, compatibilidade
├── integration-impact-quality.md                # Dependências, terceiros, contratos externos, limites
├── failure-modes-quality.md                     # Unhappy paths, edge cases, rollback, degradação segura
├── test-design-quality.md                       # Unit/integration/e2e/contract/load definidos antes do código
├── security-review-quality.md                   # Auth, permissões, dados sensíveis, misuse cases, abuso
├── performance-review-quality.md                # Latência, throughput, escalabilidade, custos, gargalos
├── observability-quality.md                     # Logs, métricas, tracing, alertas, debuggability
├── build-vs-buy-quality.md                      # Reuso, dependências, lock-in, manutenção, ROI
├── legacy-compatibility-quality.md              # Backward compatibility, migração, blast radius
├── estimation-quality.md                        # Breakdown, esforço, risco, dependências, buffers
├── readiness-review-quality.md                  # Go/No-Go para implementação
├── handoff-package-quality.md                   # Dev package completo: docs, contratos, testes, riscos
├── decision-memo-quality.md                     # Contexto, opções, trade-offs, recomendação, owner, data
├── assumptions-log-quality.md                   # Suposições, validações pendentes, owners, revisão
├── dependency-map-quality.md                    # Dependências técnicas, organizacionais, externas
├── environment-readiness-quality.md             # Ambientes, acessos, ferramentas, mocks, datasets
├── ai-solution-readiness-quality.md             # Se for IA: prompts, evals, guardrails, fallback, observability
├── legacy-refactor-readiness-quality.md         # Se for refactor: boundaries, characterization, rollout
├── incident-risk-precheck-quality.md            # Risco operacional antes de tocar produção
├── change-management-quality.md                 # Comunicação, rollout, rollback, stakeholders
└── cross-squad-handoff-quality.md               # Handoff com Product, Design, Data, Cyber, C-Level, etc.
```

## 2.2 Subpastas por escola / função

### 2.2.1 Discovery

```text
checklists/discovery/
├── problem-definition-audit.md                  # Problema está claro e delimitado?
├── symptom-vs-root-cause-audit.md               # Sintoma ≠ causa
├── stakeholder-intent-audit.md                  # O que cada stakeholder realmente quer?
├── ambiguity-kill-list.md                       # Perguntas em aberto, termos vagos, decisões pendentes
├── success-criteria-audit.md                    # Como saber que deu certo?
├── constraint-mapping-audit.md                  # Restrições reais vs assumidas
└── mvp-boundary-check.md                        # Menor escopo valioso
```

### 2.2.2 Architecture

```text
checklists/architecture/
├── boundary-definition-audit.md                 # Responsabilidades e fronteiras claras
├── module-decomposition-audit.md                # Quebra correta em módulos / serviços / camadas
├── complexity-budget-check.md                   # Complexidade justificada ou acidental?
├── coupling-and-cohesion-audit.md               # Acoplamento e coesão
├── reversibility-check.md                       # Decisões reversíveis vs irreversíveis
├── simplicity-vs-robustness-audit.md           # Solução certa no nível certo
└── first-version-architecture-check.md          # Arquitetura da v1 sem overengineering
```

### 2.2.3 Testing

```text
checklists/testing/
├── requirement-to-test-traceability.md          # Cada requisito gera verificação?
├── unhappy-path-test-coverage.md                # Falhas mapeadas antes do código
├── contract-test-readiness.md                   # Contratos entre sistemas verificáveis
├── integration-test-readiness.md                # Integrações críticas testáveis
├── load-and-perf-test-readiness.md              # Critérios não-funcionais verificáveis
├── testability-audit.md                         # Arquitetura é testável?
└── definition-of-done-readiness.md              # Critérios de pronto definidos
```

### 2.2.4 Risk / Security / Ops

```text
checklists/risk/
├── blast-radius-check.md                        # O que quebra se der errado?
├── rollback-strategy-audit.md                   # Reversão realista
├── operational-risk-check.md                    # Operação, suporte, monitoramento
├── dependency-failure-audit.md                  # E se o terceiro cair?
├── data-consistency-risk-check.md               # Integridade e concorrência
├── migration-risk-check.md                      # Migrações e compatibilidade
└── risk-prioritization-matrix.md                # Probabilidade x impacto x detectabilidade
```

### 2.2.5 Handoff / Readiness

```text
checklists/readiness/
├── implementation-ready-check.md                # O time pode começar sem adivinhar?
├── unanswered-questions-zero-check.md          # Existe ambiguidade crítica aberta?
├── dev-package-completeness.md                  # Artefatos suficientes para implementação
├── decision-log-currency.md                     # Decisões registradas e atuais
├── owner-and-accountability-check.md            # Donos claros
├── timeline-and-gates-check.md                  # Fases, gates, marcos
└── final-go-no-go-audit.md                      # Liberação formal
```

---

# 3. 🧩 FRAMEWORKS/ — Como o squad pensa

## 3.1 Frameworks universais (núcleo)

```text
frameworks/
├── problem-framing-canvas.md
├── five-whys-plus-boundaries.md
├── symptom-cause-separation.md
├── stakeholder-intent-map.md
├── assumptions-to-evidence-framework.md
├── constraints-led-design.md
├── mvp-scope-pruning-framework.md
├── outcome-driven-development.md
├── reversible-vs-irreversible-decisions.md
├── build-vs-buy-decision-framework.md
├── simplicity-vs-robustness-framework.md
├── architectural-option-comparison.md
├── failure-mode-thinking-framework.md
├── edge-case-explosion-framework.md
├── requirement-to-test-mapping.md
├── testability-by-design.md
├── risk-weighted-planning.md
├── blast-radius-assessment-framework.md
├── dependency-criticality-matrix.md
├── legacy-boundary-isolation-framework.md
├── rollout-and-rollback-framework.md
├── readiness-score-framework.md
├── go-no-go-decision-framework.md
├── project-slicing-framework.md
├── estimation-under-uncertainty-framework.md
├── observability-by-design.md
├── security-by-design-primer.md
├── performance-by-design-primer.md
├── architecture-decision-record-framework.md
└── handoff-completeness-framework.md
```

## 3.2 Frameworks proprietários dos agentes

```text
frameworks/discovery/
├── real-problem-locator.md
├── ambiguity-burn-down-system.md
├── solution-jump-prevention.md
├── constraint-truth-table.md

frameworks/architecture/
├── v1-architecture-lens.md
├── boundary-first-design.md
├── integration-pressure-map.md
├── data-shape-before-code.md

frameworks/testing/
├── tests-before-tasks.md
├── requirement-proof-chain.md
├── unhappy-path-first.md
├── test-surface-mapping.md

frameworks/risk/
├── pre-bug-risk-forecast.md
├── production-impact-screen.md
├── rollback-safety-ladder.md
├── failure-rehearsal-framework.md

frameworks/readiness/
├── implementation-readiness-score.md
├── zero-guesswork-handoff.md
├── red-flag-escalation-framework.md
├── decision-maturity-model.md
```

## 3.3 Frameworks de stack / contexto

```text
frameworks/stacks/
├── backend-pre-coding-framework.md
├── frontend-pre-coding-framework.md
├── mobile-pre-coding-framework.md
├── api-first-readiness-framework.md
├── legacy-refactor-readiness-framework.md
├── automation-workflow-readiness-framework.md
├── ai-agent-solution-readiness-framework.md
├── enterprise-integration-readiness-framework.md
└── internal-tooling-readiness-framework.md
```

## 3.4 Frameworks de referência intelectual

```text
frameworks/reference-intellectual/
├── ousterhout-complexity-management.md          # John Ousterhout: complexity is the enemy (A Philosophy of Software Design)
├── kleppmann-data-intensive-design.md           # Martin Kleppmann: design for data, not just code
├── fowler-evolutionary-architecture.md          # Martin Fowler: arquitetura evolutiva, refactoring contínuo
├── beck-test-driven-design.md                   # Kent Beck: TDD como ferramenta de design (não só de teste)
├── evans-domain-driven-design.md                # Eric Evans: linguagem ubíqua, bounded contexts, aggregates
├── feathers-legacy-code.md                      # Michael Feathers: trabalhar com legado sem medo
├── nygard-release-it.md                         # Michael Nygard: design for production (circuit breakers, bulkheads)
├── cagan-discovery-vs-delivery.md               # Marty Cagan: descobrir o que construir antes de construir
├── kahneman-noise-in-planning.md                # Kahneman: noise e bias em estimativas e decisões técnicas
├── taleb-antifragile-systems.md                 # Taleb: sistemas antifrágeis, redundância, optionalidade
├── meadows-leverage-points-in-systems.md        # Meadows: pontos de alavancagem em sistemas complexos
├── goldratt-bottleneck-thinking.md              # Goldratt: theory of constraints aplicada a software
├── goodhart-law-in-metrics.md                   # Goodhart: quando métrica vira meta, deixa de ser boa métrica
└── brooks-mythical-man-month.md                 # Fred Brooks: "adding people to a late project makes it later"
```

---

# 4. 📚 REFERENCE/ — Base de conhecimento curada

## 4.1 Livros

```text
reference/books/
├── a-philosophy-of-software-design-john-ousterhout.md
├── designing-data-intensive-applications-martin-kleppmann.md
├── software-engineering-at-google.md
├── accelerate.md
├── fundamentals-of-software-architecture.md
├── clean-architecture-robert-martin.md
├── domain-driven-design-eric-evans.md
├── implementing-domain-driven-design-vaughn-vernon.md
├── system-design-interview-alex-xu.md
├── test-driven-development-by-example-kent-beck.md
├── specification-by-example-gj-adzic.md
├── working-effectively-with-legacy-code-michael-feathers.md
├── release-it-michael-nygard.md
├── building-evolutionary-architectures.md
├── team-topologies.md
├── continuous-delivery.md
├── inspired-marty-cagan.md
├── empowered-marty-cagan.md
├── the-devops-handbook.md
├── site-reliability-engineering-google.md
```

## 4.2 Outras referências

```text
reference/papers/
├── cost-of-change-and-defect-detection.md
├── design-doc-culture-google.md
├── requirements-engineering-failure-patterns.md
├── shift-left-testing-principles.md

reference/engineering/
├── design-doc-examples.md
├── adr-examples.md
├── prd-examples.md
├── architecture-review-examples.md

reference/testing/
├── test-pyramid.md
├── contract-testing.md
├── property-based-testing.md
├── chaos-and-failure-testing.md

reference/product/
├── user-story-quality.md
├── job-to-be-done-primer.md
├── product-discovery-principles.md

reference/ai/
├── llm-evals-primer.md
├── ai-guardrails-primer.md
├── agentic-system-risk-primer.md

reference/industries/
├── fintech-readiness-primer.md
├── healthcare-readiness-primer.md
├── ecommerce-readiness-primer.md
├── enterprise-saas-readiness-primer.md
├── internal-ops-readiness-primer.md
├── marketplace-readiness-primer.md
├── edtech-readiness-primer.md
├── media-readiness-primer.md
├── crypto-readiness-primer.md
└── brazil-latam-readiness-context.md

reference/psychology/
├── confirmation-bias-in-requirements.md       # Viés de confirmação: ver só o que quer nos requisitos
├── anchoring-in-estimation.md                 # Ancoragem: primeira estimativa contamina tudo
├── sunk-cost-in-architecture.md               # Custo afundado: não jogar fora decisão ruim
├── overconfidence-in-planning.md              # Overconfidence: "vai ser simples" quando não é
├── planning-fallacy.md                        # Falácia do planejamento: subestimar sempre
├── dunning-kruger-in-tech-choices.md          # Dunning-Kruger: não saber o que não sabe
├── groupthink-in-design-reviews.md            # Groupthink: concordar sem questionar
├── availability-heuristic-in-risk.md          # Disponibilidade: superestimar riscos recentes
├── status-quo-bias-in-legacy.md               # Viés de status quo: "sempre foi assim"
├── narrative-fallacy-in-postmortems.md        # Falácia narrativa: inventar causa simples para falha complexa
├── survivorship-bias-in-stack-choice.md       # Viés de sobrevivência: "empresa X usa, então funciona"
└── optimism-bias-in-timelines.md              # Otimismo: "dessa vez vai ser diferente"
```

---

# 5. 🧱 TEMPLATES/ — Outputs reutilizáveis

```text
templates/
├── project-brief-template.md
├── discovery-template.md
├── requirements-clarification-template.md
├── stakeholder-alignment-template.md
├── constraint-map-template.md
├── scope-definition-template.md
├── solution-options-template.md
├── architecture-sketch-template.md
├── domain-model-template.md
├── api-contract-template.md
├── integration-map-template.md
├── data-model-template.md
├── risk-register-template.md
├── assumptions-log-template.md
├── failure-mode-review-template.md
├── test-design-template.md
├── definition-of-done-template.md
├── environment-readiness-template.md
├── estimation-template.md
├── rollout-plan-template.md
├── rollback-plan-template.md
├── observability-plan-template.md
├── security-review-template.md
├── performance-plan-template.md
├── build-vs-buy-template.md
├── legacy-impact-template.md
├── decision-memo-template.md
├── readiness-review-template.md
├── implementation-handoff-template.md
└── go-no-go-template.md
```

---

# 6. 🗂️ TASKS/ — Tipos de tarefa que o squad executa

```text
tasks/
├── project-intake/
│   ├── intake-brief.md
│   ├── clarify-request.md
│   └── classify-project.md
├── discovery/
│   ├── run-problem-framing.md
│   ├── map-stakeholders.md
│   ├── identify-constraints.md
│   └── define-success.md
├── scoping/
│   ├── define-mvp.md
│   ├── split-phases.md
│   ├── mark-out-of-scope.md
│   └── prioritize-risks.md
├── architecture/
│   ├── sketch-architecture-v1.md
│   ├── compare-solution-options.md
│   ├── define-boundaries.md
│   └── define-contracts.md
├── quality/
│   ├── map-edge-cases.md
│   ├── design-test-strategy.md
│   ├── run-security-precheck.md
│   └── run-performance-precheck.md
├── legacy/
│   ├── analyze-existing-system.md
│   ├── assess-compatibility.md
│   └── plan-migration.md
├── readiness/
│   ├── score-readiness.md
│   ├── build-dev-package.md
│   ├── run-go-no-go.md
│   └── handoff-to-dev.md
├── postmortem-learning/
│   ├── analyze-planning-failure.md
│   ├── update-checklists.md
│   └── update-frameworks.md
```

---

# 7. 🎯 SWIPE + SWIPE-SOURCES/ — Exemplos e fontes-modelo

## 7.1 Swipe

```text
swipe/
├── great-project-briefs.md
├── great-design-docs.md
├── great-adrs.md
├── great-api-contracts.md
├── great-test-plans.md
├── great-risk-registers.md
├── great-rollout-plans.md
├── great-handoff-packets.md
├── bad-briefs-and-why-they-failed.md
├── bad-architectures-and-why-they-broke.md
├── bad-migration-plans.md
├── bad-estimation-patterns.md
└── bad-pre-coding-smells.md
```

## 7.2 Swipe sources

```text
swipe-sources/
├── google-design-docs-source.md
├── amazon-working-backwards-source.md
├── stripe-engineering-source.md
├── uber-engineering-source.md
├── netflix-tech-source.md
├── martin-fowler-source.md
├── thoughtworks-source.md
└── sre-and-devops-source.md
```

---

# 8. 🗣️ VOICE/ — Como o squad comunica

```text
voice/
├── tone-profiles/
│   ├── staff-engineer.md
│   ├── principal-engineer.md
│   ├── architect.md
│   ├── product-tech-bridge.md
│   ├── executive-summary.md
│   └── implementation-handoff.md
├── calibration/
│   ├── concise.md
│   ├── standard.md
│   ├── deep-dive.md
│   └── audit-mode.md
├── language/
│   ├── anti-vague-language.md
│   ├── tradeoff-language.md
│   ├── risk-language.md
│   ├── uncertainty-language.md
│   ├── decision-language.md
│   └── escalation-language.md
├── channels/
│   ├── memo-style.md
│   ├── review-style.md
│   ├── handoff-style.md
│   ├── incident-precheck-style.md
│   └── exec-readout-style.md
```

---

# 9. 💬 PHRASES/ — Frases operacionais

```text
phrases/
├── clarify-before-build.md
├── no-guesswork-language.md
├── tradeoff-framing.md
├── risk-framing.md
├── scope-control-language.md
├── anti-overengineering-language.md
├── anti-solution-jump-language.md
├── test-first-language.md
├── stakeholder-alignment-language.md
├── architecture-review-language.md
├── dependency-language.md
├── handoff-language.md
├── go-no-go-language.md
├── uncertainty-language.md
├── assumption-language.md
├── rollback-language.md
├── legacy-warning-language.md
└── readiness-language.md
```

---

# 10. 🔄 WORKFLOWS/ — Playbooks ponta-a-ponta

```text
workflows/
├── 01-project-intake-to-clarity.md
├── 02-discovery-to-scope.md
├── 03-scope-to-architecture.md
├── 04-architecture-to-risk-review.md
├── 05-risk-review-to-test-design.md
├── 06-test-design-to-readiness.md
├── 07-readiness-to-dev-handoff.md
├── 08-legacy-change-readiness.md
├── 09-api-first-readiness-workflow.md
├── 10-backend-readiness-workflow.md
├── 11-frontend-readiness-workflow.md
├── 12-mobile-readiness-workflow.md
├── 13-automation-readiness-workflow.md
├── 14-ai-agent-readiness-workflow.md
├── 15-enterprise-integration-readiness-workflow.md
├── 16-refactor-readiness-workflow.md
├── 17-security-and-performance-precheck.md
├── 18-rollout-and-rollback-readiness.md
├── 19-go-no-go-cadence.md
└── 20-ralphloop-planning-retro.md
```

---

# 11. 🧠 DATA/ — Memória operacional

```text
data/
├── research/
│   ├── project-context-notes.md
│   ├── domain-research-notes.md
│   ├── stack-research-notes.md
│   └── dependency-research-notes.md
├── registries/
│   ├── assumptions-log.yaml
│   ├── decision-log.yaml
│   ├── architecture-decisions.yaml
│   ├── test-design-registry.yaml
│   ├── risk-register.yaml
│   ├── dependency-map.yaml
│   ├── readiness-reviews.yaml
│   ├── project-brief-registry.yaml
│   ├── scope-cuts-registry.yaml
│   ├── integration-contracts.yaml
│   ├── legacy-impact-registry.yaml
│   ├── go-no-go-log.yaml
│   └── handoff-registry.yaml
├── metrics/
│   ├── planning-quality-kpis.yaml
│   ├── ambiguity-burndown.yaml
│   ├── rework-rate.yaml
│   ├── missed-edge-case-rate.yaml
│   ├── defect-origin-map.yaml
│   ├── planning-cycle-time.yaml
│   ├── handoff-clarity-score.yaml
│   ├── test-readiness-score.yaml
│   ├── risk-capture-rate.yaml
│   └── rollback-readiness-score.yaml
├── readiness-reviews/
├── decision-memos/
├── assumptions/
├── risks/
├── test-designs/
├── architecture-notes/
└── project-briefs/
```

---

# 12. 📝 DOCS/ — Documentação executiva e técnica

```text
docs/
├── squad-charter.md
├── operating-model.md
├── readiness-definition.md
├── what-good-looks-like.md
├── project-intake-standard.md
├── discovery-standard.md
├── scoping-standard.md
├── architecture-review-standard.md
├── test-design-standard.md
├── risk-review-standard.md
├── security-precheck-standard.md
├── performance-precheck-standard.md
├── build-vs-buy-standard.md
├── legacy-readiness-standard.md
├── estimation-standard.md
├── handoff-standard.md
├── go-no-go-standard.md
└── ralphloop-retro-standard.md
```

---

# 13. ⚙️ SCRIPTS/ — Automação do processo

```text
scripts/
├── validation/
│   ├── validate-project-brief.py
│   ├── validate-architecture-note.py
│   ├── validate-risk-register.py
│   └── validate-handoff-package.py
├── reporting/
│   ├── readiness-score-report.py
│   ├── ambiguity-burndown-report.py
│   ├── defect-origin-report.py
│   └── planning-quality-dashboard.py
├── utilities/
│   ├── adr-generator.py
│   ├── checklist-runner.py
│   ├── dependency-map-builder.py
│   ├── test-matrix-builder.py
│   ├── rollout-checker.py
│   └── decision-memo-generator.py
```

---

# 14. 🧰 LIB/ — Componentes reutilizáveis

```text
lib/
├── components/
│   ├── project-brief-schema.json
│   ├── architecture-note-schema.json
│   ├── api-contract-schema.json
│   ├── risk-register-schema.json
│   ├── test-plan-schema.json
│   ├── readiness-review-schema.json
│   ├── handoff-package-schema.json
│   └── decision-memo-schema.json
├── patterns/
│   ├── boundary-patterns.md
│   ├── anti-overengineering-patterns.md
│   ├── migration-patterns.md
│   ├── observability-patterns.md
│   ├── rollback-patterns.md
│   ├── interface-design-patterns.md
│   ├── decomposition-patterns.md
│   └── estimation-patterns.md
├── utilities/
│   ├── scoring-models.md
│   ├── readiness-formulas.md
│   ├── risk-heatmap-logic.md
│   ├── decision-tree-helpers.md
│   ├── effort-sizing-helpers.md
│   ├── dependency-scoring-helpers.md
│   └── ambiguity-detection-helpers.md
├── taxonomies/
│   ├── requirement-taxonomy.md
│   ├── risk-taxonomy.md
│   ├── failure-taxonomy.md
│   ├── test-taxonomy.md
│   ├── project-type-taxonomy.md
│   └── readiness-taxonomy.md
```

---

# 15. 🗃️ ARCHIVE/ — Casos, falhas e learnings

```text
archive/
├── iconic/
│   ├── great-prd-examples.md
│   ├── great-design-docs-examples.md
│   ├── great-adr-examples.md
│   └── great-rollout-examples.md
├── failures/
│   ├── requirement-misread-failures.md
│   ├── edge-case-omission-failures.md
│   ├── legacy-impact-failures.md
│   ├── premature-architecture-failures.md
│   ├── bad-build-vs-buy-failures.md
│   ├── missing-rollback-failures.md
│   └── no-test-design-failures.md
├── evolution/
│   ├── v1-to-v2-preprogramming-maturity.md
│   ├── readiness-model-evolution.md
│   └── checklist-evolution-log.md
```

---

# 16. 🏛️ AUTHORITY/ — Resumos executivos de autoridade

```text
authority/
├── john-ousterhout-summary.md
├── martin-kleppmann-summary.md
├── software-engineering-at-google-summary.md
├── kent-beck-summary.md
├── michael-feathers-summary.md
├── marty-cagan-summary.md
├── michael-nygard-summary.md
├── allspaw-summary.md
├── thoughtworks-summary.md
├── sre-summary.md
├── design-doc-workshop-kit.md
├── readiness-review-workshop-kit.md
├── risk-review-workshop-kit.md
├── test-design-workshop-kit.md
└── pre-coding-audit-workshop-kit.md
```

---

# 17. 🚀 PROJECTS/ — Tipos de projeto com fases numeradas

```text
projects/
├── new-feature/
│   ├── 01-intake.md
│   ├── 02-discovery.md
│   ├── 03-scope.md
│   ├── 04-architecture.md
│   ├── 05-risks.md
│   ├── 06-tests.md
│   ├── 07-readiness.md
│   └── 08-handoff.md
├── bugfix-critical/
├── legacy-refactor/
├── api-integration/
├── internal-tool/
├── automation-project/
├── ai-agent-project/
├── enterprise-rollout/
└── mobile-feature/
```

---

# 18. 🧭 ROOT/CONFIG — Sistema operacional executável

## 18.1 `ARCHITECTURE.md`

Deve documentar:

- missão do squad;
- definição de "implementation readiness";
- regras de roteamento;
- papéis dos agentes;
- quality gates obrigatórios;
- como o RalphLoop funciona;
- quais casos exigem escalonamento;
- como o squad interage com Coding, Design, Data, Cyber, Product e C-Level.

## 18.2 `config.yaml` — O "Cérebro de Roteamento" (completo)

```yaml
# ============================================================
# PRE-PROGRAMMING SQUAD — config.yaml (Cérebro de Roteamento)
# ============================================================

squad:
  name: pre-programming
  version: "2.0.0"
  description: "Implementation Readiness: tudo que acontece ANTES da primeira linha de código"
  chief_agent: pre-programming-chief
  agents: 18
  pipeline: "Pedido → Descoberta → Escopo → Decomposição → Arquitetura → Riscos → Testes → Prontidão → Handoff → Memória"

principles:
  - understand_before_build           # Entender o problema antes de resolver
  - clarity_over_speed                # Clareza > velocidade
  - test_design_before_code           # Testes desenhados antes do código
  - anticipate_failure                # Antecipar falhas antes que virem bugs
  - simplest_viable_architecture      # Arquitetura mais simples que resolve o problema
  - evidence_over_assumption          # Evidência > suposição
  - zero_guesswork_handoff            # Dev recebe pacote sem adivinhar

# ============================================================
# ROUTING
# ============================================================

routing:

  # ---- INTAKE & DISCOVERY ----
  project-intake:
    agents: [pre-programming-chief, problem-framer, requirements-clarifier]
    frameworks: [problem-framing-canvas, symptom-cause-separation]
    checklists: [project-brief-quality, discovery-quality]
    templates: [project-brief-template, discovery-template]
    registry: [data/registries/project-brief-registry, data/registries/assumptions-log]

  run-discovery:
    agents: [problem-framer, requirements-clarifier, business-translator, stakeholder-mapper]
    frameworks: [five-whys-plus-boundaries, stakeholder-intent-map, assumptions-to-evidence-framework, discovery/real-problem-locator, discovery/ambiguity-burn-down-system]
    checklists: [discovery-quality, requirements-quality, discovery/problem-definition-audit, discovery/symptom-vs-root-cause-audit, discovery/ambiguity-kill-list, discovery/success-criteria-audit]
    templates: [discovery-template, requirements-clarification-template, stakeholder-alignment-template, constraint-map-template]
    registry: [data/registries/assumptions-log, data/registries/decision-log]

  clarify-requirements:
    agents: [requirements-clarifier, business-translator]
    frameworks: [discovery/solution-jump-prevention, discovery/constraint-truth-table, outcome-driven-development]
    checklists: [requirements-quality, assumptions-log-quality, discovery/constraint-mapping-audit]
    templates: [requirements-clarification-template, assumptions-log-template]
    registry: [data/registries/assumptions-log, data/registries/decision-log]

  map-stakeholders:
    agents: [stakeholder-mapper, pre-programming-chief]
    frameworks: [stakeholder-intent-map]
    checklists: [discovery/stakeholder-intent-audit, dependency-map-quality]
    templates: [stakeholder-alignment-template]
    registry: [data/registries/dependency-map]

  # ---- SCOPING ----
  define-scope:
    agents: [pre-programming-chief, problem-framer, business-translator]
    frameworks: [mvp-scope-pruning-framework, constraints-led-design, project-slicing-framework]
    checklists: [scope-definition-quality, discovery/mvp-boundary-check]
    templates: [scope-definition-template]
    registry: [data/registries/scope-cuts-registry, data/registries/decision-log]

  # ---- ARCHITECTURE ----
  sketch-architecture-v1:
    agents: [system-architect, domain-modeler, interface-designer, decomposition-engineer]
    frameworks: [architecture/v1-architecture-lens, architecture/boundary-first-design, architecture/data-shape-before-code, architectural-option-comparison, simplicity-vs-robustness-framework]
    checklists: [architecture-sketch-quality, architecture/boundary-definition-audit, architecture/module-decomposition-audit, architecture/complexity-budget-check, architecture/reversibility-check, architecture/first-version-architecture-check]
    templates: [architecture-sketch-template, domain-model-template, decision-memo-template]
    registry: [data/registries/architecture-decisions, data/registries/decision-log]

  compare-solution-options:
    agents: [system-architect, build-vs-buy-analyst, pre-programming-chief]
    frameworks: [architectural-option-comparison, build-vs-buy-decision-framework, reversible-vs-irreversible-decisions]
    checklists: [solution-options-quality, build-vs-buy-quality]
    templates: [solution-options-template, build-vs-buy-template, decision-memo-template]
    registry: [data/registries/architecture-decisions, data/registries/decision-log]

  define-api-contracts:
    agents: [interface-designer, system-architect]
    frameworks: [architecture/integration-pressure-map, stacks/api-first-readiness-framework]
    checklists: [api-contract-quality, integration-impact-quality]
    templates: [api-contract-template, integration-map-template]
    registry: [data/registries/integration-contracts]

  define-domain-model:
    agents: [domain-modeler, system-architect]
    frameworks: [architecture/data-shape-before-code]
    checklists: [domain-model-quality]
    templates: [domain-model-template, data-model-template]
    registry: [data/registries/architecture-decisions]

  # ---- QUALITY & RISK ----
  map-failure-modes:
    agents: [failure-analyst, system-architect, security-and-trust-reviewer]
    frameworks: [failure-mode-thinking-framework, edge-case-explosion-framework, blast-radius-assessment-framework, risk/pre-bug-risk-forecast, risk/production-impact-screen]
    checklists: [failure-modes-quality, risk/blast-radius-check, risk/rollback-strategy-audit, risk/dependency-failure-audit, risk/data-consistency-risk-check]
    templates: [failure-mode-review-template, risk-register-template]
    registry: [data/registries/risk-register, data/risks]

  design-test-strategy:
    agents: [test-strategist, failure-analyst]
    frameworks: [requirement-to-test-mapping, testability-by-design, testing/tests-before-tasks, testing/unhappy-path-first, testing/test-surface-mapping]
    checklists: [test-design-quality, testing/requirement-to-test-traceability, testing/unhappy-path-test-coverage, testing/testability-audit, testing/definition-of-done-readiness]
    templates: [test-design-template, definition-of-done-template]
    registry: [data/registries/test-design-registry, data/test-designs]

  run-security-precheck:
    agents: [security-and-trust-reviewer, system-architect]
    frameworks: [security-by-design-primer]
    checklists: [security-review-quality]
    templates: [security-review-template]
    registry: [data/registries/risk-register]

  run-performance-precheck:
    agents: [performance-capacity-planner, system-architect]
    frameworks: [performance-by-design-primer]
    checklists: [performance-review-quality]
    templates: [performance-plan-template]
    registry: [data/registries/risk-register]

  # ---- LEGACY ----
  assess-legacy-impact:
    agents: [legacy-impact-auditor, system-architect, failure-analyst]
    frameworks: [legacy-boundary-isolation-framework, stacks/legacy-refactor-readiness-framework]
    checklists: [legacy-compatibility-quality, legacy-refactor-readiness-quality]
    templates: [legacy-impact-template]
    registry: [data/registries/legacy-impact-registry]

  # ---- ESTIMATION ----
  estimate-effort:
    agents: [estimation-planner, pre-programming-chief, decomposition-engineer]
    frameworks: [estimation-under-uncertainty-framework, risk-weighted-planning, project-slicing-framework]
    checklists: [estimation-quality]
    templates: [estimation-template]
    registry: [data/registries/decision-log]

  # ---- AI SYSTEMS ----
  ai-agent-readiness:
    agents: [system-architect, test-strategist, failure-analyst, performance-capacity-planner]
    frameworks: [stacks/ai-agent-solution-readiness-framework]
    checklists: [ai-solution-readiness-quality]
    templates: [architecture-sketch-template, test-design-template, risk-register-template]
    registry: [data/registries/architecture-decisions, data/registries/risk-register]

  # ---- READINESS & HANDOFF ----
  score-readiness:
    agents: [readiness-gatekeeper, pre-programming-chief]
    frameworks: [readiness/implementation-readiness-score, readiness/decision-maturity-model, go-no-go-decision-framework]
    checklists: [readiness-review-quality, readiness/implementation-ready-check, readiness/unanswered-questions-zero-check, readiness/final-go-no-go-audit]
    templates: [readiness-review-template, go-no-go-template]
    registry: [data/registries/readiness-reviews, data/registries/go-no-go-log]

  run-go-no-go:
    agents: [readiness-gatekeeper, pre-programming-chief]
    frameworks: [go-no-go-decision-framework, readiness/red-flag-escalation-framework]
    checklists: [readiness/final-go-no-go-audit]
    templates: [go-no-go-template]
    registry: [data/registries/go-no-go-log, data/registries/decision-log]

  handoff-to-dev:
    agents: [handoff-orchestrator, pre-programming-chief]
    frameworks: [handoff-completeness-framework, readiness/zero-guesswork-handoff]
    checklists: [handoff-package-quality, readiness/dev-package-completeness, cross-squad-handoff-quality]
    templates: [implementation-handoff-template]
    registry: [data/registries/handoff-registry]

  # ---- SPECIFIC READINESS TYPES ----
  new-feature-readiness:
    agents: [pre-programming-chief, problem-framer, system-architect, test-strategist, readiness-gatekeeper]
    frameworks: [problem-framing-canvas, architecture/v1-architecture-lens, testing/tests-before-tasks, readiness-score-framework]
    checklists: [project-brief-quality, requirements-quality, architecture-sketch-quality, test-design-quality, readiness-review-quality]
    templates: [project-brief-template, architecture-sketch-template, test-design-template, readiness-review-template]
    registry: [data/registries/project-brief-registry, data/registries/readiness-reviews]

  api-first-readiness:
    agents: [interface-designer, system-architect, test-strategist, readiness-gatekeeper]
    frameworks: [stacks/api-first-readiness-framework, architecture/integration-pressure-map]
    checklists: [api-contract-quality, integration-impact-quality, testing/contract-test-readiness]
    templates: [api-contract-template, integration-map-template]
    registry: [data/registries/integration-contracts, data/registries/readiness-reviews]

  critical-bug-patch-readiness:
    agents: [pre-programming-chief, failure-analyst, legacy-impact-auditor]
    frameworks: [blast-radius-assessment-framework, risk/production-impact-screen]
    checklists: [incident-risk-precheck-quality, risk/blast-radius-check, risk/rollback-strategy-audit]
    templates: [risk-register-template, rollback-plan-template]
    registry: [data/registries/risk-register, data/registries/decision-log]

  # ---- LEARNING ----
  planning-retro:
    agents: [pre-programming-chief, readiness-gatekeeper]
    frameworks: [readiness/decision-maturity-model]
    checklists: []
    templates: []
    registry: [data/registries/decision-log, data/metrics/rework-rate, data/metrics/missed-edge-case-rate]

  cross-squad-sync:
    agents: [pre-programming-chief, handoff-orchestrator]
    frameworks: []
    checklists: [cross-squad-handoff-quality]
    templates: [implementation-handoff-template]
    registry: [data/registries/handoff-registry]

# ============================================================
# CROSS-SQUAD INTEGRATION (bidirecional)
# ============================================================

cross_squad:
  coding_squad:
    handoff_to_coding:
      - implementation package → coding/tasks (pacote completo: brief, arch, contracts, tests, risks)
      - definition of done → coding/checklists (critérios de pronto)
    handoff_from_coding:
      - implementation feedback → data/registries/decision-log (o que mudou vs planejado)
      - rework reports → data/metrics/rework-rate (retrabalho causado por planejamento)
    shared_assets: [architecture-decisions, api-contracts, test-designs, risk-register]

  design_squad:
    handoff_to_design:
      - UX requirements → design/tasks (fluxos, estados, edge cases de UI)
      - interaction contracts → design/reference (comportamentos esperados)
    handoff_from_design:
      - wireframes + prototypes → data/research (validação visual)
      - UX constraints → data/registries/assumptions-log (limitações de design)
    shared_assets: [user-flows, interaction-specs, state-diagrams]

  data_squad:
    handoff_to_data:
      - metric definitions → data/registries/metric-registry (métricas do feature)
      - observability requirements → data/tasks (eventos, tracking, dashboards)
    handoff_from_data:
      - data model constraints → data/registries/architecture-decisions (limitações de dados)
      - benchmark data → data/research (evidência para decisões)
    shared_assets: [metric-definitions, event-taxonomy, data-model-specs]

  cybersecurity_squad:
    handoff_to_cyber:
      - security review request → cybersecurity/tasks (threat model, authz, data sensitivity)
      - compliance requirements → cybersecurity/checklists (LGPD, PCI, etc.)
    handoff_from_cyber:
      - security assessment → data/registries/risk-register (riscos de segurança)
      - security requirements → data/registries/assumptions-log (requisitos de segurança)
    shared_assets: [threat-model, security-requirements, compliance-checklist]

  deepresearch_squad:
    handoff_to_deepresearch:
      - research requests → deepresearch/tasks (stack research, domain unknowns)
      - uncertainty questions → deepresearch/tasks/planning (decisões incertas)
    handoff_from_deepresearch:
      - research findings → data/research (evidência para decisões)
      - technology evaluations → data/registries/architecture-decisions (avaliações de stack)
    shared_assets: [tech-evaluations, domain-research, evidence-tables]

  c_level_squad:
    handoff_to_c_level:
      - irreversible decisions → c-level/tasks (alto risco, alto investimento)
      - strategic trade-offs → c-level/data/memos (trade-offs que afetam negócio)
    handoff_from_c_level:
      - strategic context → data/research (prioridades de negócio)
      - budget/resource decisions → data/registries/decision-log (alocação)
    shared_assets: [strategic-priorities, resource-allocation, risk-tolerance]

  advisory_board:
    handoff_to_advisory:
      - strategic technical decisions → advisory/tasks (decisões de longo prazo)
    handoff_from_advisory:
      - strategic guidance → data/registries/decision-log (direcionamento)
    shared_assets: [strategic-decisions]

  traffic_squad:
    handoff_to_traffic:
      - tracking requirements → traffic/tasks (UTMs, pixels, eventos)
    handoff_from_traffic:
      - channel constraints → data/registries/assumptions-log (limitações de canal)
    shared_assets: [tracking-specs, event-taxonomy]

  storytelling_squad:
    handoff_to_storytelling:
      - feature narrative → storytelling/tasks (narrativa do produto)
    handoff_from_storytelling:
      - user journey insights → data/research (jornada do usuário)
    shared_assets: [user-journey, feature-narrative]

# ============================================================
# QUALITY GATES
# ============================================================

quality_gates:
  mandatory:
    - project-brief-quality          # Todo projeto tem brief aprovado
    - requirements-quality           # Requisitos claros e sem ambiguidade
    - scope-definition-quality       # Escopo definido e acordado
    - architecture-sketch-quality    # Arquitetura v1 desenhada
    - failure-modes-quality          # Falhas antecipadas
    - test-design-quality            # Testes desenhados antes do código
    - readiness-review-quality       # Readiness aprovado
    - handoff-package-quality        # Pacote de handoff completo
  per_domain:
    discovery: [discovery-quality, assumptions-log-quality]
    architecture: [domain-model-quality, api-contract-quality]
    risk: [incident-risk-precheck-quality, security-review-quality, performance-review-quality]
    testing: [testing/requirement-to-test-traceability, testing/testability-audit]
    legacy: [legacy-compatibility-quality, legacy-refactor-readiness-quality]
    operations: [observability-quality, environment-readiness-quality]
    ai: [ai-solution-readiness-quality]
    handoff: [readiness/implementation-ready-check, readiness/final-go-no-go-audit]

# ============================================================
# KPIs
# ============================================================

kpis:
  planning_quality:
    - ambiguity_burndown_rate          # Velocidade de eliminação de ambiguidades
    - missed_requirement_rate          # Taxa de requisitos perdidos (descobertos após handoff)
    - missed_edge_case_rate            # Taxa de edge cases não previstos
    - defect_origin_in_requirements    # % de defeitos originados em requisitos
    - assumption_validation_rate       # % de suposições validadas antes do handoff
  efficiency:
    - readiness_cycle_time             # Tempo de intake → readiness
    - planning_to_delivery_ratio       # Proporção planejamento / entrega
    - rework_reduction_rate            # Redução de retrabalho vs baseline
    - pre_prod_defect_escape_rate      # Taxa de defeitos que escapam para prod
  architecture:
    - architecture_reversal_rate       # Taxa de reversão de decisões arquiteturais
    - build_vs_buy_savings             # Economia por decisões build/buy corretas
    - dependency_surprise_rate         # Dependências não previstas
    - test_readiness_score             # Score de prontidão de testes
  operational:
    - handoff_clarity_score            # Clareza do pacote de handoff (avaliado pelo dev)
    - rollback_readiness_score         # Prontidão de rollback
    - production_incident_prevented    # Incidentes prevenidos pelo planejamento
    - readiness_gate_pass_rate         # Taxa de aprovação no go/no-go

# ============================================================
# DEFAULTS
# ============================================================

defaults:
  review_agent: pre-programming-chief
  gatekeeper: readiness-gatekeeper
  min_checklists: 3
  registry_on_completion: true
  output_format: markdown
  go_no_go_required: true
  handoff_package_required: true
  test_design_before_code: true
  assumption_validation: mandatory
  escalation_on_irreversible: true
```

---

## 📊 RESUMO TOTAL DO MAPEAMENTO

| Diretório       | Antes | V2    | Expansão |
|-----------------|-------|-------|----------|
| agents/         | 18    | 18    | ✓ |
| checklists/     | ~120+ | ~130+ | +8% (gates sistêmicos expandidos) |
| frameworks/     | ~70+  | ~85+  | +21% (+14 referência intelectual, +9 stacks expandidos) |
| reference/      | ~70+  | ~90+  | +29% (+12 psychology, +10 industries, papers expandidos) |
| templates/      | ~30+  | ~30+  | ✓ (já completo) |
| tasks/          | ~40+  | ~40+  | ✓ (já completo) |
| swipe/          | ~12+  | ~13+  | ✓ |
| swipe-sources/  | ~8    | ~8    | ✓ |
| voice/          | ~20+  | ~22+  | +10% |
| phrases/        | ~18   | ~18   | ✓ |
| workflows/      | ~20   | ~20   | ✓ |
| data/           | ~45+  | ~45+  | ✓ |
| docs/           | ~18   | ~18   | ✓ |
| scripts/        | ~14   | ~14   | ✓ |
| lib/            | ~30+  | ~30+  | ✓ |
| archive/        | ~15+  | ~15+  | ✓ |
| authority/      | ~15   | ~15   | ✓ |
| projects/       | ~40+  | ~40+  | ✓ |
| root files      | 4     | 4     | ✓ |
| **TOTAL**       | **~607+** | **~690+** | **config.yaml COMPLETO + cross-squad + KPIs + psychology + intellectual frameworks** |

---

## 🧠 REFLEXÕES ESTRATÉGICAS (GOLD STANDARD / SOTA)

### Verificação das 18 etapas (MMOS) — RalphLooping Check (V2)

| # | Seção | Status | Nota |
|---|-------|--------|------|
| 1 | Agents | ✅ GOLD | 18 agentes cobrindo descoberta → risco → handoff |
| 2 | Checklists | ✅ GOLD | ~130+ gates macro + 7 subpastas por domínio + readiness |
| 3 | Frameworks | ✅ GOLD | ~85+: 29 universais + 20 proprietários (discovery/arch/testing/risk/readiness) + 9 stacks + 14 referência intelectual (Ousterhout, Kleppmann, Fowler, Beck, Evans, Feathers, Nygard, Cagan, Kahneman, Taleb, Meadows, Goldratt, Goodhart, Brooks) |
| 4 | Reference | ✅ GOLD | ~90+: 20 livros nomeados + papers + engineering + testing + product + AI + **12 psychology** (confirmation bias, anchoring, sunk cost, overconfidence, planning fallacy, Dunning-Kruger, groupthink, availability, status quo, narrative fallacy, survivorship, optimism) + **10 industries** |
| 5 | Templates | ✅ GOLD | ~30+ outputs reutilizáveis |
| 6 | Tasks | ✅ GOLD | ~40+ com subpastas (intake/discovery/scoping/arch/quality/legacy/readiness/learning) |
| 7 | Swipe + Sources | ✅ GOLD | 13 swipe + 8 sources (Google, Amazon, Stripe, Uber, Netflix, Fowler, ThoughtWorks, SRE) |
| 8 | Voice | ✅ GOLD | ~22+ com 4 subpastas (tone/calibration/language/channels) |
| 9 | Phrases | ✅ GOLD | 18 frases operacionais |
| 10 | Workflows | ✅ GOLD | 20 numerados ponta-a-ponta |
| 11 | Data | ✅ GOLD | ~45+ (research/4, registries/13, metrics/10, readiness-reviews, decision-memos, etc.) |
| 12 | Docs | ✅ GOLD | 18 standards operacionais |
| 13 | Scripts | ✅ GOLD | ~14 (validation/4, reporting/4, utilities/6) |
| 14 | Lib | ✅ GOLD | ~30+ (components/8 schemas, patterns/8, utilities/7, taxonomies/6) |
| 15 | Archive | ✅ GOLD | ~15+ (iconic/4, failures/7, evolution/3) |
| 16 | Authority | ✅ GOLD | ~15 (10 author summaries + 5 workshop kits) |
| 17 | Projects | ✅ GOLD | ~40+ (9 tipos: new-feature, bugfix, legacy-refactor, api-integration, internal-tool, automation, ai-agent, enterprise-rollout, mobile-feature) |
| 18 | Root/Config | ✅ GOLD | **config.yaml COMPLETO** com 25+ tasks roteadas, **cross-squad bidirecional com 9 squads** (Coding, Design, Data, Cyber, DeepResearch, C-Level, Advisory, Traffic, Storytelling), **16 KPIs em 4 categorias** (planning_quality/5, efficiency/4, architecture/4, operational/4), **quality gates** (mandatory/8 + per_domain/8) |

### O que você pode não estar enxergando?

- **Pré-programação não é “pensar antes”.** É um **sistema formal de redução de retrabalho**.
- **O maior custo invisível não é programar errado — é começar cedo demais.**
- **Teste antes do código não é só qualidade; é ferramenta de design.**
- **Boa arquitetura v1 não é a mais robusta — é a que resolve o problema certo no nível certo.**
- **Sem `readiness-gatekeeper`, o squad vira checklist decorativo.**
- **Sem `data/registries/` e `data/metrics/`, o squad não aprende — repete os mesmos erros em cada projeto.**
- **Sem handoff estruturado, o coding squad volta a adivinhar — e todo o valor da pré-programação evapora.**

### Tem uma forma mais simples ou melhor?

Sim: construir em camadas.

#### Pack 1 (Core)
- agents/
- frameworks/
- checklists/
- templates/
- ARCHITECTURE.md
- config.yaml

#### Pack 2 (Operacional)
- workflows/
- data/registries/
- data/metrics/
- docs/
- tasks/

#### Pack 3 (Maturidade)
- scripts/
- lib/
- authority/
- archive/
- swipe/

#### Pack 4 (Excelência)
- scorecards
- dashboards de qualidade de planejamento
- retro de prontidão por tipo de projeto
- cross-squad bidirecional formal

### Está correto o raciocínio?

Sim. Este squad replica fielmente o padrão MMOS com **18 seções**, `config.yaml` como roteador central,
`ARCHITECTURE.md` como constituição, **RalphLoop** como mecanismo de aprendizagem, handoffs bidirecionais,
quality gates obrigatórios e foco em **implementation readiness**, que é exatamente a lacuna crítica entre
“entender o projeto” e “começar a construir”.

### O que alguém 100x mais inteligente faria de verdade?

Não criaria apenas um agente que “pensa antes”.
Criaria um sistema onde **ninguém consegue começar a desenvolver sem evidência suficiente** de que:

1. entendeu o problema;
2. escolheu a abordagem conscientemente;
3. antecipou o que pode falhar;
4. definiu como vai provar que funciona;
5. sabe exatamente o que entregar para o time de implementação.

Esse é o verdadeiro papel do **Pre-Programming Squad**:
ser o **filtro de qualidade anterior ao código**.

