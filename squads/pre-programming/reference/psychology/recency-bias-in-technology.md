# Viés de Recência em Escolhas Tecnológicas

## Viés/Efeito

**Viés de Recência em Escolhas Tecnológicas:** A tendência de dar peso desproporcional a experiências recentes ao tomar decisões técnicas, ignorando dados de longo prazo e análise estatística.

## Como se Manifesta em Pré-Programação

### Pós-Incidente
Após incidente causado por PostgreSQL, time propõe migrar para MongoDB. Ignora: 200 projetos bem-sucedidos com PostgreSQL vs 1 incidente causado por query mal otimizada, não pelo database.

### Pós-Sucesso
Último projeto usou React e foi sucesso. Próximo projeto também será React — mesmo que seja backend puro onde React é irrelevante.

### Influência de Conteúdo
Dev leu artigo sobre Deno ontem e agora propõe migrar de Node. Artigo mostrava um caso de uso específico que não se aplica ao projeto atual.

## Como Mitigar

### 1. Reference Class Forecasting
Basear decisões em amostra adequada (10+ projetos), não em 1-2 experiências recentes. Manter banco de dados de decisões e resultados.

**Implementação prática no squad:**
- Aplicar durante as fases relevantes do pipeline
- Registrar decisões influenciadas por este viés no decision log
- Revisar em RalphLoop retro se o viés foi detectado e mitigado

### 2. Cooling Period
Após incidente, esperar 1-2 semanas antes de tomar decisões de stack. Decisões reativas pós-incidente são quase sempre enviesadas.

**Implementação prática no squad:**
- Aplicar durante as fases relevantes do pipeline
- Registrar decisões influenciadas por este viés no decision log
- Revisar em RalphLoop retro se o viés foi detectado e mitigado

### 3. Análise Multi-Critério
Avaliar tecnologias em 5+ critérios objetivos. 'Experiência recente' pode ser UM critério, mas não o único.

**Implementação prática no squad:**
- Aplicar durante as fases relevantes do pipeline
- Registrar decisões influenciadas por este viés no decision log
- Revisar em RalphLoop retro se o viés foi detectado e mitigado

## Referências
- Kahneman, D. — Thinking, Fast and Slow
- Tversky, A. & Kahneman, D. — Judgment under Uncertainty
- Aplicação prática no pipeline de pré-programação do MMOS
