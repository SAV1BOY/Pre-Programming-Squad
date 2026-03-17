# Michael Nygard — Resumo de Autoridade

## Autor

**Nome**: Michael Nygard
**Afiliação**: Arquiteto de software, VP na Sabre Corporation
**Obra Principal**: "Release It! Design and Deploy Production-Ready Software" (2a ed., 2018)
**Área de Expertise**: Sistemas em produção, resiliência, estabilidade, padrões de deploy

---

## Tese Central

A maioria dos problemas em produção não é causada por bugs lógicos — é causada por **falhas de estabilidade** que poderiam ter sido prevenidas com design adequado. Software que funciona em testes frequentemente falha em produção porque o ambiente de produção tem características que o teste não reproduz: carga real, falhas parciais, timeouts, recursos esgotados e interações inesperadas entre componentes. Projetar para produção desde o início é fundamentalmente diferente de projetar para "funcionar".

Nygard também é criador do formato ADR (Architecture Decision Record), ferramenta fundamental para documentar decisões de arquitetura.

---

## Conceitos-Chave

### 1. Anti-Padrões de Estabilidade
- **Integration Points**: Todo ponto de integração é um ponto de falha potencial. Tratar como hostil por default.
- **Chain Reactions**: Falha em um nó sobrecarrega os demais, que falham em cascata.
- **Cascading Failures**: Falha em um serviço se propaga para dependentes.
- **Users**: Usuários fazem coisas inesperadas. Tráfego real não é distribuído uniformemente.
- **Blocked Threads**: Thread que espera indefinidamente por recurso é a causa mais comum de sistemas "travados".
- **Unbounded Result Sets**: Queries sem LIMIT que retornam milhões de registros inesperadamente.

### 2. Padrões de Estabilidade
- **Timeouts**: Toda chamada externa deve ter timeout. Sem exceção.
- **Circuit Breaker**: Interromper chamadas para serviço que está falhando, evitando cascata.
- **Bulkheads**: Isolar componentes para que falha em um não afete outros.
- **Steady State**: Sistemas devem ser projetados para rodar indefinidamente sem intervenção manual (limpar logs, reciclar conexões).
- **Fail Fast**: Se vai falhar, falhe imediatamente. Não consuma recursos esperando.
- **Handshaking**: Validar que o outro lado está pronto antes de enviar carga completa.

### 3. Architecture Decision Records (ADRs)
Nygard criou o formato ADR como documento curto e focado:
- Contexto: Situação que motivou a decisão
- Decisão: O que foi decidido
- Status: Proposta/Aceita/Depreciada/Superada
- Consequências: O que resulta da decisão

### 4. Design for Production
Produção não é deployment — é operação contínua. Design para produção inclui: transparência (logging, monitoring), manutenibilidade (configuração sem deploy), resilência (falha parcial, não total).

---

## Aplicação ao Squad

- **Anti-padrões como checklist de revisão**: Em cada design doc, verificar: todos os integration points têm timeout? Existe circuit breaker? Queries têm LIMIT? Thread pools são bounded?

- **Padrões de estabilidade no design**: Timeout, circuit breaker e bulkhead devem estar no design doc, não como afterthought de operação.

- **ADRs como prática padrão**: Usar o formato de Nygard para todas as decisões de arquitetura do squad. Curto, focado, imutável.

- **"Design for Production" como critério de readiness**: Na readiness review, perguntar: "Este sistema foi projetado para rodar em produção por 1 ano sem intervenção manual?". Se a resposta é não, o design precisa de ajuste.

- **Failure mode analysis obrigatória**: Para cada integration point, documentar: O que acontece se falhar? O que acontece se ficar lento? O que acontece se retornar dados inesperados?

---

## Citações Relevantes

> "The only way to avoid failure is to never deploy anything. Failing is normal. The question is whether you recover quickly or slowly."

> "Every integration point will eventually fail in some way, and you need to be prepared for that failure."

> "The most common failure mode in production systems is not crashes — it's hangs."

> "In production, problems tend to manifest as slow responses rather than errors."

> "Design for failure is not pessimism. It's professionalism."
