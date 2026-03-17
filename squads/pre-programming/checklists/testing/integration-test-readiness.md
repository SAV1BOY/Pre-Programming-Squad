# Checklist: Prontidão de Testes de Integração

## Propósito
Garantir que integrações críticas entre componentes, serviços e sistemas externos são testáveis de forma confiável e reproduzível.

## Quando Usar
- Ao planejar testes para fluxos que cruzam múltiplos componentes
- Quando a solução depende de serviços externos ou bancos de dados
- Antes de implementar integrações complexas

---

## Checklist

### Integrações Críticas
- [ ] Integrações que precisam de teste estão identificadas e priorizadas
- [ ] Fluxos end-to-end que cruzam múltiplos componentes estão mapeados
- [ ] Integrações com maior risco de falha estão priorizadas para teste
- [ ] Integrações com bancos de dados estão incluídas
- [ ] Integrações com filas/mensageria estão incluídas

### Ambiente de Teste
- [ ] Ambiente isolado para testes de integração está planejado
- [ ] Containers (Docker) para dependências locais estão definidos
- [ ] Sandbox de terceiros está disponível para teste
- [ ] Ambiente de teste é reproduzível (pode ser recriado do zero)
- [ ] Testes de integração não dependem de estado de outros testes

### Dados de Teste
- [ ] Dados de teste para cada integração estão definidos
- [ ] Setup e teardown de dados estão automatizados
- [ ] Dados sensíveis não são usados em testes (dados sintéticos)
- [ ] Volume de dados é representativo para os cenários testados
- [ ] Dados podem ser resetados entre execuções de teste

### Cenários de Teste
- [ ] Happy path da integração está coberto
- [ ] Timeout e lentidão da integração estão testados
- [ ] Erro/indisponibilidade da integração estão testados
- [ ] Dados inválidos/inesperados da integração estão testados
- [ ] Comportamento sob carga moderada está testado

### Execução e CI
- [ ] Testes de integração rodam no pipeline de CI
- [ ] Tempo de execução dos testes de integração é aceitável
- [ ] Testes são estáveis (não flaky)
- [ ] Falha em teste de integração é tratada (não ignorada)
- [ ] Resultados dos testes são visíveis para o time

---

## Critérios de Aprovação
- **Mínimo**: Integrações Críticas e Ambiente de Teste completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Integrações críticas sem ambiente de teste ou sem cenários definidos

## Sinais de Alerta (Red Flags)
- "Testamos integração manualmente antes do deploy" (não automatizado)
- Testes de integração que dependem de produção
- Testes flaky ignorados ("esse falha às vezes, é normal")
- Ambiente de teste compartilhado que quebra quando dois devs testam junto
- Nenhum teste de cenário de falha de integração

## Agente Responsável
**Agente de Test & Quality Design** — responsável por garantir testabilidade das integrações.
