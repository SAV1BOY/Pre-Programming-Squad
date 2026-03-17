# Workflow 14: Prontidão para Agentes de IA

## Objetivo
Garantir que projetos envolvendo AI/ML ou agentes inteligentes tenham dados, modelos, avaliação e guardrails adequadamente planejados antes da implementação.

## Trigger
- Projeto classificado como "Projeto de AI/ML" ou com componente significativo de inteligência artificial.

## Agentes Envolvidos
- Agente de Arquitetura (AI/ML)
- Cientista de Dados / ML Engineer
- Agente de Qualidade
- Agente de Risco

## Passos

### 1. Definir Escopo do AI/ML
- Qual problema o modelo/agente resolve.
- Tipo de tarefa (classificação, geração, recomendação, agente autônomo).
- Baseline humano para comparação.
- **Output:** Escopo AI/ML definido.

### 2. Avaliar Disponibilidade de Dados
- Quais dados são necessários para treinar/ajustar.
- Dados estão disponíveis, são suficientes e de qualidade?
- Necessidade de anotação/labeling.
- LGPD: dados pessoais envolvidos?
- **Output:** Avaliação de dados.

### 3. Escolher Abordagem
- Modelo pré-treinado (GPT, Claude, etc.) vs. treinar do zero.
- Fine-tuning vs. prompt engineering vs. RAG.
- Custo por inferência estimado.
- **Output:** Abordagem de AI definida e justificada.

### 4. Definir Guardrails e Limites
- O que o agente/modelo NÃO deve fazer.
- Limites de autonomia (quando escalar para humano).
- Filtros de conteúdo e segurança.
- Monitoramento de alucinações/erros.
- **Output:** Guardrails documentados.

### 5. Definir Métricas de Avaliação
- Métricas de qualidade do modelo (accuracy, F1, BLEU, etc.).
- Métricas de negócio (impacto da AI no processo).
- Critérios de aceite para "bom o suficiente".
- **Output:** Framework de avaliação.

### 6. Planejar Pipeline de ML (se aplicável)
- Treinamento, validação, deploy de modelos.
- Monitoramento de drift.
- Retreinamento periódico.
- **Output:** Pipeline de MLOps planejado.

### 7. Planejar Testes de AI
- Testes de qualidade do modelo.
- Testes de edge cases (inputs adversariais).
- Testes de segurança (prompt injection, jailbreak).
- Testes de custo (consumo de tokens).
- **Output:** Estratégia de testes AI.

## Gates de Qualidade
- [ ] Escopo AI/ML está claro e justificado.
- [ ] Dados necessários estão disponíveis ou há plano para obtê-los.
- [ ] Abordagem está escolhida e justificada.
- [ ] Guardrails e limites de autonomia estão definidos.
- [ ] Métricas de avaliação estão definidas com thresholds.
- [ ] Pipeline de MLOps está planejado (se aplicável).
- [ ] Testes de AI estão planejados (incluindo segurança).
- [ ] Custo de inferência está estimado.

## Output
- AI/ML pronto para implementação.
- Guardrails definidos.
- Framework de avaliação.
- Pipeline planejado.

## Próximo Workflow
→ Retorna ao workflow principal (06-test-design-to-readiness).
