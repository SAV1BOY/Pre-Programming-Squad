# Bugfix Crítico — Fase 02: Discovery

## Objetivo da Fase

Investigar e isolar a causa raiz do bug crítico, distinguindo entre sintoma e problema real, e mapear todos os caminhos de código afetados.

## Agentes Envolvidos

- **Agente de Requisitos** (líder da fase) — Reconstrói o comportamento esperado vs. real
- **Agente de Riscos** — Avalia se a causa raiz afeta outros componentes

## Inputs

- Classificação de severidade e blast radius (Fase 01)
- Evidências coletadas (logs, stack traces, métricas)
- Código-fonte do componente afetado
- Histórico recente de deploys e mudanças

## Atividades

1. **Reproduzir o bug** — Definir passos exatos para reprodução. Se não reproduzível deterministicamente, identificar condições que aumentam probabilidade.
2. **Isolar causa raiz** — Usar técnica de bisect: qual foi o último deploy bom? Quais mudanças entraram entre o último bom e o bug? Correlacionar com timeline.
3. **Mapear caminhos afetados** — Identificar todos os fluxos de código que passam pelo ponto de falha. O bug pode afetar mais cenários do que o reportado.
4. **Verificar se é regressão** — O comportamento correto existia antes? Se sim, o que mudou? Se não, é bug latente exposto por nova condição.
5. **Avaliar dados corrompidos** — O bug causou dados inconsistentes? Há registros que precisam ser corrigidos além do fix de código?
6. **Documentar comportamento esperado** — Definir claramente o que DEVERIA acontecer, baseado em requisitos ou comportamento anterior.

## Outputs

- Causa raiz identificada e documentada
- Passos de reprodução detalhados
- Lista de todos os caminhos de código afetados
- Avaliação de dados corrompidos (se aplicável)
- Definição do comportamento esperado

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Causa raiz isolada | Ponto exato de falha identificado no código | Sim |
| Reprodutível | Bug pode ser reproduzido em ambiente de teste | Sim |
| Caminhos mapeados | Todos os fluxos afetados identificados (não apenas o reportado) | Sim |
| Dados avaliados | Impacto em dados persistidos verificado | Sim |

**SLA:** Discovery de Sev1 deve ser concluída em **2 horas**.

## Próxima Fase

→ [03-scope.md](./03-scope.md) — Definição do escopo mínimo do fix
