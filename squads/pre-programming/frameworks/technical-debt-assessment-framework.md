# Technical Debt Assessment Framework

## Propósito
Identificar, classificar e priorizar dívida técnica existente antes de iniciar implementação, evitando que novo código herde problemas e garantindo que decisões de "pagar agora vs depois" sejam conscientes.

## Problema que Resolve
Times constroem features novas em cima de código com dívida técnica e depois se surpreendem quando tudo quebra. Este framework faz a avaliação antes de começar, para que o custo da dívida entre no planejamento.

## Quando Usar
- Antes de qualquer feature que toque código existente
- Em projetos de refactoring (obrigatório)
- Quando Legacy Impact Auditor identifica áreas de risco
- Em avaliações de esforço (dívida técnica = custo oculto)

## Taxonomia de Dívida Técnica

| Tipo | Descrição | Exemplo | Detectável por |
|------|-----------|---------|---------------|
| **Design debt** | Arquitetura não adequada ao problema atual | God class com 3000 linhas | System Architect |
| **Code debt** | Código difícil de manter | Sem testes, nomes ruins, copy-paste | Legacy Impact Auditor |
| **Test debt** | Cobertura insuficiente ou testes frágeis | 0% coverage em módulo crítico | Test Strategist |
| **Infrastructure debt** | Infra manual, sem IaC, sem CI/CD | Deploy manual via SSH | Performance Capacity Planner |
| **Documentation debt** | Falta de docs ou docs desatualizados | ADRs de 2019 que não refletem realidade | Requirements Clarifier |
| **Dependency debt** | Libs desatualizadas ou vulneráveis | Framework 3 major versions atrás | Security & Trust Reviewer |

## Processo

### Passo 1 — Mapear Áreas Afetadas
Identificar todos os módulos/serviços/componentes que serão tocados pela nova feature.

### Passo 2 — Avaliar Dívida por Área
Para cada área, preencher:

| Área | Tipo de Dívida | Severidade | Impacto no Novo Trabalho | Custo para Pagar |
|------|---------------|------------|-------------------------|-----------------|
| auth-service | Design (monolito) | Alta | Bloqueia isolamento | 2 sprints |
| payment-api | Test (0% coverage) | Crítica | Impossível refatorar com segurança | 1 sprint |
| user-model | Code (legacy patterns) | Média | Aumenta tempo de dev em 30% | 3 dias |

### Passo 3 — Classificar Decisão

Para cada dívida identificada:

**Pagar Agora (antes de implementar):**
- Dívida que bloqueia a nova feature
- Dívida que torna o novo código inseguro (test debt em área crítica)
- Custo de pagar agora < custo de manter + risco

**Pagar Depois (backlog de tech debt):**
- Dívida que não bloqueia mas aumenta custo
- Custo de pagar agora > benefício imediato
- Registrar em backlog com prazo e owner

**Aceitar Conscientemente:**
- Dívida que não impacta o novo trabalho
- Custo de pagar é desproporcional ao benefício
- Registrar decisão em ADR com justificativa

### Passo 4 — Incluir no Planejamento
- Dívida a pagar agora → entra no escopo e estimativa
- Dívida a pagar depois → entra no backlog com owner e prazo
- Dívida aceita → documentada em ADR como decisão consciente

### Passo 5 — Validar com o Time
O time de implementação (Coding Squad) valida:
- Concordam com a avaliação de severidade?
- Concordam com a classificação pagar/depois/aceitar?
- Estimativas de custo são realistas?

## Heurísticas de Priorização
1. **Test debt em área que será modificada → sempre pagar antes** (sem testes = refactoring cego)
2. **Design debt que força workarounds no novo código → pagar antes** (workaround vira nova dívida)
3. **Dependency debt com vulnerabilidades conhecidas → pagar antes** (risco de segurança)
4. **Documentation debt → pagar durante** (documentar enquanto aprende)
5. **Code debt estético (nomes, formatação) → pagar depois** (baixo impacto)

## Armadilhas
- **Ignorar dívida e construir em cima** → Nova feature herda todos os problemas
- **Querer pagar toda dívida antes de começar** → Paralisia; pague só o que impacta
- **Não quantificar custo** → "Tem dívida técnica" sem dimensionar não é acionável
- **Confundir dívida deliberada com acidental** → Dívida deliberada (trade-off consciente) é ok; acidental (descuido) é problema
- **Não registrar dívida aceita** → Decisão de aceitar sem ADR = dívida esquecida

## Métricas
- **Dívida identificada vs paga:** Rastrear % de dívida resolvida por sprint
- **Custo de dívida no planejamento:** Horas adicionais por causa de dívida existente
- **Dívida nova criada:** Novas decisões de "pagar depois" por projeto
