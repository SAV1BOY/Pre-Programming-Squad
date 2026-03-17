# Checklist: Qualidade da Análise de Modos de Falha

## Propósito
Garantir que unhappy paths, edge cases, estratégias de rollback e degradação segura foram mapeados antes do código, não depois do incidente.

## Quando Usar
- Após definição de arquitetura e fluxos principais
- Antes de iniciar implementação
- Em revisões de resiliência e confiabilidade

---

## Checklist

### Unhappy Paths
- [ ] Falhas de input do usuário estão mapeadas (dados inválidos, formato errado)
- [ ] Falhas de autenticação e autorização estão mapeadas
- [ ] Falhas de comunicação entre serviços estão mapeadas (timeout, rede)
- [ ] Falhas de dependências externas estão mapeadas
- [ ] Falhas de infraestrutura estão consideradas (disco cheio, memória, CPU)

### Edge Cases
- [ ] Comportamento com dados vazios/nulos está definido
- [ ] Comportamento com volumes extremos (0, 1, máximo) está definido
- [ ] Concorrência e race conditions foram avaliadas
- [ ] Comportamento com dados duplicados está definido
- [ ] Timezone, encoding e caracteres especiais foram considerados

### Rollback
- [ ] Estratégia de rollback de deploy está definida
- [ ] Estratégia de rollback de dados/migração está definida
- [ ] Tempo estimado de rollback está calculado
- [ ] Rollback foi testado ou tem plano de teste
- [ ] Critérios para acionar rollback estão definidos (triggers)

### Degradação Segura
- [ ] Modos de degradação graceful estão definidos por dependência
- [ ] Funcionalidades que podem operar em modo degradado estão identificadas
- [ ] Funcionalidades que devem parar totalmente em caso de falha estão identificadas
- [ ] Comunicação ao usuário em modo degradado está definida
- [ ] Tempo máximo aceitável em modo degradado está definido

### Recuperação
- [ ] Procedimentos de recuperação pós-falha estão documentados
- [ ] Dados podem ser reconciliados após falha parcial
- [ ] Existe runbook para cenários de falha mais prováveis
- [ ] Alertas que acionam o processo de recuperação estão definidos
- [ ] Responsáveis por acionar recuperação estão designados

---

## Critérios de Aprovação
- **Mínimo**: Unhappy Paths e Rollback completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Nenhum unhappy path mapeado ou sem estratégia de rollback

## Sinais de Alerta (Red Flags)
- "Isso nunca vai acontecer" (falsa segurança)
- Apenas happy path documentado
- Rollback que depende de "refazer o deploy da versão anterior" sem mais detalhes
- Nenhum edge case identificado em sistema com dados de usuário
- Degradação que resulta em perda silenciosa de dados

## Agente Responsável
**Agente de Risk & Failure Analysis** — responsável por mapear e validar todos os modos de falha.
