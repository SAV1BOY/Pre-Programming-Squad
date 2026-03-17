# Checklist: Verificação de Prontidão para Implementação

## Propósito
Verificar se o time de desenvolvimento pode começar a implementar sem precisar adivinhar requisitos, decisões ou abordagens técnicas.

## Quando Usar
- Como gate final antes de iniciar a implementação
- Quando o time de dev pergunta "posso começar?"
- Quando há dúvida se a pré-programação está suficiente

---

## Checklist

### Clareza do Que Fazer
- [ ] Requisitos estão claros e sem ambiguidade para o time de dev
- [ ] Critérios de aceite por funcionalidade estão definidos
- [ ] Prioridade de implementação está definida (o que fazer primeiro)
- [ ] Definition of Done está acordada entre todos
- [ ] Exemplos concretos de comportamento esperado estão disponíveis

### Clareza de Como Fazer
- [ ] Arquitetura está definida e compreendida pelo time
- [ ] Contratos de API estão especificados
- [ ] Modelo de domínio está documentado
- [ ] Padrões e convenções de código estão definidos
- [ ] Decisões técnicas estão registradas com justificativa (ADRs)

### Recursos Disponíveis
- [ ] Time está alocado e disponível
- [ ] Ambiente de desenvolvimento está funcional
- [ ] Repositórios e pipelines estão configurados
- [ ] Acessos necessários estão provisionados
- [ ] Ferramentas de desenvolvimento estão padronizadas

### Dependências Resolvidas
- [ ] Dependências bloqueantes estão resolvidas ou têm workaround
- [ ] APIs de terceiros estão acessíveis (sandbox/staging)
- [ ] Bibliotecas e frameworks necessários estão disponíveis
- [ ] Aprovações pendentes que bloqueiam início foram obtidas
- [ ] Times dependentes estão alinhados com prazos

### Dúvidas Respondidas
- [ ] Sessão de walkthrough do handoff foi realizada com o time de dev
- [ ] Dúvidas levantadas pelo time de dev foram respondidas
- [ ] Canal de comunicação para dúvidas durante implementação está definido
- [ ] Responsável por responder dúvidas técnicas está identificado
- [ ] FAQ com dúvidas comuns está disponível

---

## Critérios de Aprovação
- **Mínimo**: Clareza do Que/Como e Dúvidas Respondidas completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Time não entende o que implementar ou como

## Sinais de Alerta (Red Flags)
- Time começa a implementar e tem que parar para esclarecer dúvidas básicas
- Dev implementa funcionalidade diferente do esperado por falta de clareza
- Ambiente de dev não funciona no primeiro dia
- "Acho que é assim, mas não tenho certeza" frequente durante implementação
- Nenhuma sessão de walkthrough entre pré-programming e dev

## Agente Responsável
**Agente de Final Review & Handoff** — responsável por verificar prontidão antes de liberar para implementação.
