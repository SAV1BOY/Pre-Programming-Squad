# Standard para Decisão Go/No-Go

## Propósito

Definir o processo formal de decisão sobre avançar (go) ou não avançar (no-go) com a entrega de um projeto para implementação. É o gate final antes do handoff, garantindo que todos os critérios de readiness são atendidos e que riscos residuais são aceitos conscientemente.

## Escopo

Todo projeto que completa a pipeline do Pre-Programming Squad. Projetos P podem ter go/no-go simplificado; projetos M/G/XG seguem o processo completo.

## Definições

| Termo | Definição |
|---|---|
| Go | Decisão de prosseguir com o handoff para implementação |
| No-Go | Decisão de não prosseguir, com justificativa e plano de resolução |
| Go condicional | Prosseguir com condições explícitas que devem ser atendidas em prazo definido |
| Gate | Ponto de decisão formal que requer aprovação para prosseguir |

## Processo

### 1. Convocação da Decisão

**Quando convocar:**
- Quando o readiness assessment indica "Ready" ou "Conditionally Ready"
- Quando todas as revisões obrigatórias estão concluídas
- Quando a estimativa de esforço está documentada

**Participantes:**
- Membro responsável pelo projeto (apresenta)
- Tech Lead do Pre-Programming Squad (decide)
- Tech Lead do squad receptor (valida capacidade)
- Stakeholders relevantes (PM, arquiteto — conforme complexidade)

### 2. Revisão dos Critérios

Revisar cada área com status explícito:

#### Escopo e Requisitos
| Critério | Status | Notas |
|---|---|---|
| Escopo definido e aprovado pelo patrocinador | ✅/🔶/🔴 | |
| Critérios de aceitação verificáveis | ✅/🔶/🔴 | |
| Requisitos não-funcionais quantificados | ✅/🔶/🔴 | |
| Out of scope explicitamente listado | ✅/🔶/🔴 | |

#### Decisões Técnicas
| Critério | Status | Notas |
|---|---|---|
| ADRs registrados para decisões significativas | ✅/🔶/🔴 | |
| Contratos de API definidos | ✅/🔶/🔴 | |
| Modelo de dados revisado | ✅/🔶/🔴 | |
| Padrões de integração definidos | ✅/🔶/🔴 | |

#### Revisões Concluídas
| Critério | Status | Notas |
|---|---|---|
| Revisão de arquitetura (se aplicável) | ✅/🔶/🔴/N/A | |
| Pre-check de segurança (se aplicável) | ✅/🔶/🔴/N/A | |
| Pre-check de performance (se aplicável) | ✅/🔶/🔴/N/A | |
| Revisão de riscos | ✅/🔶/🔴 | |

#### Estimativa e Planejamento
| Critério | Status | Notas |
|---|---|---|
| Estimativa de esforço com decomposição | ✅/🔶/🔴 | |
| Premissas documentadas | ✅/🔶/🔴 | |
| Sequência de implementação definida | ✅/🔶/🔴 | |
| Dependências mapeadas com status | ✅/🔶/🔴 | |

#### Handoff
| Critério | Status | Notas |
|---|---|---|
| Pacote de handoff completo | ✅/🔶/🔴 | |
| Artefatos acessíveis | ✅/🔶/🔴 | |
| Squad receptor com capacidade | ✅/🔶/🔴 | |

### 3. Avaliação de Riscos Residuais

Para cada risco que permanece após mitigações:
- O risco é aceitável dado o contexto e as mitigações implementadas?
- O stakeholder adequado está ciente e aceita o risco?
- Existe plano de contingência se o risco se materializar?

### 4. Decisão

**GO** — Todos os critérios obrigatórios atendidos (✅), riscos residuais aceitos.
- Prosseguir para handoff imediatamente
- Registrar decisão com data e participantes

**GO CONDICIONAL** — Critérios obrigatórios atendidos, mas com condições:
- Lista de condições com owner e prazo
- Handoff pode prosseguir, mas condições devem ser resolvidas antes do início de Sprint 1
- Exemplo: "Go condicional — confirmar disponibilidade da API do parceiro até sexta-feira"

**NO-GO** — Um ou mais critérios obrigatórios não atendidos:
- Lista de gaps com plano de resolução
- Data de re-avaliação definida
- Comunicação ao solicitante com justificativa e timeline

**Regra fundamental:** No-go é um resultado legítimo que protege a qualidade. Nunca deve ser visto como falha do squad — é o squad cumprindo sua missão de prevenir implementação sem preparação adequada.

### 5. Registro

Toda decisão go/no-go é registrada com:
- Data e participantes
- Resultado (go / go condicional / no-go)
- Justificativa
- Condições (se condicional)
- Gaps e plano (se no-go)
- Riscos aceitos (se go)

## Critérios de Qualidade

- 100% dos projetos passam por go/no-go antes do handoff
- Decisão documentada e rastreável para cada projeto
- No-go nunca é pressionado para se tornar go — a decisão é técnica
- Go condicional tem condições resolvidas dentro do prazo em > 90% dos casos
- Taxa de no-go < 20% (indica qualidade do processo upstream)

## Responsáveis

| Papel | Responsabilidade |
|---|---|
| Membro do squad | Preparar material para decisão, apresentar status |
| Tech Lead (Pre-Prog) | Tomar a decisão, garantir rigor do processo |
| Tech Lead (receptor) | Confirmar capacidade, validar que pacote é suficiente |
| PM/Patrocinador | Fornecer contexto de prioridade, aceitar riscos de negócio |

## Referências

- Definição de Readiness: `docs/readiness-definition.md`
- Standard de Handoff: `docs/handoff-standard.md`
- Standard de Revisão de Riscos: `docs/risk-review-standard.md`
- Linguagem de Decisão: `voice/language/decision-language.md`
