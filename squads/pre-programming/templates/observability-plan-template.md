# Template: Plano de Observabilidade

## Título
Observability Plan — Estratégia de Monitoramento, Logging e Rastreamento

## Propósito
Definir como o sistema será monitorado, quais métricas serão coletadas, como logs serão estruturados e como rastrear problemas em ambientes distribuídos.

## Quando Usar
- Durante o design da arquitetura.
- Antes de iniciar a implementação.
- Ao preparar o sistema para produção.

## Seções

### 1. Informações Gerais
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| Responsável | `[nome]` |
| Data | `[YYYY-MM-DD]` |
| Stack de Observabilidade | `[Datadog/Grafana/New Relic/etc.]` |

### 2. Métricas (Metrics)
#### Métricas de Negócio
| Métrica | Descrição | Fonte | Dashboard | Alerta |
|---------|-----------|-------|-----------|--------|
| `[ex: pedidos/minuto]` | `[o que mede]` | `[de onde vem]` | `[link]` | `[threshold]` |

#### Métricas de Infraestrutura
| Métrica | Valor Normal | Alerta | Crítico |
|---------|-------------|--------|---------|
| CPU | `[< 70%]` | `[> 80%]` | `[> 95%]` |
| Memória | `[< 75%]` | `[> 85%]` | `[> 95%]` |
| Disco | `[< 70%]` | `[> 80%]` | `[> 90%]` |

#### Métricas de Aplicação (RED/USE)
| Métrica | Valor Alvo | Alerta | Crítico |
|---------|-----------|--------|---------|
| Rate (requests/s) | `[valor]` | `[threshold]` | `[threshold]` |
| Errors (% de erro) | `[< 0.1%]` | `[> 1%]` | `[> 5%]` |
| Duration (latência p99) | `[< 500ms]` | `[> 1s]` | `[> 3s]` |

### 3. Logs (Logging)
| Componente | Nível | Formato | Destino | Retenção |
|------------|-------|---------|---------|----------|
| `[componente]` | `[INFO/WARN/ERROR]` | `[JSON estruturado]` | `[CloudWatch/ELK/etc.]` | `[dias]` |

**Campos obrigatórios no log:**
- `timestamp`, `level`, `service`, `trace_id`, `message`
- `[campos adicionais específicos do projeto]`

### 4. Rastreamento Distribuído (Tracing)
| Ferramenta | Protocolo | Serviços Instrumentados |
|-----------|-----------|------------------------|
| `[Jaeger/Zipkin/OpenTelemetry]` | `[W3C Trace Context/B3]` | `[lista de serviços]` |

### 5. Alertas
| Alerta | Condição | Severidade | Canal | Quem é Notificado | Ação Esperada |
|--------|----------|-----------|-------|-------------------|---------------|
| `[nome]` | `[condição]` | `[P1/P2/P3/P4]` | `[PagerDuty/Slack/Email]` | `[equipe/pessoa]` | `[o que fazer]` |

### 6. Dashboards
| Dashboard | Público | Métricas Incluídas | Link |
|-----------|---------|-------------------|------|
| `[nome]` | `[equipe/gestão/todos]` | `[métricas]` | `[URL]` |

### 7. SLIs e SLOs
| Serviço | SLI | SLO | Janela | Error Budget |
|---------|-----|-----|--------|-------------|
| `[serviço]` | `[indicador]` | `[objetivo]` | `[30d]` | `[budget restante]` |

## Exemplo de Preenchimento

### 5. Alertas
| Alerta | Condição | Severidade | Canal | Quem | Ação |
|--------|----------|-----------|-------|------|------|
| Alta taxa de erros | Error rate > 5% por 5 min | P1 | PagerDuty + Slack #incidents | SRE de plantão | Verificar logs, considerar rollback |
| Latência degradada | p99 > 2s por 10 min | P2 | Slack #alerts | Equipe backend | Investigar queries lentas e dependências |
| Disco quase cheio | Uso > 85% | P3 | Slack #infra | DevOps | Limpar logs antigos ou expandir volume |

## Dicas de Qualidade
- **Observabilidade desde o dia 1:** Não deixe para adicionar monitoramento depois do deploy.
- **Alertas acionáveis:** Todo alerta deve ter uma ação clara. Alertas ignorados são ruído.
- **Logs estruturados:** JSON com campos padronizados facilita busca e correlação.
- **Defina SLOs:** Sem SLOs, não há como saber se o sistema está "saudável".
- **Dashboards para cada público:** Engenharia quer detalhes técnicos; gestão quer métricas de negócio.
