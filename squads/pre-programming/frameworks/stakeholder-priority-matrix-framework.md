# Stakeholder Priority Matrix Framework

## Propósito
Mapear, classificar e gerenciar expectativas de stakeholders para evitar conflitos, desalinhamentos e surpresas durante o pipeline de pré-programação.

## Problema que Resolve
Stakeholders têm expectativas diferentes (e às vezes conflitantes). Sem mapeamento explícito, o time descobre conflitos tarde demais e perde tempo mediando em vez de decidindo.

## Quando Usar
- No início de todo projeto (durante intake/discovery)
- Quando há múltiplos stakeholders com interesses divergentes
- Quando priorização de escopo gera conflito
- Antes de decisões irreversíveis que afetam múltiplas partes

## Matriz de Classificação

### Eixo 1: Influência (poder de decisão)
- **Alta:** Pode aprovar/vetar decisões, controla budget ou recursos
- **Baixa:** Pode opinar mas não tem poder de veto

### Eixo 2: Interesse (envolvimento)
- **Alto:** Resultado do projeto impacta diretamente seu trabalho/métricas
- **Baixo:** Impacto indireto ou informacional

### Quadrantes

| | Alta Influência | Baixa Influência |
|--|----------------|-----------------|
| **Alto Interesse** | **GERENCIAR DE PERTO** — Engajar ativamente, consultar em decisões-chave, manter informado proativamente | **MANTER INFORMADO** — Updates regulares, canal aberto para feedback, não ignorar |
| **Baixo Interesse** | **MANTER SATISFEITO** — Resumos executivos, escalar quando necessário, não sobrecarregar com detalhes | **MONITORAR** — Informar em marcos, estar disponível se interesse aumentar |

## Processo

### Passo 1 — Listar Stakeholders
Para cada stakeholder:
```
Nome: [nome]
Papel: [product owner / CTO / tech lead / cliente / compliance / etc.]
Influência: [alta / baixa]
Interesse: [alto / baixo]
Expectativa declarada: [o que disse que quer]
Expectativa implícita: [o que provavelmente quer mas não disse]
Potencial de conflito com: [outros stakeholders]
```

### Passo 2 — Identificar Conflitos
Mapear onde expectativas de diferentes stakeholders são incompatíveis:
- PO quer escopo grande, CTO quer simplicidade
- Compliance exige features, timeline é apertado
- Time A quer API X, Time B quer API Y

### Passo 3 — Estratégia por Quadrante
Definir cadência e canal de comunicação para cada stakeholder baseado no quadrante.

### Passo 4 — Validar em Checkpoints
Em cada gate transition, verificar:
- [ ] Stakeholders de alta influência + alto interesse foram consultados
- [ ] Conflitos identificados estão resolvidos ou escalados
- [ ] Expectativas implícitas foram tornadas explícitas

## Exemplo Real
```
Projeto: Migração de Sistema de Pagamentos

Stakeholders:
1. CTO (Alta Influência, Alto Interesse) → GERENCIAR DE PERTO
   - Expectativa: Migração sem downtime, arquitetura moderna
   - Risco: Pode vetar se arquitetura não convencer

2. Head de Compliance (Alta Influência, Baixo Interesse) → MANTER SATISFEITO
   - Expectativa: PCI-DSS compliance mantido
   - Risco: Pode bloquear se compliance não for garantido

3. Time de Suporte (Baixa Influência, Alto Interesse) → MANTER INFORMADO
   - Expectativa: Não aumentar volume de tickets
   - Risco: Feedback valioso sobre edge cases de clientes

4. Marketing (Baixa Influência, Baixo Interesse) → MONITORAR
   - Expectativa: Sistema continua funcionando
   - Risco: Nenhum, mas informar em go-live

Conflito identificado: CTO quer microservices, Compliance quer audit trail centralizado
→ Resolução: Event sourcing com audit log centralizado (ADR-007)
```

## Armadilhas
- **Tratar todos com mesma prioridade** → Stakeholder de alta influência + alto interesse precisa de 10x mais atenção
- **Ignorar stakeholders de baixa influência** → Eles têm contexto valioso (time de suporte conhece edge cases reais)
- **Não tornar expectativas implícitas em explícitas** → O que não foi dito gera surpresa depois
- **Assumir que silêncio = concordância** → Stakeholder quieto pode estar acumulando objeções
