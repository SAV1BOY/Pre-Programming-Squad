# Template: Plano de Rollout

## Título
Rollout Plan — Plano de Implantação Gradual

## Propósito
Definir a estratégia de implantação do sistema em produção, incluindo etapas, critérios de avanço, monitoramento e comunicação, minimizando riscos de impacto negativo.

## Quando Usar
- Antes de qualquer deploy em produção.
- Quando a funcionalidade afeta muitos usuários.
- Para coordenar releases complexos com múltiplas dependências.

## Seções

### 1. Informações Gerais
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| Release | `[versão]` |
| Data Planejada | `[YYYY-MM-DD]` |
| Responsável pelo Rollout | `[nome]` |
| Janela de Deploy | `[horário e duração]` |

### 2. Estratégia de Rollout
- **Tipo:** `[Big Bang / Canary / Blue-Green / Feature Flag / Rolling]`
- **Justificativa:** `[por que esta estratégia]`
- **Duração Total Estimada:** `[tempo]`

### 3. Etapas do Rollout
| Etapa | Público | % de Tráfego | Duração | Critério de Avanço | Critério de Rollback |
|-------|---------|-------------|---------|--------------------|--------------------|
| 1 | `[grupo interno]` | `[1%]` | `[X horas]` | `[métricas OK]` | `[métricas NOK]` |
| 2 | `[early adopters]` | `[10%]` | `[X horas]` | `[métricas OK]` | `[métricas NOK]` |
| 3 | `[todos]` | `[100%]` | `[estável]` | `[métricas OK]` | `[métricas NOK]` |

### 4. Pré-requisitos do Rollout
- [ ] Todas as migrations executadas em staging com sucesso
- [ ] Testes E2E passando em staging
- [ ] Plano de rollback testado
- [ ] Monitoramento e alertas configurados
- [ ] Equipe de plantão escalada
- [ ] Comunicação enviada aos stakeholders
- [ ] `[pré-requisito adicional]`

### 5. Métricas de Monitoramento
| Métrica | Valor Normal | Threshold de Alerta | Threshold de Rollback |
|---------|-------------|---------------------|----------------------|
| `[error rate]` | `[< 0.1%]` | `[> 1%]` | `[> 5%]` |
| `[latência p99]` | `[< 500ms]` | `[> 1000ms]` | `[> 3000ms]` |
| `[disponibilidade]` | `[> 99.9%]` | `[< 99.5%]` | `[< 99%]` |

### 6. Plano de Comunicação
| Quando | Público | Canal | Mensagem |
|--------|---------|-------|----------|
| Antes do rollout | `[stakeholders]` | `[email/Slack]` | `[informar sobre o deploy]` |
| Durante | `[equipe técnica]` | `[Slack/war room]` | `[status updates]` |
| Após conclusão | `[todos]` | `[email]` | `[confirmação de sucesso]` |

### 7. Equipe de Plantão
| Papel | Nome | Contato | Disponibilidade |
|-------|------|---------|----------------|
| `[Líder do rollout]` | `[nome]` | `[telefone/Slack]` | `[horário]` |
| `[DBA de plantão]` | `[nome]` | `[telefone/Slack]` | `[horário]` |
| `[SRE de plantão]` | `[nome]` | `[telefone/Slack]` | `[horário]` |

## Exemplo de Preenchimento

### 3. Etapas do Rollout
| Etapa | Público | % Tráfego | Duração | Critério de Avanço | Critério de Rollback |
|-------|---------|-----------|---------|--------------------|--------------------|
| 1 | Equipe interna | 1% | 2h | Error rate < 0.1%, latência p99 < 500ms | Qualquer erro 5xx acima de 1% |
| 2 | Usuários beta | 10% | 24h | Métricas estáveis, zero bugs críticos | Error rate > 2% ou bug bloqueante |
| 3 | Todos os usuários | 100% | Indefinido | Métricas estáveis por 48h | Degradação significativa |

## Dicas de Qualidade
- **Nunca faça rollout na sexta-feira:** Problemas em produção no fim de semana são piores.
- **Monitore ativamente:** Não faça deploy e vá embora. Observe as métricas.
- **Defina rollback antes:** O plano de rollback deve estar pronto antes do rollout começar.
- **Comunique sempre:** Stakeholders e equipe devem saber o que está acontecendo.
- **Comece pequeno:** Canary e feature flags reduzem o raio de explosão de problemas.
