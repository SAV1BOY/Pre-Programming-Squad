# Refatoração de Legado — Fase 08: Handoff

## Objetivo da Fase

Entregar o plano de refatoração ao time com ênfase em: mapa de dependências, testes de caracterização, plano de transição faseado e contato do conhecedor do legado.

## Agentes Envolvidos

- **Agente Coordenador** (líder da fase) — Organiza entrega
- **Agente de Readiness** — Apresenta scorecard e riscos principais
- **Agente de Testes** — Demonstra suite de testes de caracterização

## Inputs

- Scorecard de readiness aprovado (Fase 07)
- Todos os artefatos das fases 01-06
- Contato do conhecedor do legado

## Atividades

1. **Organizar pacote de handoff** — Estrutura navegável com prioridade em: mapa de dependências, testes de caracterização, plano de transição.
2. **Sessão de walkthrough do legado** — Apresentação com foco em: armadilhas conhecidas, Chesterton's Fences, lógica de negócio oculta. Idealmente com participação do conhecedor.
3. **Demonstrar testes de caracterização** — Rodar testes ao vivo para que o time veja os golden tests em ação e entenda como usá-los durante o refactoring.
4. **Revisar plano de fases** — Walkthrough do plano incremental com rollback por fase. Confirmar que o time entende a ordem e os gates.
5. **Definir checkpoints** — Pontos de verificação durante o refactoring onde o Pre-Programming Squad revisa progresso e ajusta plano.
6. **Estabelecer canal de suporte estendido** — Para legado, suporte pós-handoff é de 4 semanas (vs. 2 semanas de feature nova).

## Outputs

- Pacote de handoff com prioridade em mapa de dependências e testes
- Ata de sessão com participação do conhecedor
- Suite de testes de caracterização entregue e demonstrada
- Plano de checkpoints durante refactoring
- Canal de suporte estendido (4 semanas)

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Pacote entregue | Mapa de dependências, testes e plano de transição incluídos | Sim |
| Conhecedor participou | Sessão de walkthrough com pessoa de contexto histórico | Sim |
| Testes demonstrados | Time viu testes de caracterização rodando | Sim |
| Checkpoints definidos | Datas de revisão durante refactoring acordadas | Sim |
| Suporte estendido | Canal e período de 4 semanas definidos | Sim |

## Próxima Fase

→ Refatoração pelo time de desenvolvimento com checkpoints periódicos do Pre-Programming Squad.

**Nota:** O Pre-Programming Squad participa ativamente dos checkpoints (a cada 1-2 semanas) para validar que o refactoring está dentro do escopo e que testes de equivalência estão sendo mantidos.
