# Workshop Kit — Auditoria de Pré-Codificação

## Objetivo

Treinar o squad na condução de auditorias completas de pré-codificação — uma revisão abrangente de todos os artefatos, decisões e preparativos antes de liberar um projeto para implementação. Diferente da readiness review (que avalia prontidão), a auditoria de pré-codificação examina a qualidade e consistência de todo o trabalho realizado, identifica contradições entre artefatos e valida que nenhum aspecto crítico foi negligenciado.

---

## Duração

**4 horas**, divididas em:
- 30min — O que é e por que fazer auditoria de pré-codificação
- 30min — Checklist de auditoria e técnicas de revisão
- 15min — Intervalo
- 90min — Exercício prático: auditoria completa de um projeto
- 30min — Consolidação de achados e classificação
- 15min — Retrospectiva e plano de ação

---

## Participantes

- **Mínimo**: 4 pessoas | **Máximo**: 10 pessoas
- **Perfil ideal**: Membros seniores do Pre-Programming Squad, arquitetos, tech leads
- **Pré-requisito**: Experiência com processos de pré-programação e familiaridade com os artefatos do squad
- **Facilitador**: Líder do squad ou consultor externo com experiência em quality gates

---

## Agenda Detalhada

### Bloco 1 — Conceitos (30 min)

1. **Readiness Review vs Auditoria** (10 min)
   - Readiness review: "Estamos prontos para avançar?"
   - Auditoria: "O que fizemos está correto e consistente?"
   - A auditoria é mais profunda, mais demorada e menos frequente
   - Ideal para projetos de alto risco ou alta complexidade

2. **Dimensões da Auditoria** (10 min)
   - **Completude**: Todos os artefatos necessários existem?
   - **Consistência**: Artefatos não se contradizem?
   - **Clareza**: Artefatos são compreensíveis por quem não os escreveu?
   - **Rastreabilidade**: Cada decisão pode ser rastreada até sua justificativa?
   - **Atualidade**: Artefatos refletem o estado atual do projeto?

3. **Quando auditar** (10 min)
   - Projetos com budget > R$500K
   - Projetos com mais de 3 meses de duração estimada
   - Projetos que impactam sistemas críticos de negócio
   - Quando o squad identifica sinais de alerta durante a preparação
   - Quando há mudança significativa de escopo durante a pré-programação

### Bloco 2 — Checklist e Técnicas (30 min)

**Checklist Mestre de Auditoria**:

**1. Project Brief**
- [ ] Problema claramente definido com métricas
- [ ] Solução proposta alinhada ao problema
- [ ] Escopo com inclusões e exclusões explícitas
- [ ] Métricas de sucesso mensuráveis e acordadas
- [ ] Stakeholders identificados e engajados
- [ ] Restrições documentadas e realistas

**2. Design Doc e ADRs**
- [ ] Design doc aprovado por revisores técnicos
- [ ] Todas as decisões de arquitetura registradas como ADRs
- [ ] Alternativas documentadas para cada ADR
- [ ] Trade-offs explícitos em cada decisão
- [ ] Diagramas presentes e atualizados
- [ ] Consistência entre design doc e ADRs

**3. Contratos de Integração**
- [ ] Todos os pontos de integração documentados
- [ ] Formatos de dados definidos com schemas
- [ ] Tratamento de erros especificado
- [ ] SLAs acordados com proprietários
- [ ] Estratégia de versionamento definida

**4. Plano de Testes**
- [ ] Cenários de teste mapeados para cada requisito
- [ ] Edge cases identificados e documentados
- [ ] Pirâmide de testes definida com percentuais
- [ ] Dados de teste planejados
- [ ] Ambiente de teste especificado

**5. Registro de Riscos**
- [ ] Riscos identificados para todas as categorias
- [ ] Probabilidade e impacto avaliados
- [ ] Planos de mitigação com ações concretas
- [ ] Planos de contingência para riscos críticos
- [ ] Responsáveis atribuídos

**6. Mapa de Dependências**
- [ ] Todas as dependências identificadas
- [ ] Estado de saúde avaliado
- [ ] Contatos estabelecidos
- [ ] Alternativas identificadas para dependências críticas

**7. Premissas**
- [ ] Todas as premissas registradas
- [ ] Premissas críticas validadas ou com plano de validação
- [ ] Impacto de falha avaliado para cada premissa

**8. Plano de Rollout/Rollback**
- [ ] Estratégia de deploy definida
- [ ] Plano de rollback documentado e testável
- [ ] Critérios de go/no-go definidos
- [ ] Comunicação planejada

**Técnica de Revisão Cruzada**:
Cada auditor recebe 2-3 seções do checklist e verifica não apenas completude, mas consistência entre seções. Exemplo: "O risco RSK-003 menciona API de pagamento, mas o mapa de dependências não lista essa API."

### Intervalo (15 min)

### Bloco 3 — Exercício Prático (90 min)

**Setup**: Facilitador prepara um conjunto completo de artefatos de pré-programação para um projeto fictício. Os artefatos contêm:
- 3 inconsistências entre documentos (ex: design doc menciona PostgreSQL, ADR decide por MySQL)
- 2 gaps de completude (ex: dependência crítica sem plano de contingência)
- 2 premissas não validadas marcadas como "confirmadas"
- 1 risco crítico não identificado (mas inferível dos artefatos)
- 1 contradição no escopo (brief diz X, design doc implementa Y)

**Dinâmica**:
1. (10 min) Distribuir artefatos e checklist
2. (40 min) Auditoria em pares — cada par revisa 2-3 seções
3. (20 min) Consolidação — cada par apresenta achados
4. (20 min) Classificação — agrupar achados por severidade:
   - **Bloqueante**: Inconsistência que impede avanço (ex: escopo contraditório)
   - **Crítico**: Gap que deve ser resolvido antes do handoff
   - **Importante**: Melhoria que fortalece a preparação
   - **Observação**: Sugestão de melhoria para próxima vez

### Bloco 4 — Consolidação (30 min)

- Verificar se todos os problemas plantados foram encontrados
- Discutir problemas adicionais identificados
- Criar relatório de auditoria modelo com:
  - Resumo executivo
  - Achados por severidade
  - Recomendações
  - Veredito: aprovado / aprovado com condições / reprovado

### Bloco 5 — Retrospectiva (15 min)

- O processo de auditoria agregou valor?
- Quão longa deveria ser uma auditoria real? (proporcional ao tamanho do projeto)
- Quem deve conduzir? (alguém de fora do projeto ideal)
- Com que frequência aplicar auditorias completas vs reviews simplificadas?

---

## Exercícios

1. **Spot the Contradiction**: Apresentar 2 artefatos com contradição sutil. Quem encontrar primeiro ganha.

2. **Missing Risk**: Apresentar artefatos completos exceto risk register. Pedir que o grupo infira os riscos a partir dos outros documentos.

3. **Rastreabilidade Reversa**: Dado um requisito, rastrear até design, testes, riscos e dependências. Onde a cadeia quebra?

4. **Auditoria Relâmpago**: Em 15 minutos, revisar um projeto real e listar os 5 problemas mais sérios. Priorizar rapidez sobre completude.

---

## Outputs Esperados

- Checklist de auditoria adaptado ao contexto da organização
- Template de relatório de auditoria
- Critérios claros de quando aplicar auditoria completa vs review simplificada
- Participantes capazes de conduzir auditorias independentemente
- Catálogo de "inconsistências comuns" para referência futura
- Processo de auditoria integrado ao fluxo do squad para projetos de alto risco
