# Template: Handoff para Implementação

## Título
Implementation Handoff — Pacote de Entrega para o Time de Desenvolvimento

## Propósito
Consolidar todos os artefatos, decisões e informações necessárias para que a equipe de desenvolvimento possa iniciar a implementação com clareza e autonomia.

## Quando Usar
- Quando a fase de pré-programação está concluída e o desenvolvimento vai começar.
- Na transição entre equipes de planejamento e implementação.
- Como documento de referência durante todo o desenvolvimento.

## Seções

### 1. Informações Gerais
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| De | `[equipe/pessoa de pré-programação]` |
| Para | `[equipe/pessoa de desenvolvimento]` |
| Data do Handoff | `[YYYY-MM-DD]` |
| Score de Readiness | `[X/100]` |

### 2. Resumo Executivo
`[Em 3-5 parágrafos, descreva: o que é o projeto, por que estamos fazendo, o que foi decidido na pré-programação e o que se espera do desenvolvimento.]`

### 3. Artefatos Entregues
| Artefato | Link/Localização | Status | Responsável |
|----------|-----------------|--------|-------------|
| Project Brief | `[link]` | `[Completo/Parcial]` | `[nome]` |
| Requisitos | `[link]` | `[Completo/Parcial]` | `[nome]` |
| Arquitetura | `[link]` | `[Completo/Parcial]` | `[nome]` |
| Contratos de API | `[link]` | `[Completo/Parcial]` | `[nome]` |
| Modelo de Dados | `[link]` | `[Completo/Parcial]` | `[nome]` |
| Estratégia de Testes | `[link]` | `[Completo/Parcial]` | `[nome]` |
| Registro de Riscos | `[link]` | `[Completo/Parcial]` | `[nome]` |
| Decisões Técnicas | `[link]` | `[Completo/Parcial]` | `[nome]` |

### 4. Decisões Importantes para o Dev
| Decisão | Contexto Resumido | Link do Memo |
|---------|-------------------|-------------|
| `[decisão]` | `[por que importa para o dev]` | `[link]` |

### 5. Backlog Inicial Sugerido
| Sprint | Itens | Prioridade | Estimativa |
|--------|-------|-----------|-----------|
| Sprint 1 | `[itens de trabalho]` | `[Must]` | `[pontos/dias]` |
| Sprint 2 | `[itens de trabalho]` | `[Must/Should]` | `[pontos/dias]` |

### 6. Pontos de Atenção
| Ponto | Contexto | Recomendação |
|-------|----------|-------------|
| `[área que requer cuidado]` | `[por quê]` | `[o que fazer]` |

### 7. Premissas Não Validadas
| Premissa | Impacto se Falsa | Ação do Dev |
|----------|-------------------|------------|
| `[premissa]` | `[consequência]` | `[o que o dev deve fazer se descobrir que é falsa]` |

### 8. Contatos e Canais
| Assunto | Contato | Canal |
|---------|---------|-------|
| Dúvidas de requisito | `[nome]` | `[Slack/email]` |
| Dúvidas de arquitetura | `[nome]` | `[Slack/email]` |
| Dúvidas de negócio | `[nome]` | `[Slack/email]` |
| Escalações | `[nome]` | `[Slack/email]` |

### 9. Sessão de Handoff
| Campo | Valor |
|-------|-------|
| Data/Hora | `[data e hora]` |
| Participantes | `[lista]` |
| Duração | `[tempo]` |
| Gravação | `[link, se gravada]` |

## Exemplo de Preenchimento

### 6. Pontos de Atenção
| Ponto | Contexto | Recomendação |
|-------|----------|-------------|
| API do parceiro instável | Nos testes, apresentou timeout 3% das vezes | Implementar circuit breaker desde o início |
| Schema do banco legado | Tabela `orders` tem 47 colunas sem documentação | Alinhar com equipe legado antes de criar integrações |
| Performance da listagem | Endpoint de listagem com filtros pode ser lento com >100k registros | Planejar paginação por cursor e cache desde o sprint 1 |

## Dicas de Qualidade
- **Faça uma sessão presencial (ou remota):** O documento complementa a conversa, não a substitui.
- **Esteja disponível após o handoff:** O time de dev terá dúvidas. Planeje 1-2 semanas de suporte.
- **Não entregue tudo de uma vez:** Priorize o que o dev precisa para a sprint 1.
- **Destaque o que NÃO está decidido:** Clareza sobre o que falta é tão importante quanto o que está pronto.
- **Colete feedback:** Pergunte ao time de dev se o handoff foi suficiente e o que faltou.
