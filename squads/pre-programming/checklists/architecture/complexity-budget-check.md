# Checklist: Verificação de Budget de Complexidade

## Propósito
Avaliar se a complexidade da solução é justificada pelo valor entregue, identificando complexidade acidental que pode ser eliminada.

## Quando Usar
- Ao revisar a arquitetura proposta
- Quando a solução parece "complexa demais" mas não se sabe onde simplificar
- Antes de aprovar decisões que adicionam complexidade significativa

---

## Checklist

### Complexidade Essencial vs Acidental
- [ ] Complexidade essencial do domínio está identificada (inerente ao problema)
- [ ] Complexidade acidental está identificada (introduzida pela solução, não pelo problema)
- [ ] Para cada ponto de complexidade acidental, existe justificativa
- [ ] Alternativas mais simples foram avaliadas para cada complexidade acidental
- [ ] A relação complexidade/valor é aceitável para cada componente

### Fontes de Complexidade
- [ ] Número de tecnologias diferentes está justificado
- [ ] Número de serviços/módulos está justificado para o escopo
- [ ] Padrões arquiteturais usados são necessários (não apenas "best practice")
- [ ] Abstrações introduzidas resolvem problema real (não abstração prematura)
- [ ] Indireções na comunicação são necessárias (não são over-engineering)

### Simplicidade
- [ ] A solução mais simples que resolve o problema foi considerada
- [ ] YAGNI (You Ain't Gonna Need It) foi aplicado para features futuras especulativas
- [ ] Código/infra que "pode ser útil depois" foi removido do escopo
- [ ] Convenção sobre configuração foi preferida onde possível
- [ ] A solução pode ser explicada para um novo dev em 30 minutos

### Manutenibilidade
- [ ] Time atual consegue manter a solução sem suporte externo contínuo
- [ ] Novo membro do time consegue ser produtivo em tempo razoável
- [ ] Documentação necessária para operar a solução é proporcional
- [ ] Debugging é possível sem ferramentas especializadas exóticas
- [ ] A solução não depende de "pessoas-chave" únicas para funcionar

### Budget Consciente
- [ ] Complexidade total está proporcional ao tamanho do projeto
- [ ] Complexidade que gera valor futuro está identificada e justificada
- [ ] Complexidade removível está catalogada como dívida técnica consciente
- [ ] Existe consenso do time sobre o nível de complexidade aceitável
- [ ] Revisão periódica de complexidade está planejada

---

## Critérios de Aprovação
- **Mínimo**: Essencial vs Acidental e Fontes de Complexidade completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Complexidade acidental significativa sem justificativa

## Sinais de Alerta (Red Flags)
- "Usamos Kubernetes para 2 containers" (infra complexa para problema simples)
- Event sourcing + CQRS para CRUD simples
- 10 abstrações para um fluxo linear
- "Precisamos disso para escalar" sem evidência de que escala será necessária
- Ninguém do time consegue explicar a arquitetura completa

## Agente Responsável
**Agente de Solution Architecture** — responsável por garantir que complexidade é consciente e justificada.
