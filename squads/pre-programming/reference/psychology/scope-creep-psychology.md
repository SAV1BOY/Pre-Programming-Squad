# Psicologia do Scope Creep

## Viés/Efeito

**Psicologia do Scope Creep:** A tendência de aceitar incrementos 'pequenos' de escopo que individualmente parecem razoáveis mas acumulativamente transformam o projeto. Cada 'já que estamos aqui' adiciona 5% de escopo. Depois de 10 adições, o projeto é 50% maior que o original.

## Como se Manifesta em Pré-Programação

### Em Reuniões de Discovery
Stakeholder menciona 'seria bom se também fizesse X'. Ninguém anota como scope change. X vira expectativa. No handoff, X está faltando e é considerado bug.

### Em Design Reviews
Arquiteto adiciona 'melhorias' que não estavam no escopo: 'já que estamos refatorando, vamos melhorar o cache'. Cache improvement vira 2 sprints extras.

### No Dia-a-Dia
Cada pessoa adiciona 'só mais uma coisinha'. Product owner, designer, dev, stakeholder. 4 pessoas × 3 adições = 12 itens fora do escopo original.

## Como Mitigar

### 1. Scope Registry Formal
Todo item de escopo registrado com ID. Qualquer adição passa por avaliação formal: impacto no prazo, impacto no esforço, quem aprova.

**Implementação prática no squad:**
- Aplicar durante as fases relevantes do pipeline
- Registrar decisões influenciadas por este viés no decision log
- Revisar em RalphLoop retro se o viés foi detectado e mitigado

### 2. Impacto Explícito
Para cada adição proposta: 'Se adicionarmos X, o prazo aumenta em Y dias e o esforço em Z story points. Aceitar?'

**Implementação prática no squad:**
- Aplicar durante as fases relevantes do pipeline
- Registrar decisões influenciadas por este viés no decision log
- Revisar em RalphLoop retro se o viés foi detectado e mitigado

### 3. Scope Cuts Registry
Manter registro do que foi cortado e por quê. Referência para quando 'podemos adicionar de volta?' surgir.

**Implementação prática no squad:**
- Aplicar durante as fases relevantes do pipeline
- Registrar decisões influenciadas por este viés no decision log
- Revisar em RalphLoop retro se o viés foi detectado e mitigado

## Referências
- Kahneman, D. — Thinking, Fast and Slow
- Tversky, A. & Kahneman, D. — Judgment under Uncertainty
- Aplicação prática no pipeline de pré-programação do MMOS
