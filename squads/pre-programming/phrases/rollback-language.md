# Frases: Linguagem de Rollback

## Contexto
Usar quando é necessário reforçar a importância de ter planos de rollback antes de qualquer mudança em produção, e quando é preciso decidir se um rollback deve ser executado.

## Frases-Modelo

1. "Se não temos plano de rollback, não estamos prontos para fazer deploy."

2. "O melhor rollback é aquele que nunca precisamos usar. O segundo melhor é aquele que funciona quando precisamos."

3. "Qual é o tempo de rollback? Se é mais de [X minutos], precisamos simplificar o procedimento."

4. "Rollback de código é fácil. Rollback de dados é o desafio real. Vamos garantir que os dois estão cobertos."

5. "Não discutimos se precisamos de rollback. Discutimos como fazer um rollback rápido e seguro."

6. "O rollback foi testado? Um plano escrito que nunca foi executado é uma ilusão de segurança."

7. "Quando em dúvida, faça o rollback. É melhor voltar e investigar do que manter um sistema instável enquanto tentamos entender o que aconteceu."

8. "Deploy sem rollback é como pular de avião sem paraquedas — pode dar certo, mas não é uma boa prática."

## Quando Usar
- Antes de qualquer deploy em produção, para verificar se o plano de rollback existe.
- Durante incidentes, quando a decisão de rollback está sendo considerada.
- Quando a equipe está tentando fazer deploy sem preparação adequada.

## Quando NÃO Usar
- Para mudanças triviais e facilmente reversíveis (toggle de configuração, por exemplo).
- Para criar medo de fazer deploys.
- Em ambientes de desenvolvimento ou staging.

## Tom Recomendado
Seguro e decisivo. Rollback não é derrota — é uma ferramenta de segurança. A equipe deve se sentir empoderada para executar um rollback rápido sem medo de julgamento. A cultura de "rollback é OK" é mais saudável que a cultura de "vamos tentar consertar em produção".
