# Checklist: Completude do Pacote de Desenvolvimento

## Propósito
Verificar se todos os artefatos necessários para o time de implementação estão presentes, atualizados e suficientes para trabalhar sem bloqueios.

## Quando Usar
- Ao montar o pacote de handoff para desenvolvimento
- Como checklist final antes de entregar para o time
- Quando o time de dev reporta que "falta alguma coisa"

---

## Checklist

### Documentos de Contexto
- [ ] Visão do projeto com problema, objetivo e escopo está incluída
- [ ] Glossário de termos do domínio está disponível
- [ ] Stakeholders e suas expectativas estão documentados
- [ ] Histórico de decisões (ADRs) está acessível
- [ ] Premissas e suposições estão listadas com status

### Especificações Técnicas
- [ ] Diagrama de arquitetura atualizado está incluído
- [ ] Modelo de domínio com entidades e regras está documentado
- [ ] Contratos de API com schemas e exemplos estão completos
- [ ] Modelo de dados (schemas de banco) está especificado
- [ ] Fluxos principais estão diagramados

### Requisitos e Critérios
- [ ] Requisitos funcionais priorizados estão disponíveis
- [ ] Requisitos não-funcionais com valores mensuráveis estão incluídos
- [ ] Critérios de aceite por funcionalidade estão definidos
- [ ] Definition of Done está documentada
- [ ] Casos de teste críticos estão descritos

### Riscos e Mitigações
- [ ] Matriz de riscos está incluída com mitigações
- [ ] Modos de falha conhecidos estão documentados
- [ ] Estratégia de rollback está descrita
- [ ] Dependências com riscos estão destacadas
- [ ] Plano de contingência para riscos críticos está incluído

### Operacional
- [ ] Estratégia de testes está definida (que testes escrever)
- [ ] Requisitos de observabilidade estão especificados
- [ ] Estimativa de esforço com breakdown está incluída
- [ ] Cronograma com gates e dependências está disponível
- [ ] Contatos de pessoas-referência por assunto estão listados

---

## Critérios de Aprovação
- **Mínimo**: Especificações Técnicas e Requisitos completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Sem contratos de API ou sem modelo de dados em projeto que necessita

## Sinais de Alerta (Red Flags)
- Pacote com apenas tasks no Jira sem contexto
- Documentação desatualizada (não reflete decisões mais recentes)
- Artefatos em 5 ferramentas diferentes sem índice
- Nenhum diagrama visual (apenas texto)
- Pacote entregue sem walkthrough com o time

## Agente Responsável
**Agente de Final Review & Handoff** — responsável por montar e validar a completude do pacote.
