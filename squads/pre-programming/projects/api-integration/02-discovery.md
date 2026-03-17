# Integração de API — Fase 02: Discovery

## Objetivo da Fase

Explorar a API em profundidade, testar endpoints reais em sandbox, mapear modelo de dados e identificar gaps entre o que a API oferece e o que o sistema precisa.

## Agentes Envolvidos

- **Agente de Requisitos** (líder da fase) — Mapeia requisitos vs. capacidades da API
- **Agente de Arquitetura** — Analisa modelo de dados e compatibilidade técnica

## Inputs

- Documentação da API (Fase 01)
- Acesso a sandbox ou ambiente de testes
- Requisitos de negócio para a integração
- Modelo de dados interno do sistema

## Atividades

1. **Testar endpoints em sandbox** — Executar chamadas reais para cada endpoint relevante. Verificar se comportamento corresponde à documentação. Documentar discrepâncias.
2. **Mapear modelo de dados** — Comparar modelo de dados da API com modelo interno. Identificar: campos que precisam de transformação, campos ausentes, diferenças de tipo/formato.
3. **Identificar gaps funcionais** — O que o sistema precisa que a API não oferece? Existe workaround? É bloqueante?
4. **Testar cenários de erro** — Enviar requests inválidos, com campos faltando, com valores fora de range. Documentar comportamento de erro (códigos, mensagens, formato).
5. **Verificar paginação e filtros** — Para endpoints de listagem: como funciona paginação? Há filtros eficientes? Qual o tamanho máximo de página?
6. **Avaliar versionamento** — A API tem versionamento? Qual a política de deprecação? Há breaking changes planejadas?
7. **Testar autenticação** — Fluxo completo de autenticação: obtenção de token, refresh, expiração, revogação. Documentar TTL e comportamento em token expirado.

## Outputs

- Relatório de testes em sandbox com resultados reais
- Mapeamento de modelo de dados (API vs. interno) com transformações necessárias
- Lista de gaps funcionais com avaliação de impacto
- Catálogo de comportamentos de erro da API
- Documentação de paginação, filtros e limites
- Análise de versionamento e política de deprecação

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Sandbox testada | Endpoints críticos testados com resultados documentados | Sim |
| Modelo mapeado | Transformações entre modelos identificadas | Sim |
| Erros documentados | Comportamento de erro para cenários comuns capturado | Sim |
| Gaps identificados | Diferença entre necessidade e oferta mapeada | Sim |
| Autenticação testada | Fluxo completo de auth validado | Sim |

## Próxima Fase

→ [03-scope.md](./03-scope.md) — Definição dos endpoints a integrar e estratégia de comunicação
