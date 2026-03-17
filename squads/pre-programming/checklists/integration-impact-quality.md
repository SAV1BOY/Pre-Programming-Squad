# Checklist: Qualidade da Análise de Impacto de Integração

## Propósito
Mapear e avaliar todas as dependências, integrações com terceiros e contratos externos, garantindo que os limites e riscos de integração estão bem compreendidos.

## Quando Usar
- Quando a solução depende de sistemas externos ou de outros times
- Antes de finalizar a arquitetura que envolve integrações
- Ao avaliar impacto de mudanças em sistemas que outros consomem

---

## Checklist

### Dependências Internas
- [ ] Todos os sistemas internos que serão consumidos estão listados
- [ ] Todos os sistemas internos que consumirão a nova solução estão listados
- [ ] Times donos de cada dependência estão identificados
- [ ] SLAs internos das dependências estão conhecidos
- [ ] Capacidade atual das dependências suporta a nova carga esperada

### Dependências de Terceiros
- [ ] Todos os serviços externos (SaaS, APIs, vendors) estão listados
- [ ] Contratos e SLAs de terceiros estão documentados
- [ ] Limites de uso (rate limits, quotas, custos) estão mapeados
- [ ] Plano de contingência para indisponibilidade de terceiros existe
- [ ] Termos de uso e compliance de terceiros foram revisados

### Contratos Externos
- [ ] Contratos de API com sistemas externos estão documentados
- [ ] Formato de dados de entrada e saída está especificado
- [ ] Mecanismos de autenticação com terceiros estão definidos
- [ ] Processo de atualização/mudança de contrato está acordado
- [ ] Ambientes de sandbox/staging de terceiros estão disponíveis para teste

### Limites e Restrições
- [ ] Limites de latência da integração estão conhecidos e aceitáveis
- [ ] Limites de throughput da integração estão mapeados
- [ ] Janelas de manutenção de dependências estão identificadas
- [ ] Restrições geográficas (região, data residency) estão avaliadas
- [ ] Custos de integração (por chamada, mensalidade) estão estimados

### Resiliência
- [ ] Comportamento quando dependência está lenta está definido (timeout, circuit breaker)
- [ ] Comportamento quando dependência está fora está definido (fallback, degradação)
- [ ] Estratégia de retry está definida (com backoff, idempotência)
- [ ] Monitoramento de saúde das integrações está planejado
- [ ] Dados de teste para simular falhas de integração estão disponíveis

---

## Critérios de Aprovação
- **Mínimo**: Dependências Internas, Terceiros e Resiliência completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Dependências não mapeadas ou sem plano de contingência

## Sinais de Alerta (Red Flags)
- "Esse serviço nunca cai" (otimismo excessivo)
- Nenhum plano para quando terceiro estiver indisponível
- Integração sem ambiente de teste (só testa em produção)
- Custos de integração não estimados
- Time dono da dependência não foi notificado sobre o novo consumo

## Agente Responsável
**Agente de Solution Architecture** — em colaboração com o **Agente de Risk & Failure Analysis** para aspectos de resiliência.
