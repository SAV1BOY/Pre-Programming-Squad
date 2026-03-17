# Solution Jump Prevention

## Título e Propósito

O **Solution Jump Prevention** é um framework para impedir que equipes pulem prematuramente para soluções antes de entender adequadamente o problema. O propósito é criar um "freio de mão" cognitivo que força a equipe a permanecer no espaço do problema tempo suficiente para que a solução emerja do entendimento, não da ansiedade de "ter que resolver rápido".

## Quando Usar

- Quando alguém diz "a solução é óbvia" nos primeiros 5 minutos da discussão
- Quando um stakeholder apresenta uma solução e a equipe aceita sem questionar
- Em brainstorms que convergem rápido demais para uma única ideia
- Quando a equipe tem histórico de retrabalho por ter resolvido o problema errado
- Em kickoffs de projeto onde a solução já foi "decidida" antes de investigar

## Conceitos-Chave

1. **Solution Jump**: O ato de pular para "como resolver" antes de entender "o que resolver". É instintivo em engenheiros.
2. **Espaço do Problema vs. Espaço da Solução**: Duas fases distintas de pensamento. Misturá-las gera soluções que não resolvem o problema.
3. **Ancoragem**: A primeira solução mencionada ancora todo o pensamento subsequente. Dificulta considerar alternativas.
4. **Divergir Antes de Convergir**: Gerar múltiplas interpretações do problema antes de escolher uma. Gerar múltiplas soluções antes de escolher uma.
5. **Tempo de Incubação**: O problema precisa de tempo para ser compreendido. Soluções prematuras são geralmente superficiais.

## Processo / Passos

### Passo 1 — Reconhecer o Padrão
Treine a equipe para reconhecer o solution jump quando ele acontece. Sinais: "Vamos usar X", "É só fazer Y", "Eu já sei como resolver" — tudo isso antes de definir o problema.

### Passo 2 — Aplicar a Regra de "Problema Primeiro"
Antes de qualquer discussão de solução, exija que o problema esteja escrito em uma frase que toda a equipe concorda. Se não há consenso sobre o problema, qualquer solução é prematura.

### Passo 3 — Gerar Múltiplas Definições do Problema
Peça a cada membro que escreva sua versão do problema independentemente. Compare. Divergências revelam ambiguidade não resolvida.

### Passo 4 — Proibir Soluções Temporariamente
Na fase de discovery, use a regra: "Nesta conversa, só falamos sobre o problema. Soluções vão para o estacionamento." Registre soluções sugeridas mas não as discuta ainda.

### Passo 5 — Validar o Problema com Dados
Busque evidência de que o problema existe, que é significativo e que afeta quem se diz afetar. Sem validação, o problema pode ser fantasma.

### Passo 6 — Abrir o Espaço de Soluções
Somente após problema validado, entre no espaço de soluções. Gere pelo menos 3 alternativas genuinamente diferentes antes de avaliar qualquer uma.

### Passo 7 — Escolher com Critérios
Avalie as soluções contra critérios derivados do problema: resolve a causa raiz? Cabe nas restrições? É validável?

## Perguntas de Ativação

- "Estamos falando sobre o problema ou já pulamos para a solução?"
- "Se proibirem essa solução, como resolveríamos o problema de outra forma?"
- "Qual problema essa solução resolve? Esse é o problema que precisamos resolver?"
- "Quem definiu que essa é a solução certa? Com base em quê?"
- "Se estivéssemos errados sobre o problema, essa solução ainda faria sentido?"
- "Estamos convergindo cedo demais? Quais alternativas não exploramos?"

## Output Esperado

```
FASE 1 — ESPAÇO DO PROBLEMA:

Pedido original: "Precisamos de um chatbot para suporte"

Problema investigado:
- Quem sofre: Equipe de suporte (sobrecarregada) e clientes (espera longa)
- Evidência: Tempo médio de resposta: 4h. SLA: 2h. 60% dos tickets são perguntas repetitivas.
- Problema real: "Clientes não encontram respostas para perguntas comuns sozinhos,
  sobrecarregando o suporte com 60% de tickets que poderiam ser self-service."

SOLUÇÕES PULADAS (estacionamento):
- Chatbot com IA (sugerida pelo diretor)
- Contratar mais 2 agentes

FASE 2 — ESPAÇO DA SOLUÇÃO:

Soluções geradas após entender o problema:
1. FAQ interativa com busca inteligente (resolve 60% dos tickets, custo baixo)
2. Chatbot baseado em regras para top 20 perguntas (resolve 40%, custo médio)
3. Chatbot com IA generativa (resolve 50-70%, custo alto, risco de alucinação)

Solução escolhida: #1 (FAQ interativa) como v1, #2 como v2 se necessário.
Critério: Maior impacto com menor custo e risco.
```

## Armadilhas Comuns

1. **"O problema é óbvio"**: A frase mais perigosa em engenharia. Problemas "óbvios" são frequentemente sintomas superficiais.
2. **Ancoragem na primeira ideia**: A primeira solução mencionada domina toda a discussão. Use escrita silenciosa antes de discussão.
3. **Autoridade como argumento**: "O diretor quer um chatbot" — a posição hierárquica não valida a solução. O problema valida.
4. **Desconforto com ambiguidade**: Engenheiros querem resolver. Ficar no problema gera desconforto. Esse desconforto é sinal de que o processo está funcionando.
5. **Solução disfarçada de problema**: "O problema é que não temos um microserviço de X" — isso é solução, não problema.
6. **Medo de questionar**: Não querer parecer "negativista" ao pedir para voltar ao problema quando todos já estão animados com a solução.
