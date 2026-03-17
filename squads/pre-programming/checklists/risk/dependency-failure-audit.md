# Checklist: Auditoria de Falha de Dependências

## Propósito
Avaliar o que acontece quando cada dependência externa falha, garantindo que o sistema se comporta de forma previsível e segura em cenários de indisponibilidade.

## Quando Usar
- Ao mapear integrações e dependências externas
- Antes de finalizar a arquitetura de resiliência
- Quando o sistema depende de serviços de terceiros críticos

---

## Checklist

### Mapeamento de Dependências
- [ ] Todas as dependências externas (APIs, SaaS, bancos, filas) estão listadas
- [ ] Criticidade de cada dependência está classificada (crítica, importante, nice-to-have)
- [ ] SLA real (não contratual) de cada dependência está conhecido
- [ ] Histórico de incidentes de cada dependência foi consultado
- [ ] Single points of failure estão identificados

### Cenários de Falha por Dependência
- [ ] Para cada dependência: comportamento quando está totalmente indisponível
- [ ] Para cada dependência: comportamento quando está lenta (alta latência)
- [ ] Para cada dependência: comportamento quando retorna erros
- [ ] Para cada dependência: comportamento quando retorna dados incorretos
- [ ] Para cada dependência: comportamento quando muda seu contrato sem aviso

### Estratégias de Resiliência
- [ ] Timeout está definido para cada dependência
- [ ] Retry com backoff exponencial está planejado onde faz sentido
- [ ] Circuit breaker está planejado para dependências com falha frequente
- [ ] Fallback está definido para cada dependência crítica
- [ ] Bulkhead está planejado para isolar falhas de dependências

### Degradação Graceful
- [ ] Funcionalidades que podem operar sem cada dependência estão definidas
- [ ] Modo degradado para cada cenário de falha está especificado
- [ ] Comunicação ao usuário em modo degradado está definida
- [ ] Dados em cache podem ser usados temporariamente quando a fonte está fora
- [ ] Filas/buffers absorvem picos quando dependência está lenta

### Testes de Resiliência
- [ ] Testes de falha de dependência estão planejados (chaos engineering lite)
- [ ] Cada cenário de fallback pode ser testado
- [ ] Ambiente para simular falha de dependência está disponível
- [ ] Testes de resiliência fazem parte do pipeline ou são executados periodicamente
- [ ] Resultados dos testes de resiliência geram ações de melhoria

---

## Critérios de Aprovação
- **Mínimo**: Mapeamento e Cenários de Falha completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Dependência crítica sem cenário de falha definido

## Sinais de Alerta (Red Flags)
- "Esse serviço nunca cai" (todos caem eventualmente)
- Nenhum timeout definido para chamadas externas
- Retry infinito sem backoff (pode derrubar a dependência quando ela voltar)
- Fallback que depende da mesma dependência que falhou
- Nenhum teste de cenário de falha

## Agente Responsável
**Agente de Risk & Failure Analysis** — responsável por mapear e validar resiliência contra falha de dependências.
