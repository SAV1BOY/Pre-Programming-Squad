# Viés de Autoridade em Decisões Técnicas

## Viés/Efeito

**Viés de Autoridade em Decisões Técnicas:** A tendência de aceitar decisões técnicas sem questionamento quando vêm de figuras de autoridade (CTOs, arquitetos seniores, tech leads). Milgram (1963) demonstrou que até 65% das pessoas obedecem autoridade mesmo contra seu próprio julgamento.

## Como se Manifesta em Pré-Programação

### Em Design Reviews
CTO propõe arquitetura. Ninguém questiona. 3 meses depois, decisão se mostra subótima. Todo mundo sabia mas ninguém falou.

### Na Escolha de Stack
'O principal engineer disse que devemos usar X' — vira verdade absoluta sem análise de alternativas. X pode ser ótimo para o contexto dele mas péssimo para o nosso.

### Em Adoção de 'Best Practices'
'O Google faz assim' encerra discussão. Mas o contexto do Google (10k engineers, bilhões de usuários) é irrelevante para time de 8.

## Como Mitigar

### 1. ADR Obrigatório
Toda decisão técnica requer ADR com trade-offs explícitos, independente de quem propõe. Senior ou junior, o processo é o mesmo.

**Implementação prática no squad:**
- Aplicar durante as fases relevantes do pipeline
- Registrar decisões influenciadas por este viés no decision log
- Revisar em RalphLoop retro se o viés foi detectado e mitigado

### 2. Psychological Safety
Criar ambiente onde questionar é encorajado. O Chief deve modelar: questionar abertamente decisões de seniores e elogiar juniors que questionam.

**Implementação prática no squad:**
- Aplicar durante as fases relevantes do pipeline
- Registrar decisões influenciadas por este viés no decision log
- Revisar em RalphLoop retro se o viés foi detectado e mitigado

### 3. Devil's Advocate Formal
Em decisões críticas, designar alguém para argumentar contra a proposta. Não é dissidência — é processo.

**Implementação prática no squad:**
- Aplicar durante as fases relevantes do pipeline
- Registrar decisões influenciadas por este viés no decision log
- Revisar em RalphLoop retro se o viés foi detectado e mitigado

## Referências
- Kahneman, D. — Thinking, Fast and Slow
- Tversky, A. & Kahneman, D. — Judgment under Uncertainty
- Aplicação prática no pipeline de pré-programação do MMOS
