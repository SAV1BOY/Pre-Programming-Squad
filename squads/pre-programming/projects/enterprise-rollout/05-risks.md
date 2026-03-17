# Rollout Enterprise — Fase 05: Riscos

## Objetivo da Fase

Identificar riscos organizacionais, de compliance, de adoção e operacionais. Rollouts enterprise falham mais por resistência organizacional do que por problemas técnicos.

## Agentes Envolvidos

- **Agente de Riscos** (líder da fase) — Identifica riscos organizacionais e técnicos
- **Agente de Arquitetura** — Valida mitigações técnicas
- **Agente de Requisitos** — Valida riscos de requisitos regulatórios

## Inputs

- Mapa de resistências (Fase 02)
- Plano de fases e critérios (Fase 03)
- Arquitetura de coexistência (Fase 04)
- Requisitos de compliance (Fase 01)

## Atividades

1. **Avaliar risco de resistência organizacional** — Departamentos podem boicotar ou subutilizar o sistema. Líderes podem não priorizar treinamento. Mitigação: sponsor executivo ativo, KPIs de adoção.
2. **Avaliar risco de compliance** — Falha em requisitos regulatórios pode gerar multas e sanções. Qual o custo de não-compliance? Mitigação: validação de compliance por fase antes de avançar.
3. **Avaliar risco de migração de dados** — Perda de dados, inconsistência entre sistemas, downtime durante migração. Mitigação: dry-run, validação, período de coexistência.
4. **Avaliar risco de produtividade** — Curva de aprendizado pode reduzir produtividade temporariamente. Quanto? Por quanto tempo? Mitigação: treinamento intensivo, suporte dedicado.
5. **Avaliar risco de dependência de timeline** — Rollout enterprise frequentemente tem deadline externo (regulatório, contratual). O que acontece se atrasar? Mitigação: buffer e plano de contingência.
6. **Avaliar risco de cascata** — Problema em uma fase pode contaminar a percepção das próximas. "Na fase 1 foi terrível, não queremos na fase 2." Mitigação: cada fase deve ser sucesso visível.
7. **Planejar rollback organizacional** — Se rollout falhar: como reverter para o estado anterior? Dados migrados são revertidos? Processos manuais retomados?

## Outputs

- Matriz de riscos organizacionais (probabilidade x impacto)
- Plano de mitigação de resistência
- Avaliação de risco de compliance por fase
- Impacto de produtividade estimado (curva de aprendizado)
- Plano de contingência para timeline
- Plano de rollback organizacional

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Resistência mitigada | Plano para cada foco de resistência identificado | Sim |
| Compliance validado | Cada fase tem checklist de compliance aprovado | Sim |
| Rollback planejado | Reversão possível em cada fase | Sim |
| Timeline com buffer | Margem de contingência para atrasos | Sim |
| Sponsor ativo | Executivo comprometido com comunicação | Sim |

## Próxima Fase

→ [06-tests.md](./06-tests.md) — Testes de rollout com foco em migração, compliance e aceitação
