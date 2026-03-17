# Efeito de Enquadramento em Requisitos

## Viés/Efeito

**Efeito de Enquadramento em Requisitos:** A forma como uma informação é apresentada influencia dramaticamente como é interpretada, independente do conteúdo objetivo. Tversky e Kahneman (1981) demonstraram que as mesmas estatísticas geram decisões opostas dependendo do enquadramento.

## Como se Manifesta em Pré-Programação

### Na Priorização
'Feature que aumenta conversão em 2%' vs 'Feature que evita perda de R$500k/ano' — mesmo impacto, prioridades completamente diferentes dependendo do frame.

### Em Estimativas
'Projeto tem 80% de chance de sucesso' vs 'Projeto tem 20% de chance de falhar' — mesma probabilidade, reações opostas do stakeholder.

### Na Comunicação de Riscos
Risco apresentado como '1 em 100 deploys causam incidente' parece aceitável. '12 incidentes por ano' parece inaceitável. Mesmo número.

## Como Mitigar

### 1. Reformulação Neutra
Exigir que requisitos sejam escritos em linguagem factual e neutra. Não 'urgente', 'crítico', 'trivial' — mas métricas concretas.

**Implementação prática no squad:**
- Aplicar durante as fases relevantes do pipeline
- Registrar decisões influenciadas por este viés no decision log
- Revisar em RalphLoop retro se o viés foi detectado e mitigado

### 2. Dual Framing
Apresentar toda informação de duas formas (ganho e perda) para neutralizar o viés. Se só apresentar um lado, a decisão é enviesada.

**Implementação prática no squad:**
- Aplicar durante as fases relevantes do pipeline
- Registrar decisões influenciadas por este viés no decision log
- Revisar em RalphLoop retro se o viés foi detectado e mitigado

### 3. Critérios Objetivos de Priorização
Usar scoring models (WSJF, Value×Effort) que forçam quantificação objetiva, independente do enquadramento narrativo.

**Implementação prática no squad:**
- Aplicar durante as fases relevantes do pipeline
- Registrar decisões influenciadas por este viés no decision log
- Revisar em RalphLoop retro se o viés foi detectado e mitigado

## Referências
- Kahneman, D. — Thinking, Fast and Slow
- Tversky, A. & Kahneman, D. — Judgment under Uncertainty
- Aplicação prática no pipeline de pré-programação do MMOS
