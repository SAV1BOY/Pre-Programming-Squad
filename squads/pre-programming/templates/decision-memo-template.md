# Template: Memo de Decisão

## Título
Decision Memo — Registro Formal de Decisão

## Propósito
Documentar decisões importantes do projeto com contexto, alternativas avaliadas, justificativa e consequências, criando um registro consultável para referência futura.

## Quando Usar
- Para qualquer decisão que afete arquitetura, escopo, tecnologia ou cronograma.
- Quando múltiplos stakeholders precisam concordar com uma direção.
- Para criar um histórico de decisões rastreável.

## Seções

### 1. Cabeçalho
| Campo | Valor |
|-------|-------|
| ID da Decisão | `[DEC-XXX]` |
| Título | `[título conciso da decisão]` |
| Projeto | `[nome do projeto]` |
| Data | `[YYYY-MM-DD]` |
| Status | `[Proposta / Aprovada / Rejeitada / Substituída]` |
| Decisor | `[nome e papel]` |
| Consultados | `[nomes]` |

### 2. Contexto
`[Descreva a situação que levou à necessidade desta decisão. Que problema estamos tentando resolver? Que forças estão em jogo?]`

### 3. Decisão
`[Declare a decisão tomada de forma clara e inequívoca.]`

### 4. Alternativas Consideradas
| Alternativa | Prós | Contras | Motivo da Rejeição |
|-------------|------|---------|-------------------|
| `[alternativa 1]` | `[vantagens]` | `[desvantagens]` | `[por que não foi escolhida]` |
| `[alternativa 2]` | `[vantagens]` | `[desvantagens]` | `[por que não foi escolhida]` |

### 5. Justificativa
`[Explique por que esta decisão é a melhor opção dados os constrangimentos, requisitos e contexto do projeto.]`

### 6. Consequências
**Positivas:**
- `[consequência positiva]`

**Negativas:**
- `[consequência negativa aceita]`

**Neutras:**
- `[consequência que requer atenção mas não é positiva nem negativa]`

### 7. Riscos Aceitos
| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| `[risco decorrente da decisão]` | `[P]` | `[I]` | `[como minimizar]` |

### 8. Critérios de Revisão
- **Revisão programada:** `[data ou evento que gatilha revisão]`
- **Condições para reverter:** `[quando esta decisão deveria ser reconsiderada]`

### 9. Assinaturas
| Nome | Papel | Concordância | Data |
|------|-------|-------------|------|
| `[nome]` | `[papel]` | `[Concordo/Discordo — registrado]` | `[data]` |

## Exemplo de Preenchimento

### 1. Cabeçalho
| Campo | Valor |
|-------|-------|
| ID da Decisão | DEC-007 |
| Título | Adotar PostgreSQL como banco principal ao invés de MongoDB |
| Projeto | Portal de Autoatendimento |
| Data | 2026-03-17 |
| Status | Aprovada |
| Decisor | Ana Costa — VP de Engenharia |

### 3. Decisão
Adotaremos PostgreSQL 16 como banco de dados principal do Portal de Autoatendimento, utilizando JSONB para dados semi-estruturados quando necessário, ao invés de MongoDB.

### 5. Justificativa
A equipe de DBA tem expertise em PostgreSQL e não possui experiência com MongoDB. O modelo de dados é predominantemente relacional, com apenas 2 coleções que se beneficiariam de schema flexível — atendidas por JSONB. O custo de capacitação em MongoDB (6 semanas) inviabiliza o prazo de entrega do Q2.

## Dicas de Qualidade
- **Decida e registre:** Decisões não documentadas são decisões esquecidas (e revisitadas infinitamente).
- **Registre o contexto:** Sem contexto, quem ler depois não entende por que a decisão foi tomada.
- **Inclua alternativas rejeitadas:** Evita que alguém sugira de novo algo que já foi avaliado.
- **Aceite discordância:** Nem todos precisam concordar. Registre discordâncias para transparência.
- **Programe revisões:** Toda decisão tem prazo de validade. Defina quando reavaliar.
