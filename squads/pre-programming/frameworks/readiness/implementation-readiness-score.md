# Implementation Readiness Score

## Título e Propósito

O **Implementation Readiness Score** é um sistema de pontuação que avalia objetivamente se todas as condições prévias para iniciar a implementação estão atendidas. O propósito é criar um gate quantificável entre pré-programação e codificação — prevenindo que a equipe comece a escrever código quando o entendimento, o design ou as dependências ainda não estão maduros o suficiente.

## Quando Usar

- Como gate formal entre fase de pré-programação e implementação
- Quando a equipe frequentemente inicia código e depois descobre que faltavam informações
- Antes de comprometer o sprint/ciclo com tarefas de implementação
- Quando há histórico de retrabalho por requisitos incompletos ou ambíguos
- Para dar visibilidade a stakeholders sobre o que ainda falta antes de implementar

## Conceitos-Chave

1. **Readiness**: O grau em que todas as precondições para implementação estão satisfeitas.
2. **Dimensão de Readiness**: Uma categoria de precondição: clareza de requisitos, design, dependências, infraestrutura, testes, etc.
3. **Score por Dimensão**: Avaliação 0-3 de cada dimensão: 0=não iniciado, 1=parcial, 2=completo, 3=completo e validado.
4. **Threshold de Go**: Score mínimo para iniciar implementação. Tipicamente 80%+.
5. **Blocker Absoluto**: Dimensão que, se score 0, impede implementação independente do score total.

## Processo / Passos

### Passo 1 — Selecionar Dimensões
Escolha dimensões relevantes para o contexto. Dimensões padrão:

| Dimensão | Peso |
|---|---|
| Requisitos claros e aceitos | 5 |
| Critérios de aceite definidos | 5 |
| Design/arquitetura definidos | 4 |
| Edge cases mapeados | 3 |
| Dependências resolvidas | 4 |
| Ambiente/infra disponível | 3 |
| Plano de testes definido | 3 |
| Riscos identificados e mitigados | 3 |

### Passo 2 — Avaliar Cada Dimensão
Para cada dimensão, avalie honestamente o estado atual (0-3).

### Passo 3 — Calcular Score
Score = Σ(avaliação × peso) ÷ Σ(3 × peso) × 100%

### Passo 4 — Verificar Blockers
Qualquer dimensão com peso ≥ 4 e avaliação 0 é blocker absoluto.

### Passo 5 — Decidir
- **≥ 80% sem blockers**: GO — implementação pode iniciar
- **60-79%**: CONDICIONAL — implementação pode iniciar com riscos documentados
- **< 60%**: STOP — mais trabalho de pré-programação necessário

### Passo 6 — Para "CONDICIONAL" e "STOP", Definir Ações
Liste o que precisa ser feito para subir o score, com responsáveis e prazos.

### Passo 7 — Reavaliar
Após ações, recalcule o score. Repita até atingir threshold.

## Perguntas de Ativação

- "Se um dev pegar essa tarefa agora, terá tudo que precisa para implementar?"
- "Há perguntas que o dev vai precisar fazer durante a implementação porque não foram respondidas antes?"
- "Os critérios de aceite são claros o suficiente para que qualquer dev da equipe implemente sem dúvida?"
- "As dependências externas estão realmente disponíveis e testadas?"
- "O ambiente de desenvolvimento e staging está pronto?"
- "Estamos iniciando implementação porque está pronto ou porque o prazo está apertando?"

## Output Esperado

```
IMPLEMENTATION READINESS SCORE — [Feature/Projeto]
Data: [data da avaliação]

| Dimensão | Peso | Score (0-3) | Ponderado | Status |
|---|---|---|---|---|
| Requisitos claros | 5 | 3 | 15/15 | ✓ |
| Critérios de aceite | 5 | 2 | 10/15 | Faltam cenários de erro |
| Design/arquitetura | 4 | 3 | 12/12 | ✓ |
| Edge cases mapeados | 3 | 1 | 3/9 | Apenas happy path mapeado |
| Dependências | 4 | 2 | 8/12 | API de CEP não testada |
| Ambiente/infra | 3 | 3 | 9/9 | ✓ |
| Plano de testes | 3 | 1 | 3/9 | Apenas esboço |
| Riscos identificados | 3 | 2 | 6/9 | Falta plano de mitigação |
| TOTAL | 30 | | 66/90 | 73% |

DECISÃO: CONDICIONAL
BLOCKERS: Nenhum absoluto
AÇÕES NECESSÁRIAS:
1. Completar critérios de aceite com cenários de erro — Resp: PO — Prazo: terça
2. Mapear edge cases — Resp: Dev Lead — Prazo: quarta
3. Testar integração com API de CEP — Resp: Dev — Prazo: terça
4. Completar plano de testes — Resp: QA — Prazo: quarta
```

## Armadilhas Comuns

1. **Score inflado**: Dar scores altos para avançar rápido. Honestidade é o valor central do framework.
2. **Gate como burocracia**: Se o score vira checkbox que todos preenchem sem reflexão, perde o propósito.
3. **Peso uniforme**: Dar o mesmo peso a tudo desvaloriza dimensões críticas.
4. **Ignorar o CONDICIONAL**: Tratar "condicional" como "go" sem endereçar os riscos.
5. **Não reavaliar**: Calcular uma vez e não atualizar conforme ações são completadas.
6. **Dimensões genéricas**: Usar as mesmas dimensões para todo tipo de projeto sem adaptar ao contexto.
