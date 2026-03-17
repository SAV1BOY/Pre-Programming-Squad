# Real Problem Locator

## Título e Propósito

O **Real Problem Locator** é um framework de descoberta para encontrar o problema real por trás do pedido original. O propósito é evitar que a equipe construa soluções para problemas inexistentes, mal formulados ou que são sintomas de algo maior — garantindo que o investimento de desenvolvimento ataque a raiz, não a folha.

## Quando Usar

- Quando um stakeholder apresenta uma solução em vez de um problema
- No início de qualquer discovery para validar o problema antes de projetar soluções
- Quando o problema declarado parece superficial ou genérico demais
- Quando diferentes stakeholders descrevem o "mesmo problema" de formas contraditórias
- Quando correções anteriores não resolveram o problema

## Conceitos-Chave

1. **Problema Declarado vs. Problema Real**: O que é pedido vs. o que realmente precisa ser resolvido. A distância entre os dois é proporcional ao risco de retrabalho.
2. **Camada de Abstração do Problema**: Problemas existem em camadas — operacional, processual, sistêmica, estratégica. Resolver na camada errada gera recorrência.
3. **Teste de Impacto**: Se resolvermos isso, quem se beneficia e como? Se a resposta for vaga, o problema não está claro.
4. **Evidência vs. Narrativa**: Dados que comprovam a existência e magnitude do problema vs. histórias e percepções.
5. **Problema Proxy**: Problema que parece ser o real mas é apenas proxy de algo que as pessoas não querem ou não sabem articular.

## Processo / Passos

### Passo 1 — Registrar o Pedido Original
Anote exatamente como o problema/pedido foi formulado. Preserve as palavras originais sem editar.

### Passo 2 — Perguntar "Para Quem?"
Identifique quem sofre com o problema. Se ninguém sofre concretamente, questione se o problema existe.

### Passo 3 — Perguntar "Desde Quando?"
Descubra quando o problema começou. O que mudou? Problemas crônicos e agudos requerem abordagens diferentes.

### Passo 4 — Buscar Evidências Concretas
Peça dados: logs, métricas, reclamações registradas, tickets de suporte. Sem evidência, pode ser percepção, não problema.

### Passo 5 — Testar Hipóteses Alternativas
Pergunte: "E se o problema real for outro?" Gere pelo menos 3 hipóteses alternativas para o que pode ser a causa real.

### Passo 6 — Validar com Quem Sofre
Fale diretamente com quem é afetado — não apenas com quem reporta. O intermediário filtra e distorce.

### Passo 7 — Reformular o Problema Real
Escreva o problema real em formato: "[Quem] não consegue [o quê] porque [por quê], resultando em [impacto mensurável]."

## Perguntas de Ativação

- "Quem me pediu isso e quem realmente sofre com o problema?"
- "Se eu entregasse exatamente o que foi pedido, o problema desapareceria?"
- "Há dados que comprovam que esse problema é real e significativo?"
- "Quais outras explicações poderiam dar conta dos mesmos sintomas?"
- "O que aconteceu quando tentaram resolver isso antes?"
- "Se esse problema fosse resolvido magicamente, o que mudaria no dia a dia de quem é afetado?"

## Output Esperado

```
PEDIDO ORIGINAL: "[citação exata do stakeholder]"

INVESTIGAÇÃO:
- Quem sofre: [lista de atores com impacto específico]
- Desde quando: [timeline do problema]
- Evidência encontrada: [dados concretos]
- Evidência não encontrada: [o que tentamos verificar mas não confirmou]

HIPÓTESES TESTADAS:
1. [Hipótese A] — Status: confirmada/refutada — Evidência: [dados]
2. [Hipótese B] — Status: confirmada/refutada — Evidência: [dados]
3. [Hipótese C] — Status: confirmada/refutada — Evidência: [dados]

PROBLEMA REAL:
"[Quem] não consegue [o quê] porque [por quê], resultando em [impacto mensurável]."

DIFERENÇA DO PEDIDO ORIGINAL: [explicação de por que o problema real difere do declarado]
```

## Armadilhas Comuns

1. **Aceitar o pedido como problema**: "Precisamos de um dashboard" não é um problema — é uma solução para um problema não articulado.
2. **Falar apenas com intermediários**: O gerente que reporta o problema pode ter interpretação diferente do usuário que sofre.
3. **Viés de confirmação**: Buscar evidência que confirme a primeira hipótese em vez de tentar refutá-la.
4. **Problema de estimação**: Assumir que o problema é grande porque uma pessoa influente reclamou, sem medir a escala real.
5. **Investigação infinita**: Às vezes o problema declarado é o problema real. Não prolongue a investigação por perfeccionismo.
6. **Política como barreira**: Às vezes o problema real é político/organizacional e a equipe técnica não tem mandato para resolvê-lo. Reconheça e escale.
