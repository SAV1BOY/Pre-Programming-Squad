# Workflow 06: Do Design de Testes à Prontidão

## Objetivo
Preparar todos os aspectos operacionais e de infraestrutura necessários para o desenvolvimento, verificando que o projeto está pronto para transição.

## Trigger
- Design de testes e estimativas completos no workflow 05.

## Agentes Envolvidos
- Agente de Readiness
- Equipe de DevOps/Infraestrutura
- Agente de Qualidade

## Passos

### 1. Verificar Prontidão de Ambiente
- Preencher template `environment-readiness-template.md`.
- Verificar repositórios, CI/CD, ambientes.
- **Output:** Checklist de ambiente preenchido.

### 2. Planejar Observabilidade
- Preencher template `observability-plan-template.md`.
- Definir métricas, logs, tracing e alertas.
- **Output:** Plano de observabilidade.

### 3. Planejar Rollout
- Preencher template `rollout-plan-template.md`.
- Definir estratégia e etapas de implantação.
- **Output:** Plano de rollout.

### 4. Planejar Rollback
- Preencher template `rollback-plan-template.md`.
- Definir procedimentos e testar em staging.
- **Output:** Plano de rollback.

### 5. Pontuar Readiness
- Executar task `score-readiness.md`.
- Preencher template `readiness-review-template.md`.
- **Output:** Score de readiness calculado.

## Gates de Qualidade
- [ ] Ambientes de desenvolvimento estão prontos.
- [ ] CI/CD está configurado e funcional.
- [ ] Plano de observabilidade está definido.
- [ ] Plano de rollout está documentado.
- [ ] Plano de rollback está documentado e testado.
- [ ] Score de readiness está calculado.
- [ ] Itens bloqueantes estão identificados.

## Output
- Environment readiness verificado.
- Observability plan definido.
- Rollout plan documentado.
- Rollback plan documentado.
- Readiness review com score.

## Próximo Workflow
→ `07-readiness-to-dev-handoff.md`
