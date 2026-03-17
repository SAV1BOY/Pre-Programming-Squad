# Template: Esboço de Arquitetura

## Título
Architecture Sketch — Esboço Arquitetural de Alto Nível

## Propósito
Registrar as decisões arquiteturais iniciais em nível de componentes, comunicação e infraestrutura, servindo como base para discussão e refinamento antes da implementação.

## Quando Usar
- Após definição de escopo e escolha da solução.
- Para alinhar a equipe sobre a estrutura técnica proposta.
- Antes de definir contratos de API e modelo de dados detalhado.

## Seções

### 1. Informações Gerais
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| Arquiteto Responsável | `[nome]` |
| Data | `[YYYY-MM-DD]` |
| Versão | `[v1.0]` |
| Status | `[Rascunho / Em Revisão / Aprovado]` |

### 2. Visão Geral da Arquitetura
`[Descrição textual da arquitetura em 3-5 parágrafos. Explique o estilo arquitetural escolhido e a justificativa.]`

### 3. Diagrama de Componentes
```
[Diagrama ASCII ou referência a arquivo de imagem]

┌──────────┐     ┌──────────┐     ┌──────────┐
│ Frontend │────▶│   API    │────▶│   DB     │
│  (React) │     │ Gateway  │     │ (Postgres)│
└──────────┘     └────┬─────┘     └──────────┘
                      │
                 ┌────▼─────┐
                 │ Service A │
                 └──────────┘
```

### 4. Componentes Principais
| Componente | Responsabilidade | Tecnologia | Proprietário |
|------------|-----------------|------------|-------------|
| `[nome]` | `[o que faz]` | `[stack]` | `[equipe]` |

### 5. Fluxos de Comunicação
| Origem | Destino | Protocolo | Padrão | Dados |
|--------|---------|-----------|--------|-------|
| `[componente]` | `[componente]` | `[HTTP/gRPC/Evento]` | `[Sync/Async]` | `[o que trafega]` |

### 6. Decisões Arquiteturais (ADRs Resumidas)
| Decisão | Alternativa Rejeitada | Justificativa |
|---------|----------------------|---------------|
| `[decisão tomada]` | `[o que foi descartado]` | `[por quê]` |

### 7. Requisitos Não-Funcionais Endereçados
| Requisito | Como a Arquitetura Atende |
|-----------|--------------------------|
| `[performance]` | `[estratégia adotada]` |
| `[segurança]` | `[estratégia adotada]` |
| `[escalabilidade]` | `[estratégia adotada]` |

### 8. Infraestrutura
| Ambiente | Provedor | Serviços | Estimativa de Custo |
|----------|----------|----------|---------------------|
| `[Prod/Staging/Dev]` | `[AWS/GCP/Azure/On-prem]` | `[serviços utilizados]` | `[custo mensal]` |

### 9. Pontos de Atenção e Riscos Técnicos
- `[Risco ou ponto que precisa de investigação adicional]`

### 10. Próximos Passos
- `[Ação necessária para evoluir a arquitetura]`

## Exemplo de Preenchimento

### 4. Componentes Principais
| Componente | Responsabilidade | Tecnologia | Proprietário |
|------------|-----------------|------------|-------------|
| Web App | Interface do usuário | React 18 + TypeScript | Equipe Frontend |
| API Gateway | Roteamento e autenticação | Kong | Equipe Plataforma |
| Order Service | Gestão de pedidos | Node.js + Express | Equipe Backend |
| Notification Service | Envio de emails e push | Python + Celery | Equipe Backend |
| PostgreSQL | Persistência principal | PostgreSQL 15 | Equipe DBA |
| Redis | Cache e sessões | Redis 7 | Equipe Plataforma |

## Dicas de Qualidade
- **Comece simples:** Um esboço não precisa de todos os detalhes. O objetivo é comunicar a ideia.
- **Justifique decisões:** Cada escolha tecnológica deve ter uma razão documentada.
- **Pense em falhas:** A arquitetura deve considerar o que acontece quando algo falha.
- **Revise com a equipe:** Arquitetura feita por uma pessoa é cega aos próprios vieses.
- **Itere:** O primeiro esboço raramente é o final. Versione e evolua.
