# Checklist: Verificação de Donos e Accountability

## Propósito
Garantir que cada aspecto do projeto tem um dono claro com responsabilidade definida, evitando a situação onde "todo mundo é responsável" (logo ninguém é).

## Quando Usar
- Antes de iniciar a implementação
- Quando há confusão sobre "quem cuida do quê"
- Em transições de fase ou handoffs entre times

---

## Checklist

### Ownership Técnico
- [ ] Cada módulo/serviço tem um tech lead ou owner designado
- [ ] Dono de cada repositório de código está definido
- [ ] Responsável por cada integração com terceiro está identificado
- [ ] Dono de decisões de infraestrutura está definido
- [ ] Responsável por segurança da solução está identificado

### Ownership de Produto
- [ ] Product Owner ou equivalente está definido e disponível
- [ ] Responsável por decisões de escopo está identificado
- [ ] Dono dos critérios de aceite está definido (quem aprova)
- [ ] Responsável por priorização de backlog está claro
- [ ] Dono da comunicação com stakeholders está designado

### Ownership Operacional
- [ ] Responsável por monitoramento pós-deploy está definido
- [ ] Equipe de plantão/on-call está designada
- [ ] Dono do runbook operacional está identificado
- [ ] Responsável por resposta a incidentes está definido
- [ ] Dono da decisão de rollback está identificado

### Accountability por Entregável
- [ ] Cada artefato do projeto tem um responsável pela qualidade
- [ ] Cada dependência externa tem um responsável por follow-up
- [ ] Cada risco tem um owner para mitigação
- [ ] Cada decisão pendente tem um responsável por resolver
- [ ] Cada milestone tem um responsável por entregar

### Governança
- [ ] RACI (Responsible, Accountable, Consulted, Informed) está definido
- [ ] Processo de escalação quando owner não resolve está claro
- [ ] Substituição de owner em caso de ausência está definida
- [ ] Ownership é revisado quando escopo ou time muda
- [ ] Não há sobreposição de accountability (dois donos para a mesma coisa)

---

## Critérios de Aprovação
- **Mínimo**: Ownership Técnico e Accountability por Entregável completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Componentes críticos sem owner ou RACI não definido

## Sinais de Alerta (Red Flags)
- "O time é responsável" sem ninguém específico accountable
- Owner designado que não sabe que é owner
- Mesmo pessoa é owner de tudo (sobrecarga, SPOF humano)
- Nenhum owner para operação pós-deploy
- Ownership definido mas sem autoridade para tomar decisões

## Agente Responsável
**Agente de Final Review & Handoff** — responsável por garantir que ownership está claro e funcional.
