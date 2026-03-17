# Bugfix Crítico — Fase 04: Arquitetura

## Objetivo da Fase

Avaliar o impacto técnico do fix proposto no sistema existente. Em bugfix crítico, não se redesenha arquitetura — se avalia se o fix é seguro para deploy rápido.

## Agentes Envolvidos

- **Agente de Arquitetura** (líder da fase) — Avalia impacto técnico e segurança do fix
- **Agente de Riscos** — Valida que fix não cria novos pontos de falha

## Inputs

- Definição do fix mínimo (Fase 03)
- Código-fonte afetado
- Mapa de dependências do componente
- Histórico de incidentes no mesmo componente

## Atividades

1. **Analisar impacto do fix** — A mudança proposta afeta outros consumidores do componente? Há efeitos colaterais em chamadores upstream ou downstream?
2. **Verificar backward compatibility** — O fix altera contratos (APIs, schemas, formatos de mensagem)? Se sim, é backward compatible?
3. **Avaliar concorrência** — O fix introduz ou resolve race conditions? Verificar se a correção é thread-safe.
4. **Verificar estados intermediários** — Durante o deploy do fix, há estado inconsistente? Exemplo: banco migrado mas código antigo, ou código novo com cache antigo.
5. **Confirmar que fix não precisa de migração** — Se o fix requer mudança de schema ou dados, isso muda drasticamente o plano de deploy.

## Outputs

- Análise de impacto do fix em componentes adjacentes
- Confirmação de backward compatibility
- Avaliação de thread-safety
- Identificação de estados intermediários durante deploy
- Confirmação de que fix é deployável independentemente (ou não)

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Impacto avaliado | Efeitos colaterais em componentes adjacentes mapeados | Sim |
| Backward compatible | Fix não quebra consumidores existentes | Sim |
| Deploy independente | Fix pode ser deployado sem coordenação com outros serviços (ou plano de coordenação definido) | Sim |
| Sem migração bloqueante | Fix não requer migração de schema para funcionar | Desejável |

**SLA:** Avaliação de arquitetura de Sev1 deve ser concluída em **1 hora**.

## Próxima Fase

→ [05-risks.md](./05-risks.md) — Riscos específicos do fix e plano de rollback
