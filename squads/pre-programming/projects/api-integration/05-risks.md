# Integração de API — Fase 05: Riscos

## Objetivo da Fase

Identificar riscos específicos de integração com API: indisponibilidade do provedor, breaking changes, rate limiting, incompatibilidade de dados e vendor lock-in.

## Agentes Envolvidos

- **Agente de Riscos** (líder da fase) — Identifica e classifica riscos de integração
- **Agente de Arquitetura** — Valida viabilidade das mitigações

## Inputs

- Arquitetura da camada de integração (Fase 04)
- SLA do provedor (Fase 01)
- Gaps funcionais identificados (Fase 02)
- Histórico de incidentes do provedor (status page, change log)

## Atividades

1. **Avaliar risco de indisponibilidade** — Qual o SLA real do provedor (não o contratual)? Verificar status page histórica. O que acontece quando a API fica fora do ar?
2. **Avaliar risco de breaking changes** — Qual a política de versionamento do provedor? Há histórico de breaking changes sem aviso? Como seremos notificados?
3. **Avaliar risco de rate limiting** — O que acontece quando atingimos o rate limit? HTTP 429 é graceful ou abrupto? Há quota burst?
4. **Avaliar risco de dados inconsistentes** — A API pode retornar dados em formato inesperado? Campos opcionais que são null em produção mas preenchidos em sandbox?
5. **Avaliar vendor lock-in** — Se precisarmos trocar de provedor, quão difícil seria? A camada de abstração é suficiente?
6. **Avaliar risco de segurança** — Tokens podem vazar em logs? Rate limiting protege contra abuso? Dados sensíveis estão criptografados?
7. **Definir plano de contingência** — Para cada risco High, definir ação quando o risco se materializar. Runbook operacional para cenários de falha.

## Outputs

- Matriz de riscos de integração (probabilidade x impacto)
- Análise de histórico de disponibilidade do provedor
- Plano de contingência para indisponibilidade
- Avaliação de vendor lock-in com custo de troca
- Análise de segurança de dados em trânsito
- Runbook operacional para cenários de falha

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Indisponibilidade planejada | Comportamento definido para API fora do ar | Sim |
| Breaking changes monitorados | Mecanismo para detectar mudanças na API | Sim |
| Rate limit projetado | Consumo projetado com margem de segurança | Sim |
| Segurança validada | Tokens e dados sensíveis protegidos | Sim |
| Contingência definida | Runbook para cenários de falha | Sim |

## Próxima Fase

→ [06-tests.md](./06-tests.md) — Estratégia de testes focada em contratos e resiliência
