# Task: Pontuar Prontidão

## Objetivo
Avaliar objetivamente o nível de prontidão do projeto para entrar na fase de desenvolvimento, atribuindo um score baseado em critérios pré-definidos e identificando itens pendentes.

## Input Necessário
- Todos os artefatos produzidos na pré-programação.
- Checklist de readiness com critérios e pesos.
- Feedback da equipe de desenvolvimento.

## Agentes Envolvidos
- **Agente de Readiness:** Conduz a avaliação.
- **Agente de Arquitetura:** Avalia prontidão técnica.
- **Agente de Qualidade:** Avalia prontidão de qualidade.
- **Tech Lead do Dev:** Avalia se tem o que precisa para começar.

## Passos

### 1. Reunir Artefatos
- Compilar lista de todos os artefatos produzidos.
- Verificar completude de cada um.
- Identificar artefatos obrigatórios vs. opcionais para este tipo de projeto.

### 2. Avaliar por Dimensão
- **Clareza de Requisitos (0-20):** Requisitos claros, aprovados e testáveis.
- **Arquitetura e Design (0-20):** Arquitetura documentada e revisada.
- **Riscos e Qualidade (0-20):** Riscos mapeados, testes planejados.
- **Infraestrutura (0-20):** Ambientes prontos, CI/CD configurado.
- **Alinhamento (0-20):** Stakeholders alinhados, equipe alocada.

### 3. Calcular Score
- Somar pontos de todas as dimensões.
- Classificar: Pronto (≥80), Pronto com ressalvas (60-79), Não pronto (<60).

### 4. Identificar Itens Bloqueantes
- Listar itens com pontuação zero ou muito baixa.
- Classificar como bloqueante ou não-bloqueante.
- Definir prazo e responsável para cada item pendente.

### 5. Documentar
- Preencher o template `readiness-review-template.md`.
- Registrar score, justificativa e itens pendentes.

## Output Esperado
- Score de readiness calculado (0-100).
- Classificação (Pronto / Pronto com ressalvas / Não pronto).
- Lista de itens pendentes com prazo e responsável.
- Readiness review preenchido.

## Checklist de Validação
- [ ] Todos os artefatos obrigatórios foram verificados.
- [ ] Cada dimensão foi avaliada com critérios objetivos.
- [ ] O score reflete a realidade (não foi inflado).
- [ ] Itens bloqueantes estão identificados.
- [ ] Itens pendentes têm responsável e prazo.
- [ ] A equipe de dev participou da avaliação.
- [ ] O resultado foi comunicado aos stakeholders.
