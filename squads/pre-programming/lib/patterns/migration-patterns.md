# Padrões de Migração

## Nome do Padrão
Padrões para Planejamento de Migrações de Sistema

## Problema que Resolve
Migrações de sistemas (legado para novo, monolito para microsserviços, troca de banco de dados) são projetos de alto risco. Sem padrões adequados, ocorrem: perda de dados, downtime prolongado, inconsistências entre sistemas e rollbacks caóticos.

## Solução

### 1. Strangler Fig (Estrangulamento Gradual)
Migrar incrementalmente, substituindo partes do sistema legado uma a uma enquanto o novo sistema cresce ao redor do antigo, até que o legado seja completamente substituído.

**Aplicação prática:**
- Mapear funcionalidades do sistema legado
- Priorizar funcionalidades por valor/risco
- Criar proxy/roteador que direciona tráfego
- Migrar uma funcionalidade por vez, validando cada etapa

### 2. Execução Paralela (Parallel Run)
Executar o sistema novo e o legado simultaneamente, comparando resultados para validar a correção da migração antes de desligar o antigo.

**Aplicação prática:**
- Duplicar requisições para ambos os sistemas
- Comparar resultados automaticamente (diff)
- Monitorar discrepâncias e corrigir
- Definir critério de convergência para cutover

### 3. Migração em Fases com Rollback
Dividir a migração em fases independentes, cada uma com seu próprio plano de rollback e critérios de sucesso.

**Aplicação prática:**
- Fase 1: Leitura dupla (ler do novo, fallback para legado)
- Fase 2: Escrita dupla (escrever em ambos)
- Fase 3: Leitura primária do novo
- Fase 4: Desligar escrita no legado
- Cada fase com rollback independente

### 4. Migração de Dados com Reconciliação
Migrar dados em lotes com verificação de integridade e reconciliação contínua entre origem e destino.

**Aplicação prática:**
- Extrair dados em lotes incrementais
- Transformar e carregar com validação
- Reconciliar contagens e checksums
- Manter log de migração para auditoria

## Quando Usar

- Ao substituir sistemas legados
- Em migrações de banco de dados
- Na transição de monolito para microsserviços
- Ao trocar provedores de infraestrutura
- Em atualizações de versão com breaking changes

## Quando NÃO Usar

- Em sistemas novos sem legado
- Quando o sistema legado pode ser desligado sem impacto (ex: sem dados históricos)
- Em protótipos ou ambientes de desenvolvimento
- Quando a migração é trivial (ex: mudança de config)

## Exemplos

### Exemplo 1: Strangler Fig - Monolito para Microsserviços
```
Fase 1 (Mês 1-2): Autenticação
  Legado: /api/auth/* -> Monolito
  Novo:   /api/v2/auth/* -> Serviço Auth
  Proxy redireciona gradualmente (10% -> 50% -> 100%)

Fase 2 (Mês 3-4): Catálogo de Produtos
  Legado: /api/products/* -> Monolito
  Novo:   /api/v2/products/* -> Serviço Catálogo
  Dados migrados com reconciliação diária

Fase 3 (Mês 5-6): Pedidos
  (mais complexo, requer execução paralela)
```

### Exemplo 2: Migração de Banco de Dados
```
Origem: PostgreSQL 12 on-premise
Destino: PostgreSQL 16 na nuvem

Fase 1: Replicação contínua (CDC)
  - Configurar replicação lógica
  - Validar lag < 5 segundos

Fase 2: Leitura dupla
  - Aplicação lê de ambos, compara resultados
  - Discrepância < 0.01% por 7 dias

Fase 3: Cutover
  - Parar escrita no origem (janela de 15 min)
  - Drenar replicação
  - Apontar aplicação para destino
  - Rollback: reverter DNS em < 5 min
```

### Exemplo 3: Troca de Provedor de Pagamento
```
Provedor atual: Gateway A
Provedor novo: Gateway B

Semana 1-2: Implementar adaptador para Gateway B
Semana 3: Execução paralela (shadow mode)
  - Todas as transações processadas em A (real)
  - Duplicadas para B (simulação, sem cobrar)
  - Comparar: taxa de aprovação, tempo de resposta

Semana 4: Canary release (5% do tráfego real em B)
Semana 5: Incrementar para 50%
Semana 6: 100% em B, manter A como fallback por 30 dias
```
