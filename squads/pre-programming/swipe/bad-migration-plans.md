# Planos de Migração Ruins — Exemplos Anotados

## Introdução

Migrações são das operações mais arriscadas em engenharia de software. Envolvem dados reais, sistemas em produção, usuários ativos e frequentemente zero margem para erro. Planos de migração ruins não falham por azar — falham por falta de planejamento na fase de pré-programação. Este documento analisa migrações que deram errado e extrai lições para prevenir as mesmas falhas.

---

## Exemplo 1 — Migração Big-Bang de Banco de Dados

### O Plano

> "Sábado às 2h da manhã: parar o sistema, rodar scripts de migração, verificar se tudo está OK, ligar o sistema de volta. Janela de 4 horas."

### Por que falhou

- **Sem ensaio**: Scripts de migração nunca foram testados com volume real de dados. Em staging com 1000 registros, rodou em 2 minutos. Em produção com 50M de registros, levou 7 horas.
- **Sem rollback**: "Se der errado, restauramos o backup". Mas o restore do backup de 200GB levava 3 horas adicionais.
- **Sem comunicação**: Clientes descobriram o downtime ao não conseguir acessar o sistema no sábado de manhã.
- **Resultado**: 14 horas de downtime (planejado era 4). Dados de transações do sábado perdidos. Equipe trabalhou 20 horas seguidas. Clientes empresariais ameaçaram cancelar contrato.

### O que a pré-programação deveria ter feito

- Testar migração com volume real de dados (cópia anonimizada de produção)
- Medir tempo de migração e tempo de rollback em ambiente equivalente
- Planejar migração incremental em vez de big-bang
- Definir plano de comunicação com clientes

---

## Exemplo 2 — Migração de API Sem Versionamento

### O Plano

> "Atualizar os endpoints da API v1 para o novo formato de resposta. Avisar os clientes por e-mail 1 semana antes."

### Por que falhou

- **Breaking changes sem versão nova**: Mudaram o formato de resposta na mesma URL. Clientes que não leram o e-mail quebraram.
- **Sem período de coexistência**: V1 antiga e V1 nova não coexistiram. Foi instantâneo.
- **Clientes com integrações automáticas**: Sistemas automatizados não "leem e-mail". Falharam silenciosamente e acumularam dados inconsistentes por 3 dias até alguém perceber.
- **Resultado**: 47 clientes com integrações quebradas. 3 dias de dados inconsistentes para reconciliar. 2 clientes enterprise perdidos.

### O que a pré-programação deveria ter feito

- Lançar como /v2 mantendo /v1 ativa por período de depreciação (mínimo 3 meses)
- Adicionar header de depreciação nas respostas da v1
- Monitorar taxa de uso de v1 vs v2
- Contatar individualmente clientes com alto volume de requests na v1

---

## Exemplo 3 — Migração de Cloud Sem Teste de Performance

### O Plano

> "Migrar de on-premise para AWS. Recriar a mesma arquitetura na cloud. Usar instâncias equivalentes. Deveria funcionar igual."

### Por que falhou

- **"Equivalente" não é igual**: Instância com mesma CPU e RAM tem performance de disco completamente diferente (EBS vs SSD local). Queries que dependiam de I/O de disco ficaram 5x mais lentas.
- **Latência de rede**: On-premise tinha < 1ms entre serviços. Na cloud, 5-15ms. Serviço que fazia 200 chamadas internas por request foi de 200ms para 3s.
- **Custos surpresa**: Data transfer entre AZs, EBS IOPS, NAT Gateway — custos que não existiam on-premise. Fatura mensal 3x maior que o estimado.
- **Resultado**: Performance degradada por 2 meses até re-arquitetar para a cloud. Custo 3x acima do orçamento até otimização.

### O que a pré-programação deveria ter feito

- Realizar PoC de performance na cloud com workload realista
- Mapear diferenças de I/O, rede e storage entre ambientes
- Estimar custos com calculadora detalhada, incluindo data transfer
- Planejar re-arquitetura cloud-native, não lift-and-shift

---

## Exemplo 4 — Migração de Dados Sem Validação

### O Plano

> "Script Python que lê do banco antigo e insere no novo. Rodar em batch de 10K registros."

### Por que falhou

- **Sem validação de integridade**: Script não verificava se todos os registros foram migrados. 2% dos registros foram silenciosamente descartados por erros de encoding.
- **Sem mapeamento de tipos**: Campos DATE no banco antigo tinham formatos inconsistentes ("DD/MM/YYYY", "YYYY-MM-DD", "MM-DD-YYYY"). Script assumiu formato único.
- **Sem idempotência**: Quando o script falhou no meio e foi reiniciado, duplicou 30K registros.
- **Resultado**: Dados de 500 clientes corrompidos. 3 semanas de reconciliação manual. Multa regulatória por dados incorretos em relatórios.

### O que a pré-programação deveria ter feito

- Analisar qualidade dos dados antes de migrar
- Criar pipeline de validação com contagem, checksums e amostragem
- Garantir idempotência do script de migração
- Rodar migração de teste com 100% dos dados em ambiente isolado

---

## Lições Extraídas

1. **Nunca big-bang**: Migrações incrementais, reversíveis e testáveis
2. **Teste com volume real**: 1000 registros vs 50 milhões é um mundo diferente
3. **Meça o rollback**: Se não sabe quanto tempo o rollback leva, não sabe seu risco real
4. **Versione APIs**: Breaking changes merecem versão nova, período de coexistência e comunicação ativa
5. **Valide dados obsessivamente**: Contagem, checksums, amostragem aleatória, comparação fonte/destino
6. **Cloud não é lift-and-shift**: Performance, custo e latência mudam. Re-arquiteture, não copie
7. **Comunique com antecedência e frequência**: Stakeholders precisam saber o que vai mudar, quando e como serão afetados
8. **Ensaie a migração**: Uma migração não testada é uma aposta
