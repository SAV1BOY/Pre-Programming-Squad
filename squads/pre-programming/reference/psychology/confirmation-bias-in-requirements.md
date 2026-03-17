# Vies de Confirmacao em Requisitos

## Vies/Efeito

**Vies de Confirmacao (Confirmation Bias):** A tendencia de buscar, interpretar e lembrar informacoes de forma que confirmem crencas preexistentes, enquanto desconsideramos evidencias contrarias.

## Descricao

O vies de confirmacao e um dos vieses cognitivos mais poderosos e pervasivos. Nao e simplesmente ignorar informacoes — e um processo ativo de filtragem onde nosso cerebro privilegia dados que confirmam o que ja acreditamos e desvaloriza dados que contradizem. Estudos de Wason (1960) e Nickerson (1998) demonstram que esse vies opera mesmo em pessoas conscientes de sua existencia.

## Como se Manifesta em Pre-Programacao

### Na Coleta de Requisitos
- **Perguntas tendenciosas:** "Os usuarios vao adorar essa feature, nao?" em vez de "Como os usuarios reagem a essa funcionalidade?"
- **Interpretacao seletiva:** Ouvir "os usuarios mencionaram problemas de performance" e interpretar como confirmacao de que precisamos de microservicos, ignorando solucoes mais simples.
- **Amostra enviesada:** Conversar apenas com stakeholders que concordam com a solucao preferida.

### Na Avaliacao de Design
- **Avaliar a solucao favorita com lente generosa** e as alternativas com lente critica.
- **Buscar evidencias de que a tecnologia favorita e adequada** e ignorar evidencias de problemas.
- **Citar cases de sucesso** da tecnologia preferida e ignorar cases de fracasso.

### Na Estimativa
- **Buscar projetos similares que confirmem a estimativa desejada** e ignorar projetos que sugerem maior complexidade.
- **Interpretar incerteza como confirmacao:** "Nao encontramos problemas no spike, entao a solucao funciona" (ausencia de evidencia nao e evidencia de ausencia).

### Na Analise de Riscos
- **Minimizar riscos da abordagem preferida** e maximizar riscos das alternativas.
- **Descartar preocupacoes levantas por outros** como "pessimismo" ou "overthinking."

## Como Mitigar

### 1. Pre-Mortem
Antes de tomar a decisao final, conduzir um exercicio de pre-mortem: "Imagine que e daqui a 6 meses e o projeto fracassou. Por que?" Forca o grupo a buscar evidencias contra a decisao.

### 2. Advocacia do Diabo Estruturada
Designar um membro da equipe para argumentar contra a opcao preferida. Nao como exercicio retorico, mas como busca genuina de problemas.

### 3. Alternativas Obrigatorias
Exigir pelo menos duas alternativas genuinas em todo design doc. Se so existe uma opcao, o vies de confirmacao provavelmente eliminou as demais prematuramente.

### 4. Dados antes de Opinioes
Em design reviews, apresentar dados e benchmarks antes de abrir para opinioes. Uma vez que alguem expressa uma opiniao forte, o grupo tende a buscar confirmacao.

### 5. Evidencia Contra
Para cada decisao significativa, exigir explicitamente: "Quais evidencias temos contra esta decisao? O que nos faria mudar de ideia?"

### 6. Revisao por Quem Discorda
Incluir revisores que tenham perspectivas diferentes ou que historicamente questionem premissas.

## Exemplo Real

**Contexto:** Uma equipe decide migrar para microservicos porque "o monolito nao escala."

**Manifestacao do vies:**
- Citam Netflix e Amazon como cases de sucesso de microservicos.
- Ignoram que o monolito atual atende 99% dos requisitos de performance.
- Entrevistam apenas desenvolvedores frustrados com o monolito (amostra enviesada).
- Descartam preocupacoes de complexidade operacional como "pensamento antiquado."
- Nao investigam opcoes intermediarias (modular monolith).

**O que deveria ter acontecido:**
- Perguntar: "Quais exatamente sao os requisitos de escala que o monolito nao atende?"
- Buscar dados: metricas de performance atuais vs. requisitos.
- Investigar alternativas: modular monolith, otimizacoes pontuais, scale-up.
- Conversar com equipes que reverteram microservicos para monolito.
- Calcular custo operacional de 8 microsservicos vs. 1 monolito.

**Resultado sem mitigacao:** Migracao de 12 meses que triplicou a complexidade operacional para um sistema que nunca atingiu a carga que justificaria microservicos.
