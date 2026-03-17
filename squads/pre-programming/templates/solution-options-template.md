# Template: Opções de Solução

## Título
Solution Options — Comparação de Alternativas de Solução

## Propósito
Documentar e comparar diferentes abordagens técnicas para resolver o problema, fornecendo base objetiva para a tomada de decisão sobre a solução a ser adotada.

## Quando Usar
- Quando há mais de uma abordagem viável para o problema.
- Antes de decisões arquiteturais significativas.
- Quando stakeholders precisam entender trade-offs entre opções.

## Seções

### 1. Contexto da Decisão
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| Decisão a Tomar | `[descrição concisa da decisão]` |
| Data Limite | `[YYYY-MM-DD]` |
| Decisor Final | `[nome e papel]` |

### 2. Critérios de Avaliação
| Critério | Peso (1-5) | Descrição |
|----------|-----------|-----------|
| `[critério]` | `[peso]` | `[o que significa e como medir]` |

### 3. Opção A: `[Nome da Opção]`
- **Descrição:** `[como funciona esta abordagem]`
- **Prós:** `[vantagens]`
- **Contras:** `[desvantagens]`
- **Custo Estimado:** `[tempo/dinheiro/esforço]`
- **Risco Principal:** `[maior risco]`
- **Esforço de Implementação:** `[Alto/Médio/Baixo]`

### 4. Opção B: `[Nome da Opção]`
- **Descrição:** `[como funciona esta abordagem]`
- **Prós:** `[vantagens]`
- **Contras:** `[desvantagens]`
- **Custo Estimado:** `[tempo/dinheiro/esforço]`
- **Risco Principal:** `[maior risco]`
- **Esforço de Implementação:** `[Alto/Médio/Baixo]`

### 5. Opção C: `[Nome da Opção]` (se aplicável)
- **Descrição:** `[como funciona esta abordagem]`
- **Prós:** `[vantagens]`
- **Contras:** `[desvantagens]`
- **Custo Estimado:** `[tempo/dinheiro/esforço]`
- **Risco Principal:** `[maior risco]`
- **Esforço de Implementação:** `[Alto/Médio/Baixo]`

### 6. Matriz Comparativa
| Critério | Peso | Opção A | Opção B | Opção C |
|----------|------|---------|---------|---------|
| `[critério 1]` | `[peso]` | `[nota 1-5]` | `[nota 1-5]` | `[nota 1-5]` |
| `[critério 2]` | `[peso]` | `[nota 1-5]` | `[nota 1-5]` | `[nota 1-5]` |
| **Total Ponderado** | | `[total]` | `[total]` | `[total]` |

### 7. Recomendação
- **Opção Recomendada:** `[nome]`
- **Justificativa:** `[por que esta é a melhor opção dado os critérios]`
- **Ressalvas:** `[condições ou riscos a monitorar]`

### 8. Decisão Tomada
| Campo | Valor |
|-------|-------|
| Opção Escolhida | `[nome]` |
| Decidido Por | `[nome]` |
| Data | `[YYYY-MM-DD]` |
| Condições | `[condições ou revisões futuras]` |

## Exemplo de Preenchimento

### 6. Matriz Comparativa
| Critério | Peso | Monolito | Microserviços | Modular Monolith |
|----------|------|----------|---------------|-----------------|
| Velocidade de entrega | 5 | 4 | 2 | 4 |
| Escalabilidade | 3 | 2 | 5 | 3 |
| Complexidade operacional | 4 | 5 | 1 | 4 |
| Custo de infra | 3 | 4 | 2 | 4 |
| **Total Ponderado** | | **57** | **37** | **57** |

## Dicas de Qualidade
- **Mínimo 2, máximo 4 opções:** Poucas demais não é análise; muitas demais gera paralisia.
- **Inclua a opção "não fazer nada":** Às vezes manter o status quo é a melhor decisão.
- **Seja honesto sobre trade-offs:** Toda opção tem desvantagens. Escondê-las enfraquece a análise.
- **Pesos antes das notas:** Defina os critérios e pesos antes de avaliar, para evitar viés.
- **Decisão != Unanimidade:** Documente a decisão mesmo que nem todos concordem.
