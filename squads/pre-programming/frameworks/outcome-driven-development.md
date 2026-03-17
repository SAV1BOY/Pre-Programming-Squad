# Outcome-Driven Development

## Título e Propósito

O **Outcome-Driven Development** é um framework para alinhar todo o trabalho de desenvolvimento a resultados mensuráveis em vez de entregas de funcionalidades. O propósito é combater o padrão onde equipes entregam features no prazo mas não geram impacto — porque ninguém definiu qual impacto era esperado.

## Quando Usar

- No planejamento de qualquer projeto ou ciclo de desenvolvimento
- Quando a equipe entrega features mas o negócio não vê resultados
- Quando métricas de sucesso não estão definidas antes do início do trabalho
- Para alinhar expectativas entre produto, engenharia e negócio
- Quando é necessário priorizar entre múltiplas iniciativas concorrentes

## Conceitos-Chave

1. **Output vs. Outcome**: Output é o que entregamos (features, código, deploys). Outcome é o resultado que isso produz (retenção, receita, satisfação).
2. **Leading Indicator**: Métrica que muda rapidamente e indica se estamos no caminho certo. Exemplo: taxa de ativação.
3. **Lagging Indicator**: Métrica que muda lentamente e confirma o resultado. Exemplo: receita mensal recorrente.
4. **Teoria de Mudança**: A lógica que conecta nosso output ao outcome desejado: "Se entregarmos X, acreditamos que Y vai acontecer porque Z."
5. **Sucesso Técnico vs. Sucesso de Negócio**: Um projeto pode ser um sucesso técnico (entregou no prazo, sem bugs) mas fracasso de negócio (não moveu as métricas).

## Processo / Passos

### Passo 1 — Definir o Outcome Desejado
Pergunte: "Que mudança no mundo queremos ver como resultado deste trabalho?" Seja específico e mensurável.

### Passo 2 — Estabelecer Métricas
Defina 1-2 leading indicators e 1 lagging indicator. Cada métrica deve ter baseline (valor atual) e target (valor desejado).

### Passo 3 — Articular a Teoria de Mudança
Escreva: "Acreditamos que [output] vai causar [outcome] porque [mecanismo causal]."

### Passo 4 — Validar a Teoria
Pergunte: "Há evidência de que esse mecanismo causal funciona? Há contra-exemplos?" Busque dados que refutem, não que confirmem.

### Passo 5 — Projetar o Output Mínimo
Qual é o menor output que pode testar a teoria de mudança? Isso alinha com MVP thinking.

### Passo 6 — Definir Pontos de Verificação
Estabeleça checkpoints onde as métricas serão avaliadas. Se os leading indicators não moverem, reconsidere antes de investir mais.

### Passo 7 — Instrumentar desde o Início
Garanta que a coleta de dados para as métricas está implementada antes ou junto com a feature. Sem instrumentação, não há como medir outcomes.

## Perguntas de Ativação

- "Se entregarmos isso perfeitamente, que número muda?"
- "Como saberemos em 2 semanas se estamos no caminho certo?"
- "Qual é a teoria que conecta essa feature ao resultado de negócio?"
- "Já construímos algo parecido antes? Qual foi o outcome real?"
- "Estamos otimizando para entregar features ou para gerar resultados?"
- "Se a métrica não mover, o que faremos diferente?"

## Output Esperado

```
OUTCOME DESEJADO: [resultado mensurável]

MÉTRICAS:
- Leading: [métrica] | Baseline: [valor atual] | Target: [valor desejado] | Prazo: [data]
- Lagging: [métrica] | Baseline: [valor atual] | Target: [valor desejado] | Prazo: [data]

TEORIA DE MUDANÇA:
"Acreditamos que [output] vai causar [outcome] porque [mecanismo]."

EVIDÊNCIA A FAVOR: [dados/referências]
EVIDÊNCIA CONTRA: [riscos/contra-exemplos]

OUTPUT MÍNIMO: [menor entrega que testa a teoria]

CHECKPOINTS:
- Semana 2: verificar [leading indicator]
- Semana 4: verificar [leading indicator]
- Semana 8: verificar [lagging indicator]

CRITÉRIO DE PIVOT: Se [condição], reconsiderar abordagem.
```

## Armadilhas Comuns

1. **Métricas de vaidade**: Medir coisas que parecem boas (pageviews) mas não indicam valor real (conversão).
2. **Teoria de mudança implícita**: Todos assumem que "é óbvio" por que a feature vai funcionar, mas ninguém articula o mecanismo.
3. **Ausência de baseline**: Sem saber o valor atual, é impossível medir mudança.
4. **Instrumentação tardia**: Lançar a feature e depois perceber que não há dados para medir o outcome.
5. **Ignorar checkpoints**: Definir checkpoints mas não parar para avaliar, continuando por inércia.
6. **Atribuição falsa**: Assumir que a melhoria na métrica foi causada pela feature quando pode ter sido por sazonalidade ou outras mudanças simultâneas.
