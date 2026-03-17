# Checklist: Auditoria de Acoplamento e Coesão

## Propósito
Verificar se os módulos da solução têm alta coesão interna e baixo acoplamento entre si, facilitando manutenção, evolução e testabilidade.

## Quando Usar
- Ao revisar a decomposição modular da arquitetura
- Quando mudanças em um módulo requerem mudanças em vários outros
- Em code reviews arquiteturais antes da implementação

---

## Checklist

### Coesão (dentro do módulo)
- [ ] Cada módulo contém apenas funcionalidades fortemente relacionadas
- [ ] Dados e comportamentos relacionados estão no mesmo módulo
- [ ] Não há funcionalidades "órfãs" jogadas em módulos por conveniência
- [ ] O nome do módulo descreve precisamente o que ele faz
- [ ] Remover qualquer parte do módulo quebraria sua funcionalidade principal

### Acoplamento (entre módulos)
- [ ] Módulos se comunicam através de interfaces bem definidas, não implementações
- [ ] Mudança interna em um módulo não requer mudança em outros
- [ ] Número de dependências de cada módulo está mapeado e é razoável
- [ ] Dependências circulares não existem (A depende de B que depende de A)
- [ ] Acoplamento temporal está minimizado (A não precisa rodar antes de B por acaso)

### Tipos de Acoplamento Avaliados
- [ ] Acoplamento de dados: módulos compartilham apenas dados necessários
- [ ] Acoplamento de controle: nenhum módulo controla o fluxo interno de outro
- [ ] Acoplamento de conteúdo: nenhum módulo acessa dados internos de outro
- [ ] Acoplamento de stamp: estruturas de dados passadas são as mínimas necessárias
- [ ] Acoplamento por mensagem: preferido (interface limpa e mínima)

### Impacto de Mudanças
- [ ] Análise de impacto mostra que mudanças são localizadas (não cascateiam)
- [ ] Feature nova pode ser adicionada tocando poucos módulos
- [ ] Bug fix pode ser feito e deployado em módulo isolado
- [ ] Módulo pode ser substituído sem afetar o restante do sistema
- [ ] Teste de um módulo não requer setup de muitos outros

### Estratégias de Desacoplamento
- [ ] Eventos assíncronos são usados onde dependência temporal não é necessária
- [ ] Interfaces/contratos abstraem detalhes de implementação
- [ ] Inversão de dependência é aplicada onde necessário
- [ ] Shared kernel (se existir) é mínimo e versionado
- [ ] Anti-corruption layers protegem módulos de dependências instáveis

---

## Critérios de Aprovação
- **Mínimo**: Coesão e Acoplamento completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Dependências circulares ou módulos sem coesão clara

## Sinais de Alerta (Red Flags)
- Módulo "utils" ou "common" com centenas de funções não relacionadas
- Mudança em uma tabela requer deploy de 5 serviços
- Módulo A importa 80% do módulo B (deveria ser um só ou fronteira está errada)
- Circular dependency entre módulos
- Teste unitário que precisa de banco de dados e 3 mocks

## Agente Responsável
**Agente de Solution Architecture** — responsável por avaliar e otimizar acoplamento e coesão.
