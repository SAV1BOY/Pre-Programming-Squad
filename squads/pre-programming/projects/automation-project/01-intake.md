# Projeto de Automação — Fase 01: Intake

## Objetivo da Fase

Receber e validar a solicitação de automação de processo, quantificar o ROI esperado, identificar o processo candidato e avaliar se a automação é viável e desejável.

## Agentes Envolvidos

- **Agente de Requisitos** (líder da fase) — Valida viabilidade e ROI da automação
- **Agente Coordenador** — Registra projeto e mapeia stakeholders do processo

## Inputs

- Descrição do processo a ser automatizado
- Métricas atuais do processo (tempo, custo, taxa de erro, volume)
- Stakeholders do processo (donos, executores, consumidores)
- Restrições (regulatórias, contratuais, técnicas)

## Atividades

1. **Quantificar ROI** — Calcular: (custo atual do processo manual x frequência) vs. (custo de desenvolvimento + manutenção da automação). ROI positivo em quanto tempo?
2. **Avaliar candidato à automação** — Processos ideais para automação: repetitivos, baseados em regras, alto volume, propensos a erro humano. Processos ruins: exceções frequentes, julgamento humano necessário.
3. **Identificar gatilhos e frequência** — A automação é disparada por evento, por schedule, ou por demanda? Qual a frequência esperada?
4. **Mapear sistemas envolvidos** — Quais sistemas participam do processo? APIs disponíveis? Necessidade de scraping ou automação de UI?
5. **Avaliar risco de automação** — O que acontece se a automação falhar silenciosamente? Há risco de dano (financeiro, dados, reputação)?
6. **Verificar requisitos regulatórios** — A automação precisa de aprovação humana em alguma etapa? Há requisitos de auditoria?

## Outputs

- Cálculo de ROI com premissas explícitas
- Avaliação de viabilidade do candidato à automação
- Frequência e gatilhos mapeados
- Inventário de sistemas e APIs envolvidos
- Avaliação preliminar de risco
- Requisitos regulatórios identificados

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| ROI positivo | Payback em menos de 6 meses | Sim |
| Candidato viável | Processo é repetitivo e baseado em regras | Sim |
| Sistemas mapeados | APIs e acessos necessários identificados | Sim |
| Risco avaliado | Impacto de falha silenciosa quantificado | Sim |

## Próxima Fase

→ [02-discovery.md](./02-discovery.md) — Mapeamento detalhado do processo e regras de negócio
