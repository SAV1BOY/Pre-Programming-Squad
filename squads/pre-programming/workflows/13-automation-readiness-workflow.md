# Workflow 13: Prontidão para Automação

## Objetivo
Garantir que projetos de automação de processos estejam prontos com processos mapeados, pontos de integração definidos e critérios de sucesso claros.

## Trigger
- Projeto classificado como "Automação de processo".

## Agentes Envolvidos
- Agente de Arquitetura
- Agente de Domínio (Processos)
- Agente de Qualidade
- Dono do processo sendo automatizado

## Passos

### 1. Mapear Processo Atual (As-Is)
- Documentar cada passo do processo manual.
- Identificar atores, inputs, outputs e decisões.
- Medir tempo e custo de cada passo.
- **Output:** Mapa do processo atual com métricas.

### 2. Projetar Processo Futuro (To-Be)
- Definir quais passos serão automatizados.
- Quais passos permanecem manuais e por quê.
- Definir pontos de intervenção humana.
- **Output:** Mapa do processo futuro.

### 3. Identificar Integrações de Automação
- Quais sistemas são tocados pela automação.
- APIs disponíveis vs. necessidade de RPA/scraping.
- Autenticação e autorização para ações automatizadas.
- **Output:** Mapa de integrações de automação.

### 4. Definir Tratamento de Exceções
- O que acontece quando a automação falha.
- Fallback para processo manual.
- Alertas e escalação.
- **Output:** Plano de exceções.

### 5. Definir Métricas de Automação
- Taxa de automação (% de casos sem intervenção).
- Tempo economizado por execução.
- Taxa de erro da automação.
- **Output:** KPIs de automação definidos.

### 6. Planejar Testes de Automação
- Testes de happy path da automação.
- Testes de cenários de exceção.
- Testes de volume (muitas execuções simultâneas).
- **Output:** Estratégia de testes de automação.

## Gates de Qualidade
- [ ] Processo atual está mapeado com métricas.
- [ ] Processo futuro está desenhado com pontos de automação claros.
- [ ] Integrações estão identificadas com viabilidade confirmada.
- [ ] Tratamento de exceções está planejado.
- [ ] KPIs de automação estão definidos.
- [ ] Testes de automação estão planejados.
- [ ] Dono do processo aprovou o design.

## Output
- Mapa de processos (As-Is e To-Be).
- Integrações de automação mapeadas.
- KPIs e plano de testes definidos.

## Próximo Workflow
→ Retorna ao workflow principal (06-test-design-to-readiness).
