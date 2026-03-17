# Checklist: Auditoria Final de Go/No-Go

## Propósito
Gate final e formal que consolida todas as verificações anteriores para liberar ou bloquear o início da implementação, garantindo que nada crítico foi esquecido.

## Quando Usar
- Como último checkpoint antes de autorizar a implementação
- Após todos os outros checklists relevantes terem sido aplicados
- Quando é necessária decisão formal de Go/No-Go

---

## Checklist

### Discovery e Problema
- [ ] Problema está claro, validado e fundamentado em dados
- [ ] Causa raiz está identificada (não apenas sintoma)
- [ ] Critérios de sucesso estão definidos e mensuráveis
- [ ] Stakeholders estão alinhados sobre problema e expectativas
- [ ] Suposições críticas foram validadas ou têm plano de validação

### Requisitos e Escopo
- [ ] Requisitos estão completos, claros e sem ambiguidade bloqueante
- [ ] MVP está definido com fronteiras claras
- [ ] Priorização está feita e aceita por Product e Engineering
- [ ] Perguntas em aberto bloqueantes estão resolvidas
- [ ] Escopo está protegido com processo de change management

### Solução e Arquitetura
- [ ] Solução escolhida tem justificativa documentada
- [ ] Arquitetura está desenhada e compreendida pelo time de dev
- [ ] Contratos de API estão completos
- [ ] Modelo de domínio está validado
- [ ] Decisões arquiteturais estão registradas como ADRs

### Riscos e Mitigações
- [ ] Riscos críticos estão mapeados com mitigações definidas
- [ ] Modos de falha estão identificados com fallback
- [ ] Estratégia de rollback existe e é viável
- [ ] Segurança foi avaliada (auth, dados sensíveis, misuse)
- [ ] Performance e escalabilidade estão planejadas

### Qualidade e Testes
- [ ] Estratégia de testes está definida por nível
- [ ] Definition of Done está clara e acordada
- [ ] Testabilidade da arquitetura foi validada
- [ ] Rastreabilidade requisito-teste existe
- [ ] Critérios de aceite estão definidos por funcionalidade

### Operação e Handoff
- [ ] Observabilidade está planejada (logs, métricas, alertas)
- [ ] Pacote de handoff está completo e atualizado
- [ ] Walkthrough com time de dev foi realizado
- [ ] Ambiente e acessos estão provisionados
- [ ] Estimativa e timeline estão definidas com gates

### Pessoas e Processo
- [ ] Time de implementação está alocado e disponível
- [ ] Owners para cada aspecto do projeto estão definidos
- [ ] Processo de comunicação durante implementação está definido
- [ ] Dependências de outros times estão alinhadas
- [ ] Sponsor do projeto confirma o Go

---

## Critérios de Aprovação

### Go
- Todos os itens marcados, ou exceções documentadas e aceitas pelo sponsor
- Nenhum bloqueante aberto
- Time de dev confirma que pode começar

### No-Go Condicional
- Até 3 itens não-bloqueantes pendentes com plano de resolução em 48h
- Time pode iniciar partes que não dependem dos itens pendentes
- Revisão de follow-up agendada

### No-Go
- Qualquer item bloqueante não resolvido
- Time de dev não entende o que implementar
- Riscos críticos sem mitigação
- Stakeholders desalinhados sobre escopo ou prioridades

## Sinais de Alerta (Red Flags)
- Pressão para dar "Go" ignorando bloqueantes
- "Vamos descobrir durante a implementação" para questões estruturais
- Nenhum risco identificado (análise insuficiente, não projeto perfeito)
- Handoff sem walkthrough ("leia o documento")
- Sponsor não revisou ou não aprovou
- Time de dev não participou de nenhum momento do pré-programming

## Agente Responsável
**Agente de Final Review & Handoff** — responsável por conduzir a auditoria final e emitir recomendação de Go/No-Go.
