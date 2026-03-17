# Checklist: Auditoria de Testabilidade

## Propósito
Verificar se a arquitetura proposta é testável, identificando pontos que dificultam a escrita de testes e propondo ajustes antes da implementação.

## Quando Usar
- Ao revisar a arquitetura com foco em qualidade
- Quando o time reporta dificuldade para escrever testes
- Antes de aprovar a arquitetura para implementação

---

## Checklist

### Isolamento
- [ ] Componentes podem ser testados isoladamente (sem subir todo o sistema)
- [ ] Dependências externas podem ser substituídas por mocks/stubs
- [ ] Banco de dados pode ser substituído por implementação em memória para testes
- [ ] Serviços externos podem ser simulados localmente
- [ ] Efeitos colaterais (envio de email, escrita em fila) podem ser interceptados

### Injeção de Dependências
- [ ] Dependências são injetadas, não instanciadas internamente
- [ ] Interfaces são usadas para dependências externas (não classes concretas)
- [ ] Configuração é externalizada (não hardcoded)
- [ ] Componentes não dependem de estado global ou singleton mutável
- [ ] Factories ou builders são usados para construção de objetos complexos

### Observabilidade para Testes
- [ ] Estado interno relevante é acessível para asserções
- [ ] Eventos ou callbacks permitem verificar comportamento assíncrono
- [ ] Logs são estruturados e podem ser assertados em testes
- [ ] Erros retornam informação suficiente para diagnóstico
- [ ] Operações assíncronas têm mecanismo de await para testes

### Design Testável
- [ ] Funções têm responsabilidade única (fáceis de testar isoladamente)
- [ ] Lógica de negócio está separada de I/O (leitura/escrita de dados)
- [ ] Side effects estão isolados nas bordas do sistema (hexagonal, clean architecture)
- [ ] Comportamento dependente de tempo usa abstração de relógio (Clock)
- [ ] Geração de IDs e valores aleatórios usa abstração injetável

### Infraestrutura de Teste
- [ ] Framework de teste está escolhido e configurado
- [ ] Padrões de teste estão definidos (naming, structure, assertions)
- [ ] Utilities de teste compartilhadas estão planejadas (factories, fixtures)
- [ ] Execução de testes está integrada ao CI/CD
- [ ] Cobertura de código é medida e reportada

---

## Critérios de Aprovação
- **Mínimo**: Isolamento e Injeção de Dependências completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Componentes que não podem ser testados isoladamente

## Sinais de Alerta (Red Flags)
- "Para testar precisa subir o sistema inteiro"
- Dependências hardcoded sem possibilidade de mock
- Lógica de negócio misturada com acesso a banco de dados
- Testes que dependem de hora do dia ou timezone
- "Não dá pra testar isso" (provavelmente é problema de design)

## Agente Responsável
**Agente de Test & Quality Design** — em colaboração com o **Agente de Solution Architecture**.
