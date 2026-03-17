# Refatoração de Legado — Fase 01: Intake

## Objetivo da Fase

Receber e validar a solicitação de refatoração de código legado, entendendo a motivação (dor atual), escopo aproximado e riscos inerentes de mexer em sistema legado.

## Agentes Envolvidos

- **Agente de Requisitos** (líder da fase) — Valida motivação e escopo inicial
- **Agente de Riscos** — Avaliação preliminar de risco por se tratar de sistema legado
- **Agente Coordenador** — Registra projeto e identifica quem tem contexto histórico

## Inputs

- Solicitação de refatoração com motivação (dívida técnica, performance, manutenibilidade)
- Métricas de dor atual (tempo de build, frequência de bugs, custo de manutenção)
- Idade e histórico do código-alvo
- Documentação existente (se houver — frequentemente não há)

## Atividades

1. **Validar motivação com dados** — "Código feio" não é motivo de refactoring. Exigir métricas: tempo gasto em manutenção, frequência de bugs, impacto em velocity.
2. **Identificar stakeholders do legado** — Quem escreveu originalmente? Quem mantém hoje? Quem são os consumidores internos e externos?
3. **Avaliar risco preliminar** — Código legado tem riscos únicos: dependências ocultas, lógica não documentada, testes ausentes, shadow IT.
4. **Verificar tentativas anteriores** — Já houve tentativas de refactoring? Por que falharam? Aprender com o histórico.
5. **Definir restrição de disponibilidade** — O sistema legado pode ter downtime? Qual a janela de manutenção?
6. **Classificar tipo de refactoring** — Renomear/reorganizar (baixo risco), extrair módulo (médio risco), reescrever (alto risco).

## Outputs

- Registro do projeto com motivação quantificada
- Mapa de stakeholders e conhecedores do legado
- Avaliação preliminar de risco
- Histórico de tentativas anteriores (se houver)
- Classificação do tipo de refactoring

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Motivação quantificada | Métricas de dor (custo, bugs, velocity) documentadas | Sim |
| Stakeholders mapeados | Conhecedores do código identificados e disponíveis | Sim |
| Risco preliminar | Classificação inicial de risco do legado | Sim |
| Histórico verificado | Tentativas anteriores documentadas | Sim |

## Próxima Fase

→ [02-discovery.md](./02-discovery.md) — Arqueologia do código legado e mapeamento de dependências
