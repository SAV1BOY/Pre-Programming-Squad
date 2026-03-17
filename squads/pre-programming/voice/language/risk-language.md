# Linguagem de Risco

## Propósito

Comunicar riscos técnicos de forma clara, classificada e acionável. Riscos devem ser apresentados com probabilidade, impacto, gatilho e plano de mitigação — nunca como alertas vagos. A linguagem de risco permite priorização racional e evita tanto o alarmismo quanto a negligência.

## Palavras-chave

`risco identificado`, `probabilidade`, `impacto`, `gatilho`, `mitigação`, `aceitação`, `transferência`, `contingência`, `exposição`, `blast radius`, `cenário de falha`, `modo de degradação`

## Frases Modelo

### Declaração de Risco Estruturada

- "Risco: [evento]. Probabilidade: [alta/média/baixa — com justificativa]. Impacto: [descrição quantificada]. Mitigação: [ação concreta]."
- "Se [gatilho] acontecer, o efeito será [impacto em termos mensuráveis]. O plano de contingência é [ação]."
- "A exposição atual é [descrição]. Sem mitigação, o cenário projetado em [prazo] é [consequência]."

### Classificação de Risco

- "Este é um risco de **severidade crítica**: afeta [todos os usuários / receita / dados] com [tempo de recuperação estimado]."
- "Este é um risco de **severidade alta**: afeta [funcionalidade X] para [Y% dos usuários], recuperável em [tempo]."
- "Este é um risco de **severidade média**: causa [degradação] em [cenário específico], com workaround disponível."
- "Este é um risco de **severidade baixa**: impacto cosmético ou restrito a [cenário raro], sem efeito em produção normal."

### Frases de Mitigação

- "Mitigação proposta: [ação]. Reduz probabilidade de [X%] para [Y%] ao custo de [esforço/recurso]."
- "Risco aceito: [descrição]. Justificativa: [custo de mitigação excede impacto esperado]. Revisão programada para [data]."
- "Risco transferido para [terceiro/seguro/SLA contratual]. Cobertura: [o que está coberto]. Lacuna: [o que não está]."

### Frases de Monitoramento

- "Indicador antecedente: [métrica que sinaliza materialização do risco]. Threshold: [valor]. Alerta configurado: [sim/não]."
- "Revisão de risco programada para [data], com owner [pessoa], considerando [novos dados disponíveis]."

## Anti-Padrões Linguísticos

### 1. Alarmismo sem Substância
**Errado:** "Isso é muito arriscado!"
**Correto:** "O risco principal é [evento específico], com probabilidade [nível] baseada em [evidência]. O impacto seria [descrição quantificada]. Mitigação recomendada: [ação]."

### 2. Risco sem Probabilidade
**Errado:** "O servidor pode cair."
**Correto:** "O servidor apresentou 3 quedas nos últimos 90 dias, causadas por memory leak no serviço X. Sem correção, estimamos recorrência a cada ~30 dias. Impacto: 15 minutos de indisponibilidade afetando ~5.000 usuários."

### 3. Risco sem Plano
**Errado:** "Existe risco de perda de dados."
**Correto:** "Existe risco de perda de dados no cenário de [falha específica]. Mitigação: implementar WAL archiving com retenção de 7 dias (esforço: 2 dias). Contingência: restore do backup diário com RPO de até 24h."

### 4. Normalização de Risco
**Errado:** "Sempre foi assim, nunca deu problema."
**Correto:** "O risco existe há [tempo] sem materialização. Porém, a exposição aumentou de [X] para [Y] porque [mudança de contexto]. Recomendo reavaliação."

### 5. Risco Binário
**Errado:** "Pode ou não dar problema."
**Correto:** "Identifico 3 cenários: (1) funcionamento normal [70% probabilidade], (2) degradação parcial [25% probabilidade, impacto: latência 3x], (3) falha total [5% probabilidade, impacto: downtime de ~30min]."

### 6. Transferência Silenciosa de Risco
**Errado:** "O time de infra vai cuidar disso."
**Correto:** "O risco operacional será gerenciado pelo time de infra, conforme alinhado com @fulano em [data]. SLA acordado: [tempo de resposta]. Escalonamento: [processo] se SLA não for atendido."
