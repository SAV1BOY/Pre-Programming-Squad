# Checklist: Qualidade do Design de Testes

## Propósito
Garantir que a estratégia de testes (unit, integration, e2e, contract, load) está definida antes do código, com cobertura adequada para os riscos identificados.

## Quando Usar
- Após definição de requisitos e arquitetura
- Antes de iniciar implementação (shift-left testing)
- Em revisões de estratégia de qualidade

---

## Checklist

### Testes Unitários
- [ ] Componentes/módulos que precisam de testes unitários estão identificados
- [ ] Regras de negócio críticas têm testes unitários planejados
- [ ] Casos de teste incluem happy path e edge cases
- [ ] Estratégia de mocking/stubbing está definida
- [ ] Meta de cobertura de código está estabelecida e é realista

### Testes de Integração
- [ ] Pontos de integração que precisam de teste estão mapeados
- [ ] Ambiente de teste de integração está planejado (containers, mocks, sandbox)
- [ ] Dados de teste para integração estão definidos
- [ ] Testes de integração cobrem cenários de falha das dependências
- [ ] Estratégia de isolamento entre testes está definida

### Testes End-to-End
- [ ] Fluxos críticos de usuário que precisam de teste e2e estão listados
- [ ] Ambiente para testes e2e está planejado
- [ ] Testes e2e são seletivos (não tentam cobrir tudo)
- [ ] Dados de teste para e2e estão definidos
- [ ] Estratégia para lidar com flakiness está definida

### Testes de Contrato
- [ ] Contratos entre serviços que precisam de teste estão identificados
- [ ] Ferramenta de contract testing está escolhida (Pact, etc.)
- [ ] Provider e consumer de cada contrato estão definidos
- [ ] Processo de atualização de contratos está definido
- [ ] Testes de contrato fazem parte do pipeline de CI

### Testes de Carga e Performance
- [ ] Cenários de carga estão definidos (normal, pico, estresse)
- [ ] Métricas de performance aceitáveis estão quantificadas
- [ ] Ferramenta de teste de carga está escolhida
- [ ] Ambiente para testes de carga está planejado (não em produção)
- [ ] Baseline de performance atual está documentada para comparação

---

## Critérios de Aprovação
- **Mínimo**: Unitários e Integração completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Nenhuma estratégia de teste definida antes da implementação

## Sinais de Alerta (Red Flags)
- "Vamos escrever testes depois" (nunca acontece)
- 100% de cobertura como meta (foco em métrica, não em qualidade)
- Testes e2e para tudo (pirâmide invertida)
- Nenhum teste de contrato para arquitetura de microsserviços
- Testes de carga planejados para uma semana antes do go-live

## Agente Responsável
**Agente de Test & Quality Design** — responsável por definir a estratégia de testes antes da implementação.
