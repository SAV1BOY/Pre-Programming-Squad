# Padrões de Estimativa

## Nome do Padrão
Padrões para Estimativa de Esforço e Prazo

## Problema que Resolve
Estimativas imprecisas são uma das principais causas de fracasso em projetos de software. Problemas comuns incluem: otimismo excessivo, desconsideração de complexidade acidental, falta de buffer para imprevistos, pressão para comprometer-se com prazos irreais e ausência de dados históricos para calibração.

## Solução

### 1. Estimativa de Três Pontos (PERT)
Para cada tarefa, estimar três cenários: otimista (O), mais provável (M) e pessimista (P). A estimativa final pondera os três valores.

**Fórmula:** E = (O + 4M + P) / 6
**Desvio padrão:** S = (P - O) / 6

**Aplicação prática:**
- Cada tarefa estimada por quem vai executar
- Documentar premissas de cada cenário
- Usar desvio padrão para calcular intervalo de confiança
- 95% de confiança: E + 2S

### 2. Planning Poker com Calibração
Usar Planning Poker com sessões de calibração periódica onde a equipe compara estimativas passadas com tempo real, ajustando o modelo mental.

**Aplicação prática:**
- Sessão de calibração a cada 3-4 sprints
- Comparar: estimado vs. realizado por categoria
- Identificar vieses sistemáticos (ex: "sempre subestimamos integração")
- Ajustar fator de correção por tipo de tarefa

### 3. Decomposição + Soma (Bottom-Up)
Decompor o trabalho em tarefas menores (< 2 dias) e somar as estimativas. Tarefas menores são mais previsíveis.

**Aplicação prática:**
- Regra: nenhuma tarefa > 2 dias de trabalho
- Se não consegue decompor, é sinal de ambiguidade
- Adicionar buffer de integração (15-25% do total)
- Adicionar buffer de risco baseado no perfil do projeto

### 4. Estimativa por Analogia
Comparar com projetos ou funcionalidades similares já realizadas, ajustando por diferenças conhecidas.

**Aplicação prática:**
- Manter base de dados de projetos anteriores
- Registrar: escopo, equipe, prazo estimado, prazo real
- Identificar projeto mais similar ao atual
- Ajustar por fatores: equipe diferente, tecnologia nova, complexidade

### 5. Cone de Incerteza
Reconhecer que estimativas no início do projeto têm margem de erro de 4x e que a precisão melhora ao longo do tempo.

**Aplicação prática:**
- Início do projeto: estimativa com fator 2x-4x
- Após requisitos definidos: fator 1.5x-2x
- Após design: fator 1.25x-1.5x
- Após implementação parcial: fator 1x-1.25x
- Comunicar a incerteza junto com a estimativa

## Quando Usar

- Em toda estimativa de projeto ou feature significativa
- No planejamento de releases e roadmap
- Ao comprometer-se com prazos para stakeholders
- Na alocação de recursos e orçamento
- No planejamento de sprints e iterações

## Quando NÃO Usar

- Em tarefas triviais e repetitivas (ex: criar endpoint CRUD padrão)
- Quando existe benchmark preciso de tarefas idênticas
- Em correções de bugs simples e bem diagnosticados
- Quando o stakeholder pede "ordem de magnitude" e não compromisso

## Exemplos

### Exemplo 1: PERT para Feature de Checkout
```
Tarefa: Implementar fluxo de checkout completo

Otimista (O):   8 dias (tudo pronto, sem surpresas)
Mais provável (M): 13 dias (complexidade normal)
Pessimista (P):    25 dias (integrações problemáticas)

Estimativa PERT: (8 + 4*13 + 25) / 6 = 14.2 dias
Desvio padrão: (25 - 8) / 6 = 2.8 dias

Comunicar ao stakeholder:
  - Provável: 14 dias
  - Confiança de 85%: 17 dias (E + 1S)
  - Confiança de 95%: 20 dias (E + 2S)
```

### Exemplo 2: Decomposição Bottom-Up
```
Feature: Sistema de notificações

Subtarefas:
  Modelagem de dados e migração:       0.5 dia
  API de preferências de notificação:  1 dia
  Serviço de envio de e-mail:          1.5 dia
  Serviço de envio de push:            1.5 dia
  Template engine para notificações:   1 dia
  Fila de processamento assíncrono:    1 dia
  Testes unitários e integração:       1.5 dia
  Testes e2e:                          1 dia
  Documentação:                        0.5 dia
                                    ----------
  Subtotal:                            9.5 dias
  Buffer de integração (20%):          1.9 dia
  Buffer de risco (15%):               1.4 dia
                                    ----------
  Total estimado:                     12.8 dias (~13 dias)
```

### Exemplo 3: Fatores de Ajuste por Analogia
```
Projeto anterior similar:
  "Sistema de relatórios v1": 6 semanas com equipe de 3

Projeto atual: "Sistema de relatórios v2"

Fatores de ajuste:
  + Equipe nova (sem experiência no domínio): x1.3
  + Tecnologia diferente (React -> Vue):       x1.2
  - Requisitos mais claros (já feito antes):   x0.8
  + Integrações adicionais:                    x1.15

  Fator combinado: 1.3 * 1.2 * 0.8 * 1.15 = 1.44

Estimativa ajustada: 6 semanas * 1.44 = 8.6 semanas (~9 semanas)
```
