# AI Systems Readiness Checklist

## Propósito
Garantir que sistemas de IA têm evals, guardrails, fallbacks e observabilidade planejados.

## Quando Usar
- Durante a fase correspondente do pipeline de pré-programação
- Em revisões de qualidade antes de avançar para a próxima fase
- Quando o Readiness Gatekeeper solicita verificação

---

## Checklist

### IA/ML Readiness
- [ ] Métricas de avaliação (evals) estão definidas
- [ ] Guardrails de output estão especificados
- [ ] Fallback para quando IA falha está planejado
- [ ] Dataset de teste está preparado
- [ ] Bias e fairness foram avaliados

### Operação de IA
- [ ] Monitoramento de drift está planejado
- [ ] Custo por inferência está estimado
- [ ] Rate limiting de API de IA está definido
- [ ] Human-in-the-loop está planejado onde necessário
- [ ] Versionamento de modelos/prompts está definido

---

## Critérios de Aprovação
- **Mínimo:** 80% dos itens marcados
- **Recomendado:** 100% dos itens marcados
- **Bloqueador:** Qualquer item crítico não atendido deve ser escalado

## Red Flags
- Mais de 3 itens não marcados sem justificativa
- Itens marcados sem evidência de verificação real
- Checklist preenchido em menos de 5 minutos (superficialidade)
