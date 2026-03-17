# Lógica do Mapa de Calor de Riscos (Risk Heatmap Logic)

## Propósito
Definir a lógica para geração de mapas de calor de riscos, incluindo classificação de severidade, cálculo de exposição ao risco e regras de visualização para comunicação eficaz com stakeholders.

## Fórmulas e Modelos

### Matriz de Severidade (5x5)

```
                        IMPACTO
                 1     2     3     4     5
           +-----+-----+-----+-----+-----+
         5 |  5  | 10  | 15  | 20  | 25  |  Muito Alta
P        4 |  4  |  8  | 12  | 16  | 20  |  Alta
R        3 |  3  |  6  |  9  | 12  | 15  |  Média
O        2 |  2  |  4  |  6  |  8  | 10  |  Baixa
B        1 |  1  |  2  |  3  |  4  |  5  |  Muito Baixa
           +-----+-----+-----+-----+-----+
              MB     B     M     A    MA
```

### Classificação de Severidade

```
Severidade = Probabilidade * Impacto

Faixas de severidade:
  Crítica:  20-25  (vermelho escuro)  -> Ação imediata obrigatória
  Alta:     12-19  (vermelho)         -> Plano de mitigação obrigatório
  Média:     6-11  (amarelo)          -> Monitoramento ativo
  Baixa:     3-5   (verde claro)     -> Aceitar ou monitorar
  Mínima:    1-2   (verde)           -> Aceitar
```

### Exposição Total ao Risco

```
ETR = sum(Si * Wi) / sum(Wi)

Onde:
  ETR = Exposição Total ao Risco (1-25)
  Si  = Severidade do risco i
  Wi  = Peso do risco i (baseado na categoria)

Pesos por categoria:
  Segurança:       2.0
  Dados:           1.8
  Performance:     1.5
  Integração:      1.3
  Técnico:         1.0
  Organizacional:  0.8
```

### Índice de Mitigação

```
IM = (Riscos_Mitigados / Riscos_Criticos_E_Altos) * 100

Onde Riscos_Mitigados = riscos com:
  - Estratégia de mitigação definida
  - Responsável atribuído
  - Prazo de implementação
```

### Velocidade de Risco (Risk Velocity)

```
VR = Impacto_Estimado / Tempo_Até_Materialização

Classificação:
  Instantâneo: VR > 10 (risco pode materializar em horas)
  Rápido:      VR 5-10  (risco pode materializar em dias)
  Gradual:     VR 2-5   (risco pode materializar em semanas)
  Lento:       VR < 2   (risco pode materializar em meses)
```

## Como Usar

1. **Listar todos os riscos** identificados no projeto
2. **Avaliar cada risco** com probabilidade (1-5) e impacto (1-5)
3. **Calcular severidade** (P * I) e classificar na matriz
4. **Atribuir categoria** e calcular exposição ponderada
5. **Gerar o mapa de calor** com a distribuição visual
6. **Identificar ações** baseadas na classificação

## Inputs e Outputs

### Inputs
- Lista de riscos com ID, descrição, probabilidade e impacto
- Categoria de cada risco
- Status de mitigação (se existe plano, responsável, prazo)
- Velocidade estimada de materialização

### Outputs
- Mapa de calor visual (5x5) com posicionamento dos riscos
- Exposição Total ao Risco (ETR)
- Índice de Mitigação (IM)
- Lista priorizada de riscos por severidade
- Recomendações de ação por faixa de severidade

## Exemplos

### Exemplo: Mapa de Calor com Riscos Posicionados
```
                        IMPACTO
                 MB     B     M     A     MA
           +-----+-----+-----+-----+-----+
  MA     5 |     |     | R03 |     | R01 |
         4 |     |     |     | R05 | R02 |
  Prob   3 |     | R09 | R06 |     | R04 |
         2 | R10 |     | R08 |     |     |
  MB     1 |     | R11 | R07 |     |     |
           +-----+-----+-----+-----+-----+

Resumo:
  Críticos (vermelho escuro): R01 (severidade 25), R02 (20)
  Altos (vermelho):           R04 (15), R03 (15), R05 (16)
  Médios (amarelo):           R06 (9), R08 (6)
  Baixos (verde):             R09 (4), R07 (3), R10 (2), R11 (2)

ETR = 8.7 (médio-alto)
IM = 60% (2 de 5 riscos críticos/altos mitigados)

Ação requerida:
  - R01, R02: plano de mitigação imediato
  - R04, R03, R05: plano de mitigação em 1 semana
  - R06, R08: monitoramento quinzenal
```

### Exemplo: Tendência de Risco ao Longo do Tempo
```
Semana 1: ETR = 12.3 (alto)       Riscos críticos: 4
Semana 2: ETR = 10.1 (médio-alto) Riscos críticos: 3  (-1 mitigado)
Semana 3: ETR = 8.7  (médio)      Riscos críticos: 2  (-1 resolvido)
Semana 4: ETR = 7.2  (médio)      Riscos críticos: 2  (estável)

Tendência: decrescente (positiva)
Projeção: ETR < 5 em 3 semanas se ritmo mantido
```
