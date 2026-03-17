# Checklist: Verificação de Blast Radius

## Propósito
Mapear o que quebra se algo der errado, dimensionando o impacto máximo de uma falha e planejando contenção antes que o problema aconteça.

## Quando Usar
- Antes de qualquer mudança que toque sistemas em produção
- Ao avaliar risco de novas funcionalidades
- Quando a mudança afeta componentes compartilhados

---

## Checklist

### Mapeamento de Impacto
- [ ] Componentes diretamente afetados pela mudança estão listados
- [ ] Componentes indiretamente afetados (efeito cascata) estão mapeados
- [ ] Número de usuários potencialmente impactados está estimado
- [ ] Funcionalidades que podem parar de funcionar estão listadas
- [ ] Sistemas downstream que podem ser afetados estão identificados

### Dimensionamento
- [ ] Impacto financeiro máximo de uma falha está estimado (receita/hora)
- [ ] Impacto reputacional está avaliado (cliente-facing vs interno)
- [ ] Impacto em SLAs está avaliado (pode violar acordos?)
- [ ] Impacto em dados está avaliado (perda, corrupção, inconsistência)
- [ ] Impacto operacional está avaliado (carga no suporte, war room)

### Contenção
- [ ] Feature flags estão planejadas para limitar blast radius
- [ ] Rollout gradual (canary, blue-green) está definido
- [ ] Circuit breakers estão planejados para isolar falhas
- [ ] Segmentação de usuários/tráfego está definida para rollout
- [ ] Ponto de corte (% de erro que aciona rollback) está definido

### Isolamento
- [ ] Falha no componente novo não derruba componentes existentes
- [ ] Dados de outros módulos estão protegidos em caso de falha
- [ ] Integração com sistemas críticos tem fallback
- [ ] Erros são contidos no módulo de origem (não propagam)
- [ ] Timeouts e bulkheads estão planejados

### Cenários de Pior Caso
- [ ] Cenário de pior caso realista está descrito
- [ ] Plano de resposta para o pior caso existe
- [ ] Tempo de recuperação para o pior caso está estimado
- [ ] Comunicação de crise para o pior caso está preparada
- [ ] Lições de incidentes anteriores similares foram consideradas

---

## Critérios de Aprovação
- **Mínimo**: Mapeamento de Impacto e Contenção completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Blast radius desconhecido ou sem estratégia de contenção

## Sinais de Alerta (Red Flags)
- "Essa mudança é pequena, não vai dar problema" (famosas últimas palavras)
- Mudança em componente compartilhado sem avaliar consumidores
- Rollout 100% no primeiro deploy (sem canary ou gradual)
- Nenhum circuit breaker em serviço que depende de terceiros
- Pior caso nunca discutido ("não precisa ser pessimista")

## Agente Responsável
**Agente de Risk & Failure Analysis** — responsável por mapear e dimensionar blast radius.
