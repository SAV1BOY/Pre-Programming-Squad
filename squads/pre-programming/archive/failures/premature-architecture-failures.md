# Falhas por Arquitetura Prematura

## Objetivo

Catalogar casos onde decisões arquiteturais foram tomadas cedo demais, baseadas em requisitos especulativos ou otimizações desnecessárias, resultando em complexidade que nunca se justificou.

---

## Caso 1: Microsserviços para MVP de 3 Desenvolvedores

### O Que Aconteceu
Startup com 3 devs decidiu começar o produto com arquitetura de microsserviços "para não ter que migrar depois". Resultado: 8 serviços, API gateway, service mesh, 3 bancos de dados, message broker — tudo para um produto com 200 usuários. Tempo de setup de ambiente local: 45 minutos. Deploy: 1 hora. O time passava mais tempo mantendo infraestrutura do que desenvolvendo features.

### O Que Deu Errado
- Decisão baseada em escala futura especulativa, não em necessidade atual
- Custo operacional de microsserviços ignorado (logging distribuído, tracing, deploy pipeline)
- Cada feature tocava 3-4 serviços, aumentando tempo de desenvolvimento 3x
- Debug de problemas em produção exigia correlacionar logs de múltiplos serviços

### Causa Raiz
**Otimização para problema que não existe.** O time otimizou para escala de 1M de usuários quando tinha 200. A complexidade operacional de microsserviços não se justifica sem volume, time grande ou necessidade de deploy independente real.

### Como Prevenir
1. Exigir justificativa quantitativa para complexidade arquitetural — "e se crescer" não é justificativa
2. Aplicar a regra: "Comece com monolito, extraia serviço quando a dor justificar"
3. Calcular TCO (Total Cost of Ownership) da arquitetura proposta, incluindo operação

### Checklist Atualizado
- [ ] A complexidade arquitetural se justifica para o volume ATUAL (não especulativo)?
- [ ] O TCO da arquitetura foi estimado incluindo operação e manutenção?
- [ ] A equipe tem capacidade de operar a arquitetura proposta?
- [ ] Existe alternativa mais simples que atende os requisitos dos próximos 6 meses?

---

## Caso 2: Event Sourcing para CRUD Simples

### O Que Aconteceu
Time adotou Event Sourcing para sistema de cadastro de clientes porque "assim temos histórico completo". O domínio era essencialmente CRUD com poucos estados. Resultado: projections para ler dados simples, event store para o que seria uma tabela, snapshot management para performance — tudo para um cadastro que tinha 5K registros e 10 alterações/dia.

### O Que Deu Errado
- Event Sourcing escolhido pela elegância teórica, não por necessidade
- Histórico de alterações poderia ser resolvido com audit log simples (10% da complexidade)
- Time gastou 3 semanas aprendendo patterns de Event Sourcing que não dominava
- Bugs em projections criaram inconsistências que não existiriam em CRUD

### Causa Raiz
**Padrão arquitetural desproporcionado ao problema.** Event Sourcing é poderoso para domínios com lógica temporal complexa (financeiro, logística). Para CRUD com necessidade de histórico, audit log resolve com fração da complexidade.

### Como Prevenir
1. Antes de adotar um pattern avançado, definir o problema concreto que ele resolve
2. Listar a alternativa mais simples e quantificar o delta de benefício
3. Considerar experiência do time com o pattern — curva de aprendizado é custo real

### Checklist Atualizado
- [ ] O pattern arquitetural resolve um problema concreto e atual?
- [ ] A alternativa mais simples foi avaliada com análise de trade-offs?
- [ ] A equipe tem experiência com o pattern ou o custo de aprendizado foi considerado?

---

## Caso 3: Abstração Genérica que Ninguém Pediu

### O Que Aconteceu
Requisito: "integrar com gateway de pagamento Stripe". Time criou camada de abstração genérica `PaymentProvider` com interfaces para N gateways, factory pattern, strategy pattern e configuração runtime. Após 2 anos, o sistema ainda usa apenas Stripe. A abstração nunca foi usada, mas todos os devs novos precisam entender 5 classes para mudar qualquer coisa no pagamento.

### O Que Deu Errado
- Abstração criada "para facilitar troca futura" que nunca aconteceu
- Cada mudança no pagamento requer alteração em interface + implementação + factory
- Devs novos levam 2-3 dias extras para entender a camada de abstração
- A abstração real necessária seria diferente da criada especulativamente

### Causa Raiz
**Abstração especulativa.** Criar abstrações para necessidades futuras imaginárias quase sempre resulta em abstração errada, porque os requisitos reais diferem dos especulados. A regra de "tres usos antes de abstrair" existe por bom motivo.

### Como Prevenir
1. Aplicar "Rule of Three": só abstrair quando houver 3 implementações concretas
2. Preferir código específico e claro sobre código genérico e complexo
3. Lembrar que refatorar para abstrair é mais fácil do que remover abstração errada

### Checklist Atualizado
- [ ] Abstrações propostas resolvem necessidade atual com múltiplas implementações concretas?
- [ ] A "Rule of Three" foi aplicada?
- [ ] O custo cognitivo da abstração foi considerado para onboarding?

---

## Caso 4: CQRS em Aplicação com 100 Requests/Minuto

### O Que Aconteceu
Time implementou CQRS (Command Query Responsibility Segregation) com modelos de leitura e escrita separados, eventual consistency entre eles e projections assíncronas. A aplicação recebia 100 requests/minuto. Usuários reportavam "salvei mas não aparece na lista" — o delay de eventual consistency confundia usuários em operações que antes eram instantâneas.

### O Que Deu Errado
- CQRS adotado "para performance" em sistema sem problema de performance
- Eventual consistency degradou a experiência do usuário
- Complexidade de sincronização entre modelos de leitura e escrita gerou bugs
- Time gastou mais tempo debugando consistency issues do que desenvolvendo features

### Causa Raiz
**Solução para problema inexistente com efeitos colaterais piores que o problema.** CQRS faz sentido quando padrões de leitura e escrita são radicalmente diferentes em escala. Em 100 req/min, um índice no banco resolve qualquer gargalo de leitura.

### Como Prevenir
1. Exigir evidência de problema de performance ANTES de adotar patterns de otimização
2. Avaliar impacto na experiência do usuário de decisões arquiteturais
3. Começar com a solução mais simples e escalar sob demanda

### Checklist Atualizado
- [ ] Existe evidência concreta do problema que a arquitetura proposta resolve?
- [ ] O impacto na experiência do usuário foi avaliado?
- [ ] A solução mais simples foi tentada e demonstrou ser insuficiente?

---

## Resumo de Padrões

| Padrão | Frequência | Impacto Médio |
|--------|------------|---------------|
| Microsserviços prematuros | Alta | Produtividade reduzida em 2-3x |
| Pattern avançado para problema simples | Alta | Complexidade acidental por meses |
| Abstração especulativa | Muito Alta | Custo cognitivo permanente |
| Otimização sem evidência de problema | Alta | Degradação de UX, bugs de consistency |

---

## Checklist Consolidado — Arquitetura Prematura

- [ ] A complexidade se justifica para o cenário ATUAL?
- [ ] Existe evidência concreta do problema que a arquitetura resolve?
- [ ] A alternativa mais simples foi avaliada?
- [ ] O TCO inclui operação, manutenção e custo cognitivo?
- [ ] A equipe tem maturidade para operar a arquitetura?
- [ ] Abstrações seguem a "Rule of Three"?
- [ ] O impacto na experiência do usuário foi considerado?
- [ ] Decisão pode ser revertida se premissas não se confirmarem?
