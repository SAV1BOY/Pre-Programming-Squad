# Definição Formal de Implementation Readiness

## Propósito

Estabelecer critérios objetivos e mensuráveis que determinam quando um projeto está pronto para ser implementado por um time de desenvolvimento. A readiness é o principal entregável do Pre-Programming Squad — é o ponto onde nosso trabalho termina e o do time de implementação começa.

## Escopo

Aplica-se a todo projeto que passa pela pipeline do Pre-Programming Squad antes de ser entregue a qualquer squad de implementação.

## Definições

| Termo | Definição |
|---|---|
| Implementation Readiness | Estado em que todas as informações, decisões e artefatos necessários para implementação estão completos, validados e acessíveis |
| Ready | Projeto atende 100% dos critérios obrigatórios e ≥ 80% dos critérios recomendados |
| Conditionally Ready | Projeto atende 100% dos critérios obrigatórios, mas < 80% dos recomendados, com plano para completar durante Sprint 1 |
| Not Ready | Projeto não atende um ou mais critérios obrigatórios |

## Processo

### Avaliação de Readiness

A avaliação é realizada pelo membro do squad responsável pelo projeto, revisada por pelo menos um par, e validada formalmente com o tech lead do squad receptor.

**Etapas:**
1. Auto-avaliação contra o checklist abaixo
2. Revisão por par dentro do Pre-Programming Squad
3. Apresentação ao tech lead do squad receptor
4. Aceite formal ou lista de gaps a endereçar

### Checklist de Readiness

#### Critérios Obrigatórios (todos devem ser atendidos)

**Escopo e Requisitos**
- [ ] Escopo claramente definido com lista explícita de "inclui" e "não inclui"
- [ ] Requisitos funcionais documentados com critérios de aceitação verificáveis
- [ ] Requisitos não-funcionais quantificados (latência, throughput, disponibilidade)
- [ ] Casos de borda (edge cases) identificados e comportamento esperado definido
- [ ] Dependências externas mapeadas com status e contato

**Decisões Técnicas**
- [ ] Decisões arquiteturais registradas em ADRs com alternativas e justificativas
- [ ] Contratos de API definidos (request/response, erros, versionamento)
- [ ] Modelo de dados definido e revisado
- [ ] Padrões de integração com outros serviços definidos

**Riscos e Mitigações**
- [ ] Riscos técnicos identificados, classificados e com plano de mitigação
- [ ] Pre-check de segurança concluído
- [ ] Pre-check de performance concluído (quando aplicável)

**Estimativa e Planejamento**
- [ ] Estimativa de esforço por fase com premissas explícitas
- [ ] Sequência de implementação recomendada
- [ ] Critérios de go/no-go definidos

**Handoff**
- [ ] Pacote de handoff completo conforme standard
- [ ] Artefatos acessíveis ao squad receptor
- [ ] Contato para dúvidas definido com disponibilidade

#### Critérios Recomendados (meta: ≥ 80%)

- [ ] Protótipo ou spike técnico para áreas de incerteza
- [ ] Cenários de teste documentados
- [ ] Diagrama de sequência para fluxos principais
- [ ] Plano de rollback definido
- [ ] Métricas de sucesso alinhadas com produto
- [ ] Análise de impacto em sistemas existentes
- [ ] Estratégia de feature flag definida
- [ ] Documentação de onboarding para engenheiros novos no contexto

### Fluxo de Decisão

```
Auto-avaliação → Todos obrigatórios OK?
  ├── Não → Endereçar gaps → Reavaliar
  └── Sim → ≥ 80% recomendados?
       ├── Sim → READY → Handoff
       └── Não → CONDITIONALLY READY → Handoff com plano de completude
```

## Critérios de Qualidade

- Avaliação de readiness documentada e arquivada para cada projeto
- Squad receptor confirma readiness com assinatura formal
- Discrepância entre readiness avaliada e realidade percebida < 10% (medido por feedback pós-handoff)
- Tempo para atingir readiness dentro do lead time target por tamanho de projeto

## Responsáveis

| Papel | Responsabilidade |
|---|---|
| Membro responsável pelo projeto | Executar auto-avaliação, endereçar gaps |
| Par revisor | Validar completude e qualidade da avaliação |
| Tech Lead (Pre-Prog) | Aprovar readiness antes do handoff |
| Tech Lead (squad receptor) | Aceitar ou rejeitar readiness com justificativa |

## Referências

- What Good Looks Like: `docs/what-good-looks-like.md`
- Standard de Handoff: `docs/handoff-standard.md`
- Standard de Go/No-Go: `docs/go-no-go-standard.md`
