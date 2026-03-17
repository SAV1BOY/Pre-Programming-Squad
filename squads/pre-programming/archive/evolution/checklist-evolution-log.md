# Log de Evolução dos Checklists

## Objetivo

Manter registro cronológico de todas as alterações nos checklists do Pre-Programming Squad, incluindo o incidente que motivou cada mudança e o impacto observado.

---

## Formato de Registro

Cada entrada segue o formato:
- **Data** da alteração
- **Checklist** afetado
- **Alteração** realizada
- **Incidente motivador** (se aplicável)
- **Impacto observado** após a mudança

---

## Registro Cronológico

### CL-001 — Adição de Verificação de Timezone
- **Data:** Mês 2
- **Checklist:** Identificação de Edge Cases
- **Alteração:** Adicionado item "Funcionalidades com data/hora foram testadas com múltiplos timezones?"
- **Incidente motivador:** Bug de agendamento em Fernando de Noronha — compromisso apareceu no dia errado por cálculo de "amanhã" no timezone do servidor
- **Impacto:** 3 bugs de timezone identificados em pré-programação nos 2 meses seguintes

### CL-002 — Adição de Validação de Inputs Degenerados
- **Data:** Mês 2
- **Checklist:** Design de Testes
- **Alteração:** Adicionado item "Inputs degenerados (vazio, null, zero, máximo) estão no plano de testes?"
- **Incidente motivador:** Upload de arquivo de 0 bytes causou loop infinito no processador de documentos
- **Impacto:** 7 cenários de input degenerado adicionados a planos de teste antes da implementação

### CL-003 — Verificação de Dependências em Banco de Dados
- **Data:** Mês 3
- **Checklist:** Impacto em Sistema Legado
- **Alteração:** Adicionado item "Dependências em banco de dados (views, triggers, procedures, database links) foram mapeadas?"
- **Incidente motivador:** Stored procedure alterada quebrou 3 integrações externas via database link
- **Impacto:** 2 alterações em procedures compartilhadas foram redesenhadas como nova versão (v2) em vez de alteração in-place

### CL-004 — Exigência de Alternativas em ADRs
- **Data:** Mês 3
- **Checklist:** Qualidade de Design Docs
- **Alteração:** Alterado de "Alternativas foram consideradas?" para "Mínimo de 3 alternativas genuínas com análise de trade-offs documentada"
- **Incidente motivador:** ADR de adoção de tecnologia tinha apenas a solução escolhida — alternativa "não fazer nada" e "solução A" eram strawman
- **Impacto:** Qualidade média de ADRs subiu de 5.8/10 para 7.3/10 nas avaliações de peer review

### CL-005 — Verificação de Lock-in em Decisões Build vs. Buy
- **Data:** Mês 4
- **Checklist:** Avaliação de Arquitetura
- **Alteração:** Adicionados itens de portabilidade de dados, custo de saída e cláusulas contratuais
- **Incidente motivador:** SaaS de workflow aumentou preço em 300% e formato proprietário impedia migração
- **Impacto:** 2 decisões de compra revisadas para incluir cláusula de export de dados

### CL-006 — Backward Compatibility Obrigatória para Contratos entre Serviços
- **Data:** Mês 5
- **Checklist:** Plano de Rollback
- **Alteração:** Adicionado item "Contratos entre serviços são backward compatible?"
- **Incidente motivador:** Deploy assimétrico de producer e consumer causou perda de 12K eventos
- **Impacto:** Testes de contrato (Pact) adotados para 4 integrações críticas entre serviços

### CL-007 — Feature Flags com Período Mínimo de Retenção
- **Data:** Mês 5
- **Checklist:** Plano de Rollback
- **Alteração:** Adicionado item "Feature toggles permanecem por período mínimo de 30 dias após ativação"
- **Incidente motivador:** Feature toggle removida após 1 semana, problema em modelo de ML exigiu deploy de emergência na sexta à noite
- **Impacto:** Zero deploys de emergência por remoção prematura de toggle nos 4 meses seguintes

### CL-008 — Teste de Concorrência para Operações de Estado
- **Data:** Mês 6
- **Checklist:** Design de Testes
- **Alteração:** Adicionado item "Operações check-then-act têm testes de concorrência planejados?"
- **Incidente motivador:** Race condition em reserva de ingressos causou venda duplicada — R$85K em reembolsos
- **Impacto:** 5 operações check-then-act identificadas e redesenhadas com locking antes da implementação

### CL-009 — Decomposição de Requisitos por Referência
- **Data:** Mês 7
- **Checklist:** Leitura de Requisitos
- **Alteração:** Adicionado item "Referências a produtos externos foram decompostas em features individuais?"
- **Incidente motivador:** "Similar ao Calendly" foi interpretado como agendamento básico; stakeholder esperava 15 features do Calendly
- **Impacto:** 3 PRDs com requisitos por referência passaram por decomposição antes de avançar

### CL-010 — Validação de Serialização em Atualizações de Biblioteca
- **Data:** Mês 7
- **Checklist:** Impacto em Sistema Legado
- **Alteração:** Adicionado item "Compatibilidade com dados persistidos (cache, filas, banco) foi testada?"
- **Incidente motivador:** Atualização de Jackson mudou serialização de datas, quebrando deserialização de milhões de registros em cache Redis
- **Impacto:** 1 atualização de biblioteca foi planejada com cache flush gradual em vez de big bang

### CL-011 — Custo de Infraestrutura em Design Docs
- **Data:** Mês 8
- **Checklist:** Qualidade de Design Docs
- **Alteração:** Adicionado item "Cálculo de custo de infraestrutura incluído para soluções que envolvem novos componentes?"
- **Incidente motivador:** Solução com 3 bancos de dados e message broker custava R$15K/mês a mais que alternativa com banco único
- **Impacto:** 2 designs revisados para alternativa mais custo-efetiva sem sacrificar requisitos

### CL-012 — Overrides Ativos de Feature Flags
- **Data:** Mês 9
- **Checklist:** Impacto em Sistema Legado
- **Alteração:** Adicionado item "Feature flags a serem removidas foram verificadas quanto a overrides ativos?"
- **Incidente motivador:** Remoção de flag com override por cliente Enterprise causou cobrança errada
- **Impacto:** Relatório de overrides ativos implementado no sistema de feature flags

### CL-013 — Testes de Integração com Componentes Reais
- **Data:** Mês 9
- **Checklist:** Design de Testes
- **Alteração:** Adicionado item "Testes de integração usam banco real (não in-memory)?"
- **Incidente motivador:** Suite de testes de integração passava com H2 mas falhava com PostgreSQL em produção
- **Impacto:** Testcontainers adotado em 6 projetos, eliminando categoria inteira de bugs de incompatibilidade SQL

### CL-014 — Plano de Migração de Dados em PRDs
- **Data:** Mês 10
- **Checklist:** Leitura de Requisitos
- **Alteração:** Adicionado item "Se há mudança de modelo de dados, existe plano de migração dos dados existentes?"
- **Incidente motivador:** Migração de endereços de formato livre para estruturado perdeu 8% dos registros por parser incorreto
- **Impacto:** 2 migrações de dados planejadas com dry-run e preservação de dados originais

---

## Estatísticas do Log

| Métrica | Valor |
|---------|-------|
| Total de alterações em checklists | 14 |
| Motivadas por incidente real | 14 (100%) |
| Tempo médio para incorporar aprendizado | 2 semanas |
| Itens que geraram impacto mensurável | 12 (86%) |

---

## Processo de Atualização

### Quando Atualizar
1. Após cada incidente que a pré-programação deveria ter prevenido
2. Após cada trimestre, baseado em análise de retrabalho
3. Quando feedback de desenvolvedores identifica gap recorrente

### Como Atualizar
1. Registrar incidente motivador com detalhes
2. Propor alteração específica no checklist relevante
3. Revisar com squad para validar relevância e praticidade
4. Implementar e monitorar impacto por 30 dias
5. Registrar impacto observado neste log

### Critérios para Remoção
- Item não é acionado há 6+ meses
- Item é redundante com outro mais abrangente
- Item gera false positives frequentes sem valor real
- Remoção requer aprovação do squad e registro do motivo
