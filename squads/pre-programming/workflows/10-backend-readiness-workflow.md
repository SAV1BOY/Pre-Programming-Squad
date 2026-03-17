# Workflow 10: Prontidão Backend

## Objetivo
Garantir que projetos com foco em backend estejam prontos para implementação, com modelo de dados, APIs, integrações e infraestrutura adequadamente planejados.

## Trigger
- Projeto classificado com componente backend significativo.

## Agentes Envolvidos
- Agente de Arquitetura
- DBA
- Agente de Qualidade
- Equipe de DevOps

## Passos

### 1. Validar Modelo de Dados
- Revisar template `data-model-template.md`.
- Verificar normalização, índices e volumetria.
- Validar com DBA.
- **Output:** Modelo de dados revisado e aprovado.

### 2. Validar Contratos de API
- Revisar template `api-contract-template.md`.
- Verificar completude de endpoints, erros e validações.
- **Output:** Contratos de API validados.

### 3. Validar Integrações
- Revisar template `integration-map-template.md`.
- Verificar que sandboxes estão disponíveis.
- Testar conectividade com serviços externos.
- **Output:** Integrações validadas.

### 4. Configurar Infraestrutura Backend
- Banco de dados provisionado (dev e staging).
- Cache configurado (se aplicável).
- Filas/mensageria configuradas (se aplicável).
- **Output:** Infraestrutura backend pronta.

### 5. Definir Estratégia de Migrations
- Ferramenta de migration escolhida.
- Convenções de nomenclatura definidas.
- Processo de rollback de migrations planejado.
- **Output:** Estratégia de migrations documentada.

### 6. Validar Segurança Backend
- Revisão de autenticação e autorização.
- Validação de input e sanitização.
- Proteção contra injeções.
- **Output:** Checklist de segurança backend validado.

### 7. Configurar Observabilidade Backend
- Logging estruturado configurado.
- Métricas de aplicação definidas (RED metrics).
- Health checks implementados.
- **Output:** Observabilidade backend planejada.

## Gates de Qualidade
- [ ] Modelo de dados revisado por DBA.
- [ ] Contratos de API completos e validados.
- [ ] Integrações testadas em sandbox.
- [ ] Banco de dados provisionado em dev e staging.
- [ ] Estratégia de migrations definida.
- [ ] Segurança backend revisada.
- [ ] Observabilidade planejada.

## Output
- Backend pronto para implementação.
- Infraestrutura provisionada.
- Contratos validados.

## Próximo Workflow
→ Retorna ao workflow principal (06-test-design-to-readiness).
