# Falhas por Impacto em Sistema Legado

## Objetivo

Catalogar casos onde mudanças em sistemas legados causaram efeitos colaterais inesperados porque a análise de impacto foi insuficiente na fase de pré-programação.

---

## Caso 1: Alteração de Stored Procedure Compartilhada

### O Que Aconteceu
Time alterou uma stored procedure de cálculo de impostos para atender nova regra fiscal. A procedure era chamada por 14 módulos diferentes, incluindo 3 sistemas externos via database link. Após o deploy, 3 integrações externas quebraram porque esperavam o formato anterior do resultado.

### O Que Deu Errado
- Stored procedure era compartilhada por múltiplos consumidores não documentados
- Análise de impacto verificou apenas o codebase do monolito, ignorando database links
- Sem versionamento — a procedure foi alterada in-place
- Testes de regressão não cobriam os consumidores externos

### Causa Raiz
**Mapa de dependências incompleto.** Em sistemas legados, dependências existem em camadas invisíveis: triggers, views, database links, jobs agendados, scripts de ETL. Análise de impacto que olha apenas código-fonte perde essas conexões.

### Como Prevenir
1. Para sistemas legados, mapear dependências em todas as camadas: código, banco, ETL, integrações, scripts cron
2. Antes de alterar artefatos compartilhados, consultar DBA e time de integrações
3. Criar versão nova da procedure em vez de alterar in-place (v2 ao lado de v1)

### Checklist Atualizado
- [ ] Dependências em banco de dados (views, triggers, procedures, database links) foram mapeadas?
- [ ] Consumidores externos do artefato alterado foram identificados?
- [ ] Alteração é feita como nova versão ou in-place? Se in-place, todos os consumidores foram notificados?

---

## Caso 2: Migração de Coluna que Alimentava Relatório do Financeiro

### O Que Aconteceu
Refactor renomeou coluna `vlr_total` para `total_amount` como parte de padronização de nomenclatura. Uma planilha de Excel usada pelo financeiro tinha query SQL direta ao banco referenciando `vlr_total`. O relatório mensal quebrou silenciosamente e o financeiro só descobriu 3 semanas depois, gerando retrabalho manual de reconciliação.

### O Que Deu Errado
- Planilhas com SQL direto ao banco não estavam documentadas
- Rename de coluna não passou por período de deprecação
- Nenhuma comunicação foi feita ao financeiro sobre a mudança
- Sem alias ou view de compatibilidade

### Causa Raiz
**Shadow IT não mapeado.** Usuários de negócio criam seus próprios acessos aos dados (planilhas, queries, scripts) que não aparecem em nenhum inventário de dependências. Mudanças no schema as quebram silenciosamente.

### Como Prevenir
1. Antes de mudanças de schema, enviar comunicação a todos os times que têm acesso ao banco
2. Usar período de deprecação: manter coluna antiga como alias/view por 30-90 dias
3. Logar queries que acessam colunas a serem removidas para identificar consumidores ocultos

### Checklist Atualizado
- [ ] Mudanças de schema foram comunicadas a todos os times com acesso ao banco?
- [ ] Existe período de deprecação para colunas/tabelas renomeadas ou removidas?
- [ ] Consumidores ocultos (planilhas, scripts, BI tools) foram identificados?

---

## Caso 3: Atualização de Biblioteca que Mudou Formato de Serialização

### O Que Aconteceu
Atualização de Jackson 2.9 para 2.14 como parte de patch de segurança. A nova versão mudou o comportamento default de serialização de datas (de timestamp para ISO 8601). Cache Redis continha milhões de registros no formato antigo. Após o deploy, deserialização falhou para todos os registros em cache, causando thundering herd no banco de dados.

### O Que Deu Errado
- Atualização de biblioteca "minor" tratada como trivial
- Changelog da biblioteca não foi lido completamente
- Cache existente com formato antigo não foi considerado
- Sem teste de compatibilidade entre formato antigo e novo

### Causa Raiz
**Atualização de dependência sem análise de breaking changes em dados persistidos.** Bibliotecas de serialização afetam dados em cache, filas e banco. Uma mudança de comportamento default pode ser breaking para dados existentes mesmo sem ser breaking para a API.

### Como Prevenir
1. Para atualização de bibliotecas de serialização, sempre testar compatibilidade com dados existentes
2. Ler changelog completo, especialmente seções de "breaking changes" e "behavioral changes"
3. Planejar estratégia de migração de dados persistidos (cache flush, migração gradual)

### Checklist Atualizado
- [ ] Changelogs de bibliotecas atualizadas foram lidos completamente?
- [ ] Compatibilidade com dados persistidos (cache, filas, banco) foi testada?
- [ ] Estratégia de migração de dados existentes está definida?

---

## Caso 4: Remoção de Feature Flag que Controlava Lógica Legada

### O Que Aconteceu
Feature flag `USE_NEW_PRICING` existia há 2 anos, sempre ligada em produção. Time decidiu remover a flag e o código do branch `false` como limpeza. O que não sabiam: um cliente Enterprise tinha a flag desligada via override específico porque seu contrato usava o modelo de pricing antigo. Após a remoção, o cliente foi migrado automaticamente para o novo pricing, gerando cobrança errada.

### O Que Deu Errado
- Feature flag tinha override por cliente não documentado
- Remoção de flag tratada como tarefa de limpeza trivial
- Nenhuma consulta ao time comercial sobre contratos especiais
- Sistema de feature flags não tinha relatório de "overrides ativos"

### Causa Raiz
**Configurações runtime não inventariadas.** Feature flags com overrides são efetivamente configuração de negócio. Removê-las sem inventariar todos os overrides ativos é equivalente a mudar regra de negócio sem aprovação.

### Como Prevenir
1. Antes de remover feature flags, listar todos os overrides ativos e seus motivos
2. Consultar time comercial sobre flags que afetam pricing, billing ou funcionalidades contratuais
3. Implementar relatório de overrides ativos no sistema de feature flags

### Checklist Atualizado
- [ ] Feature flags a serem removidas foram verificadas quanto a overrides ativos?
- [ ] Times de negócio foram consultados sobre implicações de flags com impacto comercial?
- [ ] Existe inventário de overrides por cliente/segmento?

---

## Resumo de Padrões

| Padrão | Frequência | Impacto Médio |
|--------|------------|---------------|
| Dependência em camada invisível (banco, ETL) | Alta | Integração quebrada |
| Shadow IT (planilhas, scripts diretos) | Alta | Quebra silenciosa, detecção tardia |
| Serialização incompatível em dados persistidos | Média | Indisponibilidade, thundering herd |
| Feature flag com override não documentado | Média | Impacto comercial/contratual |

---

## Checklist Consolidado — Impacto em Sistema Legado

- [ ] Dependências em todas as camadas foram mapeadas (código, banco, ETL, integrações, cron)?
- [ ] Consumidores externos e ocultos foram identificados?
- [ ] Mudanças de schema têm período de deprecação?
- [ ] Atualizações de bibliotecas foram testadas contra dados persistidos?
- [ ] Feature flags têm inventário de overrides ativos antes da remoção?
- [ ] Times de negócio foram consultados sobre impactos comerciais/contratuais?
- [ ] Existe plano de rollback para cada mudança em componente compartilhado?
- [ ] Comunicação prévia foi enviada a todos os stakeholders afetados?
