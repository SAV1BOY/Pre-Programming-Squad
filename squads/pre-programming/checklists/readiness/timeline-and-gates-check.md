# Checklist: Verificação de Timeline e Gates

## Propósito
Garantir que fases, gates de qualidade e marcos do projeto estão definidos, com critérios claros para avançar entre fases.

## Quando Usar
- Ao planejar o cronograma de implementação
- Antes de comprometer datas com stakeholders
- Quando há pressão para "pular" fases ou gates

---

## Checklist

### Fases Definidas
- [ ] Fases de implementação estão definidas com escopo claro por fase
- [ ] Duração estimada de cada fase está calculada
- [ ] Entregáveis de cada fase estão listados
- [ ] Dependências entre fases estão mapeadas
- [ ] Paralelismo possível entre fases está identificado

### Gates de Qualidade
- [ ] Gate de code review está definido (critérios de aprovação)
- [ ] Gate de testes está definido (quais testes devem passar)
- [ ] Gate de segurança está definido (scan, review)
- [ ] Gate de performance está definido (benchmarks que devem passar)
- [ ] Gate de readiness para produção está definido

### Marcos (Milestones)
- [ ] Marcos significativos estão identificados com datas
- [ ] Cada marco tem deliverable concreto e verificável
- [ ] Marcos são usados para comunicar progresso a stakeholders
- [ ] Atraso em marco aciona revisão de plano (não é ignorado)
- [ ] Marcos são realistas dado as restrições do projeto

### Riscos de Timeline
- [ ] Dependências que podem atrasar o cronograma estão identificadas
- [ ] Buffer para imprevistos está incluído na timeline
- [ ] Caminho crítico está identificado e monitorado
- [ ] Cenário de atraso tem plano de mitigação (cortar escopo, adicionar recurso)
- [ ] Datas comprometidas com stakeholders têm nível de confiança informado

### Comunicação
- [ ] Formato e frequência de report de progresso estão definidos
- [ ] Quem recebe updates de progresso está definido
- [ ] Processo para comunicar atrasos está definido (proativo, não reativo)
- [ ] Métricas de progresso estão definidas (burn-down, velocity, etc.)
- [ ] Retrospectivas de fase estão planejadas

---

## Critérios de Aprovação
- **Mínimo**: Fases e Gates completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Nenhuma fase ou gate definido ou timeline sem buffer

## Sinais de Alerta (Red Flags)
- Timeline sem buffer algum ("cada dia conta")
- Gates de qualidade que podem ser pulados por pressão de prazo
- Marcos definidos por data sem considerar escopo ou capacidade
- Nenhum caminho crítico identificado
- Timeline que não inclui tempo para testes, review e deploy

## Agente Responsável
**Agente de Estimation & Planning** — responsável por definir timeline realista com gates adequados.
