# Task: Planejar Migração

## Objetivo
Definir um plano detalhado para migrar dados, funcionalidades e usuários do sistema legado para o novo sistema, minimizando riscos e interrupções no serviço.

## Input Necessário
- Análise do sistema existente.
- Avaliação de compatibilidade.
- Esboço de arquitetura do sistema novo.
- Volumetria de dados do legado.
- Requisitos de disponibilidade durante a migração.

## Agentes Envolvidos
- **Agente de Legado:** Conduz o planejamento da migração.
- **DBA:** Planeja migração de dados.
- **Agente de Arquitetura:** Define infraestrutura de migração.
- **Equipe de Operações:** Planeja execução da migração.

## Passos

### 1. Definir Estratégia de Migração
- **Big Bang:** Migrar tudo de uma vez (risco alto, duração curta).
- **Incremental:** Migrar por módulo/funcionalidade (risco menor, duração maior).
- **Strangler Fig:** Substituir gradualmente o legado (risco mínimo, duração longa).
- Justificar a escolha com base em risco, prazo e complexidade.

### 2. Planejar Migração de Dados
- Mapear transformações necessárias campo a campo.
- Definir ferramentas de migração (ETL, scripts, CDC).
- Planejar validação de integridade pós-migração.
- Definir estratégia de rollback de dados.

### 3. Planejar Migração de Funcionalidades
- Definir ordem de migração por funcionalidade.
- Para cada funcionalidade, definir critério de aceite pós-migração.
- Planejar período de parallel run (ambos sistemas ativos).

### 4. Planejar Migração de Usuários
- Definir estratégia de transição de usuários (gradual, por grupo, big bang).
- Planejar comunicação para os usuários.
- Definir suporte pós-migração.

### 5. Definir Testes de Migração
- Teste de migração de dados em ambiente de staging.
- Teste de parallel run.
- Teste de rollback.
- Teste de performance pós-migração.

### 6. Documentar
- Criar plano de migração detalhado.
- Atualizar o template `legacy-impact-template.md`.

## Output Esperado
- Plano de migração detalhado com fases e critérios.
- Scripts/ferramentas de migração de dados planejados.
- Plano de rollback para cada fase.
- Plano de comunicação para usuários.

## Checklist de Validação
- [ ] Estratégia de migração está definida e justificada.
- [ ] Migração de dados está planejada com mapeamento de campos.
- [ ] Validação de integridade de dados está planejada.
- [ ] Ordem de migração de funcionalidades está definida.
- [ ] Estratégia de rollback existe para cada fase.
- [ ] Testes de migração estão planejados.
- [ ] Plano de comunicação para usuários está definido.
- [ ] Downtime estimado está documentado e aceito.
