# Template: Revisão de Prontidão

## Título
Readiness Review — Avaliação de Prontidão para Desenvolvimento

## Propósito
Avaliar se o projeto está pronto para entrar na fase de desenvolvimento, verificando que todos os artefatos, decisões e condições necessárias estão atendidos.

## Quando Usar
- Antes de iniciar a fase de implementação.
- Como gate de qualidade entre pré-programação e desenvolvimento.
- Em revisões periódicas para projetos longos.

## Seções

### 1. Informações Gerais
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| Avaliador | `[nome]` |
| Data | `[YYYY-MM-DD]` |
| Score de Prontidão | `[X/100]` |
| Resultado | `[Pronto / Pronto com ressalvas / Não pronto]` |

### 2. Checklist de Prontidão

#### Clareza de Requisitos (0-20 pontos)
| Critério | Atendido? | Pontos | Evidência |
|----------|----------|--------|-----------|
| Requisitos funcionais documentados e aprovados | `[Sim/Parcial/Não]` | `[0-5]` | `[link]` |
| Requisitos não-funcionais definidos com métricas | `[Sim/Parcial/Não]` | `[0-5]` | `[link]` |
| Critérios de aceite escritos e testáveis | `[Sim/Parcial/Não]` | `[0-5]` | `[link]` |
| Perguntas em aberto resolvidas | `[Sim/Parcial/Não]` | `[0-5]` | `[link]` |

#### Arquitetura e Design (0-20 pontos)
| Critério | Atendido? | Pontos | Evidência |
|----------|----------|--------|-----------|
| Arquitetura documentada e revisada | `[Sim/Parcial/Não]` | `[0-5]` | `[link]` |
| Contratos de API definidos | `[Sim/Parcial/Não]` | `[0-5]` | `[link]` |
| Modelo de dados definido | `[Sim/Parcial/Não]` | `[0-5]` | `[link]` |
| Decisões técnicas documentadas | `[Sim/Parcial/Não]` | `[0-5]` | `[link]` |

#### Riscos e Qualidade (0-20 pontos)
| Critério | Atendido? | Pontos | Evidência |
|----------|----------|--------|-----------|
| Riscos identificados com plano de mitigação | `[Sim/Parcial/Não]` | `[0-5]` | `[link]` |
| Estratégia de testes definida | `[Sim/Parcial/Não]` | `[0-5]` | `[link]` |
| Revisão de segurança realizada | `[Sim/Parcial/Não]` | `[0-5]` | `[link]` |
| Definition of Done acordada | `[Sim/Parcial/Não]` | `[0-5]` | `[link]` |

#### Infraestrutura e Ambiente (0-20 pontos)
| Critério | Atendido? | Pontos | Evidência |
|----------|----------|--------|-----------|
| Ambientes de desenvolvimento prontos | `[Sim/Parcial/Não]` | `[0-5]` | `[link]` |
| CI/CD configurado | `[Sim/Parcial/Não]` | `[0-5]` | `[link]` |
| Acessos concedidos à equipe | `[Sim/Parcial/Não]` | `[0-5]` | `[link]` |
| Monitoramento planejado | `[Sim/Parcial/Não]` | `[0-5]` | `[link]` |

#### Alinhamento e Planejamento (0-20 pontos)
| Critério | Atendido? | Pontos | Evidência |
|----------|----------|--------|-----------|
| Stakeholders alinhados e aprovaram escopo | `[Sim/Parcial/Não]` | `[0-5]` | `[link]` |
| Estimativas revisadas pela equipe de dev | `[Sim/Parcial/Não]` | `[0-5]` | `[link]` |
| Equipe alocada e disponível | `[Sim/Parcial/Não]` | `[0-5]` | `[link]` |
| Plano de rollout e rollback definidos | `[Sim/Parcial/Não]` | `[0-5]` | `[link]` |

### 3. Itens Pendentes
| Item | Impacto | Responsável | Prazo | Bloqueante? |
|------|---------|-------------|-------|------------|
| `[item pendente]` | `[como afeta o desenvolvimento]` | `[nome]` | `[data]` | `[Sim/Não]` |

### 4. Recomendação
`[Recomendação do avaliador com justificativa.]`

### 5. Assinaturas
| Nome | Papel | Concordância | Data |
|------|-------|-------------|------|
| `[nome]` | `[papel]` | `[Concordo/Discordo]` | `[data]` |

## Exemplo de Preenchimento

### 1. Informações Gerais
| Campo | Valor |
|-------|-------|
| Projeto | Portal de Autoatendimento |
| Score de Prontidão | 78/100 |
| Resultado | Pronto com ressalvas |

### 4. Recomendação
O projeto está substancialmente pronto para desenvolvimento. Os 22 pontos faltantes referem-se a: (1) falta de sandbox do parceiro de pagamento (5 pts) — não bloqueante para sprint 1; (2) monitoramento ainda não configurado (5 pts) — pode ser feito em paralelo; (3) estimativa do módulo de relatórios não revisada (5 pts) — não está na sprint 1. Recomendação: iniciar desenvolvimento com sprint 1 focada em autenticação e CRUD básico.

## Dicas de Qualidade
- **Seja honesto no score:** Um score inflado causa problemas depois.
- **Diferencie bloqueante de não-bloqueante:** Nem todo item pendente impede o início.
- **Documente ressalvas:** "Pronto com ressalvas" exige que as ressalvas estejam claras.
- **Revise com a equipe de dev:** Eles sabem melhor o que precisam para começar.
- **Use como checkpoint, não como burocracia:** O objetivo é garantir qualidade, não criar papelada.
