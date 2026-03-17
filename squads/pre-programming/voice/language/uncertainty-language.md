# Linguagem de Incerteza

## Propósito

Comunicar níveis de confiança e incerteza com honestidade e precisão. Em pré-programação, muitas decisões são tomadas com informação incompleta. A linguagem de incerteza permite distinguir entre o que sabemos, o que estimamos, o que assumimos e o que desconhecemos — evitando falsa certeza e paralisia por falta de dados.

## Palavras-chave

`nível de confiança`, `premissa`, `hipótese`, `validação pendente`, `incógnita conhecida`, `incógnita desconhecida`, `faixa estimada`, `margem de erro`, `evidência parcial`, `sinal fraco`

## Frases Modelo

### Escala de Confiança

- **Alta confiança (>80%):** "Os dados confirmam que [X]. Baseado em [evidência concreta: métricas, testes, histórico]."
- **Confiança moderada (50-80%):** "A evidência parcial sugere [X]. Baseado em [dados incompletos, analogia com sistema Y, opinião de especialista]. Validação necessária: [ação]."
- **Baixa confiança (20-50%):** "A hipótese é [X], mas não temos dados suficientes. Baseado em [intuição informada, benchmark de terceiros, documentação desatualizada]. Recomendo spike de [N dias] antes de decidir."
- **Incerteza declarada (<20%):** "Não temos informação suficiente para estimar [X]. Os dados necessários são [lista]. Caminho para obter: [ação, prazo, responsável]."

### Frases de Premissa Explícita

- "Esta estimativa assume que [premissa]. Se [premissa] não se confirmar, o impacto na estimativa é [variação]."
- "Premissas do plano: (1) [A], (2) [B], (3) [C]. Validação de premissas programada para [data]."
- "Estamos assumindo [X] porque [razão]. Risco da premissa ser falsa: [consequência]."

### Frases de Estimativa com Faixa

- "Estimativa: [N] dias (melhor caso: [X], caso esperado: [Y], pior caso: [Z]). A variação deve-se a [fatores de incerteza]."
- "O volume esperado é entre [min] e [max], com valor mais provável de [modal]. A incerteza é alta porque [razão]."
- "Com os dados atuais, a faixa de confiança de 80% é [X a Y]. Para estreitar, precisamos de [informação específica]."

### Frases de Incógnita Declarada

- "Incógnita conhecida: não sabemos [X]. Impacto se [X] for desfavorável: [consequência]. Plano para descobrir: [ação até data]."
- "Possíveis incógnitas desconhecidas nesta área: [domínio não explorado, integração não testada, comportamento sob carga]. Mitigação: [spike, POC, canary release]."
- "Estamos decidindo com informação incompleta. O que sabemos é suficiente para [próximo passo], mas insuficiente para [compromisso de longo prazo]."

## Anti-Padrões Linguísticos

### 1. Falsa Certeza
**Errado:** "A migração vai levar 3 semanas."
**Correto:** "Estimativa da migração: 3 semanas (melhor caso: 2, pior caso: 5). A principal incerteza é a compatibilidade com o sistema legado, que ainda não testamos. Spike de 2 dias planejado para reduzir incerteza."

### 2. Falsa Precisão
**Errado:** "O custo será de R$ 47.832,00."
**Correto:** "O custo estimado é de R$ 45k a R$ 55k, dependendo de [variáveis]. O principal fator de variação é [X]."

### 3. Incerteza sem Plano
**Errado:** "Não temos certeza se vai funcionar."
**Correto:** "Não validamos [aspecto X] ainda. Plano: POC de 3 dias com critério de sucesso [métrica > valor]. Se não atingir, alternativa é [B]."

### 4. Premissa Implícita
**Errado:** "Vai funcionar no volume de produção."
**Correto:** "Testamos com 10% do volume de produção. Premissa: o comportamento escala linearmente. Validação: load test com 100% do volume antes do go-live."

### 5. Opinião como Fato
**Errado:** "Esse design é o correto."
**Correto:** "Esse design atende os requisitos conhecidos. Nível de confiança: moderado — não validamos [cenário X] e [requisito Y] ainda está sendo refinado com produto."

### 6. Paralisia por Incerteza
**Errado:** "Não podemos decidir sem mais dados."
**Correto:** "A informação atual é suficiente para decidir [escopo limitado]. Para decidir [escopo maior], precisamos de [dados específicos] que obtemos em [prazo]. Recomendo avançar com [escopo limitado] enquanto coletamos o restante."
