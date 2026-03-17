# Modo Conciso

## Nível de Detalhe

Mínimo necessário para ação. Apenas conclusões, decisões e próximos passos. Sem contexto histórico, sem análise intermediária, sem justificativas extensas. Cada bullet é uma unidade de informação completa e acionável.

**Proporção alvo:** 80% conclusão, 20% contexto essencial.

## Quando Usar

- **Atualizações de status** em standups ou check-ins rápidos
- **Respostas em threads** do Slack/Teams onde o contexto já existe
- **Resumos executivos** para quem já conhece o projeto
- **Decisões já tomadas** — comunicar o resultado, não o processo
- **Bloqueios e escalações** — ir direto ao ponto para desbloquear rápido
- **Checklists operacionais** — passos a executar sem margem para interpretação

**Não usar quando:**
- A audiência não tem contexto prévio
- A decisão é controversa e precisa de justificativa
- O tema envolve trade-offs que precisam ser entendidos
- É a primeira vez que o assunto é apresentado

## Extensão Esperada

- **Atualizações de status:** 3-5 bullets, máximo 1 parágrafo introdutório
- **Decisões:** 1 frase de contexto + decisão + 1-3 implicações
- **Bloqueios:** O quê + impacto + o que precisa de quem até quando
- **Total:** Raramente excede 10 linhas

## Exemplo

```
## Status Migração de Pagamentos — 10/mar

- ✅ Fase 1 (cartão) em produção, zero incidentes em 14 dias
- 🔶 Fase 2 (PIX) atrasada 2 semanas — SDK do parceiro ainda não entregue
- 🔴 Bloqueio: contrato do gateway atual expira 30/abr; sem Fase 2,
  multa de R$ 45k
- **Decisão necessária:** aprovar plano B (dual-run, +R$ 15k) até sexta
- **Owner:** @maria.silva | **Próximo check-in:** quinta 14h
```

```
## Decisão: Banco para serviço de auditoria

PostgreSQL. Motivo: equipe já opera, volume cabe, não justifica
tecnologia nova. DynamoDB descartado por custo desproporcional
para o volume esperado (< 1M registros/mês).

Implicações:
- Usar particionamento por mês desde o início
- Incluir índice em (entity_type, timestamp)
- Retenção de 12 meses na tabela principal, depois S3
```
