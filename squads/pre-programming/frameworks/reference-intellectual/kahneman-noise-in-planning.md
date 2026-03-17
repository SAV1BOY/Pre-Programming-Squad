# Kahneman: Noise e Bias em Estimativas

## Título e Propósito

Framework baseado no trabalho de **Daniel Kahneman** (*Thinking, Fast and Slow*, *Noise*). A tese central: **estimativas humanas sofrem de vieses sistemáticos e ruído (variação aleatória)** — e ambos podem ser reduzidos com técnicas deliberadas. O propósito é aplicar insights da psicologia cognitiva para produzir estimativas mais honestas e úteis em projetos de software.

## Quando Usar

- Em qualquer sessão de estimativa de esforço ou prazo
- Quando estimativas anteriores falharam consistentemente
- Para calibrar o otimismo natural de equipes de engenharia
- Em decisões onde vieses cognitivos podem distorcer a avaliação
- Ao comparar estimativas de diferentes membros da equipe

## Conceitos-Chave

1. **Planning Fallacy**: A tendência universal de subestimar tempo, custos e riscos enquanto superestima benefícios. Não é falta de competência — é viés cognitivo.
2. **Inside View vs. Outside View**: Inside view: "analisando nossa situação específica, vai levar X". Outside view: "projetos similares historicamente levaram Y". Outside view é mais preciso.
3. **Anchoring**: O primeiro número mencionado ancora todas as estimativas subsequentes. Quem fala primeiro influencia todos.
4. **Noise**: Variação aleatória em julgamentos. Dois devs estimando a mesma tarefa dão números muito diferentes — isso é noise.
5. **Reference Class Forecasting**: Estimar baseado em dados de projetos similares anteriores, não em análise específica do caso.

## Processo / Passos

### Passo 1 — Usar Outside View Primeiro
Antes de analisar o projeto específico, pergunte: "Quanto tempo projetos similares levaram na realidade?" Use dados históricos.

### Passo 2 — Estimar Independentemente
Cada membro da equipe estima sozinho, sem ver as estimativas dos outros. Isso evita anchoring.

### Passo 3 — Comparar e Discutir Divergências
Divergências grandes indicam ambiguidade ou risco. Discuta não para convergir forçosamente, mas para entender a fonte da diferença.

### Passo 4 — Aplicar Correção de Otimismo
Multiplique a estimativa consensual por um fator de correção baseado em dados históricos. Se projetos similares levaram 1.5x o estimado, aplique 1.5x.

### Passo 5 — Estimar em Ranges
Em vez de pontos, use ranges: "entre 3 e 8 semanas, com maior probabilidade em 5". Comunica incerteza explicitamente.

## Perguntas de Ativação

- "Nossas estimativas anteriores foram otimistas ou pessimistas? Por quanto?"
- "Estamos estimando com base na análise específica ou em referências de projetos similares?"
- "Quem estimou primeiro e quanto isso influenciou os demais?"
- "Se 5 pessoas estimassem independentemente, os números convergiriam?"
- "Estamos estimando o cenário base ou o cenário em que tudo dá certo?"

## Output Esperado

Estimativas em range com nível de confiança, fator de correção baseado em dados históricos, divergências documentadas com justificativa.

## Armadilhas Comuns

1. **Anchoring pelo líder**: O tech lead fala "acho que 2 semanas" e todo mundo concorda. Elimine com estimativas independentes.
2. **Planning fallacy não corrigida**: Saber que existe o viés mas não aplicar correção. Conhecer o viés não o elimina.
3. **Inside view exclusiva**: Analisar apenas o caso específico sem referência a projetos anteriores.
4. **Estimativa como compromisso**: Tratar a estimativa como prazo fixo em vez de melhor palpite com incerteza.
5. **Ignorar noise**: Aceitar que "cada um tem sua opinião" sem investigar por que estimativas divergem tanto.
