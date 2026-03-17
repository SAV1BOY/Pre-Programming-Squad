# Ótimos Registros de Risco — Exemplos Anotados

## Introdução

Um registro de risco excepcional não é uma formalidade burocrática — é uma ferramenta viva que protege o projeto de surpresas. Os melhores registros são específicos (não genéricos), quantificados (não vagos), com planos de ação concretos (não "monitorar") e atualizados regularmente. Risco genérico como "pode haver atrasos" é inútil; risco específico como "a API do fornecedor X tem SLA de apenas 99.5% e tivemos 3 incidentes nos últimos 2 meses" é acionável.

---

## Exemplo 1 — Registro de Risco para Projeto de Migração

### O Registro

> **RSK-001**: Perda de dados durante migração de MySQL para PostgreSQL
> - **Probabilidade**: Média | **Impacto**: Catastrófico | **Severidade**: Crítica
> - **Causa raiz**: Diferenças de tipos de dados (DATETIME vs TIMESTAMPTZ, charset handling, ENUM vs CHECK constraints)
> - **Gatilhos**: Falha em testes de validação pós-migração, contagem de registros divergente, dados truncados
> - **Mitigação**: Suite de validação com 500+ assertions comparando dados fonte/destino. Migração em dry-run 3x antes do go-live. Backup completo antes de cada tentativa.
> - **Contingência**: Rollback para MySQL com restauração do backup. RPO: zero (backup pré-migração). RTO: 2 horas.
> - **Responsável**: DBA Lead
>
> **RSK-002**: Regressão de performance após migração
> - **Probabilidade**: Alta | **Impacto**: Alto | **Severidade**: Crítica
> - **Causa raiz**: Queries otimizadas para MySQL podem não performar igual em PostgreSQL. Índices diferentes, query planner diferente, connection pooling diferente.
> - **Gatilhos**: p99 de latência > 200ms em queries críticas, CPU do banco > 70%
> - **Mitigação**: Benchmark de top 50 queries em ambos os bancos. Shadow traffic por 2 semanas. Tuning de postgresql.conf baseado no workload real.
> - **Contingência**: Reverter para MySQL e refazer tuning. Manter MySQL operacional por 30 dias pós-migração.
> - **Responsável**: Backend Lead

### Por que funciona

- **Causa raiz específica**: Não "pode dar problema", mas exatamente que tipo de problema
- **Gatilhos mensuráveis**: p99 > 200ms, CPU > 70% — o time sabe quando reagir
- **Mitigação com números**: 500+ assertions, top 50 queries, 2 semanas de shadow traffic
- **Contingência com RPO/RTO**: Métricas de recuperação definidas previamente

---

## Exemplo 2 — Registro de Risco para Integração com Terceiros

### O Registro

> **RSK-005**: Indisponibilidade da API de verificação de identidade (KYC)
> - **Probabilidade**: Alta (fornecedor teve 4 incidentes nos últimos 3 meses)
> - **Impacto**: Alto (bloqueia onboarding de novos sellers)
> - **Estratégia**: Mitigar + Transferir
> - **Mitigação**: Implementar circuit breaker com fallback para verificação manual. Cache de verificações já realizadas (TTL 30 dias). Negociar SLA formal com fornecedor incluindo penalidades.
> - **Transferência**: Integrar fornecedor secundário (Fornecedor B) como fallback automático. Custo estimado: R$15K/mês adicional.
> - **Contingência**: Modo degradado — aceitar sellers com verificação pendente (até 24h) com limites de transação reduzidos (R$1000/dia).
> - **Monitoramento**: Alerta se taxa de erro > 5% em janela de 15 minutos.

### Por que funciona

- **Histórico de incidentes**: 4 em 3 meses — evidência, não palpite
- **Combinação de estratégias**: Mitigar E transferir — não depende de uma única abordagem
- **Modo degradado definido**: Não é "sistema fora do ar" vs "sistema funcionando" — há gradações
- **Monitoramento proativo**: Alerta antes de virar crise

---

## Lições Extraídas

1. **Seja específico**: "Risco técnico" não é um risco. "Timeout da API X causa falha silenciosa no cálculo de frete" é um risco
2. **Quantifique com evidências**: Histórico de incidentes, benchmarks, dados reais
3. **Defina gatilhos mensuráveis**: O time precisa saber quando o risco está se materializando
4. **Mitigação com ações concretas**: "Monitorar" não é mitigação. "Configurar alerta quando X > Y" é
5. **Contingência operacional**: O que fazer nos primeiros 30 minutos quando o risco vira realidade
6. **Revise semanalmente**: Riscos mudam — probabilidades aumentam, novos riscos surgem
7. **Atribua donos**: Risco sem responsável é risco ignorado
