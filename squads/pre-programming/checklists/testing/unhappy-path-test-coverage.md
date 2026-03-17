# Checklist: Cobertura de Testes de Unhappy Path

## Propósito
Garantir que cenários de falha, erros e edge cases estão mapeados e terão testes antes do código, não depois do primeiro incidente.

## Quando Usar
- Ao planejar testes para cada funcionalidade
- Após mapeamento de modos de falha
- Quando o plano de testes cobre apenas happy paths

---

## Checklist

### Falhas de Input
- [ ] Campos obrigatórios ausentes estão testados
- [ ] Tipos de dados inválidos estão testados (string onde espera número, etc.)
- [ ] Valores extremos estão testados (0, negativo, máximo, overflow)
- [ ] Strings vazias, nulas e com caracteres especiais estão testadas
- [ ] Payloads malformados (JSON inválido, encoding errado) estão testados

### Falhas de Estado
- [ ] Operações em estados inválidos estão testadas (deletar item já deletado)
- [ ] Race conditions estão mapeadas e testadas
- [ ] Operações concorrentes no mesmo recurso estão testadas
- [ ] Transições de estado inválidas estão testadas
- [ ] Timeout durante operações de longa duração está testado

### Falhas de Integração
- [ ] Dependência indisponível (timeout, connection refused) está testada
- [ ] Dependência retorna erro (500, 503) está testada
- [ ] Dependência retorna dados inesperados está testada
- [ ] Dependência retorna dados parciais ou corrompidos está testada
- [ ] Latência excessiva de dependência está testada

### Falhas de Autorização
- [ ] Acesso sem autenticação está testado
- [ ] Acesso com token expirado está testado
- [ ] Acesso a recurso de outro usuário está testado
- [ ] Acesso com permissão insuficiente está testado
- [ ] Tentativa de escalação de privilégio está testada

### Edge Cases
- [ ] Lista vazia / primeiro item / último item estão testados
- [ ] Paginação no limite (última página, página inexistente) está testada
- [ ] Dados duplicados estão testados (idempotência)
- [ ] Operações simultâneas do mesmo usuário estão testadas
- [ ] Volumes extremos (payload grande, muitos itens) estão testados

---

## Critérios de Aprovação
- **Mínimo**: Falhas de Input e Falhas de Integração completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Nenhum cenário de falha mapeado para funcionalidade crítica

## Sinais de Alerta (Red Flags)
- Plano de teste com apenas happy paths
- "O frontend valida, então o backend não precisa" (defesa em profundidade ausente)
- Nenhum teste de timeout ou indisponibilidade de dependência
- "Isso nunca vai acontecer" como justificativa para não testar
- Testes de autorização ausentes em sistema multi-tenant

## Agente Responsável
**Agente de Test & Quality Design** — em colaboração com o **Agente de Risk & Failure Analysis**.
