# Bugfix Crítico — Fase 06: Testes

## Objetivo da Fase

Definir o conjunto mínimo de testes que valida o fix sem atrasar o deploy de urgência. Foco em: reproduzir o bug, confirmar o fix, garantir que nada mais quebrou.

## Agentes Envolvidos

- **Agente de Testes** (líder da fase) — Define testes mínimos obrigatórios
- **Agente de Riscos** — Valida que testes cobrem cenários de risco do fix

## Inputs

- Fix proposto (Fase 03)
- Passos de reprodução do bug (Fase 02)
- Caminhos de código afetados (Fase 02)
- Critérios de sucesso do fix (Fase 05)

## Atividades

1. **Criar teste de reprodução** — Teste automatizado que reproduz o bug com os dados exatos do cenário original. Este teste DEVE falhar antes do fix e passar depois.
2. **Criar testes de regressão** — Para cada caminho de código afetado, validar que o comportamento correto é mantido. Focar em cenários que usam o mesmo código.
3. **Executar suite de testes existente** — Rodar testes unitários e de integração do componente. Se algum falhar por causa do fix, avaliar se é falha real ou teste desatualizado.
4. **Teste de smoke em staging** — Deploy do fix em staging e validar cenário principal manualmente antes de produção.
5. **Definir teste de validação pós-deploy** — Cenário que será executado em produção imediatamente após deploy para confirmar fix.

## Outputs

- Teste de reprodução do bug (automatizado)
- Testes de regressão para caminhos afetados
- Resultado da suite de testes existente (passando)
- Plano de smoke test em staging
- Plano de validação pós-deploy em produção

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Teste de reprodução | Teste que falha antes do fix e passa depois | Sim |
| Suite existente passa | Testes existentes do componente passando | Sim |
| Smoke test em staging | Cenário principal validado em staging | Sim |
| Validação pós-deploy definida | Cenário para validar em produção após deploy | Sim |

**Nota:** Em Sev1, se testes automatizados atrasariam deploy em mais de 1 hora, teste manual é aceitável com commit de automatizar em 48h.

**SLA:** Testes de Sev1 devem ser concluídos em **1 hora**.

## Próxima Fase

→ [07-readiness.md](./07-readiness.md) — Validação rápida de prontidão para deploy do fix
