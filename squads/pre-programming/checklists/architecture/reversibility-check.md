# Checklist: Verificação de Reversibilidade

## Propósito
Classificar decisões como reversíveis ou irreversíveis, garantindo que decisões de difícil reversão recebem análise proporcional ao seu impacto.

## Quando Usar
- Ao tomar qualquer decisão arquitetural significativa
- Quando há debate sobre nível de análise necessário para uma decisão
- Antes de comprometer recursos significativos em uma direção

---

## Checklist

### Classificação de Decisões
- [ ] Cada decisão arquitetural está classificada como reversível ou irreversível
- [ ] O custo de reverter cada decisão está estimado (tempo, dinheiro, retrabalho)
- [ ] O tempo necessário para reverter está estimado
- [ ] Decisões irreversíveis estão destacadas e recebem mais análise
- [ ] Decisões reversíveis são tomadas com velocidade adequada (não over-analyze)

### Decisões Irreversíveis
- [ ] Escolha de linguagem/plataforma principal foi avaliada com profundidade
- [ ] Escolha de banco de dados principal foi avaliada com PoC se necessário
- [ ] Modelo de dados fundamental foi validado com cenários reais
- [ ] Contratos públicos de API foram revisados por consumidores antes de publicar
- [ ] Decisões de vendor lock-in foram tomadas conscientemente com alternativas avaliadas

### Decisões Reversíveis
- [ ] Decisões reversíveis foram tomadas rapidamente (bias for action)
- [ ] Ponto de revisão futuro está definido para decisões reversíveis
- [ ] A arquitetura permite mudar facilmente: framework de frontend
- [ ] A arquitetura permite mudar facilmente: ferramenta de CI/CD
- [ ] A arquitetura permite mudar facilmente: provedor de serviços específicos

### Estratégias de Reversibilidade
- [ ] Feature flags estão planejadas para mudanças que podem precisar de rollback
- [ ] Abstrações estão criadas onde vendor lock-in é possível (ex: interface para storage)
- [ ] Pontos de decisão futuros estão marcados no timeline (quando reavaliar)
- [ ] Migrations de banco são reversíveis (up e down)
- [ ] Contratos de API suportam evolução sem breaking changes

### Governança
- [ ] Decisões irreversíveis requerem aprovação de mais de uma pessoa
- [ ] Decisões irreversíveis estão documentadas como ADRs (Architecture Decision Records)
- [ ] Contexto que levou à decisão está registrado (para futuras revisões)
- [ ] Critérios que invalidariam a decisão estão definidos
- [ ] Responsável por cada decisão está identificado

---

## Critérios de Aprovação
- **Mínimo**: Classificação e Decisões Irreversíveis completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Decisão irreversível tomada sem análise adequada

## Sinais de Alerta (Red Flags)
- Toda decisão tratada como irreversível (paralisia por análise)
- Decisão irreversível tomada em 5 minutos sem análise
- "Podemos mudar depois" para decisão que é claramente irreversível
- Nenhum ADR para decisões estruturais
- Decisão de banco de dados baseada apenas em preferência pessoal

## Agente Responsável
**Agente de Solution Architecture** — responsável por classificar e governar a reversibilidade das decisões.
