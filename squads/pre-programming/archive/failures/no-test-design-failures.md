# Falhas por Ausência de Design de Testes

## Objetivo

Catalogar casos onde a falta de planejamento de testes na fase de pré-programação resultou em bugs em produção, cobertura falsa ou testes que não testavam nada relevante.

---

## Caso 1: 95% de Cobertura, Zero Confiança

### O Que Aconteceu
Time atingiu 95% de code coverage como meta obrigatória. Após atingir, deployaram com confiança. Primeiro dia em produção: 3 bugs críticos. Investigação revelou que a maioria dos testes verificava apenas o "happy path", mocks substituíam toda lógica de negócio complexa, e assertions eram superficiais (`assert result != null`).

### O Que Deu Errado
- Meta de cobertura sem critério de qualidade dos testes
- Testes escritos para atingir métrica, não para validar comportamento
- Mocks excessivos: testes não executavam lógica real
- Assertions verificavam existência, não corretude (`!= null` em vez de `== valor_esperado`)
- Nenhum teste de integração entre componentes reais

### Causa Raiz
**Teste como métrica, não como design.** Quando testes são escritos após o código para atingir coverage, eles tendem a testar o que foi implementado, não o que deveria ter sido implementado. Sem design de testes na pré-programação, a estratégia de teste é reativa e superficial.

### Como Prevenir
1. Design de testes deve ser feito ANTES da implementação, como parte da pré-programação
2. Definir cenários de teste baseados em requisitos, não em código
3. Proibir metas de cobertura sem critério de qualidade (mutation testing como complemento)
4. Exigir assertions específicas — banir `!= null` como assertion principal

### Checklist Atualizado
- [ ] Cenários de teste foram derivados dos requisitos (não do código)?
- [ ] Estratégia de testes inclui happy path, sad path e edge cases?
- [ ] Assertions verificam valores específicos, não apenas existência?
- [ ] Proporção de mocks é justificada e não esconde lógica complexa?

---

## Caso 2: Testes de Integração que Não Integram Nada

### O Que Aconteceu
Suite de testes de integração rodava com banco em memória (H2), API stubs para todos os serviços externos e clock mockado. Todos os 200 testes passavam. Em produção: incompatibilidade de SQL entre H2 e PostgreSQL, timeouts com serviços reais que stubs não simulavam, e race condition em processamento concorrente que clock mockado escondia.

### O Que Deu Errado
- "Testes de integração" não integravam com nenhum componente real
- H2 aceita SQL que PostgreSQL rejeita (e vice-versa)
- Stubs retornavam instantaneamente, mascarando problemas de latência
- Clock mockado eliminava toda condição temporal

### Causa Raiz
**Testes de integração sem nenhuma integração real.** O nome "teste de integração" foi usado para testes que executam mais código mas não integram com componentes reais. A pirâmide de testes ficou com um buraco na camada que realmente importa.

### Como Prevenir
1. Testes de integração devem usar banco real (Testcontainers para PostgreSQL, Redis, etc.)
2. Pelo menos um teste por integração externa deve usar sandbox real do serviço
3. Classificar testes explicitamente: unitário, integração (componentes reais) e contrato
4. Testes de contrato (Pact) para validar interfaces entre serviços

### Checklist Atualizado
- [ ] Testes de integração usam banco real (não in-memory)?
- [ ] Integrações externas têm testes com sandbox real ou teste de contrato?
- [ ] Testes estão classificados (unitário, integração, contrato, e2e)?
- [ ] Latência e timeouts são testados (não apenas happy path instantâneo)?

---

## Caso 3: Sem Testes de Concorrência — Race Condition em Produção

### O Que Aconteceu
Sistema de reserva de ingressos. Testes passavam: "reservar ingresso" funcionava. Em produção, dois usuários reservaram o mesmo ingresso simultaneamente. O teste nunca simulava acesso concorrente. Resultado: venda duplicada de 340 ingressos no primeiro evento, R$85K em reembolsos.

### O Que Deu Errado
- Nenhum teste simulava acesso concorrente ao mesmo recurso
- Lógica de "check-then-act" sem lock otimista ou pessimista
- Testes sequenciais passavam porque condição de corrida não se manifesta sem concorrência
- Revisão de código não identificou o problema porque a lógica individual estava correta

### Causa Raiz
**Ausência de testes de concorrência no design.** Operações de "verificar e reservar" (check-then-act) são inerentemente vulneráveis a race conditions. Se o design de testes não inclui cenários concorrentes para operações de estado, esse bug é garantido.

### Como Prevenir
1. Identificar todas as operações de check-then-act no design
2. Para cada uma, incluir teste com 10+ threads concorrentes no mesmo recurso
3. Definir mecanismo de concurrency control no design (optimistic locking, pessimistic locking, serializable isolation)
4. Teste de carga com cenários de contention antes do launch

### Checklist Atualizado
- [ ] Operações check-then-act foram identificadas?
- [ ] Testes de concorrência estão planejados para operações de estado?
- [ ] Mecanismo de concurrency control está definido no design?
- [ ] Teste de carga inclui cenários de contention?

---

## Caso 4: Testes E2E Frágeis que Ninguém Confia

### O Que Aconteceu
Suite de 500 testes E2E com Selenium. 30% falhavam intermitentemente por: waits hardcoded, dependência de dados de teste voláteis, acoplamento a texto da UI ("Clique em 'Salvar'"), ordem de execução dependente. Time começou a ignorar falhas ("é flaky, reroda"). Bug real chegou em produção mascarado por flakiness — o teste que deveria pegar estava na lista de "sempre falha, ignora".

### O Que Deu Errado
- Testes frágeis não foram consertados — foram ignorados
- Sem política de quarentena para testes flaky
- Waits hardcoded (`sleep 5`) em vez de condições explícitas
- Dados de teste compartilhados entre testes, criando dependência de ordem
- Acoplamento a textos da UI que mudam frequentemente

### Causa Raiz
**Testes E2E sem design de manutenibilidade.** Testes E2E são os mais caros de manter. Sem design cuidadoso (page objects, dados isolados, waits inteligentes), eles se degradam até serem ignorados — pior que não ter testes.

### Como Prevenir
1. Limitar testes E2E a fluxos críticos de negócio (máximo 50-100, não 500)
2. Usar page objects e seletores data-testid (nunca texto da UI)
3. Cada teste cria e limpa seus dados (sem compartilhamento)
4. Política de quarentena: teste flaky vai para quarentena em 48h, consertado ou removido em 1 semana

### Checklist Atualizado
- [ ] Testes E2E são limitados a fluxos críticos de negócio?
- [ ] Page objects e seletores estáveis são usados?
- [ ] Dados de teste são isolados por teste?
- [ ] Existe política de quarentena para testes flaky?

---

## Resumo de Padrões

| Padrão | Frequência | Impacto Médio |
|--------|------------|---------------|
| Cobertura alta sem qualidade de assertions | Muito Alta | Falsa confiança, bugs em prod |
| Testes de integração sem integração real | Alta | Incompatibilidades em prod |
| Ausência de testes de concorrência | Alta | Race conditions, perda financeira |
| Testes E2E frágeis ignorados | Muito Alta | Bugs mascarados por flakiness |

---

## Checklist Consolidado — Design de Testes

- [ ] Cenários de teste foram derivados dos requisitos na fase de pré-programação?
- [ ] Estratégia de testes define camadas (unitário, integração, contrato, E2E)?
- [ ] Testes de integração usam componentes reais?
- [ ] Operações concorrentes têm testes de concorrência planejados?
- [ ] Assertions são específicas e verificam corretude?
- [ ] Testes E2E são limitados a fluxos críticos?
- [ ] Dados de teste são isolados e independentes?
- [ ] Existe política de quarentena para testes flaky?
- [ ] Mutation testing é usado como complemento a coverage?
