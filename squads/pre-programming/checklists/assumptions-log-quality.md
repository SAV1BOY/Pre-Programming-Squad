# Checklist: Qualidade do Log de Suposições

## Propósito
Garantir que todas as suposições feitas durante o pré-programming estão registradas, com validações pendentes identificadas, owners designados e plano de revisão.

## Quando Usar
- Continuamente durante todo o processo de pré-programming
- Antes de cada gate/review, para verificar suposições pendentes
- Quando uma decisão é baseada em algo não confirmado

---

## Checklist

### Registro de Suposições
- [ ] Cada suposição tem descrição clara e objetiva
- [ ] Cada suposição tem justificativa (por que foi assumida)
- [ ] O impacto caso a suposição se prove falsa está documentado
- [ ] Suposições estão categorizadas (negócio, técnica, organizacional)
- [ ] Suposições críticas estão diferenciadas das de baixo impacto

### Validações Pendentes
- [ ] Cada suposição não validada tem método de validação definido
- [ ] Fonte de validação está identificada (quem pode confirmar/negar)
- [ ] Prazo para validação está definido
- [ ] Ações contingenciais estão definidas caso suposição se prove falsa
- [ ] Status de validação está atualizado (pendente, validada, invalidada)

### Owners
- [ ] Cada suposição tem um owner responsável por validá-la
- [ ] O owner tem capacidade e acesso para realizar a validação
- [ ] Existe follow-up regular sobre suposições pendentes
- [ ] Escalação está definida para suposições que não foram validadas no prazo
- [ ] Owner de suposições críticas é alguém sênior

### Revisão
- [ ] Log de suposições é revisado em cada fase/gate do projeto
- [ ] Suposições invalidadas geraram ações de ajuste
- [ ] Novas suposições foram adicionadas quando identificadas
- [ ] Suposições validadas foram atualizadas como fatos confirmados
- [ ] Decisões impactadas por suposições invalidadas foram revisitadas

### Rastreabilidade
- [ ] Cada suposição está vinculada à decisão que ela influencia
- [ ] Suposições são rastreáveis aos artefatos que dependem delas
- [ ] Histórico de mudanças de status está registrado
- [ ] Suposições transferidas para o time de implementação estão marcadas
- [ ] Log está acessível a todos os envolvidos

---

## Critérios de Aprovação
- **Mínimo**: Registro e Validações Pendentes completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Suposições críticas sem owner ou sem plano de validação

## Sinais de Alerta (Red Flags)
- Nenhuma suposição registrada (overconfidence ou falta de análise)
- Suposições críticas sem plano de validação há mais de uma semana
- Suposições invalidadas que não geraram mudança em decisões
- Owner de todas as suposições é a mesma pessoa
- Log nunca revisado durante o projeto

## Agente Responsável
**Agente de Discovery & Framing** — responsável por manter o log de suposições atualizado ao longo do processo.
