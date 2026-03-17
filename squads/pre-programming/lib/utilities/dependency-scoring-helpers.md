# Auxiliares de Pontuação de Dependências (Dependency Scoring Helpers)

## Propósito
Fornecer modelos para avaliar e pontuar dependências entre componentes do projeto, identificando caminhos críticos, pontos de fragilidade e riscos de acoplamento para orientar decisões de arquitetura e planejamento.

## Fórmulas e Modelos

### Score de Criticidade de Dependência

```
SCD = (Fan_In * P1) + (Fan_Out * P2) + (Profundidade * P3) + (Volatilidade * P4)

Onde:
  Fan_In:       Número de componentes que dependem deste (0-N)
  Fan_Out:      Número de dependências deste componente (0-N)
  Profundidade: Posição na cadeia de dependência (1-N)
  Volatilidade: Frequência esperada de mudanças (1-5)

Pesos:
  P1 = 0.35 (Fan_In, indica importância)
  P2 = 0.25 (Fan_Out, indica fragilidade)
  P3 = 0.15 (Profundidade, indica impacto em cascata)
  P4 = 0.25 (Volatilidade, indica risco de mudança)
```

### Índice de Acoplamento

```
IA = (Dependencias_Reais / Dependencias_Possíveis) * 100

Dependencias_Possiveis = N * (N - 1)  (N = número de componentes)

Classificação:
  IA < 10%:   Baixo acoplamento (saudável)
  IA 10-25%:  Acoplamento moderado (aceitável)
  IA 25-40%:  Acoplamento alto (requer atenção)
  IA > 40%:   Acoplamento excessivo (ação necessária)
```

### Score de Risco de Dependência Externa

```
SRDE = Criticidade * Confiabilidade_Inversa * Substituibilidade_Inversa

Criticidade (1-5):
  1: Funcionalidade periférica
  2: Funcionalidade importante mas não crítica
  3: Funcionalidade de negócio crítica
  4: Funcionalidade de infraestrutura core
  5: Ponto único de falha (SPOF)

Confiabilidade_Inversa (1-5):
  1: SLA 99.99%+, histórico excelente
  2: SLA 99.9%, histórico bom
  3: SLA 99.5%, incidentes ocasionais
  4: SLA < 99%, incidentes frequentes
  5: Sem SLA definido ou instável

Substituibilidade_Inversa (1-5):
  1: Múltiplas alternativas, migração trivial
  2: Alternativas disponíveis, migração moderada
  3: Poucas alternativas, migração significativa
  4: Alternativa única, migração complexa
  5: Sem alternativa viável (vendor lock-in)
```

### Caminho Crítico de Dependências

```
Caminho_Critico = sequência de dependências com maior soma de duração

Duração_Nó = Esforço_Base * Fator_Risco_Dependencia

Fator_Risco = 1 + (SCD_normalizado * 0.3)

Folga = Data_Limite - (Data_Início + Caminho_Crítico)
```

### Índice de Saúde de Dependências

```
ISD = (1 - (Dep_Problemáticas / Total_Dependências)) * 100

Dependência problemática se:
  - Circular (faz parte de um ciclo)
  - SRDE > 15 (risco externo alto)
  - SCD > média + 2*desvio_padrão (criticidade extrema)
  - Sem proprietário definido
```

## Como Usar

1. **Mapear** todas as dependências do projeto (internas e externas)
2. **Calcular Fan-In e Fan-Out** para cada componente
3. **Avaliar dependências externas** com score SRDE
4. **Identificar caminho crítico** e componentes com maior SCD
5. **Calcular índices** de acoplamento e saúde
6. **Priorizar ações** para dependências de maior risco

## Inputs e Outputs

### Inputs
- Mapa de dependências (grafo de componentes)
- Lista de dependências externas (APIs, serviços, bibliotecas)
- SLAs e histórico de confiabilidade de sistemas externos
- Estimativas de esforço por componente
- Frequência esperada de mudanças

### Outputs
- Score de Criticidade (SCD) por componente
- Índice de Acoplamento geral
- Score de Risco para cada dependência externa
- Caminho crítico com duração estimada
- Índice de Saúde de Dependências
- Recomendações de desacoplamento

## Exemplos

### Exemplo: Análise de Dependências de Microsserviço
```
Serviço: Order Service

Dependências:
  Internas:
    -> User Service     (Fan_In: 5, Fan_Out: 2, Vol: 2)  SCD: 3.5
    -> Product Service  (Fan_In: 4, Fan_Out: 3, Vol: 3)  SCD: 3.8
    -> Payment Service  (Fan_In: 2, Fan_Out: 1, Vol: 2)  SCD: 2.1
    -> Notification Svc (Fan_In: 6, Fan_Out: 0, Vol: 1)  SCD: 2.5

  Externas:
    -> Stripe API       Criticidade: 5, Confiab: 2, Subst: 3 -> SRDE: 30
    -> SendGrid API     Criticidade: 2, Confiab: 2, Subst: 1 -> SRDE: 4
    -> AWS S3           Criticidade: 3, Confiab: 1, Subst: 3 -> SRDE: 9

Índice de Acoplamento: 7/12 = 58% (ALTO - ação necessária)

Recomendações:
  1. Stripe API (SRDE=30): Implementar circuit breaker e fila de retry
  2. Product Service (SCD=3.8): Considerar cache local, reduzir acoplamento
  3. Acoplamento geral alto: Migrar comunicação síncrona para eventos
```
