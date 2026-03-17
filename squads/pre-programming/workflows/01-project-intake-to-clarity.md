# Workflow 01: Do Intake à Clareza

## Objetivo
Transformar uma solicitação bruta de projeto em um entendimento claro e documentado, pronto para a fase de discovery.

## Trigger
- Nova solicitação de projeto recebida (email, ticket, reunião, documento).

## Agentes Envolvidos
- Agente de Intake
- Agente de Clarificação
- Stakeholder solicitante

## Passos

### 1. Receber e Registrar a Solicitação
- Capturar a solicitação no formato original.
- Registrar metadados: data, canal, solicitante.
- **Output:** Solicitação arquivada.

### 2. Elaborar o Intake Brief
- Executar task `intake-brief.md`.
- Preencher o template `project-brief-template.md`.
- **Output:** Project Brief rascunho.

### 3. Clarificar Ambiguidades
- Executar task `clarify-request.md`.
- Preencher o template `requirements-clarification-template.md`.
- **Output:** Requisitos clarificados, brief atualizado.

### 4. Classificar o Projeto
- Executar task `classify-project.md`.
- Determinar tipo, complexidade e workflow adequado.
- **Output:** Classificação documentada, workflow selecionado.

### 5. Obter Aprovação do Brief
- Enviar brief final ao solicitante.
- Incorporar ajustes finais.
- Obter assinatura formal.
- **Output:** Project Brief aprovado.

## Gates de Qualidade
- [ ] O problema está descrito sem viés de solução.
- [ ] Não há ambiguidades bloqueantes.
- [ ] Stakeholders estão identificados.
- [ ] Restrições conhecidas estão documentadas.
- [ ] O solicitante aprovou o brief.
- [ ] O workflow de pré-programação foi selecionado.

## Output
- Project Brief aprovado.
- Requirements Clarification preenchido.
- Classificação do projeto definida.
- Workflow de pré-programação selecionado.

## Próximo Workflow
→ `02-discovery-to-scope.md`
