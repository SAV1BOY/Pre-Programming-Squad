# Nova Feature — Fase 05: Riscos

## Objetivo da Fase

Identificar, classificar e planejar mitigação para todos os riscos relevantes da nova feature, incluindo riscos técnicos, de negócio e operacionais.

## Agentes Envolvidos

- **Agente de Riscos** (líder da fase) — Identifica e classifica riscos
- **Agente de Arquitetura** — Valida viabilidade das mitigações técnicas
- **Agente de Testes** — Identifica riscos de qualidade e cobertura

## Inputs

- Design doc e ADRs (Fase 04)
- Mapa de impacto no sistema existente
- Requisitos não-funcionais
- Histórico de incidentes em componentes afetados (archive de falhas)

## Atividades

1. **Identificar riscos técnicos** — Componentes novos sem precedente, integrações com sistemas instáveis, migrações de dados, pontos de falha única.
2. **Identificar riscos de negócio** — Impacto em receita se feature falhar, dependência de parceiros externos, prazos regulatórios.
3. **Identificar riscos operacionais** — Capacidade de monitorar, depurar e corrigir problemas em produção. Necessidade de runbooks.
4. **Classificar por probabilidade x impacto** — Matriz de risco com classificação High/Medium/Low para probabilidade e impacto.
5. **Definir blast radius** — Para cada risco de alto impacto, mapear o que seria afetado se o risco se materializasse (usuários, receita, dados, SLA).
6. **Planejar mitigações** — Para cada risco High, definir ação preventiva e plano de contingência. Para Medium, definir pelo menos ação preventiva.
7. **Definir plano de rollback** — Mecanismo para reverter a feature se necessário (feature flag, deploy reverso, migração reversa).

## Outputs

- Matriz de riscos classificada (probabilidade x impacto)
- Mapa de blast radius para riscos de alto impacto
- Plano de mitigação para riscos High e Medium
- Plano de rollback detalhado
- Lista de dependências de terceiros com plano de contingência

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Riscos identificados | Mínimo de 5 riscos avaliados por categoria (técnico, negócio, operacional) | Sim |
| Blast radius mapeado | Riscos High têm mapa de impacto | Sim |
| Mitigações definidas | Todo risco High tem ação preventiva E plano de contingência | Sim |
| Rollback planejado | Mecanismo de rollback definido e testável | Sim |
| Archive consultado | Falhas históricas similares foram verificadas | Sim |

## Próxima Fase

→ [06-tests.md](./06-tests.md) — Design da estratégia de testes para a feature
