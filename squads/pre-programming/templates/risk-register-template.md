# Template: Registro de Riscos

## Título
Risk Register — Registro e Gestão de Riscos do Projeto

## Propósito
Identificar, avaliar e planejar respostas para riscos que possam impactar o sucesso do projeto, mantendo um registro vivo e atualizado ao longo de toda a fase de pré-programação.

## Quando Usar
- Desde o início do projeto e durante toda a sua duração.
- Ao identificar novas ameaças ou oportunidades.
- Em revisões periódicas de risco com a equipe.

## Seções

### 1. Informações Gerais
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| Responsável pelos Riscos | `[nome]` |
| Data da Última Revisão | `[YYYY-MM-DD]` |
| Próxima Revisão | `[YYYY-MM-DD]` |

### 2. Registro de Riscos
| ID | Risco | Categoria | Probabilidade | Impacto | Severidade | Responsável | Status |
|----|-------|-----------|---------------|---------|-----------|-------------|--------|
| R-01 | `[descrição do risco]` | `[Técnico/Negócio/Organizacional/Externo]` | `[1-5]` | `[1-5]` | `[P x I]` | `[nome]` | `[Aberto/Mitigado/Aceito/Fechado]` |

### 3. Matriz de Probabilidade x Impacto
```
Impacto →   1-Mínimo  2-Baixo  3-Médio  4-Alto  5-Crítico
Prob. ↓
5-Certo       5        10       15       20       25
4-Provável    4         8       12       16       20
3-Possível    3         6        9       12       15
2-Improvável  2         4        6        8       10
1-Raro        1         2        3        4        5
```

### 4. Planos de Resposta
| ID do Risco | Estratégia | Ação de Mitigação | Plano de Contingência | Gatilho |
|-------------|-----------|-------------------|-----------------------|---------|
| R-01 | `[Evitar/Mitigar/Transferir/Aceitar]` | `[ação preventiva]` | `[o que fazer se ocorrer]` | `[indicador de que o risco está se materializando]` |

### 5. Riscos Materializados
| ID | Data | Impacto Real | Ação Tomada | Lição Aprendida |
|----|------|-------------|-------------|-----------------|
| `[ID]` | `[data]` | `[o que aconteceu]` | `[como respondemos]` | `[o que aprendemos]` |

### 6. Tendências
| Revisão | Riscos Abertos | Severidade Média | Novos | Fechados |
|---------|---------------|-----------------|-------|----------|
| `[data]` | `[número]` | `[valor]` | `[número]` | `[número]` |

## Exemplo de Preenchimento

### 2. Registro de Riscos
| ID | Risco | Categoria | Prob. | Impacto | Severidade | Responsável | Status |
|----|-------|-----------|-------|---------|-----------|-------------|--------|
| R-01 | API do parceiro de pagamento fora do ar por mais de 4h | Externo | 3 | 5 | 15 | João | Aberto |
| R-02 | Dev sênior sair da equipe antes do MVP | Organizacional | 2 | 4 | 8 | Maria | Mitigado |
| R-03 | Requisitos de LGPD mais restritivos que o esperado | Negócio | 3 | 3 | 9 | Ana | Aberto |

### 4. Planos de Resposta
| ID | Estratégia | Ação de Mitigação | Plano de Contingência | Gatilho |
|----|-----------|-------------------|-----------------------|---------|
| R-01 | Mitigar | Implementar circuit breaker e fila de retry | Ativar modo offline com fila de processamento posterior | Mais de 3 timeouts consecutivos |

## Dicas de Qualidade
- **Atualize regularmente:** Riscos são dinâmicos. Revise semanalmente.
- **Seja específico:** "Algo pode dar errado" não é um risco. Descreva o cenário concreto.
- **Defina gatilhos:** Saber quando o risco está se materializando permite agir cedo.
- **Envolva a equipe:** Diferentes perspectivas identificam riscos que uma pessoa sozinha não vê.
- **Não exagere:** Foque nos riscos realmente relevantes. Não liste 50 riscos triviais.
