# Modelos de Pontuação (Scoring Models)

## Propósito
Fornecer modelos padronizados de pontuação para avaliar e priorizar diferentes aspectos do planejamento de projetos na fase de pré-programação, incluindo priorização de requisitos, avaliação de riscos e seleção de alternativas técnicas.

## Fórmulas e Modelos

### 1. WSJF (Weighted Shortest Job First)
Priorização baseada no valor econômico relativo do trabalho.

```
WSJF = Custo do Atraso / Tamanho do Trabalho

Custo do Atraso = Valor de Negócio + Criticidade Temporal + Redução de Risco

Onde:
  Valor de Negócio:      1 (baixo) a 13 (muito alto) - Fibonacci
  Criticidade Temporal:  1 (flexível) a 13 (deadline fixa)
  Redução de Risco:      1 (baixo risco) a 13 (bloqueador)
  Tamanho do Trabalho:   1 (trivial) a 13 (muito grande)
```

### 2. Matriz de Priorização MoSCoW com Peso
Extensão do MoSCoW com pesos numéricos para ordenação fina.

```
Score MoSCoW = Categoria * Peso_Impacto * Fator_Urgência

Categorias:
  Must Have:   peso 10
  Should Have: peso 6
  Could Have:  peso 3
  Won't Have:  peso 0

Peso_Impacto: 0.5 (baixo) a 2.0 (crítico)
Fator_Urgência: 0.5 (pode esperar) a 2.0 (imediato)
```

### 3. Score de Complexidade Técnica
Avaliação multidimensional da complexidade de uma tarefa.

```
Complexidade = sum(Di * Pi) / sum(Pi)

Dimensões (Di) e Pesos (Pi):
  D1: Algoritmo/Lógica           P1: 0.25  (1-5 pontos)
  D2: Integrações                P2: 0.20  (1-5 pontos)
  D3: Volume de Dados            P3: 0.15  (1-5 pontos)
  D4: Requisitos não-funcionais  P4: 0.15  (1-5 pontos)
  D5: Domínio de Negócio         P5: 0.15  (1-5 pontos)
  D6: Incerteza Técnica          P6: 0.10  (1-5 pontos)
```

### 4. Score de Valor vs. Esforço (Value-Effort Matrix)
Classificação de itens em quadrantes baseada em valor e esforço.

```
Score = (Valor_Normalizado * 0.6) - (Esforço_Normalizado * 0.4)

Quadrantes:
  Quick Wins:    Valor Alto + Esforço Baixo   (Score > 0.4)
  Grandes Apostas: Valor Alto + Esforço Alto  (0 < Score < 0.4)
  Preenchimento: Valor Baixo + Esforço Baixo  (-0.2 < Score < 0)
  Poço de Tempo: Valor Baixo + Esforço Alto   (Score < -0.2)
```

## Como Usar

1. **Selecionar o modelo** adequado ao contexto de decisão
2. **Calibrar pesos** com a equipe antes de usar (primeira sessão de calibração)
3. **Pontuar individualmente** e depois discutir discrepâncias
4. **Documentar justificativas** para pontuações extremas (1 ou 5)
5. **Recalibrar periodicamente** comparando scores com resultados reais

## Inputs e Outputs

### Inputs
- Lista de itens a priorizar (requisitos, funcionalidades, riscos)
- Contexto de negócio (prazos, restrições, objetivos)
- Participantes com conhecimento do domínio e técnico
- Dados históricos de projetos anteriores (para calibração)

### Outputs
- Lista ordenada por prioridade com scores
- Quadrante de classificação de cada item
- Justificativas documentadas para decisões de priorização
- Relatório de distribuição (quantos itens por categoria/quadrante)

## Exemplos

### Exemplo: WSJF para Backlog de Features
```
Feature A: Login com SSO
  Valor de Negócio:     8  (alto - requisito de cliente enterprise)
  Criticidade Temporal: 5  (Q2 desejável, não obrigatório)
  Redução de Risco:     3  (baixo risco)
  Tamanho:              5  (médio)
  WSJF = (8+5+3)/5 = 3.2

Feature B: Cache distribuído
  Valor de Negócio:     3  (médio - melhoria de performance)
  Criticidade Temporal: 8  (bloqueando crescimento)
  Redução de Risco:     8  (risco de indisponibilidade)
  Tamanho:              8  (grande)
  WSJF = (3+8+8)/8 = 2.375

Feature C: Dark mode
  Valor de Negócio:     2  (baixo)
  Criticidade Temporal: 1  (sem urgência)
  Redução de Risco:     1  (sem risco)
  Tamanho:              2  (pequeno)
  WSJF = (2+1+1)/2 = 2.0

Prioridade: A (3.2) > B (2.375) > C (2.0)
```
