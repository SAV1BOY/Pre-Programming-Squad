# Checklist: Prontidão da Definition of Done

## Propósito
Garantir que critérios de "pronto" estão definidos antes da implementação começar, evitando debates sobre completude durante o desenvolvimento.

## Quando Usar
- Antes de iniciar a implementação de qualquer funcionalidade
- Ao alinhar expectativas entre pré-programming e time de desenvolvimento
- Quando há histórico de divergência sobre o que é "pronto"

---

## Checklist

### Critérios Funcionais
- [ ] Funcionalidade implementa todos os requisitos definidos
- [ ] Happy path funciona conforme especificado
- [ ] Cenários de erro tratados conforme definido
- [ ] Validações de input implementadas
- [ ] Respostas de API seguem o contrato especificado

### Critérios de Qualidade
- [ ] Testes unitários escritos e passando
- [ ] Testes de integração escritos e passando (onde aplicável)
- [ ] Cobertura de testes atinge o mínimo definido
- [ ] Code review realizado e aprovado
- [ ] Sem warnings críticos no linting/análise estática

### Critérios de Operação
- [ ] Logs relevantes implementados nos pontos definidos
- [ ] Métricas de negócio instrumentadas
- [ ] Health check endpoint implementado (se aplicável)
- [ ] Configuração externalizada (sem hardcode de URLs, credenciais)
- [ ] Documentação de API atualizada (Swagger/OpenAPI)

### Critérios de Segurança
- [ ] Autenticação implementada conforme especificado
- [ ] Autorização implementada e testada
- [ ] Dados sensíveis protegidos (criptografia, mascaramento)
- [ ] Vulnerabilidades de dependências verificadas
- [ ] Input sanitizado contra injection

### Critérios de Deploy
- [ ] Feature pode ser deployada sem downtime
- [ ] Feature flag configurada (se necessário)
- [ ] Migração de dados testada e reversível
- [ ] Pipeline de CI/CD passa sem erros
- [ ] Documentação de deploy/runbook atualizada (se necessário)

### Acordo e Visibilidade
- [ ] Definition of Done está documentada e acessível a todo o time
- [ ] Time de desenvolvimento revisou e concordou com os critérios
- [ ] Critérios são realistas e atingíveis dentro das restrições
- [ ] Processo para exceções (quando algo não se aplica) está definido
- [ ] DoD é revisada periodicamente e atualizada quando necessário

---

## Critérios de Aprovação
- **Mínimo**: Critérios Funcionais, de Qualidade e Acordo completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Nenhuma Definition of Done definida antes de iniciar implementação

## Sinais de Alerta (Red Flags)
- "Pronto é quando funciona" (sem critérios de qualidade)
- DoD que ninguém lê ou segue
- DoD com 50 itens (impraticável)
- DoD sem critérios de teste (qualidade opcional)
- DoD diferente para cada dev do time (inconsistência)

## Agente Responsável
**Agente de Test & Quality Design** — em colaboração com o **Agente de Final Review & Handoff**.
