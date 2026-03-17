# Workshop Kit — Readiness Review

## Objetivo

Ensinar e praticar o processo de Readiness Review — a avaliação estruturada que determina se um projeto está pronto para avançar da pré-programação para a codificação. Ao final do workshop, participantes serão capazes de conduzir e participar de readiness reviews com critérios objetivos, identificar gaps de preparação e tomar decisões go/no-go fundamentadas.

---

## Duração

**3 horas**, divididas em:
- 30min — Conceitos e importância
- 30min — Critérios de avaliação e scorecards
- 15min — Intervalo
- 60min — Simulação de readiness review
- 30min — Debriefing e calibração
- 15min — Retrospectiva

---

## Participantes

- **Mínimo**: 5 pessoas | **Máximo**: 15 pessoas
- **Perfil ideal**: Membros do Pre-Programming Squad, tech leads, product managers, QA leads
- **Pré-requisito**: Familiaridade básica com processos de planejamento de software
- **Facilitador**: Líder do squad ou membro sênior com experiência em gates de qualidade

---

## Agenda Detalhada

### Bloco 1 — Conceitos e Importância (30 min)

1. **O que é Readiness Review** (10 min)
   - Gate de qualidade entre pré-programação e codificação
   - Não é aprovação burocrática — é validação de preparação
   - Diferença de "pronto para codificar" vs "pronto para entregar"
   - Custo de começar cedo demais vs custo de preparação excessiva

2. **Quando aplicar** (10 min)
   - Projetos novos: review completa obrigatória
   - Features grandes (> 5 story points): review padrão
   - Features pequenas (< 5 story points): review simplificada (checklist)
   - Hotfixes: review pós-facto dentro de 48h

3. **Papéis na review** (10 min)
   - Facilitador: conduz a sessão, mantém foco e tempo
   - Apresentador: quem preparou os artefatos, apresenta o estado
   - Revisores: questionam, desafiam, avaliam
   - Decisor: quem dá o veredito final (normalmente tech lead + product owner)

### Bloco 2 — Critérios e Scorecards (30 min)

Apresentar e discutir cada critério da scorecard padrão:

| Critério | Peso | O que Avalia |
|----------|------|-------------|
| Clareza de Requisitos | 20% | Requisitos documentados, sem ambiguidade, validados com stakeholders |
| Completude do Design | 20% | Design doc completo, ADRs escritos, diagramas presentes |
| Contratos de Integração | 15% | APIs definidas, formatos acordados, SLAs estabelecidos |
| Plano de Testes | 15% | Cenários mapeados, dados planejados, pirâmide definida |
| Riscos Mapeados | 10% | Risk register atualizado, mitigações definidas |
| Dependências Resolvidas | 10% | Mapa de dependências com status verde ou plano B |
| Plano de Rollout/Rollback | 10% | Estratégia de deploy, critérios de rollback, runbook |

Nota mínima para aprovação: 3/5 em cada critério, 4/5 na média geral.
Critérios bloqueantes: qualquer critério com nota 1 bloqueia aprovação.

### Intervalo (15 min)

### Bloco 3 — Simulação de Readiness Review (60 min)

**Setup**: Facilitador prepara um cenário de projeto fictício com artefatos intencionalmente imperfeitos — alguns completos, outros com gaps plantados.

**Dinâmica**:
1. (10 min) Participantes leem os artefatos em silêncio
2. (5 min) Apresentador fictício apresenta o projeto
3. (25 min) Revisores questionam e avaliam cada critério
4. (10 min) Cada revisor preenche scorecard individualmente
5. (10 min) Discussão coletiva e decisão go/no-go

**Cenários para a simulação**:
- Projeto A: Quase pronto, mas falta plano de rollback e 2 premissas não validadas
- Projeto B: Design doc excelente, mas zero plano de testes e dependência crítica sem contato
- Projeto C: Tudo "OK" mas superficial — nada é profundo o suficiente para guiar implementação

### Bloco 4 — Debriefing e Calibração (30 min)

- Comparar scorecards individuais — onde houve divergência?
- Calibrar entendimento: o que é nota 3 vs nota 4 em cada critério?
- Discutir: os gaps plantados foram todos identificados?
- Que gaps adicionais os participantes encontraram que não foram plantados?

### Bloco 5 — Retrospectiva (15 min)

- O que funcionou no processo?
- O que ajustar para nosso contexto?
- Quanto tempo deveria durar uma readiness review real?
- Quem deveria participar de reviews reais?

---

## Exercícios

1. **Exercício de Scorecard Rápida**: Dado um projeto real passado, preencher scorecard em 10 minutos. Comparar com resultado real do projeto.

2. **Exercício de "O que falta?"**: Apresentar artefatos de um projeto e pedir que cada pessoa liste os 3 itens mais importantes que faltam.

3. **Exercício de Go/No-Go**: Apresentar 5 cenários rápidos (1 parágrafo cada). Para cada um, decidir Go, No-Go ou Go Condicional em 2 minutos.

4. **Exercício de Calibração**: Grupo avalia o mesmo projeto. Comparar notas. Discutir divergências até alcançar entendimento comum.

---

## Outputs Esperados

- Scorecard de readiness review calibrada e acordada pelo grupo
- Critérios de aprovação, aprovação condicional e reprovação definidos
- Template de readiness review adaptado ao contexto da organização
- Lista de "gaps mais perigosos" que a review deve sempre verificar
- Participantes confiantes para conduzir ou participar de readiness reviews reais
