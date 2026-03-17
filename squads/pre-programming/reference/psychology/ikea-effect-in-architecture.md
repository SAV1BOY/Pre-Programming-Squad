# Efeito IKEA em Decisões de Arquitetura

## Viés/Efeito

**Efeito IKEA em Decisões de Arquitetura:** A tendência de valorizar desproporcionalmente soluções que nós mesmos construímos, resistindo a substituí-las por alternativas objetivamente melhores. Norton, Mochon e Ariely (2012) demonstraram que pessoas valorizam 63% mais objetos que montaram parcialmente.

## Como se Manifesta em Pré-Programação

### No Build vs Buy
Time insiste em manter ORM customizado de 2018 com 47 bugs conhecidos porque 'é nosso' — em vez de migrar para biblioteca madura com 0 bugs.

### Em Architecture Reviews
Arquiteto que desenhou o sistema atual resiste a mudanças porque 'funciona há 3 anos' — ignorando que o contexto mudou e a dívida técnica acumulou.

### Em Avaliações de Stack
Time avalia 3 opções e 'coincidentemente' a solução interna sempre vence — mesmo quando análise objetiva mostra o contrário.

## Como Mitigar

### 1. Reviewer Externo
Incluir pelo menos 1 pessoa que NÃO construiu a solução atual na avaliação. Fresh eyes identificam sunk cost.

**Implementação prática no squad:**
- Aplicar durante as fases relevantes do pipeline
- Registrar decisões influenciadas por este viés no decision log
- Revisar em RalphLoop retro se o viés foi detectado e mitigado

### 2. Critérios Antes da Avaliação
Definir critérios objetivos ANTES de avaliar opções. Sem critérios, a avaliação é enviesada para confirmar a escolha existente.

**Implementação prática no squad:**
- Aplicar durante as fases relevantes do pipeline
- Registrar decisões influenciadas por este viés no decision log
- Revisar em RalphLoop retro se o viés foi detectado e mitigado

### 3. Pergunta Chave
'Se não tivéssemos construído isso, construiríamos hoje com o que sabemos agora?' Se a resposta é não, é hora de mudar.

**Implementação prática no squad:**
- Aplicar durante as fases relevantes do pipeline
- Registrar decisões influenciadas por este viés no decision log
- Revisar em RalphLoop retro se o viés foi detectado e mitigado

## Referências
- Kahneman, D. — Thinking, Fast and Slow
- Tversky, A. & Kahneman, D. — Judgment under Uncertainty
- Aplicação prática no pipeline de pré-programação do MMOS
