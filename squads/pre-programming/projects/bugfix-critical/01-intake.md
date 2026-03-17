# Bugfix Crítico — Fase 01: Intake

## Objetivo da Fase

Receber e triagear o bug crítico com urgência, classificar severidade, identificar blast radius inicial e acionar os agentes corretos em modo fast-track.

## Agentes Envolvidos

- **Agente de Riscos** (líder da fase) — Avalia severidade e blast radius imediato
- **Agente Coordenador** — Ativa protocolo de urgência e comunica stakeholders

## Inputs

- Relato do bug (ticket, alerta de monitoramento, report de cliente)
- Logs e métricas de observabilidade relacionados
- Informações de impacto (usuários afetados, receita impactada, SLA violado)
- Timestamp de início do problema

## Atividades

1. **Classificar severidade** — Sev1 (sistema fora do ar), Sev2 (funcionalidade crítica degradada), Sev3 (funcionalidade secundária com workaround). Cada nível tem SLA de resolução diferente.
2. **Determinar blast radius atual** — Quantos usuários são afetados? Qual funcionalidade? Há impacto financeiro? Dados estão em risco?
3. **Verificar se há mitigação imediata** — Feature flag para desabilitar? Rollback de deploy recente? Workaround manual para usuários?
4. **Coletar evidências** — Logs, stack traces, métricas de antes e depois do problema. Preservar estado para investigação.
5. **Identificar time responsável** — Qual time ou dev tem contexto sobre o componente afetado?
6. **Comunicar stakeholders** — Notificar PM, suporte ao cliente e liderança conforme severidade.

## Outputs

- Classificação de severidade com justificativa
- Blast radius quantificado (usuários, funcionalidade, receita)
- Mitigação imediata aplicada (se disponível)
- Evidências coletadas e preservadas
- War room ativada (para Sev1/Sev2)

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Severidade classificada | Sev1/Sev2/Sev3 com critérios objetivos | Sim |
| Blast radius quantificado | Número de usuários e funcionalidades afetadas | Sim |
| Mitigação avaliada | Feature flag ou rollback tentado/descartado com motivo | Sim |
| Evidências preservadas | Logs e métricas salvos antes de qualquer intervenção | Sim |

**SLA:** Intake de bugfix crítico (Sev1) deve ser concluído em **30 minutos**.

## Próxima Fase

→ [02-discovery.md](./02-discovery.md) — Investigação da causa raiz do bug
