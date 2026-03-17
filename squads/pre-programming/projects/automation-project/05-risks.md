# Projeto de Automação — Fase 05: Riscos

## Objetivo da Fase

Identificar riscos específicos de automação: falha silenciosa, amplificação de erros, perda de conhecimento do processo manual, e degradação gradual de qualidade.

## Agentes Envolvidos

- **Agente de Riscos** (líder da fase) — Identifica riscos de automação
- **Agente de Arquitetura** — Valida resiliência técnica

## Inputs

- Arquitetura de orquestração (Fase 04)
- Guardrails definidos (Fase 03)
- Catálogo de exceções (Fase 02)

## Atividades

1. **Avaliar risco de falha silenciosa** — A automação pode falhar sem que ninguém perceba? Cenários: job não executa, executa parcialmente, executa com dados errados sem erro técnico.
2. **Avaliar risco de amplificação de erros** — Automação processa alto volume. Um bug na lógica afeta todos os registros, não um. Qual o blast radius de uma regra errada?
3. **Avaliar risco de perda de conhecimento** — Quando o processo é automatizado, as pessoas esquecem como fazer manualmente. Se a automação falhar em 6 meses, alguém sabe operar?
4. **Avaliar risco de dados inconsistentes** — Automação que processa dados de múltiplas fontes pode encontrar inconsistências. Como trata? Ignora silenciosamente?
5. **Avaliar risco de mudança de regras** — Regras de negócio mudam. Quem atualiza a automação? Há processo para manter regras atualizadas?
6. **Definir circuit breakers da automação** — Condições que PARAM a automação automaticamente: taxa de erro > X%, volume anômalo, resultado fora do range esperado.

## Outputs

- Matriz de riscos de automação
- Plano de detecção de falha silenciosa
- Análise de blast radius por tipo de erro
- Plano de preservação de conhecimento manual
- Circuit breakers da automação definidos
- Processo de atualização de regras de negócio

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Falha silenciosa mitigada | Monitoramento detecta não-execução e execução parcial | Sim |
| Blast radius estimado | Impacto de bug na lógica quantificado | Sim |
| Circuit breakers | Automação para automaticamente em condições anômalas | Sim |
| Conhecimento preservado | Processo manual documentado e acessível | Sim |

## Próxima Fase

→ [06-tests.md](./06-tests.md) — Testes focados em validação de regras e resiliência
