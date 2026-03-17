# Checklist: Auditoria de Decomposição em Módulos

## Propósito
Verificar se a quebra da solução em módulos, serviços ou camadas está correta, com granularidade adequada e critérios claros de separação.

## Quando Usar
- Ao definir a estrutura de módulos/serviços da solução
- Quando há debate sobre "um serviço ou dois"
- Em revisões de arquitetura para validar a decomposição

---

## Checklist

### Critérios de Decomposição
- [ ] Critério de separação está explícito (por domínio, por capacidade, por time)
- [ ] Cada módulo tem coesão alta (faz coisas relacionadas)
- [ ] Acoplamento entre módulos é baixo (mudanças em um não cascateiam)
- [ ] Decomposição segue fronteiras de negócio, não fronteiras técnicas
- [ ] Cada módulo pode ser compreendido isoladamente

### Granularidade
- [ ] Módulos não são grandes demais (monolito disfarçado)
- [ ] Módulos não são pequenos demais (nano-serviços)
- [ ] A granularidade é adequada para o tamanho do time e do projeto
- [ ] Existe justificativa para cada separação (não é separação por separação)
- [ ] Custo operacional da granularidade escolhida é aceitável

### Serviços / Microsserviços
- [ ] Cada serviço tem razão de existir independente
- [ ] Comunicação entre serviços está definida (sync, async, events)
- [ ] Falha de um serviço não derruba todo o sistema (isolamento de falha)
- [ ] Cada serviço pode ser deployado independentemente
- [ ] Dados de cada serviço são encapsulados (não compartilham banco)

### Camadas
- [ ] Camadas da aplicação estão definidas (apresentação, negócio, dados)
- [ ] Direção de dependência entre camadas é clara (de cima para baixo)
- [ ] Camadas não pulam níveis (apresentação não acessa dados diretamente)
- [ ] Responsabilidade de cada camada é respeitada (sem lógica de negócio no controller)
- [ ] Interfaces entre camadas estão definidas

### Validação
- [ ] A decomposição suporta os fluxos principais sem complexidade excessiva
- [ ] A decomposição permite evolução independente dos módulos
- [ ] A decomposição não introduz distributed monolith (microsserviços acoplados)
- [ ] Performance não é comprometida pela decomposição (latência de rede)
- [ ] A decomposição foi validada com cenários reais de uso

---

## Critérios de Aprovação
- **Mínimo**: Critérios de Decomposição e Granularidade completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Decomposição sem critério ou granularidade inadequada

## Sinais de Alerta (Red Flags)
- Módulo com 20+ responsabilidades diferentes
- Serviço que não pode ser deployado sem redeployar outros 5
- Decomposição por camada técnica (service, repository, controller) em vez de domínio
- 50 microsserviços para um time de 3 pessoas
- Comunicação síncrona em cadeia entre 5+ serviços

## Agente Responsável
**Agente de Solution Architecture** — responsável por validar a decomposição modular.
