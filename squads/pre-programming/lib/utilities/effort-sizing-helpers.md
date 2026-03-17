# Auxiliares de Dimensionamento de Esforço (Effort Sizing Helpers)

## Propósito
Fornecer modelos e referências para dimensionamento de esforço de desenvolvimento, incluindo tabelas de referência por tipo de tarefa, fatores de ajuste e métodos de estimativa para uso durante a fase de pré-programação.

## Fórmulas e Modelos

### Tabela de Referência de Esforço Base (T-Shirt Sizing)

```
Tamanho    Story Points    Dias (1 dev)    Complexidade
---------- -------------- --------------- ----------------
XS          1               0.5             Trivial, sem ambiguidade
S           2               1               Simples, caminho claro
M           3-5             2-3             Moderado, alguma incerteza
L           8               5               Complexo, múltiplas partes
XL          13              8-10            Muito complexo, alto risco
XXL         21+             10+             Épico, precisa ser decomposto
```

### Tabela de Esforço por Tipo de Tarefa

```
Tipo de Tarefa                    Esforço Base (dias)    Desvio
---------------------------------  -------------------    ------
Endpoint CRUD simples              0.5                    +0.5
Endpoint com lógica de negócio     1-2                    +1
Integração com API externa         2-3                    +2
Migração de schema de banco        1-2                    +1
Componente de UI simples           0.5-1                  +0.5
Componente de UI complexo          2-3                    +2
Pipeline de dados                  3-5                    +3
Implementação de autenticação      3-5                    +2
Setup de CI/CD                     2-3                    +2
Configuração de monitoramento      1-2                    +1
```

### Fatores de Ajuste

```
Esforço_Final = Esforço_Base * F_equipe * F_tech * F_dominio * F_qualidade

F_equipe (experiência da equipe):
  Muito experiente:    0.7
  Experiente:          0.9
  Média:               1.0
  Pouca experiência:   1.3
  Nova na tecnologia:  1.6

F_tech (maturidade da tecnologia):
  Tecnologia madura e conhecida:  0.8
  Tecnologia conhecida:           1.0
  Tecnologia nova para a equipe:  1.3
  Tecnologia experimental:        1.8

F_dominio (complexidade do domínio):
  Domínio simples e conhecido:    0.8
  Domínio moderado:               1.0
  Domínio complexo:               1.3
  Domínio desconhecido:           1.5

F_qualidade (nível de qualidade exigido):
  Protótipo/MVP:                  0.6
  Produto padrão:                 1.0
  Alta qualidade (fintech/saúde): 1.4
  Crítico (aviação/nuclear):      2.0
```

### Fórmula de Buffer por Perfil de Projeto

```
Buffer_Total = Esforço_Desenvolvimento * Fator_Buffer

Fator_Buffer por perfil:
  Projeto bem definido, equipe experiente:   0.15 (15%)
  Projeto moderado, equipe mista:            0.25 (25%)
  Projeto com incertezas, equipe nova:       0.40 (40%)
  Projeto exploratório, tecnologia nova:     0.60 (60%)

Composição do buffer:
  Integração e dependências:  40% do buffer
  Bugs e retrabalho:          25% do buffer
  Reuniões e comunicação:     20% do buffer
  Imprevistos:                15% do buffer
```

### Velocidade da Equipe

```
Velocidade = SP_Entregues / Sprint

Capacidade_Sprint = Velocidade_Media * (1 - Fator_Ausencia)

Fator_Ausencia:
  Férias planejadas:    X dias / dias_sprint
  Feriados:             Y dias / dias_sprint
  Reuniões recorrentes: ~15% (média)
  Suporte/manutenção:   ~10% (se aplicável)
```

## Como Usar

1. **Identificar o tipo** de cada tarefa na tabela de referência
2. **Atribuir tamanho** T-Shirt inicial
3. **Aplicar fatores de ajuste** relevantes
4. **Calcular buffer** baseado no perfil do projeto
5. **Validar** com a equipe em sessão de estimativa
6. **Registrar** premissas e fatores usados

## Inputs e Outputs

### Inputs
- Lista de tarefas decompostas
- Perfil da equipe (experiência, familiaridade)
- Stack tecnológica do projeto
- Nível de qualidade exigido
- Dados históricos de velocidade (se disponíveis)

### Outputs
- Estimativa em story points e dias por tarefa
- Estimativa total do projeto com buffer
- Fatores de ajuste aplicados e justificativas
- Intervalo de confiança (otimista/pessimista)
- Cronograma sugerido com marcos

## Exemplos

### Exemplo: Dimensionamento de Feature Completa
```
Feature: Sistema de Notificações Push

Decomposição:
  1. Modelagem e migração DB         (S)   1 dia
  2. API de registro de dispositivo  (S)   1 dia
  3. API de preferências             (M)   2 dias
  4. Integração com FCM/APNS         (L)   5 dias
  5. Serviço de enfileiramento       (M)   3 dias
  6. Template engine                 (M)   2 dias
  7. Testes unitários                (S)   1.5 dias
  8. Testes de integração            (M)   2 dias
  9. Documentação                    (XS)  0.5 dia
                                    ----------
  Subtotal:                          18 dias

Fatores de ajuste:
  F_equipe = 1.0 (equipe experiente)
  F_tech = 1.3 (FCM/APNS é novo para a equipe)
  F_dominio = 1.0 (domínio conhecido)
  F_qualidade = 1.0 (produto padrão)

Esforço ajustado: 18 * 1.0 * 1.3 * 1.0 * 1.0 = 23.4 dias

Buffer (25% - projeto moderado): 5.85 dias

Total: 29.25 dias -> ~6 semanas (1 dev)
       ou ~3 semanas (2 devs com fator de comunicação 1.15)
```
