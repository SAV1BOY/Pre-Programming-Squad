# Modelo Operacional — Pre-Programming Squad

## Propósito

Descrever como o Pre-Programming Squad opera no dia-a-dia: ritmo de trabalho, cerimônias, fluxo de projetos, interações com outros squads e mecanismos de feedback.

## Escopo

Aplica-se a todas as atividades recorrentes do squad e à interação com stakeholders internos e externos ao squad.

## Definições

| Termo | Definição |
|---|---|
| Ciclo | Período de trabalho do squad (2 semanas, alinhado com sprints da organização) |
| Pipeline | Fila de projetos em diferentes estágios de preparação |
| WIP Limit | Limite de projetos em andamento simultâneo por membro do squad |
| Throughput | Número de projetos que completam a pipeline por ciclo |

## Processo

### Fluxo de Trabalho

```
Intake → Triagem → Discovery → Scoping → Revisões → Estimativa → Handoff → Retro
```

Cada projeto percorre a pipeline da esquerda para a direita. Nem todos os projetos passam por todas as etapas — projetos simples podem pular etapas conforme critérios de triagem.

### Classificação de Projetos

| Tamanho | Critério | Etapas | Tempo Típico |
|---|---|---|---|
| P (Pequeno) | Escopo contido, sem dependência externa, tecnologia conhecida | Intake → Scoping → Handoff | 2-3 dias |
| M (Médio) | Escopo moderado, 1-2 dependências, pode envolver decisão arquitetural | Intake → Discovery → Scoping → Revisão → Handoff | 1-2 semanas |
| G (Grande) | Escopo amplo, múltiplas dependências, decisão arquitetural significativa | Pipeline completa | 2-4 semanas |
| XG (Extra-grande) | Cross-organization, mudança de plataforma, alto risco | Pipeline completa + revisões adicionais | 4-8 semanas |

### Limites de WIP

- **Por membro:** Máximo 2 projetos simultâneos (1 ativo + 1 aguardando input)
- **Por squad:** Máximo de 6 projetos simultâneos no total
- **Regra de ouro:** Se tudo é prioridade, nada é prioridade. Novos projetos entram na fila se WIP estiver no limite.

### Cerimônias

| Cerimônia | Frequência | Duração | Participantes | Propósito |
|---|---|---|---|---|
| Daily Sync | Diária | 15 min | Squad completo | Bloqueios, progresso, priorização do dia |
| Pipeline Review | 2x/semana (seg, qua) | 30 min | Squad + stakeholders | Status de todos os projetos na pipeline |
| Deep Work Blocks | Diária | 3-4h | Individual | Tempo protegido para análise e documentação |
| Revisão entre Pares | Sob demanda | 30-60 min | 2+ membros | Revisão de entregáveis antes de handoff |
| Retrospectiva (RalphLoop) | A cada ciclo | 60 min | Squad completo | Melhoria contínua do processo |
| Office Hours | 1x/semana (qui) | 60 min | Squad + qualquer pessoa | Consultas, dúvidas, orientação técnica |

### Interação com Outros Squads

**Entrada de trabalho:**
- Projetos entram via formulário de intake (standard de intake)
- PM ou Tech Lead do squad solicitante preenche o intake
- Triagem em até 24h úteis com priorização definida

**Saída de trabalho:**
- Handoff formal com checklist de aceitação pelo squad receptor
- Período de suporte pós-handoff de 2 semanas
- Feedback estruturado coletado 2 semanas após início da implementação

**Comunicação:**
- Canal Slack: #pre-programming-squad (comunicação geral)
- Canal Slack: #pre-prog-handoffs (handoffs e entregas)
- Reuniões: agenda compartilhada com slots bookáveis

### Métricas Operacionais

| Métrica | Meta | Medição |
|---|---|---|
| Lead time (intake → handoff) | ≤ tempo target por tamanho | Jira/Tracker |
| Throughput | ≥ 4 projetos P/M por ciclo | Jira/Tracker |
| Taxa de rejeição no handoff | < 10% | Feedback do squad receptor |
| Retrabalho pós-handoff | < 5% dos itens | Tickets de esclarecimento |
| Satisfação do squad receptor | ≥ 8/10 | Survey pós-handoff |
| WIP | Dentro do limite | Daily review |

## Critérios de Qualidade

- Pipeline visível e atualizada para todos os stakeholders
- Nenhum projeto parado por mais de 3 dias sem ação documentada
- Todas as cerimônias acontecem no horário com agenda clara
- Métricas revisadas a cada ciclo na retrospectiva
- Bloqueios escalados em até 24h

## Responsáveis

| Papel | Responsabilidade no Modelo Operacional |
|---|---|
| Tech Lead | Priorização da pipeline, facilitação de cerimônias, resolução de conflitos |
| Membros | Atualização diária de status, cumprimento de WIP limits, revisão entre pares |
| EM | Remoção de bloqueios organizacionais, alocação de capacidade |
| Stakeholders | Resposta a pedidos de input em até 48h, participação em reviews |

## Referências

- Carta do Squad: `docs/squad-charter.md`
- Standard de Intake: `docs/project-intake-standard.md`
- Standard de Handoff: `docs/handoff-standard.md`
- Standard de Retrospectiva: `docs/ralphloop-retro-standard.md`
