# Refatoração de Legado — Fase 02: Discovery

## Objetivo da Fase

Realizar arqueologia do código legado: mapear dependências ocultas, entender lógica de negócio não documentada e identificar as fronteiras reais do sistema.

## Agentes Envolvidos

- **Agente de Requisitos** (líder da fase) — Reconstrói requisitos implícitos no código
- **Agente de Arquitetura** — Mapeia dependências e fronteiras do sistema
- **Agente de Riscos** — Identifica armadilhas específicas de legado

## Inputs

- Código-fonte do sistema legado
- Documentação existente (mesmo desatualizada)
- Acesso a pessoas com conhecimento histórico
- Logs de produção e métricas de uso

## Atividades

1. **Mapear dependências em todas as camadas** — Código, banco de dados (triggers, views, stored procedures, database links), ETL, scripts cron, integrações externas, planilhas com queries diretas.
2. **Identificar lógica de negócio no código** — Regras de negócio hardcoded, magic numbers, comentários com contexto histórico, workarounds com motivo perdido.
3. **Criar testes de caracterização** — Testes que documentam o comportamento ATUAL do sistema (não o desejado). Executar código e capturar outputs reais para criar golden tests.
4. **Mapear pontos de acoplamento** — Onde o código legado é chamado por outros sistemas? Quais interfaces são públicas (mesmo que não intencionalmente)?
5. **Analisar dados em produção** — Quais caminhos de código são realmente executados? Há código morto? Dados em formatos inesperados que o código trata silenciosamente?
6. **Entrevistar conhecedores** — Sessões com pessoas que trabalharam no código para capturar decisões que não foram documentadas. Gravar ou transcrever.
7. **Identificar shadow IT** — Planilhas, scripts Python, queries diretas ao banco que dependem do schema atual.

## Outputs

- Mapa de dependências multi-camada (código, banco, ETL, integrações, shadow IT)
- Inventário de lógica de negócio encontrada no código
- Suite de testes de caracterização (golden tests)
- Lista de pontos de acoplamento e interfaces públicas
- Análise de uso real em produção (caminhos ativos vs. código morto)
- Transcrição de entrevistas com conhecedores

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Dependências mapeadas | Todas as camadas verificadas (não só código) | Sim |
| Testes de caracterização | Suite que captura comportamento atual para áreas-chave | Sim |
| Interfaces identificadas | Pontos de acoplamento com outros sistemas documentados | Sim |
| Conhecedores consultados | Pelo menos 2 pessoas com histórico entrevistadas | Sim |
| Shadow IT verificado | Consulta a times de negócio sobre acessos diretos | Sim |

## Próxima Fase

→ [03-scope.md](./03-scope.md) — Definição de fronteiras do refactoring e estratégia de isolamento
