# Feature Mobile — Fase 01: Intake

## Objetivo da Fase

Receber e validar a solicitação de feature mobile, identificar plataformas-alvo (iOS, Android, cross-platform), avaliar restrições de app stores e entender o contexto mobile específico.

## Agentes Envolvidos

- **Agente de Requisitos** (líder da fase) — Valida requisitos com contexto mobile
- **Agente de Riscos** — Avaliação preliminar de riscos de app store e plataforma
- **Agente Coordenador** — Registra projeto e identifica devs mobile

## Inputs

- Solicitação de feature com contexto mobile
- Plataformas-alvo (iOS, Android, ambas)
- Versões mínimas de OS suportadas
- Métricas de uso mobile (analytics de plataforma)
- Requisitos de app store (guidelines Apple/Google)

## Atividades

1. **Identificar plataformas e versões** — iOS mínimo, Android mínimo, tablets suportados? Cada versão tem APIs e restrições diferentes.
2. **Avaliar restrições de app store** — Apple App Store Review Guidelines e Google Play policies. A feature viola alguma guideline? (pagamentos in-app, permissões, conteúdo).
3. **Verificar permissões necessárias** — Câmera, localização, notificações push, biometria, armazenamento. Cada permissão tem implicação de UX e privacidade.
4. **Avaliar conectividade** — A feature funciona offline? Parcialmente offline? Apenas online? Qual o comportamento em conexão lenta (3G)?
5. **Identificar diferenças de plataforma** — Mesma feature pode ter comportamento diferente em iOS e Android (navegação, gestos, notificações, background processing).
6. **Verificar ciclo de release** — Review da app store leva 1-7 dias. Hotfix não é instantâneo como web. Feature flags e remote config são essenciais.
7. **Avaliar impacto no tamanho do app** — A feature adiciona SDKs, assets ou dados que aumentam o tamanho do binário? Impacto na taxa de download.

## Outputs

- Plataformas e versões mínimas definidas
- Avaliação de compliance com guidelines de app store
- Lista de permissões necessárias com justificativa
- Estratégia de offline/conectividade
- Diferenças de plataforma identificadas
- Impacto no tamanho do app estimado

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Plataformas definidas | iOS, Android, versões mínimas | Sim |
| App store compliance | Sem violação de guidelines conhecida | Sim |
| Permissões listadas | Cada permissão com justificativa | Sim |
| Offline avaliado | Comportamento offline/online definido | Sim |

## Próxima Fase

→ [02-discovery.md](./02-discovery.md) — Exploração de UX mobile, constraints de plataforma e padrões de uso
