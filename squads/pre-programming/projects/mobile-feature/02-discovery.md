# Feature Mobile — Fase 02: Discovery

## Objetivo da Fase

Investigar o contexto mobile em profundidade: padrões de uso, constraints de plataforma, cenários de conectividade e expectativas de UX mobile.

## Agentes Envolvidos

- **Agente de Requisitos** (líder da fase) — Mapeia cenários mobile-specific
- **Agente de Arquitetura** — Analisa constraints técnicas de cada plataforma

## Inputs

- Plataformas e versões definidas (Fase 01)
- Analytics de uso mobile (sessões, telas, fluxos, dispositivos)
- Feedback de usuários mobile (app store reviews, suporte)
- Design system mobile existente

## Atividades

1. **Analisar padrões de uso mobile** — Quando usam (commute, trabalho, noite)? Sessões curtas ou longas? Interrupções frequentes? Contexto de uso (uma mão, em movimento).
2. **Mapear constraints de plataforma** — Background processing (iOS é mais restritivo), push notifications (diferenças iOS/Android), deep linking, permissões runtime.
3. **Definir cenários de conectividade** — Online (Wi-Fi), online (4G/5G), online (3G lento), offline completo, transição entre estados. Comportamento em cada um.
4. **Mapear cenários de dispositivo** — Telas pequenas (iPhone SE), telas grandes (tablets), orientação retrato/paisagem, modo escuro, tamanho de fonte acessível.
5. **Identificar padrões de navegação** — Navegação nativa da plataforma (bottom tabs iOS, drawer Android) vs. custom. Gestos esperados (swipe, pull-to-refresh).
6. **Avaliar impacto em bateria e dados** — A feature consome bateria excessivamente? Downloads grandes em dados móveis? Otimização necessária?
7. **Documentar cenários de lifecycle** — App vai para background, volta para foreground, é terminada pelo OS, memória insuficiente. Estado é preservado?

## Outputs

- Análise de padrões de uso mobile com dados
- Mapa de constraints por plataforma
- Matriz de cenários de conectividade com comportamento
- Cenários de dispositivo e tela
- Padrões de navegação por plataforma
- Avaliação de impacto em bateria e dados
- Cenários de lifecycle documentados

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Conectividade mapeada | Comportamento em cada cenário de rede | Sim |
| Plataformas diferenciadas | Constraints específicas de iOS e Android | Sim |
| Lifecycle coberto | Background, foreground, termination tratados | Sim |
| Dispositivos variados | Telas pequenas e grandes consideradas | Sim |

## Próxima Fase

→ [03-scope.md](./03-scope.md) — Definição do escopo mobile com paridade ou diferenciação de plataforma
