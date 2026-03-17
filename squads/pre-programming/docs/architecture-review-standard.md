# Standard para Revisão de Arquitetura

## Propósito

Garantir que decisões arquiteturais sejam avaliadas de forma estruturada, com trade-offs explícitos, antes da implementação. A revisão de arquitetura identifica riscos estruturais, valida adequação do design aos requisitos e registra decisões para referência futura.

## Escopo

Projetos classificados como M, G ou XG que envolvam: novo serviço, mudança significativa em serviço existente, nova integração, mudança de padrão de dados ou introdução de nova tecnologia.

## Definições

| Termo | Definição |
|---|---|
| ADR | Architecture Decision Record — registro formal de uma decisão arquitetural |
| Fitness Function | Métrica automatizada que valida se a arquitetura atende a um atributo de qualidade |
| Atributo de Qualidade | Propriedade do sistema (latência, disponibilidade, manutenibilidade, segurança, etc.) |
| Blast Radius | Escopo do impacto de uma falha ou mudança |

## Processo

### 1. Preparação

**O que revisar:**
- Proposta de arquitetura (RFC, diagrama, design doc)
- ADRs relacionados
- Contratos de API propostos
- Modelo de dados
- Diagramas de integração

**Quem revisa:**
- Pelo menos 1 membro do Pre-Programming Squad
- Pelo menos 1 pessoa externa com profundidade no domínio técnico
- Para projetos G/XG: participação do arquiteto da organização

### 2. Execução da Revisão

Revisar contra os seguintes eixos:

**Adequação Funcional**
- O design atende aos requisitos funcionais documentados?
- Todos os fluxos principais têm diagrama de sequência ou descrição clara?
- Edge cases estão endereçados no design?

**Atributos de Qualidade**
- Latência: o design atende às metas de performance? Onde estão os gargalos?
- Disponibilidade: qual o impacto de falha de cada componente? Há SPOFs?
- Escalabilidade: o design suporta 10x o volume atual? Onde está o limite?
- Manutenibilidade: o time consegue evoluir este sistema sem o autor original?
- Segurança: o design segue os princípios de security by design?

**Acoplamento e Coesão**
- As fronteiras de serviço estão corretas? Cada serviço tem responsabilidade coesa?
- Existe acoplamento oculto (banco compartilhado, estado global, dependência circular)?
- Os contratos entre componentes estão bem definidos e versionados?

**Operabilidade**
- O design é observável (métricas, logs, traces)?
- Deploy é independente por componente?
- Rollback é possível sem perda de dados?
- O design considera failure modes e degradação graciosa?

**Consistência Organizacional**
- O design segue os padrões da organização (linguagem, infra, patterns)?
- Desvios de padrão são justificados em ADR?
- O time que vai implementar tem a skill necessária?

### 3. Documentação dos Achados

Cada achado documentado como:

```
### Achado [N] — [Título] [SEVERIDADE: Crítico/Alto/Médio/Baixo]
- **Observação:** [O que foi identificado]
- **Evidência:** [Por que isso é um problema — dados, princípios, experiência]
- **Impacto:** [O que acontece se não for endereçado]
- **Recomendação:** [Ação concreta para resolver]
```

### 4. Veredicto

- **Aprovado** — design adequado, pode prosseguir
- **Aprovado com condições** — ajustes necessários antes da implementação (lista de itens)
- **Não aprovado** — redesign necessário (achados críticos não resolvidos)

### 5. Acompanhamento

- Itens condicionais rastreados com owner e prazo
- Re-revisão para itens críticos após ajustes
- ADRs criados/atualizados com decisões tomadas

## Critérios de Qualidade

- Toda revisão cobre os 5 eixos listados
- Achados têm evidência (não apenas opinião)
- Veredicto é claro e acionável
- ADRs produzidos para toda decisão significativa
- Re-revisão concluída antes do início da implementação
- Tempo de revisão proporcional ao risco do projeto

## Responsáveis

| Papel | Responsabilidade |
|---|---|
| Membro do squad (revisor principal) | Conduzir revisão, documentar achados, emitir veredicto |
| Revisor externo | Contribuir com profundidade técnica, validar achados |
| Autor da proposta | Apresentar design, responder questionamentos, endereçar achados |
| Tech Lead | Garantir que revisão foi completa, mediar divergências |

## Referências

- Standard de Revisão de Riscos: `docs/risk-review-standard.md`
- Standard de Segurança: `docs/security-precheck-standard.md`
- Standard de Performance: `docs/performance-precheck-standard.md`
- Estilo de Revisão Técnica: `voice/channels/review-style.md`
