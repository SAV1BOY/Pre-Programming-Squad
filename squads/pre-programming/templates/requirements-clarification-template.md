# Template: Clarificação de Requisitos

## Título
Requirements Clarification — Refinamento e Validação de Requisitos

## Propósito
Estruturar o processo de clarificação de requisitos ambíguos, incompletos ou contraditórios, garantindo que todas as partes tenham o mesmo entendimento antes de avançar.

## Quando Usar
- Quando requisitos recebidos estão vagos ou incompletos.
- Quando há conflito entre requisitos de diferentes stakeholders.
- Antes de definir escopo ou iniciar arquitetura.

## Seções

### 1. Informações do Requisito
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| Requisito Original | `[transcrição literal do requisito como recebido]` |
| Fonte | `[quem forneceu o requisito]` |
| Data de Recebimento | `[YYYY-MM-DD]` |
| Responsável pela Clarificação | `[nome]` |

### 2. Análise de Ambiguidades
| Trecho Ambíguo | Interpretação A | Interpretação B | Impacto da Diferença |
|----------------|-----------------|-----------------|---------------------|
| `[trecho]` | `[interpretação]` | `[interpretação]` | `[como muda o escopo/esforço]` |

### 3. Perguntas de Clarificação
| # | Pergunta | Resposta | Respondido Por | Data |
|---|----------|----------|----------------|------|
| 1 | `[pergunta específica]` | `[resposta ou pendente]` | `[nome]` | `[data]` |
| 2 | `[pergunta específica]` | `[resposta ou pendente]` | `[nome]` | `[data]` |

### 4. Requisitos Funcionais Refinados
| ID | Requisito | Prioridade | Critério de Aceite |
|----|-----------|------------|-------------------|
| RF-01 | `[requisito claro e testável]` | `[Must/Should/Could/Won't]` | `[como validar]` |

### 5. Requisitos Não-Funcionais
| ID | Requisito | Métrica | Valor Alvo |
|----|-----------|---------|-----------|
| RNF-01 | `[performance, segurança, etc.]` | `[unidade de medida]` | `[valor esperado]` |

### 6. Regras de Negócio
| ID | Regra | Exceções | Validado Com |
|----|-------|----------|-------------|
| RN-01 | `[regra de negócio]` | `[exceções conhecidas]` | `[stakeholder]` |

### 7. Dependências Identificadas
- `[Dependência de outro sistema, equipe ou decisão]`

### 8. Requisitos Descartados ou Adiados
| Requisito | Motivo | Decisão |
|-----------|--------|---------|
| `[requisito]` | `[por que foi descartado/adiado]` | `[Descartado/Fase 2/Backlog]` |

### 9. Aprovação
| Stakeholder | Concordância | Data |
|-------------|-------------|------|
| `[nome]` | `[Sim/Não/Pendente]` | `[data]` |

## Exemplo de Preenchimento

### 2. Análise de Ambiguidades
| Trecho Ambíguo | Interpretação A | Interpretação B | Impacto da Diferença |
|----------------|-----------------|-----------------|---------------------|
| "O sistema deve ser rápido" | Resposta em menos de 1s | Resposta em menos de 200ms | Arquitetura de cache vs. sem cache — 2 semanas de diferença |
| "Suportar múltiplos idiomas" | Interface bilíngue (PT/EN) | Suporte a 15 idiomas com i18n completo | Esforço de 1 semana vs. 6 semanas |

### 4. Requisitos Funcionais Refinados
| ID | Requisito | Prioridade | Critério de Aceite |
|----|-----------|------------|-------------------|
| RF-01 | O usuário deve conseguir filtrar pedidos por data, status e valor | Must | Filtros combinados retornam resultados em menos de 2s para até 10.000 registros |

## Dicas de Qualidade
- **Nunca assuma:** Se há dúvida, pergunte. Suposições erradas custam caro.
- **Use linguagem testável:** "O sistema deve ser rápido" não é testável. "Resposta em < 500ms para 95% das requests" é.
- **Priorize com MoSCoW:** Must, Should, Could, Won't ajuda a alinhar expectativas.
- **Documente o "não":** Requisitos descartados devem ser registrados com justificativa.
- **Validação cruzada:** Confirme requisitos com mais de um stakeholder.
