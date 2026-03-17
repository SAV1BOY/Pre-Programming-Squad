# Feature Mobile — Fase 05: Riscos

## Objetivo da Fase

Identificar riscos específicos de mobile: rejeição na app store, fragmentação de dispositivos, impossibilidade de hotfix rápido, problemas de conectividade e bateria.

## Agentes Envolvidos

- **Agente de Riscos** (líder da fase) — Identifica riscos mobile-specific
- **Agente de Arquitetura** — Valida mitigações técnicas

## Inputs

- Arquitetura mobile (Fase 04)
- Guidelines de app store (Fase 01)
- Performance targets (Fase 03)
- Estratégia offline (Fase 03)

## Atividades

1. **Avaliar risco de rejeição na app store** — Apple rejeita apps por: uso de APIs privadas, violação de design guidelines, monetização fora do in-app purchase, crashes em review. Mitigação: compliance checklist, teste em dispositivos de referência.
2. **Avaliar risco de fragmentação** — Android tem centenas de dispositivos com telas, versões de OS e customizações diferentes. Mitigação: test matrix com top 20 dispositivos, Testlab/BrowserStack.
3. **Avaliar risco de impossibilidade de rollback** — App publicada não pode ser "des-publicada" de dispositivos existentes. Versão bugada fica ativa até usuário atualizar. Mitigação: feature flags remotos, remote config, forced update para versões críticas.
4. **Avaliar risco de perda de dados offline** — Dados criados offline podem ser perdidos se app é desinstalada ou device é resetado. Mitigação: sync frequente, warning ao usuário sobre dados não sincronizados.
5. **Avaliar risco de consumo excessivo** — Bateria, dados móveis, armazenamento. App que consome muito é desinstalada. Mitigação: profiling de bateria e dados, otimização lazy.
6. **Avaliar risco de review time** — Apple review pode levar 1-7 dias. Fix urgente não chega ao usuário imediatamente. Mitigação: server-driven UI, feature flags remotos, expedited review para bugs críticos.
7. **Avaliar risco de permissões** — Usuário nega permissão necessária. Feature funciona degradada? Mensagem clara de por que precisa? Timing do pedido de permissão?

## Outputs

- Matriz de riscos mobile
- Compliance checklist para app store
- Test matrix de dispositivos
- Plano de feature flags remotos (remote config)
- Estratégia de forced update para versões críticas
- Plano para cenários de permissão negada
- Profiling de bateria e dados planejado

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| App store compliance | Checklist validado para iOS e Android | Sim |
| Feature flags remotos | Capacidade de desabilitar feature sem nova versão | Sim |
| Device matrix | Top 20 dispositivos definidos para teste | Sim |
| Permissão negada | Comportamento definido para cada permissão negada | Sim |
| Rollback via remote | Feature pode ser desligada remotamente | Sim |

## Próxima Fase

→ [06-tests.md](./06-tests.md) — Testes mobile: dispositivos, conectividade, lifecycle
