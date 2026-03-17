# Viés de Normalidade em Avaliação de Riscos

## Viés/Efeito
**Viés de Normalidade em Avaliação de Riscos:** A tendência de subestimar tanto a probabilidade quanto os efeitos de desastres porque 'sempre funcionou assim' — levando a preparação insuficiente para cenários de falha.

## Como se Manifesta em Pré-Programação

- 'O database nunca caiu, não precisa de failover'
- Não planejar rollback porque deploys 'sempre' dão certo
- Subestimar impacto de picos de tráfego porque nunca aconteceram
- Ignorar riscos de segurança porque 'nunca fomos atacados'

## Como Mitigar

### 1. Estudar incidentes de empresas similares, não apen
Estudar incidentes de empresas similares, não apenas histórico próprio

### 2. Usar pre-mortem: imaginar que o projeto falhou e a
Usar pre-mortem: imaginar que o projeto falhou e analisar por quê

### 3. Exigir rollback plan para todo deploy significativ
Exigir rollback plan para todo deploy significativo

### 4. Incluir Failure Analyst no pipeline de pré-program
Incluir Failure Analyst no pipeline de pré-programação

## Referências
- Kahneman, D. — Thinking, Fast and Slow
- Tversky, A. & Kahneman, D. — Judgment under Uncertainty
- Aplicação prática no pipeline de pré-programação do MMOS
