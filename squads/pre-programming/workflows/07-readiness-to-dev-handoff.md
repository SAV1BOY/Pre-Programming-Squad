# Workflow 07: Da Prontidão ao Handoff para Dev

## Objetivo
Executar a decisão final de Go/No-Go e, se aprovado, realizar o handoff formal para a equipe de desenvolvimento com todos os artefatos necessários.

## Trigger
- Score de readiness calculado no workflow 06.

## Agentes Envolvidos
- Agente de Readiness
- Decisor Final
- Tech Lead do Dev
- Equipe de Desenvolvimento
- Stakeholders-chave

## Passos

### 1. Executar Go/No-Go
- Executar task `run-go-no-go.md`.
- Preencher template `go-no-go-template.md`.
- **Output:** Decisão Go/No-Go registrada.

### 2. Se No-Go: Resolver Pendências
- Identificar e resolver itens bloqueantes.
- Reagendar Go/No-Go.
- Retornar ao passo 1.

### 3. Se Go: Montar Pacote de Dev
- Executar task `build-dev-package.md`.
- Preencher template `implementation-handoff-template.md`.
- **Output:** Pacote de desenvolvimento completo.

### 4. Realizar Handoff
- Executar task `handoff-to-dev.md`.
- Conduzir sessão de handoff com toda a equipe.
- **Output:** Sessão realizada, dúvidas registradas.

### 5. Iniciar Suporte Pós-Handoff
- Definir período de suporte (2 semanas recomendado).
- Agendar check-in após primeira sprint.
- **Output:** Plano de suporte ativo.

## Gates de Qualidade
- [ ] Decisão Go/No-Go está registrada formalmente.
- [ ] Todos os decisores participaram.
- [ ] Pacote de desenvolvimento está completo e acessível.
- [ ] Sessão de handoff foi realizada com toda a equipe de dev.
- [ ] Dúvidas da equipe de dev foram respondidas ou estão em resolução.
- [ ] Suporte pós-handoff está planejado.

## Output
- Decisão Go/No-Go documentada.
- Pacote de desenvolvimento entregue.
- Handoff realizado.
- Suporte pós-handoff ativo.

## Próximo Workflow
→ `20-ralphloop-planning-retro.md` (após conclusão do desenvolvimento)
