# Task: Comparar Opções de Solução

## Objetivo
Avaliar e comparar diferentes abordagens técnicas para resolver o problema, utilizando critérios objetivos e ponderados para chegar à melhor decisão.

## Input Necessário
- Requisitos funcionais e não-funcionais.
- Mapa de restrições.
- Contexto tecnológico da organização.
- Experiência da equipe.

## Agentes Envolvidos
- **Agente de Arquitetura:** Conduz a análise e documenta opções.
- **Agente de Risco:** Avalia riscos de cada opção.
- **Tech Lead:** Avalia viabilidade de implementação.
- **Decisor técnico:** Toma a decisão final.

## Passos

### 1. Identificar Opções Viáveis
- Listar pelo menos 2 e no máximo 4 opções.
- Incluir a opção "não fazer nada" quando relevante.
- Cada opção deve ser genuinamente diferente (não variações triviais).

### 2. Definir Critérios de Avaliação
- Critérios sugeridos: custo, time-to-market, escalabilidade, manutenibilidade, risco técnico, alinhamento com equipe.
- Atribuir pesos antes de avaliar as opções (evitar viés).
- Validar critérios e pesos com os decisores.

### 3. Avaliar Cada Opção
- Para cada opção, detalhar prós e contras.
- Atribuir notas de 1-5 para cada critério.
- Calcular score ponderado.

### 4. Fazer PoC (Proof of Concept) se Necessário
- Se a diferença entre opções é pequena e o risco é alto, fazer PoC.
- Definir escopo mínimo do PoC e critérios de sucesso.
- Time-boxar o PoC (máx 2-5 dias).

### 5. Documentar e Decidir
- Preencher o template `solution-options-template.md`.
- Apresentar recomendação com justificativa.
- Registrar a decisão no template `decision-memo-template.md`.

## Output Esperado
- Análise comparativa documentada com score ponderado.
- Recomendação fundamentada.
- Decisão registrada com justificativa e alternativas rejeitadas.

## Checklist de Validação
- [ ] Pelo menos 2 opções genuinamente diferentes foram avaliadas.
- [ ] Critérios de avaliação foram definidos antes da análise.
- [ ] Pesos foram atribuídos com base em prioridades do projeto.
- [ ] Cada opção tem prós e contras documentados.
- [ ] O score ponderado está calculado corretamente.
- [ ] A recomendação está fundamentada em evidências.
- [ ] A decisão foi registrada com contexto e alternativas.
- [ ] O decisor assinou a decisão.
