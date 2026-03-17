# Ferramenta Interna — Fase 04: Arquitetura

## Objetivo da Fase

Definir arquitetura pragmática para a ferramenta interna. Princípio: simplicidade máxima, complexidade mínima. Ferramentas internas não precisam de arquitetura enterprise.

## Agentes Envolvidos

- **Agente de Arquitetura** (líder da fase) — Desenha solução pragmática
- **Agente de Riscos** — Avalia riscos de acesso a dados de produção

## Inputs

- MVP definido (Fase 03)
- Inventário de dados e sistemas (Fase 02)
- Nível de UX (Fase 03)
- Decisão de vida útil (permanente vs. temporária)

## Atividades

1. **Escolher stack simplificada** — Para ferramenta temporária: script ou notebook pode ser suficiente. Para permanente: framework leve (Retool, Streamlit, ou app web simples).
2. **Definir acesso a dados** — Read-only vs. read-write em produção. Se write: quais proteções? Confirmação antes de ações destrutivas? Dry-run mode?
3. **Planejar autenticação** — SSO corporativo quando possível. Evitar criar sistema de autenticação próprio para ferramenta interna.
4. **Definir audit trail** — Para ações que modificam dados: quem fez, quando, o quê. Essencial para troubleshooting e compliance.
5. **Avaliar hosting** — Interno (VM, container) ou cloud. Para ferramenta interna, priorizar facilidade de deploy e manutenção.
6. **Planejar evolução** — Se ferramenta temporária virar permanente, qual o caminho de evolução? Evitar technical debt acumulada em ferramentas "temporárias" que duram anos.

## Outputs

- Stack tecnológica escolhida com justificativa
- Modelo de acesso a dados (read-only vs. read-write com proteções)
- Plano de autenticação (SSO preferencial)
- Design de audit trail
- Plano de hosting e deploy
- Caminho de evolução (se ferramenta temporária se tornar permanente)

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Stack justificada | Complexidade proporcional à vida útil e público | Sim |
| Acesso seguro | Proteções para acesso a dados de produção | Sim |
| Autenticação | SSO ou mecanismo corporativo (não custom) | Sim |
| Audit trail | Ações de escrita são rastreáveis | Condicional |

## Próxima Fase

→ [05-risks.md](./05-risks.md) — Riscos de ferramentas internas com acesso a produção
