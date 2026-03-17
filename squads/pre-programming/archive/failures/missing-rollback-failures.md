# Falhas por Ausência de Plano de Rollback

## Objetivo

Catalogar casos onde a falta de plano de rollback transformou problemas gerenciáveis em incidentes prolongados. Rollback é seguro de engenharia — caro de planejar, catastrófico de não ter.

---

## Caso 1: Migração de Schema sem Rollback — 14 Horas de Downtime

### O Que Aconteceu
Migração de banco de dados alterou tipo de coluna de `VARCHAR(50)` para `UUID` nativo em tabela com 80M de registros. A migração rodou em produção por 3 horas. Após conclusão, aplicação começou a retornar erros porque ORM gerava queries incompatíveis com o novo tipo. Rollback da migração (converter UUID de volta para VARCHAR) levaria outras 3 horas. Sem alternativa, time tentou fix-forward, gerando mais erros. Downtime total: 14 horas.

### O Que Deu Errado
- Migração destrutiva (alteração de tipo) sem teste em réplica de produção
- Incompatibilidade com ORM descoberta após migração em produção
- Rollback da migração era tão demorado quanto a migração
- Sem feature flag para alternar entre código que usa VARCHAR e código que usa UUID
- Pressão para "resolver logo" levou a fix-forward mal planejado

### Causa Raiz
**Migração irreversível sem validação prévia.** Migrações de schema que alteram tipo de dados são inerentemente perigosas porque rollback tem o mesmo custo da migração. Sem validação completa em ambiente de staging com dados realistas, o risco é altíssimo.

### Como Prevenir
1. Migrações destrutivas devem ser divididas: (1) criar nova coluna, (2) dual-write, (3) migrar dados, (4) alternar leituras, (5) remover coluna antiga
2. Testar migração em réplica de produção com dados e volume reais
3. Sempre ter rollback que pode ser executado em <15 minutos
4. Feature flags para alternar entre código antigo e novo

### Checklist Atualizado
- [ ] A migração é reversível em tempo aceitável (<15 min)?
- [ ] Se irreversível, foi testada em réplica com dados reais?
- [ ] Existe estratégia de dual-write para migrações de tipo de dados?
- [ ] Feature flag permite alternar entre código antigo e novo?

---

## Caso 2: Deploy de Microsserviço sem Backward Compatibility

### O Que Aconteceu
Serviço A (producer) e Serviço B (consumer) foram deployados simultaneamente com contrato de API novo. Deploy do Serviço A foi bem-sucedido. Deploy do Serviço B falhou no health check e fez rollback automático. Resultado: Serviço A enviando formato novo, Serviço B esperando formato antigo. Incompatibilidade causou perda de 12.000 eventos até detecção.

### O Que Deu Errado
- Deploy simultâneo de producer e consumer
- Novo formato de mensagem não era backward compatible
- Sem versionamento de contrato de mensageria
- Dead letter queue existia mas sem alerta
- Perda silenciosa de eventos — consumer descartava mensagens que não podia deserializar

### Causa Raiz
**Deploy acoplado em arquitetura que deveria ser desacoplada.** Microsserviços que precisam ser deployados juntos não são microsserviços. Sem backward compatibility no contrato, qualquer assimetria de deploy causa perda de dados.

### Como Prevenir
1. Contratos de mensageria devem ser backward compatible (novos campos opcionais)
2. Deploy de producer e consumer nunca devem ser acoplados
3. Consumer deve logar (não descartar) mensagens que não consegue processar
4. Dead letter queue com alerta em volume > 0

### Checklist Atualizado
- [ ] Contratos entre serviços são backward compatible?
- [ ] Serviços podem ser deployados independentemente?
- [ ] Mensagens não processáveis são enviadas para DLQ com alerta?
- [ ] Deploy order está definida (consumer primeiro, producer depois)?

---

## Caso 3: Feature Toggle Removida Antes de Estabilização

### O Que Aconteceu
Nova feature de recomendação lançada com feature toggle. Após 1 semana sem incidentes, toggle foi removida do código e da configuração. Na semana seguinte, a feature de recomendação começou a retornar resultados errados devido a modelo de ML desatualizado. Sem toggle, a única opção era deploy de código para desabilitar — durante uma sexta-feira às 18h.

### O Que Deu Errado
- Feature toggle removida após apenas 1 semana de estabilidade
- Sem critério formal de "estabilização" que justificasse remoção
- Deploy de emergência necessário para o que seria um toggle flip
- Dependência de modelo de ML não estava no critério de estabilidade

### Causa Raiz
**Remoção prematura de mecanismo de rollback.** Feature toggles são o rollback mais rápido disponível. Removê-las antes de estabilização completa elimina a capacidade de resposta rápida a incidentes.

### Como Prevenir
1. Feature toggles devem permanecer por mínimo de 30 dias após ativação
2. Critério de remoção: zero incidentes + todas as dependências estáveis + aprovação de on-call
3. Documentar todas as dependências da feature (APIs, modelos ML, dados) no critério de estabilidade

### Checklist Atualizado
- [ ] Feature toggles têm período mínimo de retenção definido?
- [ ] Critério de remoção de toggle inclui estabilidade de todas as dependências?
- [ ] Toggle pode ser desligada sem deploy?

---

## Caso 4: Migração de Dados Sem Ponto de Restauração

### O Que Aconteceu
Script de migração de dados transformou registros de endereço de formato livre para formato estruturado (rua, número, complemento, CEP). A transformação era lossy — dados que não parseavam foram descartados. Após migração, 8% dos endereços estavam incorretos (parser errou em formatos regionais). Sem backup dos dados originais, não havia como restaurar os endereços corretos.

### O Que Deu Errado
- Migração lossy (descartava dados não parseáveis) sem backup dos originais
- Parser testado com amostra de 100 registros, falhou em 8% dos 500K registros reais
- Sem ponto de restauração — dados originais sobrescritos
- Correção manual de 40K registros levou 3 semanas com time terceirizado

### Causa Raiz
**Migração destrutiva sem preservação de dados originais.** Qualquer transformação de dados que pode perder informação deve preservar os dados originais até validação completa do resultado.

### Como Prevenir
1. Migrações de dados devem preservar dados originais em coluna ou tabela auxiliar
2. Validação de migração com amostra estatisticamente significativa (não 100 de 500K)
3. Período de "soft delete": dados originais acessíveis por 30 dias após migração
4. Dry-run obrigatório com relatório de registros que seriam alterados/descartados

### Checklist Atualizado
- [ ] Dados originais são preservados durante migração transformacional?
- [ ] Validação usa amostra estatisticamente significativa?
- [ ] Dry-run foi executado com relatório de impacto?
- [ ] Existe período de retenção dos dados originais pós-migração?

---

## Resumo de Padrões

| Padrão | Frequência | Impacto Médio |
|--------|------------|---------------|
| Migração de schema sem rollback rápido | Alta | 4-14h de downtime |
| Deploy acoplado sem backward compat | Média | Perda de dados |
| Remoção prematura de feature toggle | Alta | Deploy de emergência |
| Migração de dados sem preservação | Média | Perda irreversível de dados |

---

## Checklist Consolidado — Plano de Rollback

- [ ] Toda mudança tem rollback que executa em <15 minutos?
- [ ] Migrações de schema são reversíveis ou testadas em réplica?
- [ ] Contratos entre serviços são backward compatible?
- [ ] Feature toggles permanecem por período mínimo de estabilização?
- [ ] Migrações de dados preservam dados originais?
- [ ] Dry-run é executado antes de migrações destrutivas?
- [ ] Deploy order está definida para mudanças multi-serviço?
- [ ] Dead letter queues têm alertas configurados?
- [ ] Rollback foi testado (não apenas planejado)?
