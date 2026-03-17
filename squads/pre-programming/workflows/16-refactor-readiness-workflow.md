# Workflow 16: Prontidão para Refatoração

## Objetivo
Garantir que projetos de refatoração técnica tenham o sistema atual bem compreendido, testes de regressão planejados e estratégia de migração gradual definida.

## Trigger
- Projeto classificado como "Refatoração técnica".

## Agentes Envolvidos
- Agente de Arquitetura
- Agente de Legado
- Agente de Qualidade
- Tech Lead

## Passos

### 1. Documentar Estado Atual
- Executar task `analyze-existing-system.md`.
- Mapear componentes, dependências e fluxos.
- Medir cobertura de testes atual.
- **Output:** Documentação do estado atual.

### 2. Definir Motivação e Escopo
- Por que refatorar? (dívida técnica, performance, manutenibilidade).
- O que será refatorado e o que não será.
- Como medir sucesso da refatoração.
- **Output:** Escopo de refatoração com métricas.

### 3. Garantir Cobertura de Testes
- Se cobertura atual é baixa, priorizar escrita de testes antes de refatorar.
- Focar em testes de integração/E2E para validar comportamento.
- Definir "golden tests" que devem continuar passando.
- **Output:** Plano de testes de regressão.

### 4. Definir Estratégia de Refatoração
- Gradual (refatorar por partes, branch by abstraction).
- Big bang (refatorar tudo de uma vez — alto risco).
- Strangler (novo código ao lado do velho, migrar gradualmente).
- **Output:** Estratégia definida e justificada.

### 5. Planejar Feature Flags
- Usar feature flags para alternar entre código velho e novo.
- Permitir rollback rápido sem deploy.
- **Output:** Estratégia de feature flags.

### 6. Definir Critérios de Sucesso
- Métricas técnicas (complexidade ciclomática, cobertura, latência).
- Métricas de negócio (mesma funcionalidade, zero regressões).
- **Output:** Critérios de sucesso da refatoração.

## Gates de Qualidade
- [ ] Estado atual está documentado e compreendido.
- [ ] Motivação e escopo da refatoração estão claros.
- [ ] Testes de regressão existem ou estão planejados.
- [ ] Estratégia de refatoração está definida e justificada.
- [ ] Feature flags estão planejados para rollback.
- [ ] Critérios de sucesso são mensuráveis.
- [ ] O comportamento funcional não será alterado.

## Output
- Refatoração planejada e pronta para execução.
- Testes de regressão garantidos.
- Estratégia gradual com rollback.

## Próximo Workflow
→ Retorna ao workflow principal (06-test-design-to-readiness).
