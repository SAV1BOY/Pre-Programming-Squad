# Pre-Programming Squad — MMOS

> **Missão:** Garantir que nenhum projeto entre em desenvolvimento sem evidência suficiente de que o problema foi entendido, a solução foi escolhida conscientemente, os riscos foram antecipados, os testes foram desenhados e o time de implementação recebe um pacote claro e completo.

## O que é o Pre-Programming Squad?

O Pre-Programming Squad é o **filtro de qualidade anterior ao código**. É um sistema formal de redução de retrabalho que cobre tudo o que precisa acontecer **antes da primeira linha de código**: descoberta, entendimento do problema, alinhamento, escopo, arquitetura inicial, modelagem, avaliação de risco, design de testes, preparação de ambiente, decisão de stack, handoff para implementação e governança de prontidão.

## Pipeline Principal

```
Pedido → Descoberta → Escopo → Decomposição → Arquitetura → Riscos → Testes → Prontidão → Handoff → Memória
```

## Princípios

1. **Entender antes de construir** — O problema real vem antes da solução
2. **Clareza > velocidade** — Ambiguidade gera retrabalho
3. **Testes antes do código** — Design de testes como ferramenta de design
4. **Antecipar falhas** — Pensar no que dá errado antes do happy path
5. **Arquitetura mais simples viável** — Resolver o problema certo no nível certo
6. **Evidência > suposição** — Validar antes de assumir
7. **Zero adivinhação no handoff** — O dev recebe pacote completo

## Estrutura

| Diretório | Descrição |
|-----------|-----------|
| `agents/` | 18 agentes especializados |
| `checklists/` | Quality gates por domínio |
| `frameworks/` | Modelos mentais e ferramentas de decisão |
| `templates/` | Outputs reutilizáveis |
| `tasks/` | Tipos de tarefa que o squad executa |
| `workflows/` | Playbooks ponta-a-ponta |
| `data/` | Memória operacional (registries, metrics, research) |
| `docs/` | Standards operacionais |
| `reference/` | Base de conhecimento curada |
| `voice/` | Como o squad comunica |
| `phrases/` | Frases operacionais |
| `scripts/` | Automação do processo |
| `lib/` | Componentes reutilizáveis |
| `archive/` | Casos, falhas e learnings |
| `authority/` | Resumos executivos de autoridade |
| `projects/` | Tipos de projeto com fases numeradas |
| `swipe/` | Exemplos e fontes-modelo |

## 18 Agentes

### Comando e Orquestração
- **Pre-Programming Chief** — Orquestrador: escopo, prioridade, governança, win condition, go/no-go
- **Readiness Gatekeeper** — Decide se o projeto está pronto para implementação

### Descoberta e Entendimento
- **Problem Framer** — Delimita o problema real, separa sintoma vs causa
- **Requirements Clarifier** — Esclarece requisitos e remove ambiguidades
- **Business Translator** — Traduz objetivos de negócio em critérios técnicos
- **Stakeholder Mapper** — Mapeia stakeholders, dependências e conflitos

### Solução e Arquitetura
- **System Architect** — Arquitetura inicial, módulos, boundaries
- **Domain Modeler** — Entidades, relações, regras de negócio, invariantes
- **Interface Designer** — APIs, contratos, eventos, integrações
- **Decomposition Engineer** — Quebra o problema em partes implementáveis

### Qualidade, Risco e Testabilidade
- **Failure Analyst** — Edge cases, unhappy paths, rollback
- **Test Strategist** — Testes antes do código
- **Security & Trust Reviewer** — Segurança, privacidade, misuse cases
- **Performance Capacity Planner** — Performance, escala, gargalos

### Implementabilidade e Entrega
- **Build vs Buy Analyst** — Reusar vs construir, stack, dependências
- **Legacy Impact Auditor** — Compatibilidade com legado, migração
- **Estimation Planner** — Esforço, fatiamento, milestones
- **Handoff Orchestrator** — Gera pacote de handoff para o coding squad

## Arquivos-Chave

- **`ARCHITECTURE.md`** — Constituição do squad
- **`config.yaml`** — Cérebro de roteamento (define quais agentes, frameworks, checklists e templates usar para cada tipo de tarefa)

## Cross-Squad Integration

O squad interage bidirecionalmente com: Coding, Design, Data, Cybersecurity, DeepResearch, C-Level, Advisory Board, Traffic e Storytelling.

## RalphLoop

Mecanismo de aprendizagem contínua: após cada projeto, o squad analisa falhas de planejamento, atualiza checklists e frameworks, e registra métricas para melhorar continuamente.
