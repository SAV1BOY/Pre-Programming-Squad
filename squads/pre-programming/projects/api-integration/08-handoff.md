# Integração de API — Fase 08: Handoff

## Objetivo da Fase

Entregar plano de integração ao time com ênfase em contratos, configuração de resiliência e acesso ao provedor.

## Agentes Envolvidos

- **Agente Coordenador** (líder da fase) — Organiza entrega
- **Agente de Readiness** — Apresenta scorecard e recomendações
- **Agente de Arquitetura** — Detalha arquitetura da camada de integração

## Inputs

- Scorecard de readiness aprovado (Fase 07)
- Todos os artefatos das fases 01-06
- Credenciais e acessos confirmados

## Atividades

1. **Organizar pacote de handoff** — Prioridade em: contratos de API, mapeamento de dados, configuração de circuit breaker e runbook de falhas.
2. **Entregar credenciais** — Sandbox e produção via canal seguro (vault, secrets manager). Nunca por email ou Slack.
3. **Demonstrar sandbox** — Sessão ao vivo com chamadas à API real em sandbox. Mostrar cenários de sucesso e erro.
4. **Revisar runbook operacional** — Walkthrough do runbook de falhas: o que fazer quando API está fora, rate limit atingido, token expirado.
5. **Definir monitoramento day-1** — Dashboard e alertas que devem estar configurados antes do deploy em produção.
6. **Estabelecer canal com provedor** — Garantir que time de dev tem acesso ao suporte do provedor para dúvidas durante implementação.

## Outputs

- Pacote de handoff focado em contratos e resiliência
- Credenciais entregues via canal seguro
- Demonstração de sandbox documentada
- Runbook operacional entregue
- Plano de monitoramento day-1
- Canal com provedor estabelecido

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Credenciais entregues | Via canal seguro, não em plaintext | Sim |
| Sandbox demonstrada | Time viu API funcionar e falhar | Sim |
| Runbook entregue | Procedimentos para cenários de falha documentados | Sim |
| Monitoramento definido | Alertas e dashboards planejados para day-1 | Sim |
| Canal com provedor | Time tem acesso a suporte do provedor | Sim |

## Próxima Fase

→ Implementação pelo time de desenvolvimento.

**Nota:** O Pre-Programming Squad permanece disponível por 3 semanas para integrações com API, dado o risco de descobertas em produção que sandbox não cobriu.
