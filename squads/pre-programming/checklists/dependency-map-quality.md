# Checklist: Qualidade do Mapa de Dependências

## Propósito
Garantir que todas as dependências (técnicas, organizacionais e externas) estão mapeadas, com riscos e planos de mitigação, evitando surpresas durante a implementação.

## Quando Usar
- Após definição de escopo e arquitetura
- Antes de criar cronograma e estimativas
- Quando surgem bloqueios por dependências não mapeadas

---

## Checklist

### Dependências Técnicas
- [ ] Serviços internos dos quais a solução depende estão listados
- [ ] Bibliotecas e frameworks necessários estão identificados com versões
- [ ] Infraestrutura necessária está mapeada (servidores, bancos, filas, cache)
- [ ] Dependências de dados (schemas, migrações, seeds) estão identificadas
- [ ] Ordem de implementação considerando dependências técnicas está definida

### Dependências Organizacionais
- [ ] Times que precisam entregar algo antes ou em paralelo estão identificados
- [ ] Aprovações necessárias (segurança, arquitetura, compliance) estão listadas
- [ ] Dependências de decisões de negócio pendentes estão mapeadas
- [ ] Dependências de contratação ou alocação de pessoas estão identificadas
- [ ] SLAs de resposta de cada time dependente estão conhecidos

### Dependências Externas
- [ ] Vendors e fornecedores envolvidos estão listados
- [ ] Contratos com terceiros estão vigentes e adequados
- [ ] Prazos de entrega de terceiros estão mapeados
- [ ] Planos de contingência para atrasos de terceiros existem
- [ ] Canais de comunicação com terceiros estão estabelecidos

### Visualização e Rastreamento
- [ ] Mapa visual de dependências está criado (grafo, diagrama)
- [ ] Caminho crítico está identificado no mapa
- [ ] Dependências bloqueantes vs nice-to-have estão diferenciadas
- [ ] Status de cada dependência está sendo rastreado (pendente, resolvida, atrasada)
- [ ] Ferramenta de rastreamento está definida e em uso

### Mitigação
- [ ] Riscos associados a cada dependência estão avaliados
- [ ] Plano B para dependências de alto risco existe
- [ ] Dependências que podem ser paralelizadas estão identificadas
- [ ] Workarounds temporários estão planejados para dependências atrasadas
- [ ] Escalação para dependências bloqueadas está definida

---

## Critérios de Aprovação
- **Mínimo**: Todas as três categorias de dependências mapeadas
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Dependências bloqueantes sem owner ou sem plano de mitigação

## Sinais de Alerta (Red Flags)
- "Não temos dependências" em projeto que integra com outros sistemas
- Dependências mapeadas sem owner ou sem prazo
- Caminho crítico com dependência de time sem SLA
- Nenhum plano B para dependências de alto risco
- Mapa de dependências criado uma vez e nunca atualizado

## Agente Responsável
**Agente de Estimation & Planning** — responsável por mapear e rastrear dependências.
