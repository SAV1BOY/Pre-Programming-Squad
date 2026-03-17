# Briefs Ruins e Por Que Falharam — Exemplos Anotados

## Introdução

Estudar fracassos é tão importante quanto estudar sucessos. Briefs ruins não são apenas inúteis — são ativamente prejudiciais, porque criam uma falsa sensação de alinhamento. O time acha que entendeu o que construir, mas cada pessoa tem uma interpretação diferente. Este documento analisa padrões recorrentes de briefs que levaram a projetos fracassados, atrasados ou significativamente acima do orçamento.

---

## Exemplo 1 — O Brief Vago

### O Brief

> "Precisamos melhorar a experiência do usuário no checkout. O processo atual é confuso e lento. Queremos algo moderno e intuitivo. Prazo: 3 meses."

### Por que falhou

- **"Melhorar a experiência"**: Melhorar como? Reduzir etapas? Mudar layout? Adicionar métodos de pagamento? Cada stakeholder interpretou diferente.
- **"Confuso e lento"**: Sem métricas. Confuso para quem? Lento quanto? Sem baseline, impossível saber se melhorou.
- **"Moderno e intuitivo"**: Palavras que não significam nada mensurável. O designer entendeu redesign completo. O dev entendeu ajustes pontuais.
- **Resultado**: 3 meses gastos. Entregaram redesign visual. Taxa de conversão não mudou. O problema real era que o cálculo de frete demorava 8 segundos.

### Lição

Sem métricas de problema e métricas de sucesso, o brief é uma carta de intenções, não um plano de projeto.

---

## Exemplo 2 — O Brief Sem Escopo

### O Brief

> "Construir uma plataforma de marketplace para conectar compradores e vendedores. Funcionalidades: cadastro, busca, carrinho, pagamento, avaliações, chat, logística, relatórios, programa de fidelidade, cupons, wish list, notificações, recomendações personalizadas."

### Por que falhou

- **Escopo infinito**: 14 funcionalidades listadas sem priorização. Tudo era "necessário" para o MVP.
- **Sem faseamento**: Não há indicação de ordem ou importância. O time tentou construir tudo em paralelo.
- **Premissas implícitas**: "Logística" pode ser desde rastreamento até fulfillment próprio. Ninguém perguntou.
- **Resultado**: Após 6 meses, nenhuma funcionalidade estava completa. Todas estavam 60-70% prontas. Lançamento atrasou 4 meses. Budget estourou 2.5x.

### Lição

Brief sem priorização e faseamento é uma lista de desejos, não um projeto. MVP precisa de "M" — mínimo.

---

## Exemplo 3 — O Brief Sem Restrições

### O Brief

> "Migrar o sistema monolítico para microsserviços. Benefícios: escalabilidade, deploy independente, resiliência. Timeline: 12 meses."

### Por que falhou

- **Sem restrições técnicas**: Não mencionou que o monolito tinha 2M de linhas de código, 400 tabelas e zero testes automatizados.
- **Sem restrições organizacionais**: Não mencionou que havia apenas 8 desenvolvedores, dos quais 3 estavam alocados em manutenção do monolito.
- **Sem critérios de priorização**: Quais módulos migrar primeiro? Quais podem ficar no monolito?
- **Benefícios genéricos**: "Escalabilidade" sem dizer qual parte precisa escalar. "Deploy independente" sem explicar por que o deploy atual é problemático.
- **Resultado**: 12 meses depois, 3 microsserviços extraídos (dos 15 planejados), monolito mais complexo que antes (agora com chamadas de rede para os 3 serviços), 2 incidentes graves de inconsistência de dados.

### Lição

Migração para microsserviços sem restrições claras é receita para distributed monolith — o pior dos dois mundos.

---

## Exemplo 4 — O Brief Copiado

### O Brief

> "Queremos fazer igual ao Spotify/Netflix/Uber" (seguido de screenshots e links para artigos de blog de engenharia dessas empresas)

### Por que falhou

- **Contexto completamente diferente**: A empresa tinha 50K usuários. Spotify tem 500M. As soluções de engenharia do Spotify resolvem problemas que esta empresa não tem.
- **Copia a solução, ignora o problema**: O brief deveria explicar o problema da empresa, não a solução de outra empresa.
- **Complexidade desnecessária**: Implementaram event sourcing, CQRS e microservices para um CRUD com 200 requests/minuto.
- **Resultado**: 8 meses de desenvolvimento. Sistema funcional mas absurdamente over-engineered. Custo de operação 10x maior que o necessário. Time não consegue manter o que construiu.

### Lição

A escala e o contexto de outras empresas não são os seus. Copiar soluções sem entender os problemas que elas resolvem é cargo cult engineering.

---

## Padrões Recorrentes de Briefs Ruins

1. **Ausência de problema**: Descreve a solução desejada sem articular o problema
2. **Métricas inexistentes**: Não há como saber se o projeto teve sucesso
3. **Escopo ilimitado**: Lista de desejos sem priorização ou faseamento
4. **Premissas ocultas**: Informações críticas que "todo mundo sabe" mas ninguém documentou
5. **Restrições ignoradas**: Budget, prazo, capacidade do time, limitações técnicas ausentes
6. **Cargo cult**: Copiar soluções de empresas com contexto radicalmente diferente
7. **Solucionismo**: Brief que começa com "precisamos de microsserviços" em vez de "precisamos resolver X"
8. **Consenso falso**: Brief aprovado por todos porque era vago o suficiente para cada um interpretar como quisesse
