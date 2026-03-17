# Evolução do Modelo de Readiness

## Objetivo

Documentar como o modelo de readiness (prontidão para programação) evoluiu ao longo do tempo, desde uma checklist binária até um framework multidimensional com scoring ponderado.

---

## Fase 1: Checklist Binário (Início)

### Formato
Lista simples de sim/não:
- [ ] Requisitos documentados?
- [ ] Arquitetura definida?
- [ ] Riscos identificados?
- [ ] Testes planejados?

### Problemas
1. **Tudo ou nada** — Um item "não" bloqueava o projeto inteiro, mesmo que fosse irrelevante para o tipo de projeto
2. **Sem gradação** — "Requisitos documentados" podia ser um parágrafo ou 50 páginas — ambos marcavam "sim"
3. **Sem ponderação** — Todos os itens tinham o mesmo peso, mas "plano de rollback para migração de banco" é mais crítico que "diagrama de componentes para bugfix"
4. **Subjetividade** — Cada pessoa interpretava "documentado" de forma diferente

### Métricas
- Tempo para avaliação: ~15 minutos
- Confiabilidade: baixa (50% dos projetos que "passavam" tinham retrabalho significativo)
- Satisfação dos times: 4/10 ("burocracia que não agrega")

---

## Fase 2: Checklist por Categoria com Níveis (Mês 4)

### Formato
Itens agrupados por categoria com níveis de completude:

**Requisitos:**
- Nível 1 (Mínimo): Problema definido, personas identificadas
- Nível 2 (Adequado): Cenários de uso detalhados, critérios de aceitação
- Nível 3 (Excelente): Edge cases mapeados, não-escopo explícito, métricas de sucesso

**Arquitetura:**
- Nível 1: Componentes principais identificados
- Nível 2: Interfaces definidas, alternativas avaliadas
- Nível 3: ADR documentado, failure modes analisados, plano de observabilidade

### Melhorias sobre Fase 1
- Gradação permitia avaliar profundidade, não apenas existência
- Categorias agrupavam itens relacionados
- Mínimo viável (Nível 1) permitia fast-track para projetos simples

### Problemas Remanescentes
1. **Sem adaptação por tipo de projeto** — Nível 3 de requisitos era exigido tanto para feature nova quanto para bugfix
2. **Sem peso** — Categoria de testes tinha 5 itens, categoria de riscos tinha 3. Isso criava viés matemático
3. **Avaliação ainda subjetiva** — "Cenários de uso detalhados" não tinha definição operacional

### Métricas
- Tempo para avaliação: ~30 minutos
- Confiabilidade: média (30% de retrabalho em projetos que passavam)
- Satisfação dos times: 6/10 ("melhor, mas ainda genérico")

---

## Fase 3: Modelo Multidimensional Adaptativo (Mês 8)

### Formato
Scoring ponderado por dimensão, adaptado ao tipo de projeto:

**Dimensões:**
1. Clareza de Requisitos (peso varia: 30% para feature nova, 10% para bugfix)
2. Solidez Arquitetural (peso varia: 25% para feature nova, 5% para bugfix)
3. Cobertura de Riscos (peso varia: 15% para feature nova, 40% para bugfix)
4. Design de Testes (peso varia: 15% para feature nova, 30% para bugfix)
5. Plano de Rollout (peso varia: 10% para feature nova, 10% para bugfix)
6. Completude de Handoff (peso fixo: 5%)

**Scoring por dimensão:** 0-10, com rubrica operacional para cada nível

**Exemplo de rubrica — Clareza de Requisitos:**
- 0-2: Problema não definido ou vago
- 3-4: Problema definido mas sem cenários de uso
- 5-6: Cenários de uso documentados, critérios de aceitação parciais
- 7-8: Cenários completos, edge cases identificados, critérios de aceitação mensuráveis
- 9-10: Tudo acima + não-escopo explícito, métricas de sucesso definidas, validado com stakeholder

**Thresholds adaptados:**
- Feature nova: score ponderado >= 7.0 para avançar
- Bugfix crítico: score ponderado >= 6.0 para avançar (fast-track)
- Legacy refactor: score ponderado >= 7.5 para avançar (risco maior)

### Melhorias sobre Fase 2
- Pesos adaptados por tipo de projeto refletem o que importa em cada contexto
- Rubricas operacionais reduzem subjetividade
- Threshold diferenciado permite fast-track sem perder qualidade
- Score numérico permite tracking de tendências

### Métricas
- Tempo para avaliação: ~45 minutos
- Confiabilidade: alta (12% de retrabalho em projetos que passavam)
- Satisfação dos times: 8/10 ("agora faz sentido, não é one-size-fits-all")

---

## Fase 4: Modelo com Feedback Loop (Atual)

### Evolução sobre Fase 3
1. **Calibração contínua** — Pesos são ajustados trimestralmente baseado em correlação entre score e retrabalho real
2. **Dimensões bloqueantes** — Algumas dimensões têm score mínimo independente do ponderado (ex: Riscos >= 5.0 sempre para bugfix)
3. **Histórico comparativo** — Score do projeto é comparado com média de projetos similares para identificar outliers
4. **Post-mortem alimenta rubrica** — Cada incidente revisa a rubrica da dimensão relevante

### Dados de Calibração (Exemplo)

| Tipo de Projeto | Dimensão | Peso Original | Peso Calibrado | Motivo |
|-----------------|----------|---------------|----------------|--------|
| Bugfix Crítico | Design de Testes | 30% | 35% | Correlação com retrabalho era mais forte que esperado |
| Feature Nova | Plano de Rollout | 10% | 15% | 3 incidentes de rollout em features nos últimos 6 meses |
| API Integration | Solidez Arquitetural | 25% | 20% | Menos impacto que Clareza de Requisitos para integrações |

### Métricas Atuais
- Tempo para avaliação: ~30 minutos (automação parcial com templates)
- Confiabilidade: muito alta (8% de retrabalho)
- Satisfação dos times: 8.5/10
- ROI estimado: cada hora investida em readiness previne 4 horas de retrabalho

---

## Lições da Evolução

1. **Comece simples, adicione complexidade sob demanda** — Checklist binário era insuficiente, mas o modelo multidimensional seria over-engineering no início

2. **Adapte por contexto** — Modelo único para todos os tipos de projeto nunca funciona. A adaptação por tipo de projeto foi a mudança com maior impacto

3. **Rubrica operacional elimina subjetividade** — "Requisitos detalhados" é subjetivo. "Cenários de uso com critérios de aceitação mensuráveis" é operacional

4. **Feedback loop é obrigatório** — Sem dados de retrabalho real, calibração é adivinhação. Medir resultado é tão importante quanto medir processo

5. **Dimensões bloqueantes previnem gaming** — Score ponderado alto com dimensão crítica baixa é perigoso. Mínimos por dimensão resolvem isso

6. **Histórico comparativo identifica anomalias** — Projeto com score 5.0 que normalmente teria 7.5 merece investigação antes de avançar
