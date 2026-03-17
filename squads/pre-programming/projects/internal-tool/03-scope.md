# Ferramenta Interna — Fase 03: Escopo

## Objetivo da Fase

Definir quais etapas do workflow serão automatizadas, quais permanecem manuais e qual o nível de UX adequado para o perfil dos usuários.

## Agentes Envolvidos

- **Agente de Escopo** (líder da fase) — Define fronteiras da automação
- **Agente de Requisitos** — Valida que escopo resolve os pain points

## Inputs

- Workflow documentado (Fase 02)
- Pain points priorizados
- Perfil dos usuários-alvo (Fase 01)
- Decisão de vida útil (permanente vs. temporária)

## Atividades

1. **Classificar etapas** — Para cada etapa do workflow: automatizar completamente, assistir com ferramenta, manter manual. Critério: (tempo gasto x frequência x taxa de erro).
2. **Definir MVP da ferramenta** — Conjunto mínimo que resolve o pain point principal. Usável e deployável independentemente.
3. **Calibrar nível de UX** — Usuários técnicos (devs) toleram CLI/scripts. Operadores precisam de UI simples. Suporte precisa de UI intuitiva. Não over-invest em UX para público técnico.
4. **Definir requisitos de acesso** — Quem pode usar? Precisa de autenticação? Níveis de permissão? Audit log de ações?
5. **Estabelecer critérios de sucesso** — Redução de tempo por operação, redução de taxa de erro, satisfação do usuário. Métricas antes e depois.
6. **Documentar o que permanece manual** — Para cada etapa manual, documentar por que não foi automatizada e quando reconsiderar.

## Outputs

- Classificação de etapas (automática, assistida, manual)
- MVP da ferramenta definido
- Nível de UX adequado ao perfil dos usuários
- Requisitos de acesso e permissão
- Critérios de sucesso mensuráveis
- Lista do que permanece manual com justificativa

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| MVP definido | Conjunto mínimo que resolve pain point principal | Sim |
| UX calibrado | Nível de UX adequado ao perfil dos usuários | Sim |
| Critérios de sucesso | Métricas antes/depois definidas | Sim |
| Acesso definido | Autenticação e permissões planejadas | Sim |

## Próxima Fase

→ [04-architecture.md](./04-architecture.md) — Arquitetura simples e pragmática da ferramenta
