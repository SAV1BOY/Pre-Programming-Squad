# LLM Evals - Primer

## O que sao LLM Evals

LLM Evals (avaliacoes de Large Language Models) sao os mecanismos sistematicos para medir a qualidade, confiabilidade e seguranca das respostas geradas por modelos de linguagem. Em sistemas que integram LLMs, evals sao o equivalente a testes automatizados: sem eles, voce esta voando cego.

## Por que Evals sao Criticos na Pre-Programacao

Quando um projeto envolve integracao com LLMs (chatbots, copilots, geracao de conteudo, agentes), a pre-programacao deve definir como o sistema sera avaliado ANTES da implementacao. Diferente de software deterministico, LLMs sao probabilisticos — a mesma entrada pode gerar saidas diferentes. Isso exige abordagens de teste fundamentalmente diferentes.

## Tipos de Evals

### 1. Evals de Corretude Factual
O modelo gera informacoes corretas?

**Metricas:**
- Accuracy: % de respostas factualmente corretas.
- Groundedness: Respostas sao baseadas em fontes fornecidas (RAG)?
- Hallucination rate: % de informacoes fabricadas.

**Na pre-programacao:** Definir o dataset de validacao com respostas esperadas. Definir threshold aceitavel de accuracy.

### 2. Evals de Relevancia
A resposta atende a pergunta do usuario?

**Metricas:**
- Relevance score: Quao relevante e a resposta para a query.
- Answer completeness: A resposta cobre todos os aspectos da pergunta?
- Conciseness: A resposta e concisa sem ser incompleta?

### 3. Evals de Seguranca (Safety)
O modelo gera conteudo toxico, ofensivo, enviesado ou perigoso?

**Metricas:**
- Toxicity rate: % de respostas com conteudo toxico.
- Bias metrics: Disparidade de tratamento entre demografias.
- Refusal rate: % de prompts perigosos corretamente recusados.
- Jailbreak resistance: % de tentativas de bypass bloqueadas.

### 4. Evals de Consistencia
O modelo mantem comportamento consistente?

**Metricas:**
- Consistency score: Mesma pergunta formulada diferente gera resposta equivalente?
- Persona adherence: O modelo mantem o tom/persona definido?
- Instruction following: O modelo segue as instrucoes do system prompt?

### 5. Evals de Performance
O sistema funciona dentro dos parametros aceitaveis?

**Metricas:**
- Latencia: Time to first token (TTFT), time to last token (TTLT).
- Throughput: Tokens por segundo.
- Custo: Custo por request (tokens de input + output).

## Framework de Evals para Pre-Programacao

### Passo 1: Definir o Dataset de Avaliacao

```markdown
## Eval Dataset

### Golden Dataset (curado manualmente)
- 100-500 pares de input/output esperado.
- Cobertura: happy path, edge cases, adversarial inputs.
- Revisado por humanos com expertise no dominio.

### Adversarial Dataset
- 50-100 prompts projetados para quebrar o sistema.
- Categorias: jailbreak, injection, exfiltration, off-topic, toxic input.

### Regression Dataset
- Inputs que causaram problemas em versoes anteriores.
- Crescente ao longo do tempo.
```

### Passo 2: Definir Metricas e Thresholds

```markdown
## Metricas e Thresholds

| Metrica | Threshold Minimo | Target | Bloqueador? |
|---|---|---|---|
| Accuracy (factual) | > 90% | > 95% | Sim |
| Hallucination rate | < 5% | < 2% | Sim |
| Safety (toxicity) | < 0.1% | 0% | Sim |
| Jailbreak resistance | > 95% | > 99% | Sim |
| Relevance score | > 80% | > 90% | Nao |
| Latencia p99 | < 5s | < 3s | Nao |
| Custo por request | < $0.05 | < $0.02 | Nao |
```

### Passo 3: Definir Pipeline de Avaliacao

```markdown
## Pipeline de Evals

1. **Pre-deploy:** Rodar golden dataset + adversarial dataset.
   Bloquear deploy se thresholds nao atingidos.
2. **Canary:** Monitorar metricas em 5% do trafego por 24h.
3. **Producao:** Monitoramento continuo com sampling de 10%.
4. **Semanal:** Eval completo com dataset expandido.
```

### Passo 4: Definir Processo de LLM-as-Judge

Usar um LLM mais capaz para avaliar as respostas do LLM em producao.

**Quando usar:** Avaliacao de qualidade subjetiva (relevancia, tom, completude).
**Cuidados:** LLM-as-judge tem seus proprios vieses. Calibrar com avaliacao humana.
**Pre-programacao:** Definir rubrica de avaliacao para o LLM juiz.

## Evals na Pre-Programacao: Checklist

### Antes de Comecar o Design
- [ ] O projeto envolve LLMs ou componentes generativos?
- [ ] Se sim, o eval framework esta definido?

### No Design Doc
- [ ] Dataset de avaliacao esta planejado (golden + adversarial)?
- [ ] Metricas e thresholds estao definidos?
- [ ] Pipeline de evals esta incluso no pipeline de CI/CD?
- [ ] Processo de LLM-as-judge esta definido (se aplicavel)?
- [ ] Estrategia de monitoramento em producao esta planejada?
- [ ] Plano de fallback definido para quando LLM degrada?

### Nos Criterios de Readiness
- [ ] "O eval dataset cobre cenarios criticos de negocio?"
- [ ] "Thresholds de seguranca sao bloqueadores de deploy?"
- [ ] "O custo por request esta dentro do budget?"
- [ ] "Existe plano de fallback se o LLM ficar indisponivel?"

## Armadilhas Comuns

### Vibe Check em vez de Evals
Testar manualmente com 5 perguntas e declarar "funciona". Sem metricas, sem reproducibilidade, sem regressao.

### Eval Dataset Desatualizado
O dataset nao acompanha mudancas no produto. Respostas corretas mudam, mas o dataset nao.

### Ignorar Seguranca
Focar em accuracy e ignorar safety. Um unico incidente de conteudo toxico pode causar dano reputacional significativo.

### Over-fitting no Eval Dataset
Otimizar o modelo especificamente para o dataset de avaliacao. Resultado: otimo nos evals, ruim com usuarios reais.
