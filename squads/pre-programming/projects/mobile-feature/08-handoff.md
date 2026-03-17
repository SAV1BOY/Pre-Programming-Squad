# Feature Mobile — Fase 08: Handoff

## Objetivo da Fase

Submeter à app store, gerenciar o processo de review, executar rollout gradual e monitorar métricas mobile pós-lançamento.

## Agentes Envolvidos

- **Agente Coordenador** (líder da fase) — Coordena submissão e rollout
- **Agente de Riscos** — Monitora crash rate e métricas de performance
- **Agente de Testes** — Acompanha feedback da app store e métricas

## Inputs

- App aprovada no readiness (Fase 07)
- Feature flags remotos configurados
- Metadata de app store preparada

## Atividades

1. **Submeter para review** — Submit para Apple App Store e Google Play. Incluir notas de review para o time da Apple explicando mudanças e funcionalidades.
2. **Gerenciar review** — Monitorar status da review. Se rejeitada: analisar motivo, corrigir e resubmeter. Média de 1-2 dias para Apple, <1 dia para Google.
3. **Rollout gradual** — Apple: phased release (1% → 2% → 5% → 10% → 20% → 50% → 100% ao longo de 7 dias). Google: staged rollout com % customizável.
4. **Monitorar métricas pós-lançamento:**
   - Crash rate (target: <0.5% de sessões com crash)
   - ANR rate Android (target: <0.5%)
   - Crash-free users rate
   - Performance (app start, screen load)
   - Reviews e ratings na app store
   - Feature adoption rate
5. **Monitorar feedback na app store** — Reviews negativas nas primeiras 48h podem indicar bugs não detectados. Responder reviews e escalar problemas.
6. **Ação de emergência se necessário** — Se crash rate > 2%: pausar rollout, desabilitar feature via remote config, submeter hotfix com expedited review.
7. **Medir sucesso da feature** — Após rollout completo: adoção, engagement, impacto em métricas de negócio, NPS mobile.

## Outputs

- Confirmação de submissão e aprovação na app store
- Relatório de rollout gradual com métricas por estágio
- Dashboard de crash rate e performance pós-lançamento
- Análise de reviews e ratings
- Métricas de adoção e sucesso da feature

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| App aprovada | Aprovação na App Store e Google Play | Sim |
| Crash rate aceitável | < 0.5% de sessões com crash em cada estágio | Sim |
| Performance estável | Métricas dentro dos targets pós-lançamento | Sim |
| Reviews monitoradas | Feedback negativo investigado em <24h | Sim |
| Rollout completo | 100% dos usuários com a nova versão | Sim |

## Próxima Fase

→ Monitoramento contínuo com iteração baseada em feedback da app store e analytics de uso.

**Nota:** Features mobile têm ciclo de feedback diferente de web. Reviews na app store são públicas e permanentes. Bugs percebidos por usuários resultam em reviews de 1 estrela que afetam ranking. A qualidade na pré-programação é especialmente crítica em mobile porque o custo de erro público é alto e o fix não é instantâneo.
