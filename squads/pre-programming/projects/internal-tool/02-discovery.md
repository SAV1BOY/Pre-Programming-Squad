# Ferramenta Interna — Fase 02: Discovery

## Objetivo da Fase

Observar e documentar o workflow operacional atual, entender os pain points reais dos usuários internos e mapear os dados e sistemas envolvidos.

## Agentes Envolvidos

- **Agente de Requisitos** (líder da fase) — Mapeia workflow e pain points
- **Agente de Arquitetura** — Identifica sistemas e dados envolvidos

## Inputs

- Solicitação validada (Fase 01)
- Acesso aos usuários-alvo para observação
- Documentação de processos existentes (se houver)
- Ferramentas e sistemas atualmente usados no workflow

## Atividades

1. **Observar o workflow atual** — Sentar com usuário e observar o processo manual completo. Cronometrar cada etapa. Identificar pontos de decisão e exceções.
2. **Documentar step-by-step** — Cada passo do workflow com: input, ação, output, decisão. Incluir caminhos de exceção e tratamento de erros manuais.
3. **Identificar pain points** — Quais etapas são mais demoradas? Quais geram mais erros? Quais são mais frustrantes para o usuário?
4. **Mapear dados e sistemas** — De onde vêm os dados? Para onde vão? Quais sistemas são acessados? Quais transformações manuais são feitas?
5. **Identificar regras de negócio** — Regras que o operador aplica mentalmente e que a ferramenta precisará automatizar. Documentar lógica de decisão.
6. **Coletar frequência e volume** — Quantas vezes o workflow é executado? Volume de dados? Picos? Variações sazonais?

## Outputs

- Documentação do workflow step-by-step com tempos
- Mapa de pain points priorizados
- Inventário de dados e sistemas envolvidos
- Regras de negócio extraídas do processo manual
- Métricas de frequência e volume

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Workflow observado | Processo real observado (não apenas descrito) | Sim |
| Pain points mapeados | Pontos de dor priorizados por impacto | Sim |
| Dados mapeados | Fontes e destinos de dados identificados | Sim |
| Regras extraídas | Lógica de decisão do operador documentada | Sim |

## Próxima Fase

→ [03-scope.md](./03-scope.md) — Definição do que a ferramenta automatiza e o que permanece manual
