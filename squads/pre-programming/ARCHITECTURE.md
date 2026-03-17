# ARCHITECTURE.md — Constituição do Pre-Programming Squad

> **Versão:** 2.0.0
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

## 12. Princípio Central

> **O maior custo invisível não é programar errado — é começar cedo demais.**

O Pre-Programming Squad existe para ser o sistema operacional que transforma:
- Ambiguidade em escopo operacional
- Contexto de negócio em decisões técnicas
- Riscos em planos de mitigação
- Requisitos em testes verificáveis
- Planejamento em pacote executável

**Sem este squad, o coding squad adivinha. Com este squad, o coding squad executa.**
