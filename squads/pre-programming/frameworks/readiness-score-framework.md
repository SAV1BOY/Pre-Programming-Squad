# Readiness Score Framework

## Título e Propósito

O **Readiness Score Framework** é um sistema de pontuação para avaliar objetivamente se um projeto, feature ou componente está pronto para avançar para a próxima fase (design → implementação → deploy → produção). O propósito é substituir a avaliação subjetiva ("acho que está pronto") por critérios mensuráveis e transparentes.

## Quando Usar

- Em gates entre fases do projeto (discovery → design → implementação)
- Antes de iniciar implementação para verificar se o pré-trabalho está completo
- Antes de deploys em produção
- Em revisões de sprint para avaliar completude de itens
- Quando há debate sobre se algo está "pronto" ou não

## Conceitos-Chave

1. **Dimensão de Readiness**: Uma área específica que precisa estar pronta. Exemplo: requisitos, arquitetura, testes, infraestrutura.
2. **Critério por Dimensão**: O que significa "pronto" naquela dimensão. Deve ser verificável, não subjetivo.
3. **Peso da Dimensão**: Importância relativa da dimensão no contexto. Nem todas as dimensões têm o mesmo peso.
4. **Score Mínimo**: O score abaixo do qual não se avança. Pode ser um total mínimo e/ou mínimos por dimensão.
5. **Blocker**: Uma dimensão com score zero que impede avanço independente do score total.

## Processo / Passos

### Passo 1 — Definir as Dimensões
Selecione as dimensões relevantes para a transição sendo avaliada. Exemplos: clareza de requisitos, design arquitetural, plano de testes, infraestrutura, monitoramento, documentação.

### Passo 2 — Definir Critérios por Dimensão
Para cada dimensão, liste critérios objetivos. Exemplo para "Clareza de Requisitos": requisitos documentados, critérios de aceite definidos, edge cases mapeados.

### Passo 3 — Atribuir Pesos
Pondere cada dimensão de 1 a 5 baseado na importância para o projeto específico.

### Passo 4 — Avaliar Cada Dimensão
Para cada dimensão, avalie o estado atual: **0** (não iniciado), **1** (parcial), **2** (completo mas não validado), **3** (completo e validado).

### Passo 5 — Calcular Score
Score = Σ (avaliação × peso) ÷ Σ (3 × peso) × 100%. Resultado é um percentual de readiness.

### Passo 6 — Verificar Blockers
Qualquer dimensão com peso ≥ 4 e avaliação 0 é um blocker. Blockers impedem avanço independente do score total.

### Passo 7 — Decidir: Go / Fix / No-Go
- **Go**: Score ≥ 80% e sem blockers
- **Fix**: Score entre 60-79% ou blockers endereçáveis rapidamente
- **No-Go**: Score < 60% ou blockers não endereçáveis

## Perguntas de Ativação

- "Se pedirmos para qualquer dev da equipe começar a implementar agora, eles teriam tudo que precisam?"
- "Quais perguntas ainda estão sem resposta?"
- "Estamos avançando porque está pronto ou porque o prazo está apertando?"
- "Qual dimensão está mais fraca e o que precisamos para fortalecê-la?"
- "Há algum blocker que estamos ignorando?"
- "Se déssemos nota 3 para tudo, estaríamos mentindo em alguma dimensão?"

## Output Esperado

| Dimensão | Peso | Avaliação (0-3) | Score Parcial | Critérios | Status |
|---|---|---|---|---|---|
| Requisitos claros | 5 | 3 | 15/15 | Documentados, com critérios de aceite | OK |
| Design arquitetural | 4 | 2 | 8/12 | Design documentado mas não revisado | Fix: agendar revisão |
| Plano de testes | 4 | 1 | 4/12 | Apenas happy path definido | Fix: mapear edge cases |
| Infraestrutura | 3 | 0 | 0/9 | Nada provisionado | BLOCKER |
| Monitoramento | 2 | 2 | 4/6 | Alertas definidos, dashboards pendentes | OK |
| **Total** | | | **31/54 = 57%** | | **NO-GO** |

**Decisão**: No-Go — Score 57% abaixo do mínimo (80%) + 1 blocker (Infraestrutura).
**Ações necessárias**: Provisionar infra (blocker), completar plano de testes, revisar arquitetura.

## Armadilhas Comuns

1. **Avaliação otimista**: Dar nota 3 para algo que está em 2 para "passar". Honestidade é o valor do framework.
2. **Score como burocracia**: Se o score vira checkbox a ser preenchido sem reflexão, perde todo o valor.
3. **Peso uniforme**: Dar o mesmo peso a tudo é o mesmo que não ponderar. Contexto importa.
4. **Ignorar blockers**: Avançar com score alto mas com uma dimensão zerada é receita para desastre.
5. **Não recalibrar**: Os critérios e pesos que funcionam para um projeto podem não funcionar para outro.
6. **Gate theater**: Fazer a avaliação pro forma e avançar de qualquer jeito porque "não temos tempo".
