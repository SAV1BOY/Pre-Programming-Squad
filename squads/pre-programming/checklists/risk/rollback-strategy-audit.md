# Checklist: Auditoria de Estratégia de Rollback

## Propósito
Garantir que a estratégia de reversão é realista, testada e executável sob pressão, não apenas um plano teórico que ninguém sabe executar.

## Quando Usar
- Antes de qualquer deploy ou mudança em produção
- Ao planejar migrações de dados
- Quando a mudança é difícil de reverter

---

## Checklist

### Rollback de Aplicação
- [ ] Versão anterior da aplicação pode ser redeployada rapidamente
- [ ] Processo de rollback de deploy está documentado passo a passo
- [ ] Rollback pode ser executado por qualquer membro do time (não só uma pessoa)
- [ ] Tempo de rollback está estimado e é aceitável
- [ ] Rollback de deploy foi testado em ambiente não-produtivo

### Rollback de Dados
- [ ] Migrações de banco de dados são reversíveis (têm rollback/down)
- [ ] Dados criados durante o período de mudança são tratados no rollback
- [ ] Integridade referencial é mantida no rollback
- [ ] Rollback de dados foi testado com volume representativo
- [ ] Backup point-in-time está disponível como último recurso

### Rollback de Configuração
- [ ] Mudanças de configuração podem ser revertidas independentemente do código
- [ ] Feature flags podem ser desligadas rapidamente
- [ ] Mudanças de infraestrutura (DNS, load balancer) podem ser revertidas
- [ ] Mudanças de permissão/acesso podem ser revertidas
- [ ] Configurações estão versionadas com histórico

### Critérios de Acionamento
- [ ] Métricas que indicam necessidade de rollback estão definidas
- [ ] Thresholds específicos para acionar rollback estão quantificados
- [ ] Tempo máximo de espera antes de decidir rollback está definido
- [ ] Quem tem autoridade para decidir o rollback está identificado
- [ ] Processo de decisão é rápido (não requer reunião/aprovação em cadeia)

### Pós-Rollback
- [ ] Comunicação pós-rollback está planejada (o que dizer, para quem)
- [ ] Processo de análise de causa raiz pós-rollback está definido
- [ ] Dados gerados entre deploy e rollback são reconciliáveis
- [ ] Plano para segundo attempt após rollback está definido
- [ ] Aprendizados são capturados para evitar repetição

---

## Critérios de Aprovação
- **Mínimo**: Rollback de Aplicação e Critérios de Acionamento completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Sem estratégia de rollback ou rollback não testado para mudança crítica

## Sinais de Alerta (Red Flags)
- "Se der errado, a gente refaz o deploy" (sem considerar dados)
- Rollback que só uma pessoa sabe fazer (e se estiver de férias?)
- Migração de banco irreversível sem backup
- Nenhum critério para decidir quando fazer rollback
- Rollback que demora mais que a janela de manutenção

## Agente Responsável
**Agente de Risk & Failure Analysis** — responsável por garantir rollback realista e testado.
