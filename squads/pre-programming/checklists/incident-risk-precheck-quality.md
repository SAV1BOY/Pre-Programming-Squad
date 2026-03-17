# Checklist: Qualidade do Precheck de Risco de Incidente

## Propósito
Avaliar o risco operacional antes de qualquer mudança que toque produção, garantindo que impacto, detecção e resposta estão preparados.

## Quando Usar
- Antes de qualquer deploy ou mudança em produção
- Ao planejar migrações de dados em produção
- Quando a mudança pode afetar sistemas em operação

---

## Checklist

### Avaliação de Impacto
- [ ] Sistemas que podem ser afetados pela mudança estão listados
- [ ] Número de usuários potencialmente impactados está estimado
- [ ] Impacto financeiro de uma falha está estimado (receita por hora de downtime)
- [ ] Janela de mudança está definida (horário de menor impacto)
- [ ] Duração estimada da mudança está calculada

### Detecção
- [ ] Métricas que indicam problema estão identificadas
- [ ] Alertas específicos para a mudança estão configurados
- [ ] Dashboard de monitoramento durante a mudança está preparado
- [ ] Smoke tests pós-mudança estão definidos
- [ ] Tempo esperado para detectar um problema está estimado

### Resposta
- [ ] Runbook de resposta a incidente durante a mudança existe
- [ ] Equipe de plantão durante a mudança está escalada
- [ ] Canais de comunicação durante a mudança estão definidos
- [ ] Critérios de escalação estão claros (quando escalar, para quem)
- [ ] Comunicação para stakeholders em caso de incidente está preparada

### Rollback
- [ ] Procedimento de rollback está documentado passo a passo
- [ ] Rollback foi testado em ambiente não-produtivo
- [ ] Tempo de rollback está estimado
- [ ] Critérios para decidir fazer rollback estão definidos
- [ ] Dados criados durante a mudança são tratados no rollback

### Pré-condições
- [ ] Mudanças dependentes (infra, config) já foram aplicadas
- [ ] Backups recentes estão confirmados
- [ ] Capacidade do sistema suporta a mudança (não está no limite)
- [ ] Nenhuma outra mudança significativa está planejada para o mesmo período
- [ ] Aprovações necessárias (change management) foram obtidas

---

## Critérios de Aprovação
- **Mínimo**: Avaliação de Impacto, Rollback e Pré-condições completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Sem rollback documentado ou sem backup confirmado

## Sinais de Alerta (Red Flags)
- Deploy na sexta-feira à tarde sem equipe de plantão
- "É uma mudança pequena, não precisa de tudo isso"
- Rollback que demora mais que a janela de manutenção
- Nenhum monitoramento específico para a mudança
- Múltiplas mudanças grandes simultâneas

## Agente Responsável
**Agente de Risk & Failure Analysis** — responsável por avaliar riscos operacionais antes de tocar produção.
