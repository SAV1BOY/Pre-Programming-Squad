# Escalação de Compromisso em Projetos

## Viés/Efeito

**Escalação de Compromisso em Projetos:** A tendência de continuar investindo em projeto ou abordagem falha porque já investimos muito — em vez de cortar perdas. Staw (1976) demonstrou que pessoas investem mais em projetos falhando quando são responsáveis pela decisão inicial.

## Como se Manifesta em Pré-Programação

### Em Projetos Atrasados
Projeto está 3 meses atrasado e 2x acima do budget. Ninguém propõe cancelar porque 'já investimos tanto'. Investem mais 3 meses e ficam 4x acima do budget.

### Em Arquitetura Problemática
Arquitetura escolhida está gerando dor. Refatorar custaria 2 sprints. Mas 'já investimos 6 meses nela', então continuam com workarounds que custam 1 sprint cada.

### Em Tecnologia Errada
Stack escolhida não atende performance requirements. Migrar custaria 3 semanas. Mas 'já escrevemos 10k LOC', então gastam 6 semanas otimizando o que nunca vai atingir o target.

## Como Mitigar

### 1. Kill Criteria Pré-Definidos
Antes de iniciar, definir: 'Cancelamos se: budget exceder X, prazo exceder Y, ou requisito Z não for atendível'. Decisão automática, não emocional.

**Implementação prática no squad:**
- Aplicar durante as fases relevantes do pipeline
- Registrar decisões influenciadas por este viés no decision log
- Revisar em RalphLoop retro se o viés foi detectado e mitigado

### 2. Separar Decisor de Investidor
Quem decide continuar ou cancelar NÃO deve ser a mesma pessoa que propôs o projeto. Elimina viés de 'proteger minha decisão'.

**Implementação prática no squad:**
- Aplicar durante as fases relevantes do pipeline
- Registrar decisões influenciadas por este viés no decision log
- Revisar em RalphLoop retro se o viés foi detectado e mitigado

### 3. Revisão em Cada Gate
Em cada gate transition, perguntar: 'Se começássemos do zero hoje, com o que sabemos agora, faríamos o mesmo?' Se não, considerar pivotar.

**Implementação prática no squad:**
- Aplicar durante as fases relevantes do pipeline
- Registrar decisões influenciadas por este viés no decision log
- Revisar em RalphLoop retro se o viés foi detectado e mitigado

## Referências
- Kahneman, D. — Thinking, Fast and Slow
- Tversky, A. & Kahneman, D. — Judgment under Uncertainty
- Aplicação prática no pipeline de pré-programação do MMOS
