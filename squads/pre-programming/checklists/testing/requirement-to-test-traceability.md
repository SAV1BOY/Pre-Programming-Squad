# Checklist: Rastreabilidade Requisito-Teste

## Propósito
Garantir que cada requisito gera pelo menos uma verificação, criando vínculo rastreável entre o que foi pedido e o que será testado.

## Quando Usar
- Após formalização de requisitos e antes de implementação
- Ao planejar a estratégia de testes
- Quando há dúvida se "tudo está coberto"

---

## Checklist

### Mapeamento
- [ ] Cada requisito funcional tem pelo menos um teste associado
- [ ] Cada requisito não-funcional tem pelo menos um critério de verificação
- [ ] Matriz de rastreabilidade requisito-teste está criada
- [ ] Requisitos sem teste associado estão identificados e justificados
- [ ] Testes sem requisito associado estão identificados (podem ser desnecessários)

### Cobertura Funcional
- [ ] Happy path de cada funcionalidade tem teste planejado
- [ ] Validações de input têm testes planejados
- [ ] Regras de negócio estão cobertas por testes
- [ ] Fluxos alternativos (branches) estão cobertos
- [ ] Cenários de autorização (quem pode fazer o quê) têm testes

### Cobertura Não-Funcional
- [ ] Requisitos de performance têm teste ou benchmark planejado
- [ ] Requisitos de segurança têm verificação planejada
- [ ] Requisitos de disponibilidade têm cenário de teste
- [ ] Requisitos de acessibilidade têm verificação definida
- [ ] Requisitos de compatibilidade (browsers, devices) têm escopo de teste

### Nível de Teste
- [ ] Cada requisito tem o nível de teste adequado definido (unit, integration, e2e)
- [ ] Requisitos de lógica de negócio são cobertos por testes unitários
- [ ] Requisitos de integração são cobertos por testes de integração
- [ ] Requisitos de fluxo de usuário são cobertos por testes e2e
- [ ] Requisitos de contrato são cobertos por testes de contrato

### Manutenção da Rastreabilidade
- [ ] Processo para atualizar a rastreabilidade quando requisitos mudam está definido
- [ ] Novos requisitos adicionados durante o projeto geram novos testes
- [ ] Requisitos removidos geram revisão/remoção de testes associados
- [ ] A rastreabilidade é revisada em cada gate/review
- [ ] Ferramenta ou formato para manter a rastreabilidade está definido

---

## Critérios de Aprovação
- **Mínimo**: Mapeamento e Cobertura Funcional completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Requisitos críticos sem nenhum teste associado

## Sinais de Alerta (Red Flags)
- Requisitos sem nenhum teste planejado
- Testes que não rastreiam para nenhum requisito (teste inútil?)
- Todos os testes são e2e (pirâmide invertida)
- Requisitos não-funcionais sem nenhuma verificação
- Rastreabilidade criada uma vez e nunca atualizada

## Agente Responsável
**Agente de Test & Quality Design** — responsável por garantir rastreabilidade requisito-teste.
