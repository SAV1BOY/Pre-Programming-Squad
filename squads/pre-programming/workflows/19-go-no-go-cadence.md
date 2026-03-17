# Workflow 19: Cadência de Go/No-Go

## Objetivo
Estabelecer uma cadência regular de avaliações Go/No-Go em pontos críticos do projeto, garantindo que decisões de prosseguir ou parar sejam tomadas com base em evidências.

## Trigger
- Chegada a qualquer gate de decisão definido no planejamento.

## Agentes Envolvidos
- Agente de Readiness (Facilitador)
- Decisor Final
- Tech Lead
- Product Owner
- Stakeholders-chave

## Passos

### 1. Identificar Gates de Go/No-Go
- Gate 1: Após discovery → prosseguir para arquitetura?
- Gate 2: Após arquitetura → prosseguir para implementação?
- Gate 3: Após implementação → prosseguir para deploy?
- Gates adicionais conforme complexidade do projeto.
- **Output:** Gates identificados e agendados.

### 2. Preparar Cada Gate
- Compilar evidências e artefatos para o gate.
- Calcular score de readiness para o ponto atual.
- Identificar itens vermelhos e amarelos.
- Enviar material antecipadamente aos decisores.
- **Output:** Material de Go/No-Go preparado.

### 3. Conduzir a Reunião de Gate
- Apresentar status (15 min máx).
- Discutir itens vermelhos e riscos (15 min).
- Coletar votos e justificativas (10 min).
- Registrar decisão (5 min).
- **Output:** Decisão registrada.

### 4. Agir Conforme Resultado
- **Go:** Avançar para próxima fase. Definir data do próximo gate.
- **Go com Condições:** Definir condições, prazos e checkpoints.
- **No-Go:** Definir ações corretivas e data de reavaliação.
- **Output:** Próximos passos definidos.

### 5. Documentar e Comunicar
- Preencher template `go-no-go-template.md`.
- Comunicar decisão a todas as partes.
- Atualizar cronograma se necessário.
- **Output:** Decisão documentada e comunicada.

## Gates de Qualidade
- [ ] Gates estão identificados e agendados para o projeto.
- [ ] Material é enviado com antecedência aos decisores.
- [ ] Critérios de Go estão definidos antes da avaliação.
- [ ] Decisão é baseada em evidências objetivas.
- [ ] Votos e justificativas são registrados.
- [ ] Próximos passos são definidos independente do resultado.
- [ ] Decisão é comunicada a todas as partes.

## Output
- Registro de cada decisão Go/No-Go.
- Histórico de gates do projeto.
- Lições aprendidas por gate.

## Próximo Workflow
→ Depende da decisão: próxima fase ou ações corretivas.
