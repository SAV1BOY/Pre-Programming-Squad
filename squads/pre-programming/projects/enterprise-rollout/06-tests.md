# Rollout Enterprise — Fase 06: Testes

## Objetivo da Fase

Definir testes com foco em migração de dados, compliance, aceitação por usuários e cenários de coexistência entre sistema antigo e novo.

## Agentes Envolvidos

- **Agente de Testes** (líder da fase) — Desenha estratégia de testes enterprise
- **Agente de Riscos** — Garante cobertura de cenários de compliance
- **Agente de Requisitos** — Valida critérios de aceitação do usuário

## Inputs

- Plano de migração de dados (Fase 04)
- Requisitos de compliance (Fase 01)
- Plano de fases e critérios (Fase 03)
- Processos mapeados (Fase 02)

## Atividades

1. **Testar migração de dados** — Dry-run completo com dados de produção anonimizados. Validar: completude (nenhum registro perdido), integridade (dados corretos), performance (tempo de migração dentro da janela).
2. **Testar coexistência** — Cenários onde parte dos usuários está no sistema novo e parte no antigo. Dados são consistentes? Processos cross-sistema funcionam?
3. **Testar compliance** — Audit trail completo? Retenção de dados conforme regulação? Controle de acesso por role? Relatórios de compliance gerados corretamente?
4. **User Acceptance Test (UAT)** — Usuários-chave de cada departamento testam processos end-to-end no novo sistema. Cada processo validado com assinatura.
5. **Testar rollback** — Simular reversão de uma fase: dados revertem? Usuários voltam ao sistema antigo? Consistência mantida?
6. **Testar performance em escala** — O sistema suporta o volume enterprise? Teste de carga com volume esperado + margem de 50%.
7. **Testar treinamento** — Material de treinamento testado com grupo piloto. Feedback incorporado antes do rollout amplo.

## Outputs

- Relatório de dry-run de migração
- Resultado de testes de coexistência
- Checklist de compliance testado e aprovado
- Relatório de UAT com assinaturas
- Resultado de teste de rollback
- Resultado de teste de performance/carga
- Feedback do grupo piloto sobre treinamento

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Migração validada | Dry-run sem perda de dados | Sim |
| Compliance aprovado | Checklist regulatório assinado | Sim |
| UAT aprovado | Processos-chave validados por usuários | Sim |
| Rollback testado | Reversão simulada com sucesso | Sim |
| Performance validada | Carga enterprise suportada | Sim |

## Próxima Fase

→ [07-readiness.md](./07-readiness.md) — Avaliação de prontidão organizacional e técnica
