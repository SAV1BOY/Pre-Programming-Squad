# Checklist: Auditoria Sintoma vs Causa Raiz

## Propósito
Garantir que a investigação distingue corretamente sintomas observáveis de causas raiz, evitando investir em soluções que tratam apenas a superfície.

## Quando Usar
- Durante a análise de qualquer problema reportado
- Quando a "solução óbvia" não resolve o problema
- Quando o mesmo problema reaparece após ser "corrigido"

---

## Checklist

### Identificação de Sintomas
- [ ] Sintomas observáveis estão listados separadamente
- [ ] Cada sintoma tem evidência de ocorrência (log, report, métrica)
- [ ] Frequência e padrão dos sintomas estão documentados
- [ ] Correlação temporal dos sintomas foi analisada (quando ocorrem)
- [ ] Sintomas foram priorizados por impacto

### Investigação de Causa
- [ ] Técnica de análise causal foi aplicada (5 Porquês, Fishbone, Fault Tree)
- [ ] Mais de uma hipótese de causa foi considerada
- [ ] Cada hipótese tem evidência a favor ou contra
- [ ] A causa identificada explica TODOS os sintomas observados
- [ ] Causas intermediárias (contribuintes) estão diferenciadas da causa raiz

### Validação da Causa Raiz
- [ ] A causa raiz foi validada com dados, não apenas com opinião
- [ ] Se a causa raiz for eliminada, os sintomas devem desaparecer (teste lógico)
- [ ] A causa raiz é acionável (é possível agir sobre ela)
- [ ] A causa raiz está no nível correto de profundidade (nem superficial, nem abstrata demais)
- [ ] Especialistas do domínio concordam com a causa identificada

### Armadilhas Evitadas
- [ ] Não se confundiu correlação com causalidade
- [ ] Não se parou na primeira causa encontrada sem aprofundar
- [ ] Viés de disponibilidade foi considerado (causa "óbvia" pode não ser a real)
- [ ] Múltiplas causas raiz foram consideradas (pode não ser uma só)
- [ ] A causa raiz identificada não é tão genérica que explica qualquer coisa

---

## Critérios de Aprovação
- **Mínimo**: Identificação de Sintomas e Validação da Causa Raiz completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Causa raiz não identificada ou não validada com dados

## Sinais de Alerta (Red Flags)
- "O problema é que não temos [ferramenta/feature]" (sintoma disfarçado de causa)
- Análise de causa feita em 10 minutos para problema complexo
- Causa raiz que não explica todos os sintomas
- Mesma causa raiz identificada para problemas completamente diferentes
- "Todo mundo sabe que a causa é..." sem evidência

## Agente Responsável
**Agente de Discovery & Framing** — responsável por garantir análise causal rigorosa.
