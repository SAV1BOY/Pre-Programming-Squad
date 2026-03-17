# Viés de Retrospectiva em Revisão de Incidentes

## Viés/Efeito

**Viés de Retrospectiva em Revisão de Incidentes:** Após um incidente, pessoas acreditam que o resultado era previsível e que as decisões tomadas foram 'obviamente' erradas. Fischhoff (1975) demonstrou que saber o resultado aumenta dramaticamente a percepção de previsibilidade.

## Como se Manifesta em Pré-Programação

### Em Post-Mortems
'Era óbvio que o timeout de 30s ia causar cascade failure' — mas ninguém levantou esse risco antes do incidente. Com hindsight, tudo parece óbvio.

### Em Avaliação de Planejamento
'O planejamento deveria ter previsto isso' — quando o risco era de 2% de probabilidade e havia 50 outros riscos priorizados acima.

### Na Cultura de Blame
Engenheiro que tomou decisão razoável no momento é culpado porque, com informação nova, a decisão parece errada. Resultado: ninguém quer tomar decisões.

## Como Mitigar

### 1. Blameless Post-Mortems
Focar em sistemas, não em pessoas. Perguntar: 'O que no sistema permitiu que isso acontecesse?' em vez de 'Quem fez isso?'

**Implementação prática no squad:**
- Aplicar durante as fases relevantes do pipeline
- Registrar decisões influenciadas por este viés no decision log
- Revisar em RalphLoop retro se o viés foi detectado e mitigado

### 2. Documentar Contexto da Decisão
Em todo ADR, registrar: informações disponíveis na época, alternativas consideradas, incertezas conhecidas. Isso protege contra julgamento retroativo.

**Implementação prática no squad:**
- Aplicar durante as fases relevantes do pipeline
- Registrar decisões influenciadas por este viés no decision log
- Revisar em RalphLoop retro se o viés foi detectado e mitigado

### 3. Pre-Mortem Proativo
Em vez de esperar o incidente para aprender, fazer pre-mortem durante o design: imaginar que falhou e analisar por quê.

**Implementação prática no squad:**
- Aplicar durante as fases relevantes do pipeline
- Registrar decisões influenciadas por este viés no decision log
- Revisar em RalphLoop retro se o viés foi detectado e mitigado

## Referências
- Kahneman, D. — Thinking, Fast and Slow
- Tversky, A. & Kahneman, D. — Judgment under Uncertainty
- Aplicação prática no pipeline de pré-programação do MMOS
