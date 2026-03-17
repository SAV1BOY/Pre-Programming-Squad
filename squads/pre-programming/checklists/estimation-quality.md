# Checklist: Qualidade da Estimativa

## Propósito
Garantir que estimativas de esforço são baseadas em breakdown detalhado, consideram riscos e dependências, e incluem buffers realistas.

## Quando Usar
- Ao estimar esforço de implementação
- Antes de comprometer prazos com stakeholders
- Em revisões de planejamento e timeline

---

## Checklist

### Breakdown
- [ ] O trabalho está quebrado em tarefas de no máximo 2-3 dias
- [ ] Cada tarefa tem escopo claro e deliverable definido
- [ ] Tarefas técnicas (infra, CI/CD, setup) estão incluídas
- [ ] Tarefas de teste estão incluídas na estimativa
- [ ] Tarefas de documentação e handoff estão incluídas

### Esforço
- [ ] Estimativa foi feita por quem vai executar (ou similar)
- [ ] Complexidade técnica foi considerada (não apenas volume)
- [ ] Curva de aprendizado de novas tecnologias está incluída
- [ ] Overhead de comunicação e reuniões está considerado
- [ ] Estimativas usam range (otimista, realista, pessimista) e não ponto único

### Risco
- [ ] Riscos técnicos que podem afetar a estimativa estão listados
- [ ] Incertezas foram identificadas e seu impacto na estimativa avaliado
- [ ] Tarefas com alta incerteza têm spike/PoC planejado antes da estimativa final
- [ ] Riscos de retrabalho estão considerados
- [ ] Histórico de estimativas anteriores similares foi consultado

### Dependências
- [ ] Dependências de outros times estão mapeadas com prazos
- [ ] Dependências de aprovações/decisões pendentes estão identificadas
- [ ] Dependências de infraestrutura/ambiente estão incluídas
- [ ] Caminho crítico está identificado
- [ ] Impacto de atrasos em dependências está avaliado

### Buffers
- [ ] Buffer para imprevistos está incluído (15-25% do total)
- [ ] Buffer para code review e correções está incluído
- [ ] Buffer para bugs encontrados durante testes está incluído
- [ ] Buffer é proporcional ao nível de incerteza do projeto
- [ ] Buffer não foi removido por pressão de stakeholders

---

## Critérios de Aprovação
- **Mínimo**: Breakdown e Esforço completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Estimativa sem breakdown ou como ponto único sem range

## Sinais de Alerta (Red Flags)
- Estimativa dada em minutos para projeto de semanas ("5 dias")
- Nenhum buffer incluído ("dá pra fazer no prazo certinho")
- Estimativa feita por quem não vai executar sem validação
- Todas as tarefas com mesmo esforço (falta de análise)
- Estimativa que não inclui testes, deploy ou documentação

## Agente Responsável
**Agente de Estimation & Planning** — responsável por coordenar e validar estimativas.
