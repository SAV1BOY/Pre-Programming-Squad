# Template: Estimativa

## Título
Estimation — Estimativa de Esforço e Prazo

## Propósito
Documentar estimativas de esforço, tempo e custo para o projeto ou funcionalidade, incluindo premissas, riscos e faixas de confiança, permitindo decisões informadas sobre planejamento.

## Quando Usar
- Após definição de escopo e arquitetura.
- Quando stakeholders precisam de previsões de prazo e custo.
- Em revisões de planejamento para ajustar estimativas.

## Seções

### 1. Informações Gerais
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| Escopo da Estimativa | `[projeto inteiro / fase / feature]` |
| Método Utilizado | `[Planning Poker / T-shirt / Análise de pontos / Histórico]` |
| Responsável | `[nome]` |
| Data | `[YYYY-MM-DD]` |
| Nível de Confiança | `[Alto/Médio/Baixo]` |

### 2. Premissas da Estimativa
- `[Premissa 1: condição assumida]`
- `[Premissa 2: recurso disponível]`
- `[Premissa 3: complexidade assumida]`

### 3. Breakdown de Esforço
| Item | Complexidade | Estimativa Otimista | Estimativa Provável | Estimativa Pessimista | PERT |
|------|-------------|--------------------|--------------------|---------------------|------|
| `[item de trabalho]` | `[P/M/G/GG]` | `[dias]` | `[dias]` | `[dias]` | `[(O+4P+Pes)/6]` |

> PERT = (Otimista + 4×Provável + Pessimista) / 6

### 4. Resumo por Fase
| Fase | Esforço (pessoa-dias) | Duração (dias corridos) | Equipe Necessária |
|------|----------------------|------------------------|------------------|
| `[fase]` | `[esforço]` | `[duração]` | `[tamanho e perfil]` |

### 5. Faixa de Confiança
| Cenário | Duração Total | Custo Estimado | Probabilidade |
|---------|-------------|---------------|--------------|
| Otimista | `[X semanas]` | `[R$ X]` | `[10%]` |
| Provável | `[X semanas]` | `[R$ X]` | `[60%]` |
| Pessimista | `[X semanas]` | `[R$ X]` | `[90%]` |

### 6. Riscos que Afetam a Estimativa
| Risco | Impacto na Estimativa | Probabilidade |
|-------|-----------------------|--------------|
| `[risco]` | `[+X dias/semanas]` | `[Alta/Média/Baixa]` |

### 7. Histórico de Revisões
| Data | Estimativa Anterior | Nova Estimativa | Motivo da Mudança |
|------|--------------------|-----------------|--------------------|
| `[data]` | `[valor]` | `[valor]` | `[razão]` |

## Exemplo de Preenchimento

### 3. Breakdown de Esforço
| Item | Complexidade | Otimista | Provável | Pessimista | PERT |
|------|-------------|----------|----------|-----------|------|
| Autenticação SSO | M | 3d | 5d | 10d | 5.5d |
| CRUD de Pedidos | M | 5d | 8d | 12d | 8.2d |
| Integração Pagamento | G | 8d | 12d | 20d | 12.7d |
| Dashboard de Relatórios | G | 10d | 15d | 25d | 15.8d |
| **Total** | | **26d** | **40d** | **67d** | **42.2d** |

## Dicas de Qualidade
- **Nunca dê um número exato:** Use faixas. Projetos são incertos por natureza.
- **Inclua overhead:** Reuniões, code review, bugs e interruções consomem 20-40% do tempo.
- **Revise com a equipe:** Quem vai implementar deve participar da estimativa.
- **Use histórico:** Projetos anteriores são a melhor base para estimar.
- **Atualize regularmente:** Estimativas mudam conforme aprendemos mais. Revise a cada fase.
