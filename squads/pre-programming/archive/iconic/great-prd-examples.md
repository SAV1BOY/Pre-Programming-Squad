# Exemplos Icônicos de PRDs (Product Requirements Documents)

## Objetivo

Documentar exemplos anotados de PRDs excepcionais que servem como referência para o Pre-Programming Squad. Cada exemplo ilustra práticas que elevam a qualidade da especificação antes do código ser escrito.

---

## Exemplo 1: PRD do Sistema de Notificações em Tempo Real

### Contexto
Plataforma SaaS B2B que precisava implementar notificações push, in-app e por email com regras de priorização e agrupamento inteligente.

### Trechos Anotados

**Seção de Problema:**
> "Usuários perdem 23% das atualizações críticas porque o sistema atual envia todas as notificações com a mesma prioridade. Dados de suporte mostram que 67% dos tickets de 'não vi a atualização' ocorrem em contas com mais de 50 notificações/dia."

*Anotação: Quantifica o problema com dados reais. Não diz apenas "notificações não funcionam bem" — demonstra impacto mensurável.*

**Seção de Personas:**
> "Persona A — Gerente de Operações (Maria): Recebe ~120 notificações/dia. Precisa ver apenas as críticas imediatamente. Usa mobile 70% do tempo. Persona B — Analista Junior (Pedro): Recebe ~30 notificações/dia. Precisa de contexto completo em cada notificação. Usa desktop 90% do tempo."

*Anotação: Personas com comportamento quantificado, não genéricas. Cada persona tem padrão de uso que influencia decisões técnicas.*

**Seção de Não-Escopo:**
> "Não faremos: (1) Motor de ML para priorização automática — será regra manual na v1. (2) Integração com Slack/Teams — planejado para Q3. (3) Notificações SMS — custo por mensagem inviável no modelo atual."

*Anotação: Cada exclusão tem justificativa. Isso previne retrabalho e scope creep.*

### O Que Torna Este PRD Excelente
- Problema definido com métricas, não com opinião
- Personas baseadas em dados de uso real
- Não-escopo explícito e justificado
- Critérios de sucesso mensuráveis (reduzir tickets de "não vi" em 40%)
- Wireframes de baixa fidelidade incluídos para alinhar expectativas

---

## Exemplo 2: PRD da Migração do Motor de Busca

### Contexto
E-commerce com 2M+ SKUs migrando de Elasticsearch 5.x para uma solução com busca semântica e filtros facetados otimizados.

### Trechos Anotados

**Seção de Restrições Técnicas:**
> "Restrição 1: A migração não pode degradar a latência p99 atual de 200ms. Restrição 2: O índice atual de 2.3TB precisa ser recriado sem downtime. Restrição 3: Queries customizadas de 47 parceiros via API não podem quebrar — mapeamento de compatibilidade obrigatório."

*Anotação: Restrições técnicas explícitas no PRD, não deixadas para o time de engenharia descobrir. Cada uma tem número concreto.*

**Seção de Rollout:**
> "Fase 1 (semana 1-2): Shadow mode — nova engine roda em paralelo, resultados comparados mas não exibidos. Fase 2 (semana 3): 5% do tráfego via feature flag. Fase 3 (semana 4-5): 25% → 50% → 100% com gates de qualidade em cada incremento."

*Anotação: Plano de rollout gradual com critérios de promoção. Não assume big bang deployment.*

### O Que Torna Este PRD Excelente
- Restrições técnicas quantificadas no documento de produto
- Plano de migração faseado com critérios de go/no-go
- Mapeamento de dependências externas (47 parceiros)
- Definição de métricas de comparação (A/B entre engines)
- Plano de rollback explícito em cada fase

---

## Exemplo 3: PRD do Sistema de Permissões Granulares (RBAC)

### Contexto
Plataforma multi-tenant que precisava evoluir de 3 roles fixos para um sistema de permissões granulares com herança e delegação.

### Trechos Anotados

**Seção de Modelo Mental:**
> "O usuário pensa em 'o que posso fazer', não em 'qual role eu tenho'. A UI deve refletir capacidades, não roles. Exemplo: em vez de mostrar 'Você é Editor', mostrar 'Você pode: editar documentos, comentar, convidar viewers'."

*Anotação: Traduz conceito técnico (RBAC) em modelo mental do usuário. Isso alinha produto e engenharia.*

**Seção de Edge Cases:**
> "Edge case 1: Usuário tem Role A (pode editar) e Role B (não pode editar) — qual prevalece? Decisão: permissão mais permissiva vence (union). Edge case 2: Admin remove própria permissão de admin — bloquear? Decisão: sim, último admin não pode se remover."

*Anotação: Edge cases resolvidos no PRD, não durante a implementação. Cada um com decisão documentada.*

### O Que Torna Este PRD Excelente
- Modelo mental do usuário explícito
- Edge cases identificados e resolvidos antes do desenvolvimento
- Matriz de permissões completa como apêndice
- Cenários de migração de dados para roles existentes
- Considerações de auditoria e compliance integradas

---

## Lições Aplicáveis

### Para o Pre-Programming Squad

1. **Exija quantificação do problema** — Se o PRD não tem números, ele não está pronto para pré-programação. Devolva com pedido de dados.

2. **Valide o não-escopo** — Todo PRD deve ter seção de não-escopo com justificativas. Isso é tão importante quanto o escopo.

3. **Busque edge cases no PRD** — Se edge cases aparecem só durante o design técnico, o PRD falhou. O Agente de Análise de Requisitos deve extrair os principais antes.

4. **Confirme restrições técnicas** — PRDs que ignoram restrições técnicas geram retrabalho. O squad deve validar que restrições conhecidas estão documentadas.

5. **Verifique critérios de sucesso** — Sem métrica de sucesso, não há como saber se o projeto entregou valor. Gate obrigatório antes de prosseguir.

6. **Plano de rollout no PRD** — Mesmo em nível alto, o PRD deve indicar se é big bang ou gradual. Isso influencia a arquitetura.

7. **Personas com dados, não ficção** — Personas genéricas ("João, 35 anos, gosta de tecnologia") não ajudam. Exija padrões de uso reais.
