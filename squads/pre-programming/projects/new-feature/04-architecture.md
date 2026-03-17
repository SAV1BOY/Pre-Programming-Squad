# Nova Feature — Fase 04: Arquitetura

## Objetivo da Fase

Desenhar a solução técnica para a feature, avaliar alternativas arquiteturais, documentar decisões e garantir que a arquitetura proposta suporta os requisitos funcionais e não-funcionais.

## Agentes Envolvidos

- **Agente de Arquitetura** (líder da fase) — Desenha solução e avalia alternativas
- **Agente de Riscos** — Identifica riscos técnicos na arquitetura proposta
- **Agente de Escopo** — Valida que arquitetura está alinhada ao escopo definido

## Inputs

- Documento de escopo com cenários priorizados (Fase 03)
- Requisitos não-funcionais com métricas (Fase 02)
- Restrições técnicas conhecidas
- Arquitetura atual do sistema (documentação existente, código)

## Atividades

1. **Mapear arquitetura atual** — Entender como a feature se encaixa no sistema existente. Identificar componentes que serão modificados ou criados.
2. **Propor solução técnica** — Design da solução com diagramas de componentes e interações. Nível de abstração: interfaces entre componentes, não implementação interna.
3. **Avaliar alternativas** — Mínimo de 3 alternativas com análise de trade-offs (complexidade, performance, custo, manutenibilidade).
4. **Documentar ADR** — Architecture Decision Record para cada decisão significativa, com contexto, decisão, alternativas e consequências.
5. **Definir contratos** — APIs, schemas de dados, formatos de mensagens entre componentes novos e existentes.
6. **Avaliar impacto no sistema** — Identificar efeitos colaterais em componentes existentes, migrações de dados necessárias, mudanças de configuração.
7. **Planejar observabilidade** — Métricas, logs estruturados e alertas que serão implementados junto com a feature.

## Outputs

- Design doc com solução proposta e diagramas
- ADRs para decisões significativas
- Análise de alternativas com trade-offs
- Contratos de API e schemas de dados
- Mapa de impacto no sistema existente
- Plano de observabilidade

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Alternativas avaliadas | Mínimo de 3 alternativas com trade-offs documentados | Sim |
| ADRs documentados | Cada decisão significativa tem ADR | Sim |
| Contratos definidos | APIs e schemas documentados para interfaces entre componentes | Sim |
| NFRs atendidos | Arquitetura demonstra como atende requisitos não-funcionais | Sim |
| Impacto mapeado | Efeitos em componentes existentes identificados | Sim |
| Observabilidade planejada | Métricas e alertas definidos | Sim |

## Próxima Fase

→ [05-risks.md](./05-risks.md) — Análise detalhada de riscos, blast radius e planos de mitigação
