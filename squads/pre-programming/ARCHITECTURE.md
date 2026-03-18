# ARCHITECTURE.md — Constituição do Pre-Programming Squad

> **Versão:** 2.1.0
> **Squad:** Pre-Programming (MMOS)
> **Última atualização:** 2026-03-17

---

## 1. Missão

Garantir **implementation readiness**: que nenhum projeto entre em fase de desenvolvimento sem evidência suficiente de que:

1. O problema foi entendido (não apenas o pedido)
2. A solução foi escolhida conscientemente (não por default)
3. Os riscos foram antecipados (não descobertos em produção)
4. Os testes foram desenhados (não improvisados depois)
5. O time de implementação recebe um pacote claro e completo (não precisa adivinhar)

**Pré-programação não é "pensar antes". É um sistema formal de redução de retrabalho.**

---

## 2. Definição de Implementation Readiness

Um projeto está **pronto para implementação** quando:

- [ ] O problema real está delimitado e documentado
- [ ] Requisitos estão claros, explícitos e sem ambiguidade crítica
- [ ] O escopo está definido (in-scope / out-of-scope / MVP)
- [ ] A arquitetura v1 foi desenhada e revisada
- [ ] O modelo de domínio está validado
- [ ] Contratos de API/integração estão definidos
- [ ] Falhas previsíveis foram mapeadas com plano de mitigação
- [ ] Testes foram desenhados antes do código
- [ ] Riscos de segurança e performance foram pré-avaliados
- [ ] Estimativa de esforço foi feita com breakdown realista
- [ ] O pacote de handoff está completo
- [ ] O Readiness Gatekeeper aprovou o go/no-go

---

## 3. Pipeline Principal

```
Pedido → Descoberta → Escopo → Decomposição → Arquitetura → Riscos → Testes → Prontidão → Handoff → Memória
```

Cada etapa tem:
- **Agentes responsáveis** (quem executa)
- **Frameworks obrigatórios** (como pensa)
- **Checklists de qualidade** (como valida)
- **Templates de output** (o que produz)
- **Registries de destino** (onde registra)

O roteamento completo está em `config.yaml`.

---

## 4. Regras de Roteamento

O `config.yaml` é o **cérebro de roteamento** do squad. Para cada tipo de tarefa, ele define:

- Quais agentes chamar
- Em qual ordem
- Quais frameworks são obrigatórios
- Quais checklists precisam passar
- Quais templates geram o output
- Onde registrar em `data/registries/`
- Quais métricas em `data/metrics/` provam que o planejamento foi bom
- Quais handoffs cross-squad são obrigatórios

### Tipos de tarefa suportados:
- `project-intake` — Entrada de novo projeto
- `run-discovery` — Descoberta completa
- `clarify-requirements` — Esclarecimento de requisitos
- `map-stakeholders` — Mapeamento de stakeholders
- `define-scope` — Definição de escopo
- `sketch-architecture-v1` — Arquitetura inicial
- `compare-solution-options` — Comparação de opções
- `define-api-contracts` — Contratos de API
- `define-domain-model` — Modelo de domínio
- `map-failure-modes` — Modos de falha
- `design-test-strategy` — Estratégia de testes
- `run-security-precheck` — Pré-check de segurança
- `run-performance-precheck` — Pré-check de performance
- `assess-legacy-impact` — Impacto em legado
- `estimate-effort` — Estimativa de esforço
- `ai-agent-readiness` — Readiness para sistemas AI
- `score-readiness` — Score de prontidão
- `run-go-no-go` — Decisão go/no-go
- `handoff-to-dev` — Handoff para desenvolvimento
- `new-feature-readiness` — Readiness para nova feature
- `api-first-readiness` — Readiness API-first
- `critical-bug-patch-readiness` — Readiness para bug crítico
- `planning-retro` — Retrospectiva de planejamento
- `cross-squad-sync` — Sincronização cross-squad

---

## 5. Papéis dos Agentes (18)

### 5.1 Comando e Orquestração
| Agente | Papel | Poder |
|--------|-------|-------|
| **Pre-Programming Chief** | Orquestrador geral | Define win condition, prioriza, protege rigor |
| **Readiness Gatekeeper** | Guardião do gate | Poder de veto: sem aprovação, não começa implementação |

### 5.2 Descoberta e Entendimento
| Agente | Papel | Poder |
|--------|-------|-------|
| **Problem Framer** | Delimitar problema real | Manda em problema real, impede solução prematura |
| **Requirements Clarifier** | Eliminar ambiguidade | Mata ambiguidade antes que vire retrabalho |
| **Business Translator** | Traduzir negócio→técnica | Garante que técnica sirva negócio |
| **Stakeholder Mapper** | Mapear stakeholders | Identifica dependências e conflitos |

### 5.3 Solução e Arquitetura
| Agente | Papel | Poder |
|--------|-------|-------|
| **System Architect** | Arquitetura v1 | Manda em estrutura, boundaries e trade-offs |
| **Domain Modeler** | Modelo de domínio | Protege integridade da lógica do domínio |
| **Interface Designer** | APIs e contratos | Impede contratos vagos ou integrações improvisadas |
| **Decomposition Engineer** | Quebra em partes | Transforma problema em partes implementáveis |

### 5.4 Qualidade, Risco e Testabilidade
| Agente | Papel | Poder |
|--------|-------|-------|
| **Failure Analyst** | Edge cases e falhas | Obriga pensar no que dá errado |
| **Test Strategist** | Testes antes do código | Transforma requisitos em verificação objetiva |
| **Security & Trust Reviewer** | Segurança | Evita que segurança vire retrofit caro |
| **Performance Capacity Planner** | Performance | Impede soluções inocentemente lentas |

### 5.5 Implementabilidade e Entrega
| Agente | Papel | Poder |
|--------|-------|-------|
| **Build vs Buy Analyst** | Reusar vs construir | Protege simplicidade e foco |
| **Legacy Impact Auditor** | Compatibilidade | Evita quebrar produção |
| **Estimation Planner** | Esforço e prazo | Transforma ambição em execução realista |
| **Handoff Orchestrator** | Pacote de handoff | Garante que dev receba pacote completo |

---

## 6. Quality Gates Obrigatórios

### Gates Mandatórios (todo projeto)
1. `project-brief-quality` — Brief aprovado
2. `requirements-quality` — Requisitos claros
3. `scope-definition-quality` — Escopo definido
4. `architecture-sketch-quality` — Arquitetura v1 desenhada
5. `failure-modes-quality` — Falhas antecipadas
6. `test-design-quality` — Testes desenhados antes do código
7. `readiness-review-quality` — Readiness aprovado
8. `handoff-package-quality` — Pacote completo

### Gates por Domínio
- **Discovery:** discovery-quality, assumptions-log-quality
- **Architecture:** domain-model-quality, api-contract-quality
- **Risk:** incident-risk-precheck-quality, security-review-quality, performance-review-quality
- **Testing:** requirement-to-test-traceability, testability-audit
- **Legacy:** legacy-compatibility-quality, legacy-refactor-readiness-quality
- **Operations:** observability-quality, environment-readiness-quality
- **AI:** ai-solution-readiness-quality
- **Handoff:** implementation-ready-check, final-go-no-go-audit

---

## 7. RalphLoop — Mecanismo de Aprendizagem

O squad aprende com cada projeto através do ciclo:

```
Execução → Métricas → Análise → Atualização → Próximo Projeto
```

### Como funciona:
1. **Após cada handoff**, registrar métricas em `data/metrics/`
2. **Após cada sprint do coding squad**, coletar feedback de retrabalho
3. **Mensalmente**, rodar `planning-retro` com Pre-Programming Chief e Readiness Gatekeeper
4. **Atualizar** checklists, frameworks e templates com learnings
5. **Registrar** em `archive/evolution/` as mudanças no processo

### KPIs monitorados:
- Ambiguity burndown rate
- Missed requirement rate
- Missed edge case rate
- Defect origin in requirements
- Rework reduction rate
- Handoff clarity score
- Readiness gate pass rate

---

## 8. Escalonamento

### Quando escalar:

| Situação | Escalar para |
|----------|-------------|
| Decisão irreversível de alto impacto | C-Level Squad |
| Conflito entre agentes sem resolução | Pre-Programming Chief |
| Risco de segurança crítico | Cybersecurity Squad |
| Incerteza técnica profunda | DeepResearch Squad |
| Requisito contradiz estratégia de negócio | C-Level Squad |
| Dependência bloqueante em outro squad | Traffic / Design / Data Squad |

### Como escalar:
1. Registrar em `data/registries/decision-log.yaml`
2. Criar decision memo em `data/decision-memos/`
3. Notificar o squad alvo via handoff formal
4. Aguardar resolução antes de prosseguir

---

## 9. Resolução de Conflitos

### Entre agentes:
1. Cada agente apresenta sua posição com evidência
2. O **Pre-Programming Chief** arbitra baseado nos princípios do squad
3. A decisão é registrada como ADR em `data/registries/architecture-decisions.yaml`
4. Se o conflito envolve risco irreversível, escala para C-Level

### Entre squad e stakeholders:
1. O **Business Translator** media a comunicação
2. O **Stakeholder Mapper** identifica interesses conflitantes
3. O **Pre-Programming Chief** propõe resolução
4. Se não há consenso, escala com decision memo

---

## 10. Decisões Irreversíveis

Decisões irreversíveis recebem tratamento especial:

1. **Identificação:** O framework `reversible-vs-irreversible-decisions` classifica cada decisão
2. **Documentação obrigatória:** Decision memo com contexto, opções, trade-offs
3. **Revisão ampliada:** Pelo menos 2 agentes revisam
4. **Aprovação do Chief:** Pre-Programming Chief assina
5. **Escalonamento se necessário:** C-Level para decisões estratégicas
6. **Registro permanente:** Em `data/registries/architecture-decisions.yaml`

---

## 11. Cross-Squad Integration

### Squads com integração bidirecional:

| Squad | O que enviamos | O que recebemos |
|-------|---------------|-----------------|
| **Coding** | Implementation package, definition of done | Implementation feedback, rework reports |
| **Design** | UX requirements, interaction contracts | Wireframes, UX constraints |
| **Data** | Metric definitions, observability requirements | Data model constraints, benchmark data |
| **Cybersecurity** | Security review request, compliance requirements | Security assessment, security requirements |
| **DeepResearch** | Research requests, uncertainty questions | Research findings, technology evaluations |
| **C-Level** | Irreversible decisions, strategic trade-offs | Strategic context, budget decisions |
| **Advisory Board** | Strategic technical decisions | Strategic guidance |
| **Traffic** | Tracking requirements | Channel constraints |
| **Storytelling** | Feature narrative | User journey insights |

---

## 12. Tratamento de Tasks Fora do Escopo

### Como o squad identifica tasks fora do escopo
O Pre-Programming Squad opera **antes da primeira linha de código**. Qualquer pedido que exija:
- Implementação de código → **delegar para Coding Squad**
- Design de UI/UX → **delegar para Design Squad**
- Análise de dados existentes em produção → **delegar para Data Squad**
- Pentest ou auditoria de segurança em sistema rodando → **delegar para Cybersecurity Squad**
- Pesquisa aprofundada que excede o escopo de discovery → **delegar para DeepResearch Squad**
- Decisão estratégica de negócio (não técnica) → **escalar para C-Level Squad**

### Protocolo de delegação
1. O **agente que identificou** a task fora do escopo notifica o **Pre-Programming Chief**.
2. O Chief classifica: **delegação pura** (sai do squad) ou **co-execução** (squad participa mas não lidera).
3. O Chief registra em `data/registries/decision-log.yaml` o motivo da delegação.
4. O **Handoff Orchestrator** prepara handoff formal para o squad receptor com contexto relevante.
5. Se o resultado do squad externo impacta o projeto em pré-programação, o Chief define como e quando integrar.

### Regra de ouro
> Se um agente não sabe se a task é do escopo, pergunte: **"Isso precisa acontecer antes da primeira linha de código?"**
> Se sim → é do Pre-Programming Squad.
> Se não → é de outro squad. Delegue com handoff formal.

---

## 12.1. Error Budget e Tolerância de Desvio

### O que é "bom o suficiente" para cada nível de projeto

| Métrica | P (Pequeno) | M (Médio) | G (Grande) | XG (Extra) |
|---------|-------------|-----------|------------|------------|
| Gate pass rate na 1ª tentativa | ≥60% | ≥70% | ≥80% | ≥90% |
| Suposições validadas pré-handoff | ≥70% | ≥85% | ≥90% | ≥95% |
| Edge cases mapeados | Top 5 | Top 10 | Exaustivo | Exaustivo + stress test |
| Requisitos sem ambiguidade | ≥80% | ≥90% | ≥95% | 100% |
| KPI targets atingidos | ≥50% | ≥65% | ≥80% | ≥90% |

### Quando o processo falhou (não a task)
O processo de pré-programação falhou quando:
- Mais de 3 gates falham na mesma sessão para o mesmo projeto.
- O mesmo tipo de falha aparece em 3+ projetos consecutivos.
- O coding squad reporta mais de 15% de retrabalho originado em pré-programação.
- O handoff clarity score cai abaixo de 6/10 por 2 projetos consecutivos.

**Ação**: acionar `planning-retro` (workflow 20 — RalphLoop) imediatamente, sem esperar cadência mensal.

---

## 12.2. Rework Loop — Protocolo de Retorno

### Quando um output é reprovado no quality gate

```
Output reprovado no gate
    │
    ├─ Gate do agente individual (Nível 1)
    │   → Retorna ao mesmo agente com feedback específico do checklist
    │   → Agente corrige e resubmete
    │   → Máximo 2 loops antes de escalar para Chief
    │
    ├─ Gate do Chief (Nível 3 — gate final do squad)
    │   → Chief identifica qual agente/team precisa corrigir
    │   → Devolve com instruções específicas e prazo
    │   → Re-avaliação pelo Readiness Gatekeeper após correção
    │
    ├─ Gate cross-squad (Nível 4 — handoff rejeitado)
    │   → Coding squad rejeita handoff por incompletude
    │   → Handoff Orchestrator identifica gaps
    │   → Chief redistribui correções aos agentes responsáveis
    │   → Novo gate completo antes de re-handoff
    │
    └─ Gate HRM Central (Nível 5)
        → Output do squad não atinge padrão GOLD exigido
        → Chief registra como lesson learned
        → RalphLoop retro é acionado
        → Checklists e frameworks são atualizados
```

### Regras do rework loop
1. **Máximo 2 loops por agente** antes de escalar para Chief.
2. **Máximo 3 loops por task** antes de escalar para C-Level para reavaliar viabilidade.
3. **Todo loop é registrado** em `data/registries/decision-log.yaml` com motivo e correção.
4. **Loops recorrentes do mesmo tipo** acionam atualização de checklist/framework (Kaizen).

---

## 12.3. Princípio Central

> **O maior custo invisível não é programar errado — é começar cedo demais.**

O Pre-Programming Squad existe para ser o sistema operacional que transforma:
- Ambiguidade em escopo operacional
- Contexto de negócio em decisões técnicas
- Riscos em planos de mitigação
- Requisitos em testes verificáveis
- Planejamento em pacote executável

**Sem este squad, o coding squad adivinha. Com este squad, o coding squad executa.**

---

## 13. Classificação de Projetos

Cada projeto é classificado por porte para determinar profundidade do pipeline:

| Porte | Escopo | Pipeline | Gates |
|-------|--------|----------|-------|
| **P** (Pequeno) | Tarefa pontual, ~1 sprint | 1-3 dias | 4 gates essenciais |
| **M** (Médio) | Feature completa, 1-3 sprints | 3-7 dias | 8 gates mandatórios |
| **G** (Grande) | Multi-sprint, possível cross-squad | 1-2 semanas | Todos os gates + per_domain |
| **XG** (Extra-Grande) | Multi-squad, alto impacto | 2-4 semanas | Todos + C-Level approval |

O `config.yaml` define quais gates são obrigatórios e quais podem ser pulados por porte.

---

## 14. Métricas e KPIs (17 indicadores em 4 categorias)

### Planning Quality (5)
| KPI | O que mede | Target |
|-----|-----------|--------|
| Ambiguity Burndown Rate | Velocidade de eliminação de ambiguidades | >80% resolvidas antes de scope |
| Missed Requirement Rate | Requisitos descobertos pós-handoff | <5% |
| Missed Edge Case Rate | Edge cases não previstos | <10% |
| Defect Origin in Requirements | % defeitos originados em requisitos | <15% |
| Assumption Validation Rate | % suposições validadas antes do handoff | >90% |

### Efficiency (4)
| KPI | O que mede | Target |
|-----|-----------|--------|
| Readiness Cycle Time | Tempo de intake → readiness | <7 dias (M), <14 dias (G) |
| Planning to Delivery Ratio | Proporção planejamento / entrega | 15-25% |
| Rework Reduction Rate | Redução de retrabalho vs baseline | >30% |
| Pre-prod Defect Escape Rate | Defeitos que escapam para prod | <3% |

### Architecture (4)
| KPI | O que mede | Target |
|-----|-----------|--------|
| Architecture Reversal Rate | Reversão de decisões arquiteturais | <10% |
| Build vs Buy Savings | Economia por decisões build/buy | Documentado por projeto |
| Dependency Surprise Rate | Dependências não previstas | <5% |
| Test Readiness Score | Score de prontidão de testes | >85/100 |

### Operational (4)
| KPI | O que mede | Target |
|-----|-----------|--------|
| Handoff Clarity Score | Clareza do pacote (avaliado pelo dev) | >8/10 |
| Rollback Readiness Score | Prontidão de rollback | >90% |
| Production Incident Prevented | Incidentes prevenidos | Documentado |
| Readiness Gate Pass Rate | Aprovação no go/no-go 1ª tentativa | >75% |

---

## 15. Inventário do Squad (694 arquivos)

| Diretório | Arquivos | Função |
|-----------|----------|--------|
| `agents/` | 18 | Definições de agentes especializados |
| `checklists/` | 141 | Quality gates (28 macro + 35 micro + 64 gates por domínio + 14 gates sistêmicos) |
| `frameworks/` | 85 | Modelos mentais e ferramentas de decisão (30 core + 20 proprietários + 14 intelectuais + 9 stacks + 12 V2) |
| `reference/` | 94 | Base de conhecimento (23 livros + 22 psychology + 20 industries + 10 papers + 4 testing + 4 engineering + 3 ai + 3 product + 3 operations + 3 architecture) |
| `templates/` | 30 | Outputs reutilizáveis com exemplos reais |
| `tasks/` | 40 | Tipos de tarefa executáveis |
| `workflows/` | 20 | Playbooks ponta-a-ponta |
| `data/` | 45 | Memória operacional (13 registries + 16 metrics + 6 research + 10 storage dirs) |
| `docs/` | 18 | Standards operacionais |
| `voice/` | 22 | Perfis de tom, calibração e canais |
| `phrases/` | 18 | Frases operacionais |
| `scripts/` | 28 | Automação (validation, reporting, utilities, schemas) |
| `lib/` | 31 | Componentes, patterns, taxonomias, utilitários |
| `archive/` | 15 | Evolução, falhas e casos icônicos |
| `authority/` | 15 | Resumos executivos de autoridade + workshop kits |
| `projects/` | 72 | 10 tipos × 8 fases |
| `swipe/` | 13 | Exemplos bons e ruins |
| `swipe-sources/` | 8 | Fontes de referência (Google, Amazon, Netflix, Stripe...) |

---

## 16. Evolução e Maturidade (RalphLoop Kaizen)

### Roadmap de Maturidade

| Nível | Estado | Critério |
|-------|--------|----------|
| **WEAK** | Processo existe mas é ad-hoc | <50% dos gates passam, sem métricas |
| **GOOD** | Processo documentado e seguido | >70% dos gates passam, métricas coletadas |
| **GOLD** | Processo otimizado com feedback loop | >85% dos gates passam, KPIs dentro do target |
| **SOTA** | Processo continuamente melhorado com dados | >95% dos gates passam, RalphLoop ativo, zero surpresas em handoff |

### Ciclo de Evolução
1. **Baseline:** Medir estado atual dos KPIs
2. **Identificar:** Top 3 áreas de melhoria via RalphLoop retro
3. **Implementar:** Ajustar checklists, frameworks, templates
4. **Medir:** Comparar KPIs pós-mudança vs baseline
5. **Registrar:** Documentar em `archive/evolution/`
6. **Repetir:** Próximo ciclo mensal
