# Padrões de Observabilidade

## Nome do Padrão
Padrões de Planejamento de Observabilidade

## Problema que Resolve
Sistemas em produção frequentemente falham de formas imprevisíveis. Sem observabilidade planejada desde a pré-programação, as equipes enfrentam: investigação lenta de incidentes, métricas insuficientes para decisões, falta de visibilidade em fluxos distribuídos e incapacidade de detectar degradação antes que afete usuários.

## Solução

### 1. Três Pilares da Observabilidade
Planejar desde o início a coleta de logs estruturados, métricas dimensionais e traces distribuídos como parte integral da arquitetura.

**Aplicação prática:**
- **Logs:** Definir formato estruturado (JSON), níveis, campos obrigatórios (correlation_id, timestamp, service)
- **Métricas:** Definir métricas RED (Rate, Errors, Duration) para cada serviço
- **Traces:** Planejar propagação de contexto entre serviços

### 2. SLI/SLO/SLA desde o Planejamento
Definir indicadores de nível de serviço (SLIs), objetivos (SLOs) e acordos (SLAs) antes do desenvolvimento, orientando decisões arquiteturais.

**Aplicação prática:**
- Definir 3-5 SLIs principais (latência, disponibilidade, taxa de erro)
- Estabelecer SLOs realistas baseados em requisitos do negócio
- Calcular error budget e definir políticas de uso
- Criar alertas baseados em burn rate do error budget

### 3. Dashboards por Camada
Planejar dashboards em camadas progressivas: negócio, serviço, infraestrutura.

**Aplicação prática:**
- **Dashboard de Negócio:** KPIs de produto (conversão, receita, engajamento)
- **Dashboard de Serviço:** Saúde de cada serviço (RED metrics)
- **Dashboard de Infraestrutura:** Recursos (CPU, memória, disco, rede)
- Criar runbook vinculado a cada alerta

### 4. Observabilidade como Código
Definir dashboards, alertas e configurações de monitoramento como código versionado, não como configuração manual.

**Aplicação prática:**
- Dashboards definidos em Terraform/Pulumi ou YAML
- Alertas versionados junto com o código do serviço
- Revisão de observabilidade no code review
- Testes de alertas no pipeline de CI/CD

## Quando Usar

- Em todo projeto que irá para produção
- Especialmente em arquiteturas distribuídas (microsserviços)
- Quando há SLAs contratuais com clientes
- Em sistemas com alta criticidade de negócio
- Quando múltiplas equipes compartilham infraestrutura

## Quando NÃO Usar

- Em protótipos descartáveis que não irão a produção
- Em ferramentas internas de uso esporádico sem criticidade
- Quando logging básico do framework é suficiente (scripts batch simples)

## Exemplos

### Exemplo 1: Métricas RED para API de Pedidos
```
Rate (Taxa):
  - pedidos_criados_total (counter)
  - pedidos_por_status (counter com label status)

Errors (Erros):
  - pedidos_erro_total (counter com label tipo_erro)
  - pedidos_erro_percentual (gauge, calculado)

Duration (Duração):
  - pedido_criacao_duracao_segundos (histogram, buckets: 0.1, 0.5, 1, 2, 5)
  - pedido_processamento_duracao_segundos (histogram)

Alertas:
  - Taxa de erro > 1% por 5 minutos -> P2
  - Latência p99 > 2s por 10 minutos -> P3
  - Taxa de pedidos cai > 50% vs. média -> P1
```

### Exemplo 2: SLOs para Serviço de Autenticação
```
SLI: Disponibilidade
  Definição: % de requisições com status < 500
  SLO: 99.95% em janela de 30 dias
  Error budget: 21.6 minutos/mês

SLI: Latência
  Definição: Tempo de resposta p99
  SLO: p99 < 200ms
  Medição: histograma no gateway

SLI: Correção
  Definição: % de logins válidos que retornam token
  SLO: 99.99%

Política de error budget:
  - Budget > 50%: desenvolvimento normal
  - Budget 20-50%: foco em estabilidade
  - Budget < 20%: congelamento de features
```

### Exemplo 3: Logging Estruturado
```json
{
  "timestamp": "2025-03-15T10:30:00Z",
  "level": "INFO",
  "service": "order-service",
  "trace_id": "abc123def456",
  "span_id": "789ghi",
  "user_id": "usr_12345",
  "action": "create_order",
  "order_id": "ord_67890",
  "duration_ms": 145,
  "status": "success",
  "metadata": {
    "items_count": 3,
    "total_value": 299.90,
    "payment_method": "credit_card"
  }
}
```
