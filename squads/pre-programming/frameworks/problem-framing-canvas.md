# Problem Framing Canvas

## Título e Propósito

O **Problem Framing Canvas** é um framework visual para estruturar e delimitar problemas antes de qualquer discussão sobre soluções. Seu propósito é garantir que a equipe compreenda profundamente o problema real — não apenas os sintomas — antes de investir tempo e recursos em implementação.

Sem um enquadramento claro do problema, equipes frequentemente constroem soluções elegantes para o problema errado.

## Quando Usar

- No início de qualquer projeto ou feature nova
- Quando há divergência na equipe sobre "o que estamos resolvendo"
- Quando um stakeholder apresenta uma solução já pronta e você precisa validar o problema subjacente
- Quando um bug recorrente sugere que o problema raiz nunca foi endereçado
- Em sessões de discovery antes de partir para design ou arquitetura

## Conceitos-Chave

1. **Problema vs. Sintoma**: O sintoma é o que se observa; o problema é a causa estrutural. Tratar sintomas gera retrabalho.
2. **Contexto do Problema**: Quem é afetado, com que frequência, em que circunstâncias e qual o impacto mensurável.
3. **Espaço de Restrições**: Limites técnicos, de negócio, regulatórios e de tempo que delimitam o espaço de soluções viáveis.
4. **Critério de Sucesso**: Como saberemos que o problema foi resolvido — definido antes de pensar em soluções.
5. **Fronteira do Problema**: O que está dentro e fora do escopo deste enquadramento.

## Processo / Passos

### Passo 1 — Capturar o Problema Declarado
Registre literalmente como o problema foi descrito pelo solicitante. Não edite nem interprete ainda.

### Passo 2 — Identificar Quem Sofre
Liste os atores afetados (usuários, equipes internas, sistemas). Para cada um, descreva o impacto concreto.

### Passo 3 — Mapear Contexto e Frequência
Responda: quando o problema ocorre? Com que frequência? Em que condições? Há sazonalidade ou gatilhos específicos?

### Passo 4 — Separar Sintomas de Causas
Use perguntas "por quê?" em cadeia para descer do sintoma observável até a causa raiz. Registre cada nível.

### Passo 5 — Definir Restrições Conhecidas
Liste restrições técnicas, de prazo, orçamento, regulatórias e organizacionais que limitam o espaço de soluções.

### Passo 6 — Estabelecer Critérios de Sucesso
Defina métricas ou condições observáveis que indicarão que o problema foi resolvido. Seja específico e mensurável.

### Passo 7 — Delimitar Fronteiras
Declare explicitamente o que está dentro e fora do escopo. Documente decisões de fronteira e suas justificativas.

### Passo 8 — Reformular o Problema
Reescreva o problema em uma frase clara que incorpore causa raiz, público afetado e critério de sucesso.

## Perguntas de Ativação

- "Se resolvêssemos isso perfeitamente, o que mudaria para o usuário final?"
- "Esse problema já existia antes? O que mudou para ele se tornar urgente agora?"
- "Quem mais é afetado por esse problema além do solicitante original?"
- "Se não fizermos nada, o que acontece em 3 meses?"
- "Estamos descrevendo um sintoma ou a causa real?"
- "Qual é a menor evidência que provaria que entendemos o problema corretamente?"

## Output Esperado

Um documento de uma página contendo:

| Seção | Conteúdo |
|---|---|
| Problema original | Declaração literal do solicitante |
| Atores afetados | Lista com impacto por ator |
| Contexto | Frequência, condições, gatilhos |
| Cadeia causal | Sintoma → causa intermediária → causa raiz |
| Restrições | Lista categorizada de restrições |
| Critério de sucesso | Métricas ou condições observáveis |
| Fronteiras | Dentro / fora do escopo |
| Problema reformulado | Frase única e clara |

## Armadilhas Comuns

1. **Pular direto para soluções**: A tentação de já pensar em "como resolver" antes de entender "o que resolver" é a armadilha número um.
2. **Aceitar o problema como declarado**: Stakeholders frequentemente descrevem soluções disfarçadas de problemas ("precisamos de um dashboard"). Questione até chegar ao problema real.
3. **Escopo infinito**: Sem fronteiras explícitas, o problema se expande até ser impossível de resolver em um ciclo.
4. **Critérios de sucesso vagos**: "Melhorar a experiência" não é critério. Sem métricas claras, não há como validar se o problema foi resolvido.
5. **Ignorar restrições**: Enquadrar o problema sem considerar restrições reais leva a soluções bonitas mas inviáveis.
6. **Consenso forçado**: Divergências sobre o problema devem ser documentadas, não suprimidas. Falso consenso gera retrabalho depois.
