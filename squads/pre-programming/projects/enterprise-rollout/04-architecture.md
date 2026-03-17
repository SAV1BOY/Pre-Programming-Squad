# Rollout Enterprise — Fase 04: Arquitetura

## Objetivo da Fase

Definir a arquitetura técnica que suporta rollout faseado com feature flags, multi-tenancy, migração de dados e coexistência entre sistema antigo e novo.

## Agentes Envolvidos

- **Agente de Arquitetura** (líder da fase) — Desenha arquitetura de rollout faseado
- **Agente de Riscos** — Valida que coexistência entre antigo e novo é segura

## Inputs

- Plano de fases (Fase 03)
- Sistemas afetados e integrações (Fase 02)
- Requisitos de compliance (Fase 01)
- Arquitetura atual

## Atividades

1. **Planejar coexistência** — Como sistema antigo e novo coexistem durante rollout? Dados sincronizados? Feature flags por tenant/departamento? Roteamento por usuário?
2. **Definir feature flags enterprise** — Flags por organização, departamento e role. Granularidade suficiente para rollout faseado sem reeploy.
3. **Planejar migração de dados** — Dados precisam ser migrados entre sistemas? Estratégia: live migration, dual-write, batch ETL? Consistência durante coexistência.
4. **Definir arquitetura de audit/compliance** — Audit trail para todas as operações (quem, quando, o quê). Relatórios de compliance automatizados. Retenção de dados conforme regulação.
5. **Planejar multi-tenancy** — Se o rollout é por cliente/organização: isolamento de dados, configuração por tenant, billing por tenant.
6. **Definir SLA por fase** — SLA pode variar por fase: fase pilot com SLA relaxado, GA com SLA produção. Monitoramento diferenciado.

## Outputs

- Arquitetura de coexistência (antigo + novo)
- Sistema de feature flags enterprise
- Estratégia de migração de dados
- Arquitetura de audit trail e compliance
- Modelo de multi-tenancy (se aplicável)
- SLA por fase de rollout

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Coexistência viável | Antigo e novo podem rodar simultaneamente | Sim |
| Feature flags enterprise | Rollout controlável por departamento/tenant | Sim |
| Migração planejada | Dados migrados sem perda e com rollback | Sim |
| Audit trail | Rastreabilidade para compliance | Sim |
| SLA definido | SLA por fase de rollout | Sim |

## Próxima Fase

→ [05-risks.md](./05-risks.md) — Riscos organizacionais e de compliance do rollout
