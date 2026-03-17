# Checklist: Qualidade da Prontidão de Ambiente

## Propósito
Garantir que ambientes, acessos, ferramentas, mocks e datasets necessários para implementação e teste estão disponíveis ou com plano de provisionamento antes do time começar.

## Quando Usar
- Antes do handoff para o time de implementação
- Ao planejar a infraestrutura de desenvolvimento e teste
- Quando o time reporta bloqueios por falta de ambiente ou acesso

---

## Checklist

### Ambientes
- [ ] Ambiente de desenvolvimento está configurado e funcional
- [ ] Ambiente de staging/homologação está disponível
- [ ] Ambiente de testes de integração está configurado
- [ ] Paridade entre ambientes está documentada (diferenças conhecidas)
- [ ] Processo de deploy para cada ambiente está definido

### Acessos
- [ ] Membros do time têm acesso aos repositórios necessários
- [ ] Acessos a bancos de dados de desenvolvimento estão provisionados
- [ ] Acessos a ferramentas de CI/CD estão configurados
- [ ] Acessos a serviços de terceiros (sandbox) estão disponíveis
- [ ] Acessos a ferramentas de monitoramento e logging estão provisionados

### Ferramentas
- [ ] Repositórios de código estão criados com branch strategy definida
- [ ] Pipeline de CI/CD está configurado (pelo menos build e lint)
- [ ] Ferramenta de gestão de tarefas está configurada com board/backlog
- [ ] Ferramentas de comunicação do time estão definidas
- [ ] IDE, linters e formatadores estão padronizados

### Mocks e Stubs
- [ ] Mocks de serviços externos estão disponíveis para desenvolvimento
- [ ] Stubs de APIs de terceiros estão configurados
- [ ] Mocks são realistas o suficiente para testar cenários reais
- [ ] Processo de atualização dos mocks está definido
- [ ] Ferramenta de mocking está escolhida e configurada (WireMock, etc.)

### Datasets
- [ ] Dados de teste estão disponíveis e representativos
- [ ] Dados de teste não contêm informações sensíveis reais (PII)
- [ ] Volume de dados de teste é adequado para cenários planejados
- [ ] Processo de reset/refresh de dados de teste está definido
- [ ] Dados para testes de carga estão preparados ou com plano de geração

---

## Critérios de Aprovação
- **Mínimo**: Ambientes e Acessos completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Ambiente de dev não funcional ou acessos críticos não provisionados

## Sinais de Alerta (Red Flags)
- Time começa a codar sem ambiente de desenvolvimento pronto
- Acessos sendo solicitados apenas quando são necessários (reativo)
- Testes de integração dependem de produção por falta de ambiente
- Dados de teste com PII real
- Nenhum mock disponível para dependências externas

## Agente Responsável
**Agente de Estimation & Planning** — em colaboração com DevOps/Infra para provisionamento.
