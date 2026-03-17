# Frases: Anti-Overengineering

## Contexto
Usar quando a equipe está projetando uma solução mais complexa do que o problema exige, adicionando camadas, abstrações ou capacidades desnecessárias para o momento.

## Frases-Modelo

1. "Estamos construindo para 10 milhões de usuários, mas vamos lançar com 500. A arquitetura precisa escalar com o negócio, não antes dele."

2. "YAGNI — You Aren't Gonna Need It. Se não está no escopo do MVP, não precisa estar no design agora."

3. "A solução mais simples que resolve o problema é a melhor solução. Complexidade sem necessidade é dívida técnica."

4. "Microserviços são ótimos para o problema certo. Para 3 endpoints e 1 equipe, um monolito bem estruturado é mais eficiente."

5. "Vamos projetar para ser fácil de mudar depois, não para prever todos os cenários futuros agora."

6. "Cada abstração que adicionamos é uma abstração que todos precisam entender e manter. O custo justifica o benefício?"

7. "Se precisarmos dessa capacidade no futuro, podemos adicioná-la. Mas adicionar agora tem um custo de manutenção que começa hoje."

8. "Simplificar é mais difícil que complicar. Se a solução parece simples demais, talvez esteja simplesmente certa."

## Quando Usar
- Quando a equipe está adicionando "por precaução" ou "por elegância".
- Quando a solução proposta é desproporcional ao problema.
- Quando frameworks ou padrões estão sendo adotados sem necessidade clara.

## Quando NÃO Usar
- Quando a complexidade é genuinamente necessária para o problema.
- Quando simplificar demais criará débito técnico real e imediato.
- Para desencorajar boas práticas de engenharia que têm custo baixo.

## Tom Recomendado
Pragmático e respeitoso. Não é sobre desmerecer a capacidade técnica da equipe, é sobre aplicar a engenharia na medida certa. Reconheça que a solução complexa é tecnicamente interessante, mas redirecione para o que o projeto precisa agora.
