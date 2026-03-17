# Ferramenta Interna — Fase 01: Intake

## Objetivo da Fase

Receber e validar a solicitação de ferramenta interna, identificar os usuários-alvo (operações, suporte, engenharia), entender o problema operacional e avaliar se build é necessário ou se ferramentas existentes resolvem.

## Agentes Envolvidos

- **Agente de Requisitos** (líder da fase) — Valida necessidade e alternativas existentes
- **Agente Coordenador** — Registra projeto e avalia prioridade

## Inputs

- Solicitação da ferramenta com problema operacional descrito
- Volume do problema (quantas vezes por dia/semana a operação manual é feita)
- Quem são os usuários-alvo internos
- Ferramentas existentes que cobrem parcialmente a necessidade

## Atividades

1. **Quantificar o problema operacional** — Quantas horas/semana são gastas no processo manual? Qual o custo de erro humano? Qual a frequência?
2. **Avaliar ferramentas existentes** — Antes de construir, verificar: ferramentas internas existentes, extensões de ferramentas de mercado, scripts existentes, spreadsheets com macros.
3. **Identificar usuários-alvo** — Perfil técnico dos usuários: são devs? operadores? suporte? Isso influencia nível de UX necessário.
4. **Definir expectativa de vida útil** — É ferramenta permanente ou temporária? Isso influencia investimento em qualidade e UX.
5. **Avaliar urgência** — A operação manual é sustentável por mais 2-4 semanas enquanto a ferramenta é desenvolvida?
6. **Verificar dados sensíveis** — A ferramenta terá acesso a dados de clientes, financeiros ou PII? Isso define requisitos de segurança.

## Outputs

- Registro do projeto com problema quantificado (horas economizadas)
- Avaliação de alternativas existentes (build vs. extend vs. buy)
- Perfil dos usuários-alvo
- Decisão de vida útil (permanente vs. temporária)
- Requisitos de segurança (acesso a dados sensíveis)

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Problema quantificado | Horas economizadas ou erros prevenidos estimados | Sim |
| Alternativas avaliadas | Verificação de ferramentas existentes feita | Sim |
| Usuários identificados | Perfil e quantidade de usuários-alvo definidos | Sim |
| Segurança avaliada | Acesso a dados sensíveis classificado | Sim |

## Próxima Fase

→ [02-discovery.md](./02-discovery.md) — Entendimento do workflow operacional atual
