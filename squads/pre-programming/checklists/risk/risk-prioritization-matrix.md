# Checklist: Matriz de Priorização de Riscos

## Propósito
Organizar riscos identificados por probabilidade, impacto e detectabilidade, garantindo que os riscos mais críticos recebem atenção e mitigação proporcionais.

## Quando Usar
- Após identificar riscos de múltiplas fontes (técnicos, operacionais, negócio)
- Para priorizar investimento em mitigação de riscos
- Em revisões periódicas de risco durante o projeto

---

## Checklist

### Probabilidade
- [ ] Cada risco tem probabilidade estimada (alta, média, baixa ou escala 1-5)
- [ ] Probabilidade é baseada em dados ou experiência documentada, não intuição
- [ ] Fatores que aumentam a probabilidade estão identificados
- [ ] Fatores que diminuem a probabilidade estão identificados
- [ ] Probabilidade é reavaliada quando contexto muda

### Impacto
- [ ] Impacto de cada risco está classificado em múltiplas dimensões
- [ ] Impacto financeiro está estimado (custo direto + custo de oportunidade)
- [ ] Impacto em usuários está estimado (quantos, por quanto tempo)
- [ ] Impacto reputacional está avaliado
- [ ] Impacto técnico está avaliado (dívida, retrabalho, instabilidade)

### Detectabilidade
- [ ] Facilidade de detecção de cada risco está avaliada
- [ ] Riscos de difícil detecção recebem investimento extra em monitoramento
- [ ] Indicadores leading (antes do problema) estão identificados
- [ ] Indicadores lagging (depois do problema) estão identificados
- [ ] Tempo médio de detecção (MTTD) está estimado para riscos críticos

### Priorização
- [ ] Score de risco (probabilidade x impacto x detectabilidade) está calculado
- [ ] Riscos estão ranqueados do mais crítico ao menos crítico
- [ ] Top 5-10 riscos estão claramente destacados
- [ ] Riscos de probabilidade baixa mas impacto catastrófico estão destacados
- [ ] Riscos aceitos (sem mitigação) estão documentados com justificativa

### Mitigação
- [ ] Cada risco crítico tem pelo menos uma ação de mitigação definida
- [ ] Cada mitigação tem owner e prazo
- [ ] Custo da mitigação é proporcional ao risco (não gastar mais que o impacto)
- [ ] Eficácia esperada da mitigação está avaliada
- [ ] Riscos residuais (após mitigação) estão documentados

### Governança
- [ ] Matriz de riscos está acessível e visível para stakeholders
- [ ] Revisão periódica de riscos está agendada
- [ ] Novos riscos são adicionados quando identificados
- [ ] Riscos mitigados são atualizados ou removidos
- [ ] Trigger para reescalar risco está definido (quando um risco piora)

---

## Critérios de Aprovação
- **Mínimo**: Probabilidade, Impacto e Priorização completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Riscos críticos sem mitigação ou sem owner

## Sinais de Alerta (Red Flags)
- Todos os riscos classificados como "baixo" (otimismo perigoso)
- Nenhum risco identificado (análise insuficiente)
- Riscos identificados mas sem nenhuma mitigação
- Matriz de riscos criada no início e nunca atualizada
- Mitigação para risco de R$10 mil que custa R$100 mil

## Agente Responsável
**Agente de Risk & Failure Analysis** — responsável por consolidar, priorizar e rastrear riscos do projeto.
