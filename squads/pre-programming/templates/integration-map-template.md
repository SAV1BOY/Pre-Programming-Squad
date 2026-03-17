# Template: Mapa de Integrações

## Título
Integration Map — Mapeamento de Integrações e Dependências Externas

## Propósito
Documentar todas as integrações do sistema com serviços externos, APIs de terceiros e sistemas internos, incluindo protocolos, dependências e planos de contingência.

## Quando Usar
- Durante o design da arquitetura, para mapear dependências externas.
- Quando o sistema precisa se comunicar com APIs ou serviços de terceiros.
- Para avaliar riscos de dependências e definir estratégias de resiliência.

## Seções

### 1. Informações Gerais
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| Responsável | `[nome]` |
| Data | `[YYYY-MM-DD]` |
| Total de Integrações | `[número]` |

### 2. Visão Geral das Integrações
```
                    ┌──────────────┐
                    │  Sistema X   │
                    └──────┬───────┘
                           │
┌──────────┐    ┌──────────▼──────────┐    ┌──────────┐
│ Serviço A│◄───│   Nosso Sistema     │───▶│ Serviço B│
└──────────┘    └──────────┬──────────┘    └──────────┘
                           │
                    ┌──────▼───────┐
                    │  Serviço C   │
                    └──────────────┘
```

### 3. Detalhamento por Integração

#### Integração 1: `[Nome do Sistema/Serviço]`
| Campo | Valor |
|-------|-------|
| Sistema/Serviço | `[nome]` |
| Tipo | `[Interno/Externo/Terceiro]` |
| Protocolo | `[REST/SOAP/gRPC/Webhook/Arquivo/Fila]` |
| Direção | `[Entrada/Saída/Bidirecional]` |
| Frequência | `[Real-time/Batch/Sob demanda]` |
| Volumetria | `[requests/dia ou registros/execução]` |
| SLA do Parceiro | `[uptime/latência garantidos]` |
| Autenticação | `[método]` |
| Responsável Técnico | `[nome/equipe]` |
| Documentação | `[link]` |

**Dados Trocados:**
| Dado | Direção | Formato | Sensível? |
|------|---------|---------|-----------|
| `[dado]` | `[envia/recebe]` | `[JSON/XML/CSV]` | `[Sim/Não]` |

**Tratamento de Falhas:**
| Cenário de Falha | Estratégia | Timeout | Retries |
|-------------------|-----------|---------|---------|
| `[cenário]` | `[circuit breaker/fallback/retry]` | `[ms]` | `[quantidade]` |

### 4. Matriz de Criticidade
| Integração | Criticidade | Pode Funcionar Offline? | Fallback |
|------------|------------|------------------------|----------|
| `[nome]` | `[Alta/Média/Baixa]` | `[Sim/Não]` | `[estratégia]` |

### 5. Ambientes e Configuração
| Integração | Dev | Staging | Prod | Sandbox Disponível? |
|------------|-----|---------|------|---------------------|
| `[nome]` | `[URL/config]` | `[URL/config]` | `[URL/config]` | `[Sim/Não]` |

### 6. Cronograma de Disponibilidade
| Integração | Ação Necessária | Responsável | Prazo | Status |
|------------|----------------|-------------|-------|--------|
| `[nome]` | `[solicitar acesso/configurar ambiente]` | `[nome]` | `[data]` | `[status]` |

## Exemplo de Preenchimento

### 3. Detalhamento
#### Integração 1: Gateway de Pagamento (Stripe)
| Campo | Valor |
|-------|-------|
| Sistema/Serviço | Stripe |
| Tipo | Externo/Terceiro |
| Protocolo | REST + Webhooks |
| Direção | Bidirecional |
| Frequência | Real-time |
| Volumetria | ~5.000 transações/dia |
| SLA do Parceiro | 99.99% uptime |
| Autenticação | API Key + Webhook Secret |

## Dicas de Qualidade
- **Mapeie tudo:** Inclua até integrações "simples" como envio de email.
- **Teste em sandbox primeiro:** Nunca integre direto em produção.
- **Documente falhas:** Toda integração vai falhar. Planeje para isso.
- **Monitore dependências:** Integrações são a principal fonte de incidentes.
- **Revise SLAs:** O SLA do seu sistema é limitado pelo SLA da integração mais fraca.
