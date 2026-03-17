# Workflow 18: Prontidão de Rollout e Rollback

## Objetivo
Garantir que os planos de implantação e reversão estejam completos, testados e prontos para serem executados quando o desenvolvimento for concluído.

## Trigger
- Arquitetura e infraestrutura definidas (workflow 03 e 06 em andamento).

## Agentes Envolvidos
- Agente de Readiness
- Equipe de DevOps/SRE
- Agente de Arquitetura
- DBA

## Passos

### 1. Definir Estratégia de Rollout
- Preencher template `rollout-plan-template.md`.
- Escolher tipo (Canary, Blue-Green, Feature Flag, Rolling).
- Definir etapas e critérios de avanço.
- **Output:** Plano de rollout.

### 2. Definir Plano de Rollback
- Preencher template `rollback-plan-template.md`.
- Definir gatilhos de rollback.
- Documentar procedimentos passo a passo.
- **Output:** Plano de rollback.

### 3. Planejar Rollback de Dados
- Identificar migrations que alteram o schema.
- Escrever scripts de rollback para cada migration.
- Identificar cenários onde rollback de dados não é possível.
- **Output:** Scripts de rollback planejados.

### 4. Definir Monitoramento Pós-Deploy
- Métricas a observar durante o rollout.
- Thresholds de alerta e rollback.
- Dashboards a acompanhar.
- **Output:** Checklist de monitoramento pós-deploy.

### 5. Testar Rollback (Dry Run)
- Executar procedimento de rollback em staging.
- Medir tempo de execução.
- Validar integridade pós-rollback.
- **Output:** Rollback testado e tempo de execução medido.

### 6. Escalar Equipe de Plantão
- Definir quem estará de plantão durante o rollout.
- Verificar disponibilidade e contatos.
- Definir processo de escalação.
- **Output:** Escala de plantão definida.

## Gates de Qualidade
- [ ] Estratégia de rollout está definida com etapas.
- [ ] Plano de rollback está documentado passo a passo.
- [ ] Scripts de rollback de dados existem para cada migration.
- [ ] Rollback foi testado em staging.
- [ ] Tempo de rollback está dentro do RTO.
- [ ] Monitoramento pós-deploy está planejado.
- [ ] Equipe de plantão está escalada.

## Output
- Rollout e rollback prontos para execução.
- Testes de rollback realizados.
- Equipe de plantão escalada.

## Próximo Workflow
→ `19-go-no-go-cadence.md`
