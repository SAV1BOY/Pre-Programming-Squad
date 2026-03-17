# Checklist: Prontidão de Testes de Carga e Performance

## Propósito
Garantir que critérios não-funcionais de performance são verificáveis, com cenários de carga definidos, ferramentas escolhidas e ambiente preparado.

## Quando Usar
- Quando há requisitos de performance definidos (latência, throughput)
- Antes de go-live de funcionalidades expostas a volume significativo
- Quando o sistema passará por crescimento esperado de carga

---

## Checklist

### Critérios de Performance
- [ ] Latência aceitável por operação está definida (p50, p95, p99)
- [ ] Throughput esperado está definido (req/s, transações/min)
- [ ] Tempo de resposta máximo aceitável está definido
- [ ] Uso máximo de recursos está definido (CPU, memória, conexões)
- [ ] Baseline de performance atual está documentada para comparação

### Cenários de Carga
- [ ] Carga normal (dia típico) está definida com perfil de uso
- [ ] Carga de pico (horário/evento) está definida
- [ ] Carga de estresse (além do esperado) está definida
- [ ] Rampa de carga (crescimento gradual) está definida
- [ ] Carga de endurance (estabilidade ao longo do tempo) está considerada

### Ferramenta e Infraestrutura
- [ ] Ferramenta de teste de carga está escolhida (k6, JMeter, Gatling, Locust)
- [ ] Scripts de teste de carga estão definidos (pelo menos os cenários principais)
- [ ] Ambiente dedicado para teste de carga está disponível
- [ ] Ambiente de teste tem capacidade similar à produção (ou proporcional)
- [ ] Monitoramento durante teste de carga está configurado

### Dados e Preparação
- [ ] Volume de dados no ambiente de teste é representativo
- [ ] Dados de teste para cenários de carga estão preparados
- [ ] Warmup do sistema antes do teste está planejado (cache, conexões)
- [ ] Dependências externas estão mockadas ou com capacidade para o teste
- [ ] Processo de execução e coleta de resultados está documentado

### Análise de Resultados
- [ ] Métricas que serão coletadas estão definidas
- [ ] Critérios de aprovação/reprovação estão definidos (limites aceitáveis)
- [ ] Processo de análise de gargalos está definido (profiling, tracing)
- [ ] Responsável por analisar resultados está designado
- [ ] Ações corretivas para performance insuficiente estão planejadas

---

## Critérios de Aprovação
- **Mínimo**: Critérios de Performance e Cenários de Carga completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Requisitos de performance sem cenário de teste ou sem ferramenta

## Sinais de Alerta (Red Flags)
- Teste de carga planejado para o dia antes do go-live
- "Vai aguentar" sem teste ou evidência
- Ambiente de teste com 1/100 da capacidade de produção
- Teste de carga sem monitoramento (rodou mas ninguém viu as métricas)
- Nenhum cenário de carga de pico definido

## Agente Responsável
**Agente de Test & Quality Design** — em colaboração com SRE/Infra para ambiente e análise.
