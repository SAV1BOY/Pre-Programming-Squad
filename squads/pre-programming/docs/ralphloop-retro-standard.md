# Standard para Retrospectiva RalphLoop

## Propósito

Definir o processo de retrospectiva contínua do Pre-Programming Squad, denominado RalphLoop. O objetivo é aprender sistematicamente com cada ciclo de trabalho, melhorar o processo de forma incremental e garantir que erros não se repitam. O nome "RalphLoop" reflete o compromisso com feedback loops rápidos e melhoria contínua.

## Escopo

Aplica-se a cada ciclo de trabalho do squad (2 semanas) e, adicionalmente, ao fechamento de projetos individuais de tamanho G ou XG.

## Definições

| Termo | Definição |
|---|---|
| RalphLoop | Ciclo de retrospectiva e melhoria contínua do Pre-Programming Squad |
| Ação de melhoria | Mudança concreta no processo derivada de aprendizado da retrospectiva |
| Indicador de saúde | Métrica que sinaliza se o processo do squad está saudável ou degradando |
| Feedback do receptor | Dados qualitativos e quantitativos do squad que recebeu o handoff |

## Processo

### 1. Coleta de Dados (Antes da Sessão)

**Métricas operacionais do ciclo:**
- Lead time médio (intake → handoff) por tamanho de projeto
- Throughput (projetos concluídos)
- WIP médio
- Taxa de handoffs aceitos vs. rejeitados
- Número de perguntas de esclarecimento pós-handoff

**Feedback de receptores:**
- Scores de satisfação dos handoffs do ciclo
- Comentários qualitativos
- Itens que faltaram ou sobraram

**Eventos notáveis:**
- Bloqueios e como foram resolvidos
- Exceções ao processo e por quê
- Surpresas positivas ou negativas

### 2. Sessão de Retrospectiva (60 minutos)

**Participantes:** Squad completo (obrigatório)

**Estrutura:**

**Parte 1 — Dados (10 min)**
Apresentar métricas e feedback sem interpretação. Deixar os números falarem.

**Parte 2 — O que Funcionou (10 min)**
- Quais práticas do processo geraram bons resultados?
- O que devemos continuar fazendo?
- Reconhecer contribuições específicas

**Parte 3 — O que Não Funcionou (15 min)**
- Onde o processo falhou ou foi ineficiente?
- Quais foram os bloqueios mais custosos?
- Onde o feedback dos receptores indicou problema?

**Parte 4 — Análise de Causa Raiz (10 min)**
Para os 2-3 problemas mais significativos, aplicar "5 Porquês":
1. O que aconteceu?
2. Por que aconteceu?
3. Por que essa causa existia?
4. O que permitiu essa causa?
5. Qual a causa sistêmica?

**Parte 5 — Ações de Melhoria (15 min)**
Para cada causa raiz identificada:
- Definir ação concreta e específica
- Atribuir owner
- Definir prazo
- Definir como medir se a ação funcionou

**Regras:**
- Máximo de 3 ações de melhoria por ciclo (foco > volume)
- Ações devem ser específicas e mensuráveis (não "melhorar comunicação", mas "incluir checklist de validação de contratos de API no template de handoff")
- Ações do ciclo anterior são revisadas primeiro — foram implementadas? Funcionaram?

### 3. Registro

Cada retrospectiva é registrada em formato padronizado:

```
## RalphLoop — Ciclo [N] ([datas])

### Métricas do Ciclo
| Métrica | Valor | Meta | Tendência |
|---|---|---|---|
| Lead time médio (M) | X dias | ≤ Y dias | ↗/→/↘ |
| Throughput | N projetos | ≥ M projetos | ↗/→/↘ |
| Satisfação receptor | X/10 | ≥ 8/10 | ↗/→/↘ |

### O que Funcionou
- [Item 1]
- [Item 2]

### O que Não Funcionou
- [Problema 1] — Causa raiz: [análise]
- [Problema 2] — Causa raiz: [análise]

### Ações do Ciclo Anterior
| Ação | Status | Resultado |
|---|---|---|
| [Ação 1] | ✅ Implementada | [Efeito observado] |
| [Ação 2] | 🔶 Parcial | [O que falta] |

### Ações para Próximo Ciclo
| Ação | Owner | Prazo | Métrica de Sucesso |
|---|---|---|---|
| [Ação concreta 1] | @fulano | [data] | [como medir] |
| [Ação concreta 2] | @ciclana | [data] | [como medir] |
```

### 4. Retrospectiva de Projeto (para G/XG)

Ao concluir handoff de projetos grandes, sessão adicional de 45 min:

- O que aprendemos sobre este tipo de projeto?
- As estimativas estavam calibradas? Se não, por quê?
- Quais armadilhas encontramos que devemos documentar para futuros projetos similares?
- O processo padrão foi adequado ou precisou de adaptação?
- Se adaptamos, a adaptação deve virar padrão?

### 5. Revisão Trimestral

A cada 6 ciclos, revisão macro:
- Tendências das métricas ao longo dos ciclos
- Ações de melhoria que mais impactaram
- Padrões recorrentes nos problemas
- Atualização de standards e templates baseada nos aprendizados
- Compartilhamento de aprendizados com a organização

## Critérios de Qualidade

- 100% dos ciclos têm retrospectiva realizada e registrada
- Máximo 3 ações de melhoria por ciclo (foco)
- ≥ 70% das ações implementadas no prazo
- Ações do ciclo anterior revisadas antes de criar novas
- Métricas apresentadas com tendência (melhora/estabilidade/piora)
- Projetos G/XG têm retrospectiva dedicada
- Revisão trimestral realizada e documentada

## Responsáveis

| Papel | Responsabilidade |
|---|---|
| Tech Lead | Facilitar sessão, garantir que ações sejam acompanhadas |
| Todos os membros | Participar ativamente, sugerir melhorias, implementar ações atribuídas |
| EM | Participar quando convidado, remover bloqueios para ações de melhoria |

## Referências

- Modelo Operacional: `docs/operating-model.md`
- Carta do Squad: `docs/squad-charter.md`
- What Good Looks Like: `docs/what-good-looks-like.md`
