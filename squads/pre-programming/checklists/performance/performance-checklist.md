# Performance & Capacity Checklist

## Propósito
Garantir que requisitos de performance, escala e capacidade foram avaliados e têm critérios verificáveis.

## Quando Usar
- Durante a fase correspondente do pipeline de pré-programação
- Em revisões de qualidade antes de avançar para a próxima fase
- Quando o Readiness Gatekeeper solicita verificação

---

## Checklist

### Performance
- [ ] SLAs de latência estão definidos (p50, p95, p99)
- [ ] Throughput esperado está documentado
- [ ] Gargalos potenciais estão identificados
- [ ] Estratégia de cache está definida
- [ ] Database query patterns estão otimizados

### Capacidade
- [ ] Projeção de crescimento está documentada
- [ ] Limites de escala estão identificados
- [ ] Auto-scaling está planejado onde necessário
- [ ] Custo computacional está estimado
- [ ] Load testing criteria estão definidos

---

## Critérios de Aprovação
- **Mínimo:** 80% dos itens marcados
- **Recomendado:** 100% dos itens marcados
- **Bloqueador:** Qualquer item crítico não atendido deve ser escalado

## Red Flags
- Mais de 3 itens não marcados sem justificativa
- Itens marcados sem evidência de verificação real
- Checklist preenchido em menos de 5 minutos (superficialidade)
