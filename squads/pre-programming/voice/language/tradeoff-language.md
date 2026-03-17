# Linguagem de Trade-offs

## Propósito

Tornar explícitos os trade-offs em cada decisão técnica. Toda escolha de engenharia envolve renúncias; a função desta linguagem é garantir que essas renúncias sejam conscientes, documentadas e comunicadas a todos os stakeholders. Eliminar a ilusão de que existe solução sem custo.

## Palavras-chave

`trade-off`, `em troca de`, `ao custo de`, `priorizando X sobre Y`, `renúncia consciente`, `alternativa descartada`, `tensão entre`, `equilíbrio`, `otimizado para`, `sacrificando`

## Frases Modelo

### Estrutura Padrão de Trade-off

- "Escolhemos [A] em vez de [B] porque [justificativa]. O custo dessa escolha é [consequência], que mitigamos com [ação]."
- "Priorizamos [atributo X] sobre [atributo Y] neste contexto porque [razão]. Se as condições mudarem para [cenário], devemos reavaliar."
- "A alternativa [B] foi descartada porque [motivo concreto], apesar de ser superior em [aspecto]."

### Frases de Tensão Explícita

- "Existe uma tensão entre [consistência] e [disponibilidade] neste design. Optamos por [disponibilidade] porque [razão]."
- "Ganhar [velocidade de entrega] aqui significa aceitar [débito técnico específico]. O plano de endereçamento é [ação até data]."
- "Otimizamos para [latência] ao custo de [custo de infraestrutura]. O custo adicional é de R$ [X]/mês, justificado pelo impacto de [Y] na conversão."

### Frases de Decisão Reversível vs. Irreversível

- "Esta é uma decisão reversível (porta de duas vias): podemos mudar de [A] para [B] em [tempo] com custo de [esforço]."
- "Esta é uma decisão irreversível (porta de uma via): migrar dados para [formato X] impede retorno a [formato Y] sem [custo elevado]. Por isso, requer análise profunda."

### Frases de Comparação

- "A Opção A é superior em [critério 1, 2] mas inferior em [critério 3, 4]. A Opção B inverte essa relação. Dado que [critérios 1, 2] são prioritários neste contexto, recomendamos A."
- "Nenhuma opção atende todos os requisitos simultaneamente. O trade-off central é entre [X] e [Y]."

## Anti-Padrões Linguísticos

### 1. Solução sem Custo
**Errado:** "Essa abordagem é a melhor em todos os aspectos."
**Correto:** "Essa abordagem é a mais adequada para nosso contexto. Os trade-offs aceitos são: [lista]. As alternativas foram descartadas por: [motivos]."

### 2. Trade-off Oculto
**Errado:** "Vamos usar microserviços para escalar melhor."
**Correto:** "Microserviços permitem escalar serviços individualmente, ao custo de complexidade operacional (tracing distribuído, deploy independente, eventual consistency). Dado nosso time de 4 pessoas, esse custo operacional é alto. Alternativa: monolito modular, que escala menos granularmente mas é operável pelo time atual."

### 3. Falso Dilema
**Errado:** "Ou fazemos rápido ou fazemos bem feito."
**Correto:** "Podemos entregar em 2 semanas com escopo reduzido (features A e B, sem C) e qualidade completa, ou em 4 semanas com escopo completo. A terceira opção — escopo completo em 2 semanas — exigiria cortar testes e observabilidade, o que não recomendamos."

### 4. Otimismo Unilateral
**Errado:** "A migração vai melhorar tudo."
**Correto:** "A migração melhora [latência, custo operacional]. Porém, introduz [período de instabilidade de 2 semanas, curva de aprendizado do novo sistema, risco de regressão]. Mitigações planejadas: [lista]."

### 5. Comparação Injusta
**Errado:** "A solução nova é muito melhor que a atual."
**Correto:** "A solução nova é superior em [critérios], mas a atual tem vantagens em [estabilidade comprovada, conhecimento do time, custo zero de migração]. A migração se justifica porque [razão quantificada]."

### 6. Decisão Irreversível Tratada como Reversível
**Errado:** "Se não funcionar, a gente volta atrás."
**Correto:** "Reverter essa decisão requer [esforço específico]. Antes de prosseguir, precisamos de [validação X] para reduzir o risco de reversão."
