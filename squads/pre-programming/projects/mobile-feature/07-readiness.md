# Feature Mobile — Fase 07: Readiness

## Objetivo da Fase

Avaliar prontidão para submissão à app store com foco em compliance de guidelines, performance em dispositivos reais e capacidade de rollback via remote config.

## Agentes Envolvidos

- **Agente de Readiness** (líder da fase) — Avalia prontidão mobile
- **Agente de Riscos** — Confirma compliance e feature flags remotos
- **Agente de Testes** — Apresenta resultados de testes de dispositivo

## Inputs

- Artefatos das fases 01-06
- Resultados de testes de dispositivo e performance
- Modelo de readiness com pesos para "Mobile Feature"

## Atividades

1. **Avaliar dimensões com pesos adaptados:**
   - Clareza de Requisitos (peso: 15%) — Cenários mobile específicos
   - Solidez Arquitetural (peso: 20%) — Offline, sync, platform-specific
   - Cobertura de Riscos (peso: 25%) — App store, fragmentação, rollback remoto
   - Design de Testes (peso: 25%) — Dispositivos, conectividade, lifecycle
   - Plano de Rollout (peso: 10%) — Submissão e rollout gradual
   - Completude de Handoff (peso: 5%)
2. **Checklist de app store submission:**
   - [ ] App Store Review Guidelines compliance (iOS)?
   - [ ] Google Play policies compliance (Android)?
   - [ ] Screenshots e metadata atualizados?
   - [ ] Privacy policy atualizada?
   - [ ] Permissões justificadas no submission form?
   - [ ] TestFlight/Internal testing validado?
3. **Confirmar feature flags remotos** — Feature pode ser desligada sem nova submissão?
4. **Verificar forced update** — Mecanismo para forçar atualização em caso de bug crítico?

## Outputs

- Scorecard de readiness mobile
- Checklist de app store submission preenchido
- Confirmação de feature flags remotos funcionando
- Decisão go/no-go (threshold >= 7.0)

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Score ponderado | >= 7.0 | Sim |
| App store compliance | Checklist de submission aprovado | Sim |
| Feature flag remoto | Feature desligável sem nova versão | Sim |
| Performance OK | Targets atingidos em device matrix | Sim |
| Acessibilidade OK | VoiceOver/TalkBack validados | Sim |

## Próxima Fase

→ [08-handoff.md](./08-handoff.md) — Submissão à app store e rollout gradual
