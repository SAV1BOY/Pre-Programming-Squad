# Checklist: Verificação de Risco de Migração

## Propósito
Avaliar riscos específicos de migrações de dados, sistema ou plataforma, garantindo compatibilidade e reversibilidade durante todo o processo.

## Quando Usar
- Antes de qualquer migração de dados significativa
- Ao planejar migração de sistema legado para novo
- Quando há mudança de plataforma, banco ou infraestrutura

---

## Checklist

### Planejamento da Migração
- [ ] Escopo da migração está claramente definido (o que migra, o que não migra)
- [ ] Estratégia está escolhida (big bang, gradual, dual-write, strangler fig)
- [ ] Cronograma com fases e gates está definido
- [ ] Equipe responsável pela migração está alocada
- [ ] Janela de migração está acordada com stakeholders

### Mapeamento de Dados
- [ ] Schema de origem e destino estão documentados
- [ ] Regras de transformação de dados estão definidas (mapeamento campo a campo)
- [ ] Dados que não têm equivalente no destino têm tratamento definido
- [ ] Volume de dados a migrar está quantificado
- [ ] Dados sensíveis têm tratamento especial durante migração

### Compatibilidade
- [ ] Nova versão é backward-compatible durante o período de migração
- [ ] Clientes/consumidores existentes continuam funcionando durante migração
- [ ] APIs mantêm contrato existente ou têm período de coexistência
- [ ] Formatos de dados são compatíveis ou têm camada de tradução
- [ ] Integrações com terceiros não são quebradas pela migração

### Validação
- [ ] Critérios de validação pós-migração estão definidos
- [ ] Contagem de registros é verificada (origem vs destino)
- [ ] Integridade referencial é verificada pós-migração
- [ ] Amostragem de dados é validada manualmente
- [ ] Testes automatizados validam funcionalidades pós-migração

### Rollback e Contingência
- [ ] Rollback de migração está planejado e testado
- [ ] Ponto de no-return está identificado (se existir)
- [ ] Dados criados durante migração gradual são tratados no rollback
- [ ] Plano de comunicação para problemas durante migração existe
- [ ] Tempo máximo aceitável de indisponibilidade durante migração está definido

---

## Critérios de Aprovação
- **Mínimo**: Planejamento, Validação e Rollback completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Migração sem validação ou sem rollback

## Sinais de Alerta (Red Flags)
- Migração big bang de milhões de registros sem teste prévio
- "Vamos migrar tudo no final de semana" sem dry run
- Nenhuma validação pós-migração planejada
- Dados sensíveis (PII) expostos durante processo de migração
- Migração que depende de downtime maior que a janela disponível

## Agente Responsável
**Agente de Risk & Failure Analysis** — em colaboração com DBA e time de dados.
