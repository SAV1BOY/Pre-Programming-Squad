# Checklist: Qualidade da Revisão de Performance

## Propósito
Garantir que requisitos de performance (latência, throughput, escalabilidade) estão definidos, gargalos potenciais identificados e custos estimados antes da implementação.

## Quando Usar
- Após definição de arquitetura e fluxos
- Antes de iniciar implementação de componentes críticos
- Quando a solução envolve escala significativa ou requisitos de tempo real

---

## Checklist

### Latência
- [ ] Requisitos de latência estão definidos por operação (p50, p95, p99)
- [ ] Budget de latência está distribuído entre componentes do fluxo
- [ ] Operações que exigem resposta em tempo real estão identificadas
- [ ] Estratégias de cache estão planejadas onde aplicável
- [ ] Latência de dependências externas está incluída no cálculo

### Throughput
- [ ] Volume esperado de requisições está estimado (por segundo, minuto, dia)
- [ ] Picos de demanda estão mapeados (horário, sazonalidade, eventos)
- [ ] Capacidade necessária de processamento está calculada
- [ ] Estratégia de queue/buffering para picos está definida
- [ ] Limites de throughput das dependências estão mapeados

### Escalabilidade
- [ ] Estratégia de escala está definida (horizontal, vertical, auto-scaling)
- [ ] Gargalos de escala estão identificados (banco, rede, CPU, memória)
- [ ] Componentes stateful vs stateless estão identificados
- [ ] Estratégia de particionamento/sharding está definida se necessário
- [ ] Testes de escala estão planejados

### Custos
- [ ] Custo de infraestrutura está estimado para carga normal
- [ ] Custo de infraestrutura está estimado para carga de pico
- [ ] Custo cresce linearmente ou exponencialmente com a escala
- [ ] Otimizações de custo estão identificadas (reserved instances, spot, etc.)
- [ ] Budget de infraestrutura foi aprovado

### Gargalos
- [ ] Potenciais gargalos de banco de dados estão identificados
- [ ] Potenciais gargalos de rede estão identificados
- [ ] Operações N+1 foram avaliadas e mitigadas
- [ ] Operações bloqueantes (I/O síncrono) foram identificadas
- [ ] Plano de ação para gargalos identificados está documentado

---

## Critérios de Aprovação
- **Mínimo**: Latência e Throughput completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Requisitos de latência indefinidos ou gargalos críticos ignorados

## Sinais de Alerta (Red Flags)
- "Vai ser rápido o suficiente" sem números
- Nenhuma estimativa de volume de uso
- Cache como solução para tudo sem estratégia de invalidação
- Custo de infraestrutura não estimado
- Escalabilidade planejada para 1000x sem demanda real

## Agente Responsável
**Agente de Solution Architecture** — em colaboração com o **Agente de Risk & Failure Analysis** para gargalos.
