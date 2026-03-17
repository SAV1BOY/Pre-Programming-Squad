# Checklist: Qualidade das Opções de Solução

## Propósito
Verificar se foram consideradas alternativas reais de solução, com análise de trade-offs fundamentada, antes de comprometer-se com uma abordagem.

## Quando Usar
- Antes de escolher a solução técnica ou de produto
- Quando houver pressão para ir direto à "solução óbvia"
- Em revisões de decisão técnica (ADR - Architecture Decision Records)

---

## Checklist

### Alternativas Consideradas
- [ ] Pelo menos 3 alternativas foram avaliadas (incluindo "não fazer nada")
- [ ] Alternativas incluem abordagens fundamentalmente diferentes (não variações do mesmo)
- [ ] Soluções off-the-shelf / SaaS foram consideradas antes de build custom
- [ ] A opção de resolver com processo (não tecnologia) foi avaliada
- [ ] Alternativas descartadas rapidamente têm justificativa documentada

### Trade-offs
- [ ] Cada alternativa tem prós e contras documentados
- [ ] Trade-offs incluem dimensões técnicas (complexidade, manutenção, performance)
- [ ] Trade-offs incluem dimensões de negócio (custo, time-to-market, risco)
- [ ] Trade-offs incluem dimensões de time (skills necessários, curva de aprendizado)
- [ ] Existe matriz comparativa ou outro artefato visual de trade-offs

### Motivo da Escolha
- [ ] A decisão está documentada com raciocínio explícito
- [ ] O motivo da escolha referencia os critérios de decisão usados
- [ ] Critérios de decisão foram definidos ANTES de avaliar alternativas
- [ ] A decisão foi tomada por pessoa/grupo com autoridade para tal
- [ ] Dissidências ou opiniões contrárias foram registradas

### Viabilidade
- [ ] A solução escolhida é viável dentro das restrições de prazo
- [ ] A solução escolhida é viável dentro das restrições de orçamento
- [ ] O time tem (ou pode adquirir) as competências necessárias
- [ ] A infraestrutura necessária está disponível ou é obtível
- [ ] Riscos de implementação foram identificados

### Reversibilidade
- [ ] O grau de reversibilidade da decisão está avaliado
- [ ] Para decisões irreversíveis, o nível de confiança é alto
- [ ] Existe plano B caso a solução escolhida não funcione
- [ ] Pontos de checkpoint para reavaliar a decisão estão definidos
- [ ] O custo de mudar de direção está estimado

---

## Critérios de Aprovação
- **Mínimo**: Alternativas e Motivo da Escolha completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Apenas uma alternativa considerada ou decisão sem justificativa

## Sinais de Alerta (Red Flags)
- "Só existe uma forma de fazer" (viés de confirmação)
- Decisão tomada antes de avaliar alternativas (post-hoc rationalization)
- Todos os trade-offs favorecem a opção "preferida" (análise enviesada)
- Alternativa escolhida é a mais complexa/interessante tecnicamente
- Nenhuma consideração de "não fazer nada" ou "fazer manual"

## Agente Responsável
**Agente de Solution Architecture** — responsável por garantir análise justa e fundamentada das opções.
