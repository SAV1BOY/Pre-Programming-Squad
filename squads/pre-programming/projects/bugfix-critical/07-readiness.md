# Bugfix Crítico — Fase 07: Readiness

## Objetivo da Fase

Validação rápida de prontidão para deploy do fix. Em bugfix crítico, readiness é checklist binário (não scoring multidimensional) para não atrasar resolução.

## Agentes Envolvidos

- **Agente de Readiness** (líder da fase) — Executa checklist de prontidão fast-track
- **Agente de Riscos** — Confirma que rollback está pronto

## Inputs

- Fix implementado e testado
- Plano de rollback (Fase 05)
- Resultado dos testes (Fase 06)
- Plano de monitoramento pós-fix

## Atividades

1. **Executar checklist de deploy de emergência:**
   - [ ] Causa raiz identificada e documentada?
   - [ ] Fix é mínimo e isolado (sem refactoring)?
   - [ ] Teste de reprodução passa com fix?
   - [ ] Suite de testes existente passa?
   - [ ] Smoke test em staging validado?
   - [ ] Rollback pode ser executado em <15 minutos?
   - [ ] Feature flag disponível (se aplicável)?
   - [ ] Monitoramento pós-fix configurado?
   - [ ] Stakeholders notificados sobre deploy iminente?
   - [ ] On-call disponível para monitorar pós-deploy?
2. **Decisão go/no-go** — Todos os itens obrigatórios devem ser "sim". Se algum é "não", resolver antes de deploy.
3. **Definir janela de deploy** — Para Sev1: imediato. Para Sev2: próxima janela disponível. Para Sev3: próximo ciclo de deploy.

## Outputs

- Checklist de deploy preenchido
- Decisão go/no-go
- Janela de deploy definida
- Confirmação de on-call para monitoramento

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Checklist completo | Todos os itens obrigatórios são "sim" | Sim |
| Rollback testado | Rollback foi verificado (não apenas planejado) | Sim |
| On-call confirmado | Pessoa de on-call disponível para pós-deploy | Sim |

**SLA:** Readiness de Sev1 deve ser concluída em **15 minutos**.

## Próxima Fase

→ [08-handoff.md](./08-handoff.md) — Deploy do fix e monitoramento
