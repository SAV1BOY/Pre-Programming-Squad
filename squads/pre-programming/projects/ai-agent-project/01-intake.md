# Projeto de Agente IA — Fase 01: Intake

## Objetivo da Fase

Receber e validar a solicitação de criação de agente de IA, entender o problema que o agente resolve, avaliar se IA é a abordagem correta e identificar requisitos de confiança e segurança.

## Agentes Envolvidos

- **Agente de Requisitos** (líder da fase) — Valida necessidade de IA vs. lógica determinística
- **Agente de Riscos** — Avaliação preliminar de riscos de IA (alucinação, bias, segurança)
- **Agente Coordenador** — Registra projeto e identifica especialistas de ML/IA

## Inputs

- Descrição do agente de IA pretendido e seu propósito
- Problema que o agente deve resolver
- Dados disponíveis para treinamento/prompt engineering
- Requisitos de confiança e precisão do stakeholder
- Restrições regulatórias (LGPD, sector-specific)

## Atividades

1. **Validar que IA é necessária** — IA resolve problemas de ambiguidade, linguagem natural e padrões complexos. Se o problema tem regras determinísticas, código tradicional é mais confiável e debugável.
2. **Definir tipo de agente** — Conversacional (chatbot), executivo (realiza ações), analítico (analisa dados), criativo (gera conteúdo). Cada tipo tem riscos diferentes.
3. **Estabelecer requisitos de confiança** — Qual a taxa de erro aceitável? 1%? 5%? 10%? Em quais cenários erro é inaceitável (financeiro, jurídico, saúde)?
4. **Identificar riscos de IA** — Alucinação, bias, jailbreak, vazamento de dados, respostas inadequadas, dependência de modelo externo.
5. **Avaliar disponibilidade de dados** — Há dados de treino/exemplos? Estão anotados? São representativos? Há viés nos dados?
6. **Verificar compliance** — LGPD, regulação setorial, política interna de IA. Dados de clientes serão enviados a APIs externas?

## Outputs

- Validação de que IA é a abordagem correta (com justificativa)
- Tipo de agente classificado
- Requisitos de confiança com threshold de erro aceitável
- Avaliação preliminar de riscos de IA
- Inventário de dados disponíveis
- Checklist de compliance

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| IA justificada | Problema requer IA (não resolvível com regras determinísticas) | Sim |
| Confiança definida | Taxa de erro aceitável explícita por cenário | Sim |
| Riscos de IA avaliados | Alucinação, bias, jailbreak considerados | Sim |
| Compliance verificado | LGPD e regulação setorial avaliados | Sim |

## Próxima Fase

→ [02-discovery.md](./02-discovery.md) — Exploração do domínio, dados e capacidades do modelo
