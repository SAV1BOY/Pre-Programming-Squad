# Bugfix Crítico — Fase 03: Escopo

## Objetivo da Fase

Definir o escopo mínimo necessário para corrigir o bug sem introduzir novos problemas. Em bugfix crítico, escopo mínimo é regra absoluta.

## Agentes Envolvidos

- **Agente de Escopo** (líder da fase) — Define fronteiras do fix
- **Agente de Riscos** — Valida que o escopo não amplia blast radius

## Inputs

- Causa raiz documentada (Fase 02)
- Lista de caminhos afetados
- Avaliação de dados corrompidos
- Comportamento esperado definido

## Atividades

1. **Definir fix mínimo** — Qual é a menor mudança que corrige a causa raiz? Resistir à tentação de refatorar ou melhorar código adjacente.
2. **Separar fix de melhoria** — Se durante a investigação foram identificadas melhorias, registrá-las como tickets separados. Não incluir no fix.
3. **Avaliar fix temporário vs. definitivo** — Se fix definitivo é complexo, considerar fix temporário (hotfix) seguido de fix definitivo em sprint normal.
4. **Definir correção de dados** — Se há dados corrompidos, definir script de correção com dry-run e validação. Separar do fix de código.
5. **Listar o que NÃO mudar** — Explicitamente documentar áreas do código que não devem ser tocadas neste fix, mesmo que pareçam relacionadas.

## Outputs

- Definição do fix mínimo com mudanças específicas de código
- Lista de melhorias identificadas (tickets separados)
- Decisão: fix temporário ou definitivo (com justificativa)
- Script de correção de dados (se necessário) com plano de dry-run
- Lista de áreas que NÃO serão alteradas

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Escopo mínimo | Fix não inclui refactoring ou melhorias | Sim |
| Fix isolado | Mudanças limitadas ao ponto de falha e caminhos afetados | Sim |
| Dados separados | Correção de dados é operação separada do fix de código | Sim |
| Melhorias backlogged | Melhorias identificadas registradas como tickets separados | Sim |

**SLA:** Definição de escopo de Sev1 deve ser concluída em **1 hora**.

## Próxima Fase

→ [04-architecture.md](./04-architecture.md) — Avaliação de impacto técnico do fix
