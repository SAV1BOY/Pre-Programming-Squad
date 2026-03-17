# Feature Mobile — Fase 03: Escopo

## Objetivo da Fase

Definir o escopo da feature mobile, decidir sobre paridade entre plataformas, definir comportamento offline e estabelecer o que é MVP mobile.

## Agentes Envolvidos

- **Agente de Escopo** (líder da fase) — Define escopo e decisões de paridade
- **Agente de Requisitos** — Valida que cenários mobile estão cobertos

## Inputs

- Constraints de plataforma (Fase 02)
- Cenários de conectividade (Fase 02)
- Analytics de uso por plataforma
- Design system mobile

## Atividades

1. **Decidir paridade de plataforma** — Feature idêntica em iOS e Android? Ou comportamento adaptado? Lançamento simultâneo ou iOS first / Android first?
2. **Definir MVP mobile** — Funcionalidade mínima que entrega valor no contexto mobile. Mobile MVP pode ser diferente de web MVP.
3. **Definir estratégia offline** — Para cada operação: online-only, cache-first, offline-first com sync. Trade-offs: complexidade vs. experiência.
4. **Definir comportamento de sync** — Quando sincroniza? Background sync? Manual? Conflitos de merge (editou offline e online)? Resolução de conflitos.
5. **Estabelecer performance targets mobile** — App launch time, time-to-interactive, scroll performance (60fps), tamanho de download, consumo de memória.
6. **Definir deep links** — Quais telas são acessíveis via deep link? Universal links (iOS) / App Links (Android)?
7. **Definir push notifications** — Quais eventos geram push? Frequência máxima? Personalização? Opt-in/opt-out granular?

## Outputs

- Decisão de paridade de plataforma com justificativa
- MVP mobile definido
- Estratégia offline por operação
- Estratégia de sync e resolução de conflitos
- Performance targets mobile
- Mapa de deep links
- Estratégia de push notifications

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| MVP mobile definido | Funcionalidade mínima para contexto mobile | Sim |
| Paridade decidida | iOS e Android com escopo definido | Sim |
| Offline definido | Comportamento em cada cenário de rede | Sim |
| Performance targets | Métricas mobile-specific definidas | Sim |

## Próxima Fase

→ [04-architecture.md](./04-architecture.md) — Arquitetura mobile com cache, sync e platform-specific
