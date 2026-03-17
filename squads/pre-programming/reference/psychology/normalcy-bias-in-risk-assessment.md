# Viés de Normalidade em Avaliação de Riscos

## Viés/Efeito

**Viés de Normalidade em Avaliação de Riscos:** A tendência de subestimar probabilidade e impacto de desastres porque 'sempre funcionou assim'. Omer e Alon (1994) demonstraram que pessoas expostas a desastres frequentes são MAIS complacentes, não menos.

## Como se Manifesta em Pré-Programação

### Em Avaliação de Infraestrutura
'O database nunca caiu em 2 anos' — portanto, não precisa de failover. Até que cai e o downtime custa R$50k/hora.

### Em Planejamento de Rollback
'Deploys sempre dão certo' — portanto, rollback plan é formalidade. Até que um deploy quebra produção em sexta às 18h.

### Em Segurança
'Nunca fomos atacados' — portanto, security review é overkill. Até que são.

## Como Mitigar

### 1. Pre-Mortem Obrigatório
Em todo projeto, fazer exercício: 'Imaginem que este projeto causou um incidente grave. O que aconteceu?' Forçar o time a pensar em cenários de falha.

**Implementação prática no squad:**
- Aplicar durante as fases relevantes do pipeline
- Registrar decisões influenciadas por este viés no decision log
- Revisar em RalphLoop retro se o viés foi detectado e mitigado

### 2. Dados Externos
Não basear avaliação de risco apenas em histórico interno. Consultar: incidentes de empresas similares, estatísticas do setor, OWASP.

**Implementação prática no squad:**
- Aplicar durante as fases relevantes do pipeline
- Registrar decisões influenciadas por este viés no decision log
- Revisar em RalphLoop retro se o viés foi detectado e mitigado

### 3. Checklist de Defesas
Para cada componente crítico, verificar: tem failover? Tem rollback? Tem monitoramento? Tem alerta? Se não, o risco está subestimado.

**Implementação prática no squad:**
- Aplicar durante as fases relevantes do pipeline
- Registrar decisões influenciadas por este viés no decision log
- Revisar em RalphLoop retro se o viés foi detectado e mitigado

## Referências
- Kahneman, D. — Thinking, Fast and Slow
- Tversky, A. & Kahneman, D. — Judgment under Uncertainty
- Aplicação prática no pipeline de pré-programação do MMOS
