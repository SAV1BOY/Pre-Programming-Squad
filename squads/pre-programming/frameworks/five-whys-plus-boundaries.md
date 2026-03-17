# Five Whys + Boundaries

## Título e Propósito

O **Five Whys + Boundaries** é uma evolução do clássico "5 Porquês" da Toyota, acrescido de delimitações explícitas para evitar que a análise se perca em causas filosóficas ou fora do controle da equipe. O propósito é chegar à causa raiz acionável — aquela que está dentro da nossa esfera de influência e pode ser resolvida com uma intervenção concreta.

## Quando Usar

- Quando um problema recorrente precisa ser investigado antes de propor solução
- Em post-mortems e análises de incidentes
- Quando a equipe está "girando em círculos" sem chegar a um diagnóstico claro
- Antes de criar tickets de bug que tratam apenas sintomas
- Em sessões de refinamento onde o "porquê" do trabalho não está claro

## Conceitos-Chave

1. **Causa Raiz Acionável**: A causa mais profunda sobre a qual a equipe tem poder de ação. Não adianta identificar "a cultura da empresa" como causa raiz se você é um time de 4 devs.
2. **Fronteira de Controle**: O limite entre o que a equipe pode mudar e o que depende de outros.
3. **Camada de Parada**: O nível onde continuar perguntando "por quê?" deixa de gerar insight acionável.
4. **Divergência de Caminhos**: Em cada "por quê?", pode haver múltiplas respostas. Todas devem ser registradas, mas priorizadas por impacto.
5. **Evidência por Nível**: Cada resposta a um "por quê?" deve ser sustentada por dados, não por opinião.

## Processo / Passos

### Passo 1 — Declarar o Problema Observável
Escreva o problema como um fato observável, sem interpretações. Use dados: "O endpoint /checkout retorna 500 em 3% das requisições desde segunda-feira."

### Passo 2 — Primeiro Porquê
Pergunte "por que isso acontece?" e registre todas as hipóteses. Marque quais têm evidência e quais são suposições.

### Passo 3 — Iterar até a Causa Raiz
Continue perguntando "por quê?" para cada resposta. Em cada nível:
- Registre a resposta
- Classifique: **fato comprovado** ou **hipótese**
- Verifique se ainda está dentro da fronteira de controle

### Passo 4 — Aplicar o Teste de Fronteira
Para cada causa identificada, pergunte:
- "Podemos agir sobre isso diretamente?"
- "Precisamos de aprovação ou cooperação externa?"
- "Isso está dentro do nosso mandato?"

### Passo 5 — Identificar a Camada de Parada
Pare quando:
- A causa está fora da fronteira de controle
- A próxima pergunta "por quê?" levaria a causas organizacionais ou filosóficas genéricas
- Você chegou a algo que pode ser resolvido com uma ação concreta

### Passo 6 — Formular a Causa Raiz Acionável
Escreva a causa raiz como uma declaração que implica uma ação: "O cache de sessão não tem TTL configurado, causando dados stale que geram erro no checkout."

### Passo 7 — Validar com Dados
Antes de aceitar a causa raiz, defina um teste rápido para validá-la. Se não for validável, trate como hipótese e planeje investigação.

## Perguntas de Ativação

- "Temos evidência concreta para essa resposta ou é intuição?"
- "Se corrigíssemos isso, o problema desapareceria ou apenas mudaria de forma?"
- "Essa causa está dentro do que podemos mudar nas próximas 2 semanas?"
- "Existem outros caminhos causais que não estamos explorando?"
- "Estamos descendo demais? Já passamos do ponto acionável?"
- "Quem pode confirmar ou refutar essa hipótese com dados?"

## Output Esperado

```
Problema: [declaração factual]

Por quê #1: [resposta] — [fato/hipótese] — [dentro/fora da fronteira]
Por quê #2: [resposta] — [fato/hipótese] — [dentro/fora da fronteira]
Por quê #3: [resposta] — [fato/hipótese] — [dentro/fora da fronteira]
Por quê #4: [resposta] — [fato/hipótese] — [dentro/fora da fronteira]
Por quê #5: [resposta] — [fato/hipótese] — [dentro/fora da fronteira]

Camada de Parada: #[N]
Causa Raiz Acionável: [declaração]
Teste de Validação: [como verificar]
Ação Proposta: [próximo passo concreto]
```

## Armadilhas Comuns

1. **Parar cedo demais**: Aceitar a primeira resposta como causa raiz por preguiça ou pressão de tempo. Geralmente o primeiro "por quê?" é apenas outro sintoma.
2. **Não parar nunca**: Continuar perguntando "por quê?" até chegar em "porque a empresa foi fundada assim" — inútil e paralisante.
3. **Caminho único**: Seguir apenas uma linha causal quando há bifurcações. Problemas complexos geralmente têm múltiplas causas contribuintes.
4. **Opinião disfarçada de fato**: Aceitar "todo mundo sabe que é por causa do legado" sem dados concretos.
5. **Ignorar a fronteira de controle**: Identificar causas reais mas fora do alcance da equipe, gerando frustração sem ação.
6. **Viés de confirmação**: Conduzir os "porquês" em direção a uma causa que já se acreditava antes da análise.
