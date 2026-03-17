# Template: Definição de Pronto

## Título
Definition of Done — Critérios de Conclusão para Entregáveis

## Propósito
Estabelecer critérios claros e mensuráveis que definem quando um item de trabalho, funcionalidade ou fase está realmente concluído, evitando débito técnico oculto e retrabalho.

## Quando Usar
- No início do projeto, para alinhar expectativas sobre qualidade.
- Ao definir critérios de aceite para funcionalidades.
- Em revisões de processo, para ajustar o nível de qualidade esperado.

## Seções

### 1. Informações Gerais
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| Escopo | `[Projeto inteiro / Fase / Feature]` |
| Responsável | `[nome]` |
| Data | `[YYYY-MM-DD]` |
| Aprovado Por | `[nomes dos aprovadores]` |

### 2. DoD — Nível de User Story / Feature
- [ ] Código implementado e revisado por pelo menos `[N]` pares
- [ ] Testes unitários escritos e passando (cobertura ≥ `[X]`%)
- [ ] Testes de integração escritos e passando
- [ ] Sem warnings de linter ou erros de compilação
- [ ] Documentação da API atualizada (se aplicável)
- [ ] Dados de teste atualizados
- [ ] Sem débitos técnicos não registrados
- [ ] Critérios de aceite do requisito atendidos
- [ ] `[critério adicional específico do projeto]`

### 3. DoD — Nível de Sprint / Iteração
- [ ] Todas as stories da sprint atendem ao DoD de Feature
- [ ] Build verde no CI/CD
- [ ] Nenhum bug crítico ou bloqueante aberto
- [ ] Ambiente de staging atualizado e funcional
- [ ] Demo realizado para stakeholders
- [ ] Retrospectiva realizada
- [ ] `[critério adicional]`

### 4. DoD — Nível de Release
- [ ] Todas as sprints do release atendem ao DoD de Sprint
- [ ] Testes E2E passando em staging
- [ ] Testes de performance executados e dentro dos limites
- [ ] Revisão de segurança realizada
- [ ] Plano de rollback documentado e testado
- [ ] Runbook de operação atualizado
- [ ] Monitoramento e alertas configurados
- [ ] Aprovação do Product Owner
- [ ] `[critério adicional]`

### 5. Exceções e Dispensas
| Critério Dispensado | Motivo | Aprovado Por | Prazo para Regularizar |
|---------------------|--------|-------------|----------------------|
| `[critério]` | `[justificativa]` | `[nome]` | `[data]` |

### 6. Histórico de Mudanças
| Data | Mudança | Motivo | Aprovado Por |
|------|---------|--------|-------------|
| `[data]` | `[o que mudou]` | `[por quê]` | `[nome]` |

## Exemplo de Preenchimento

### 2. DoD — Nível de Feature
- [x] Código implementado e revisado por pelo menos 1 par
- [x] Testes unitários escritos e passando (cobertura ≥ 80%)
- [x] Testes de integração escritos e passando
- [x] Sem warnings de linter ou erros de compilação
- [x] Documentação da API atualizada no Swagger
- [x] Sem débitos técnicos não registrados
- [x] Critérios de aceite do requisito atendidos
- [x] Tradução de strings para PT-BR e EN completa

## Dicas de Qualidade
- **Seja realista:** DoD impossível de cumprir será ignorado pela equipe.
- **Evolua gradualmente:** Comece com critérios básicos e aumente conforme a maturidade.
- **Visível e acessível:** A DoD deve estar em um lugar que todos consultam facilmente.
- **Sem exceções silenciosas:** Se um critério for dispensado, documente com aprovação.
- **Consenso da equipe:** A DoD deve ser acordada por todos que a cumprem, não imposta de cima.
