# Checklist: Atualidade do Log de Decisões

## Propósito
Verificar se todas as decisões tomadas durante o pré-programming estão registradas, atuais e refletem o estado real do projeto.

## Quando Usar
- Antes de cada gate/revisão do projeto
- Ao preparar o pacote de handoff
- Quando há conflito sobre "o que foi decidido"

---

## Checklist

### Completude do Log
- [ ] Todas as decisões técnicas significativas estão registradas
- [ ] Todas as decisões de negócio/escopo estão registradas
- [ ] Decisões implícitas (tomadas sem discussão formal) foram tornadas explícitas
- [ ] Decisões que NÃO foram tomadas (adiadas) estão registradas como pendentes
- [ ] Decisões revertidas ou alteradas têm registro de mudança

### Conteúdo de Cada Decisão
- [ ] Contexto e motivação da decisão estão descritos
- [ ] Alternativas consideradas estão documentadas
- [ ] Justificativa da decisão está clara
- [ ] Data da decisão está registrada
- [ ] Decisor (quem decidiu) está identificado

### Atualidade
- [ ] Log reflete o estado atual (não uma versão antiga do projeto)
- [ ] Decisões superadas foram marcadas como obsoletas
- [ ] Decisões que dependem de contexto que mudou foram reavaliadas
- [ ] Última revisão do log tem data recente
- [ ] Decisões que conflitam entre si foram identificadas e resolvidas

### Rastreabilidade
- [ ] Cada decisão está vinculada aos artefatos que ela influencia
- [ ] Requisitos afetados por cada decisão estão identificados
- [ ] Decisões podem ser encontradas facilmente (indexação, busca)
- [ ] Cadeia de decisões relacionadas é navegável
- [ ] Impacto de reverter cada decisão está avaliado

### Acesso e Visibilidade
- [ ] Log está acessível a todos os membros do time
- [ ] Log está em formato e local padronizado
- [ ] Time sabe onde encontrar o log de decisões
- [ ] Novas decisões são adicionadas em tempo real (não acumuladas)
- [ ] Log é referenciado em discussões e reviews

---

## Critérios de Aprovação
- **Mínimo**: Completude e Atualidade completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Decisões críticas não registradas ou log desatualizado

## Sinais de Alerta (Red Flags)
- "Acho que decidimos X na reunião passada, mas não tenho certeza"
- Log de decisões criado de uma vez no final do projeto (retroativo)
- Decisões conflitantes no log sem resolução
- Ninguém do time sabe onde está o log de decisões
- Decisões tomadas verbalmente sem registro

## Agente Responsável
**Agente de Final Review & Handoff** — responsável por garantir que o log de decisões está completo e atual.
