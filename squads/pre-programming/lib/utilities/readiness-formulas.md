# Fórmulas de Prontidão (Readiness Formulas)

## Propósito
Definir as fórmulas matemáticas utilizadas para calcular o score de prontidão de um projeto para transição da fase de pré-programação para desenvolvimento, incluindo dimensões avaliadas, pesos e limiares.

## Fórmulas e Modelos

### Fórmula Principal: Score de Prontidão Geral

```
SPG = sum(Di * Pi)

Onde:
  SPG = Score de Prontidão Geral (0-100)
  Di  = Score da dimensão i (0-100)
  Pi  = Peso da dimensão i (soma dos pesos = 1.0)
```

### Dimensões e Pesos

| Dimensão | Peso | Descrição |
|----------|------|-----------|
| Completude de Artefatos (CA) | 0.25 | Presença e qualidade dos artefatos obrigatórios |
| Clareza de Requisitos (CR) | 0.20 | Grau de especificação e testabilidade dos requisitos |
| Cobertura de Riscos (RK) | 0.15 | Identificação e mitigação de riscos |
| Qualidade Arquitetural (QA) | 0.15 | Completude das decisões arquiteturais |
| Preparação de Testes (PT) | 0.10 | Definição de estratégia e cenários de teste |
| Plano de Rollout (PR) | 0.10 | Completude do plano de implantação |
| Aprovações (AP) | 0.05 | Sign-offs dos stakeholders |

### Fórmulas por Dimensão

#### Completude de Artefatos (CA)
```
CA = (Artefatos_Presentes / Artefatos_Obrigatorios) * 100

Artefatos obrigatórios:
  1. Project Brief
  2. Notas de Arquitetura
  3. Registro de Riscos
  4. Plano de Testes
  5. Contratos de API
  6. Critérios de Aceite

Bônus (+5 pontos cada, máx 20):
  - Decision Log
  - Mapa de Dependências
  - Plano de Rollout
  - Plano de Monitoramento
```

#### Clareza de Requisitos (CR)
```
CR = (sum(Score_Requisito_i) / N) * 100

Score de cada requisito (0-1):
  +0.25 se tem descrição > 20 caracteres
  +0.25 se tem critério de aceite
  +0.25 se tem prioridade definida
  +0.25 se tem rastreabilidade (link com objetivo)
```

#### Cobertura de Riscos (RK)
```
RK = (RC * 0.6) + (RM * 0.2) + (RQ * 0.2)

RC = (Riscos_Com_Mitigacao / Total_Riscos) * 100
RM = (Riscos_Com_Responsavel / Total_Riscos) * 100
RQ = min(Total_Riscos / 5, 1.0) * 100
```

#### Qualidade Arquitetural (QA)
```
QA = (Itens_Presentes / Total_Itens) * 100

Itens avaliados:
  1. Decisões documentadas
  2. Diagramas presentes
  3. Componentes listados
  4. Integrações mapeadas
  5. Restrições definidas
  6. Alternativas registradas
```

### Classificação do Score

| Faixa | Classificação | Ação |
|-------|---------------|------|
| 90-100 | Excelente | Pronto para desenvolvimento |
| 75-89 | Bom | Pode iniciar com ressalvas menores |
| 60-74 | Regular | Necessita melhorias antes de iniciar |
| 40-59 | Insuficiente | Lacunas significativas a resolver |
| 0-39 | Crítico | Revisão completa necessária |

### Limiar Mínimo para Go/No-Go

```
Decisão = GO se:
  SPG >= 70  AND
  CA >= 80   AND
  CR >= 60   AND
  Nenhuma dimensão individual < 40
```

## Como Usar

1. Coletar dados de cada dimensão a partir dos artefatos do projeto
2. Calcular o score de cada dimensão usando as fórmulas acima
3. Aplicar os pesos para obter o Score de Prontidão Geral
4. Verificar as condições de go/no-go
5. Gerar relatório com detalhamento por dimensão

## Inputs e Outputs

### Inputs
- Inventário de artefatos do projeto
- Dados de requisitos (com critérios de aceite e prioridade)
- Registro de riscos (com mitigações e responsáveis)
- Notas de arquitetura (com decisões e diagramas)
- Status de aprovações de stakeholders

### Outputs
- Score de Prontidão Geral (0-100)
- Score por dimensão (0-100)
- Classificação (Excelente/Bom/Regular/Insuficiente/Crítico)
- Decisão go/no-go com justificativa
- Lista de itens para melhoria (se não atingiu limiar)

## Exemplos

### Exemplo: Cálculo Completo
```
Projeto: "Novo Sistema de Pagamentos"

Dimensões:
  CA = (6/6)*100 = 100 (todos os artefatos presentes)
  CR = 72 (18/25 requisitos com critério de aceite)
  RK = (0.6*85) + (0.2*70) + (0.2*100) = 51 + 14 + 20 = 85
  QA = (5/6)*100 = 83.3 (faltam diagramas de sequência)
  PT = (3/4)*100 = 75 (falta definição de dados de teste)
  PR = (3/4)*100 = 75 (falta plano de feature flags)
  AP = (2/3)*100 = 66.7 (falta aprovação do QA Lead)

SPG = 100*0.25 + 72*0.20 + 85*0.15 + 83.3*0.15 + 75*0.10 + 75*0.10 + 66.7*0.05
SPG = 25 + 14.4 + 12.75 + 12.5 + 7.5 + 7.5 + 3.33
SPG = 82.98 -> 83.0

Classificação: Bom
Decisão: GO (SPG=83 >= 70, CA=100 >= 80, CR=72 >= 60, mín=66.7 >= 40)
```
