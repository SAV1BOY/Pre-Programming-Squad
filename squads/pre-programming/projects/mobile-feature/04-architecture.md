# Feature Mobile — Fase 04: Arquitetura

## Objetivo da Fase

Definir a arquitetura mobile incluindo: camada de dados local, estratégia de cache/sync, platform-specific implementations e comunicação com backend.

## Agentes Envolvidos

- **Agente de Arquitetura** (líder da fase) — Desenha arquitetura mobile
- **Agente de Riscos** — Avalia resiliência em cenários mobile (offline, background kill)

## Inputs

- Estratégia offline e sync (Fase 03)
- Performance targets (Fase 03)
- Constraints de plataforma (Fase 02)
- Arquitetura backend existente

## Atividades

1. **Definir camada de dados local** — SQLite, Realm, CoreData (iOS), Room (Android)? Estratégia de persistência: quais dados são cacheados localmente? TTL? Tamanho máximo?
2. **Desenhar estratégia de sync** — Protocolo de sincronização: full sync, delta sync, event-based? Resolução de conflitos: last-write-wins, merge, manual?
3. **Definir arquitetura de networking** — Retry strategy para requests falhados, request queuing para offline, connection monitoring, certificate pinning.
4. **Planejar platform-specific code** — Quanto é compartilhado (business logic, data layer) vs. platform-specific (UI, permissões, notificações)? Se cross-platform: Flutter, React Native, KMP?
5. **Definir gerenciamento de estado** — State management: Redux, BLoC, MVI, MVVM? Estado sobrevive a background kill? Restauração de estado após termination.
6. **Planejar background processing** — iOS Background Tasks, Android WorkManager. Limitações de cada plataforma. Garantia de execução?
7. **Definir observabilidade mobile** — Crash reporting (Crashlytics/Sentry), analytics de uso, performance monitoring (app start, screen load), network monitoring.

## Outputs

- Arquitetura da camada de dados local
- Design do protocolo de sync com resolução de conflitos
- Estratégia de networking (retry, queue, certificate pinning)
- Divisão shared vs. platform-specific
- State management com restauração
- Background processing design
- Plano de observabilidade mobile

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Dados locais | Estratégia de cache e persistência definida | Sim |
| Sync desenhado | Protocolo e resolução de conflitos | Sim (se offline) |
| Estado restaurável | State sobrevive a background kill | Sim |
| Observabilidade | Crash reporting e performance monitoring | Sim |

## Próxima Fase

→ [05-risks.md](./05-risks.md) — Riscos específicos de mobile
