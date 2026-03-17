# Task: Priorizar Riscos

## Objetivo
Identificar, avaliar e priorizar os riscos do projeto, definindo planos de mitigação para os riscos mais críticos e garantindo que a equipe esteja preparada para respondê-los.

## Input Necessário
- Discovery completa.
- Definição de escopo e fases.
- Mapa de restrições.
- Mapa de integrações e dependências.
- Premissas não validadas.

## Agentes Envolvidos
- **Agente de Risco:** Conduz a identificação e avaliação.
- **Agente de Arquitetura:** Identifica riscos técnicos.
- **Agente de Qualidade:** Identifica riscos de qualidade.
- **Stakeholders:** Identificam riscos de negócio.

## Passos

### 1. Brainstorm de Riscos
- Reunir equipe multidisciplinar (técnica + negócio).
- Usar categorias: Técnico, Negócio, Organizacional, Externo.
- Perguntar: "O que pode dar errado? O que pode atrasar? O que pode custar mais?"

### 2. Avaliar Probabilidade e Impacto
- Para cada risco, classificar probabilidade (1-5) e impacto (1-5).
- Calcular severidade = Probabilidade x Impacto.
- Posicionar na matriz de risco.

### 3. Priorizar pelo Top 10
- Ordenar por severidade (maior para menor).
- Selecionar os 10 riscos mais críticos para plano de ação imediato.
- Os demais ficam em monitoramento.

### 4. Definir Estratégia de Resposta
- Para cada risco do Top 10:
  - **Evitar:** Mudar o plano para eliminar o risco.
  - **Mitigar:** Ações para reduzir probabilidade ou impacto.
  - **Transferir:** Passar o risco para terceiros (seguro, contrato).
  - **Aceitar:** Reconhecer e monitorar, com plano de contingência.

### 5. Documentar e Atribuir
- Preencher o template `risk-register-template.md`.
- Atribuir um responsável para cada risco do Top 10.
- Definir frequência de revisão.

## Output Esperado
- Registro de riscos completo e priorizado.
- Top 10 riscos com planos de mitigação.
- Responsáveis atribuídos.
- Agenda de revisão de riscos definida.

## Checklist de Validação
- [ ] Riscos foram identificados com participação multidisciplinar.
- [ ] Cada risco tem probabilidade e impacto avaliados.
- [ ] Os 10 riscos mais críticos têm plano de mitigação.
- [ ] Cada risco do Top 10 tem um responsável atribuído.
- [ ] Gatilhos de materialização estão definidos.
- [ ] Frequência de revisão de riscos está agendada.
- [ ] Premissas não validadas estão refletidas como riscos.
