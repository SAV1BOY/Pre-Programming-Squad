# Data Migration Readiness Framework

## Propósito
Planejar migrações de dados com segurança, validação e rollback, evitando as armadilhas mais comuns: perda de dados, downtime não planejado e inconsistência.

## Problema que Resolve
80% das migrações de dados que dão errado falham por falta de planejamento: sem rollback, sem validação pós-migração, sem estimativa realista de tempo, sem comunicação de downtime.

## Quando Usar
- Em todo projeto que envolve mudança de schema
- Em migrações entre sistemas ou databases
- Em merges de dados de múltiplas fontes
- Quando Legacy Impact Auditor identifica necessidade de migração

## Classificação de Migração

| Tipo | Risco | Exemplo |
|------|-------|---------|
| **Schema evolution** | Baixo-Médio | Adicionar coluna nullable, criar índice |
| **Data transformation** | Médio | Normalizar formatos, split de tabela |
| **Cross-system migration** | Alto | Migrar de MongoDB para PostgreSQL |
| **Live migration** | Muito Alto | Migrar com sistema em produção |

## Processo

### Passo 1 — Análise de Dados
- Volume: quantos registros/GB?
- Qualidade: dados sujos? Duplicatas? Nulos inesperados?
- Velocidade: tempo estimado de migração?
- Dependências: quem consome estes dados?

### Passo 2 — Estratégia
| Estratégia | Quando usar | Risco | Downtime |
|-----------|-------------|-------|----------|
| **Big bang** | Dados pequenos, janela de manutenção ok | Médio | Sim |
| **Incremental** | Dados grandes, precisa de zero-downtime | Baixo | Mínimo |
| **Dual-write** | Transição gradual com coexistência | Baixo | Zero |
| **CDC (Change Data Capture)** | Sincronização contínua durante transição | Médio | Zero |

### Passo 3 — Rollback Plan
**Obrigatório.** Para cada migração:
- Script de rollback testado em staging
- Backup verificado antes de executar
- Critério de "abort": quando acionar rollback
- Tempo estimado de rollback

### Passo 4 — Validação Pós-Migração
```
Checklist de validação:
- [ ] Contagem de registros: origem = destino ± tolerância
- [ ] Amostragem: 100 registros aleatórios verificados manualmente
- [ ] Integridade referencial: FKs consistentes
- [ ] Queries críticas: mesmos resultados no novo schema
- [ ] Performance: queries dentro do SLA
```

### Passo 5 — Comunicação e Execução
- Notificar stakeholders sobre janela de migração
- Executar em horário de menor tráfego
- Monitorar em tempo real durante execução
- Manter canal de comunicação aberto com time de suporte

## Armadilhas
- **Migrar sem backup verificado** → Backup não testado não é backup
- **Subestimar volume** → 1M registros migra em minutos; 1B registros pode levar horas
- **Não validar dados de origem** → Garbage in, garbage out
- **Rollback "na teoria"** → Se o rollback script nunca rodou em staging, ele não funciona
- **Comunicar downtime tarde demais** → Stakeholders devem saber com antecedência
