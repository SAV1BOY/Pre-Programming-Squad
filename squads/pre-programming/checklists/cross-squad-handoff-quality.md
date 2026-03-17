# Checklist: Qualidade do Handoff Cross-Squad

## Propósito
Garantir que o handoff com Product, Design, Data, Cyber e C-Level está completo, com artefatos adequados para cada audiência e acordos claros de responsabilidade.

## Quando Usar
- Ao entregar artefatos para outros squads ou áreas
- Quando o projeto requer colaboração multi-squad
- Em transições de fase que envolvem outros times

---

## Checklist

### Handoff para Product
- [ ] Requisitos priorizados estão alinhados com o roadmap de produto
- [ ] Trade-offs de escopo foram discutidos e aceitos pelo Product Owner
- [ ] Métricas de sucesso estão acordadas entre Engineering e Product
- [ ] MVP está validado por Product como viável do ponto de vista de negócio
- [ ] Backlog pós-MVP está compartilhado e priorizado

### Handoff para Design
- [ ] Restrições técnicas que afetam UX foram comunicadas
- [ ] Requisitos de acessibilidade estão alinhados
- [ ] Fluxos técnicos que impactam a experiência estão documentados
- [ ] Limitações de performance que afetam interações estão compartilhadas
- [ ] Estados de erro e loading estão especificados para Design

### Handoff para Data
- [ ] Eventos e métricas que precisam de tracking estão listados
- [ ] Schema de dados para analytics está definido
- [ ] Requisitos de data quality estão especificados
- [ ] Pipelines de dados necessários estão mapeados
- [ ] Privacidade e compliance de dados estão alinhados com o time de Data

### Handoff para Cyber Security
- [ ] Threat model foi compartilhado ou revisado com Cyber
- [ ] Requisitos de segurança estão documentados e validados
- [ ] Plano de pen testing está acordado
- [ ] Compliance requirements estão mapeados e aceitos
- [ ] Processo de vulnerability disclosure está definido

### Handoff para C-Level / Liderança
- [ ] Executive summary do projeto está preparado (1 página)
- [ ] Riscos principais estão comunicados em linguagem de negócio
- [ ] Timeline com marcos está compartilhada
- [ ] Investimento necessário (time, infra, ferramentas) está apresentado
- [ ] Decisões que requerem aprovação executiva estão identificadas

### Acordos de Responsabilidade
- [ ] RACI (Responsible, Accountable, Consulted, Informed) está definido
- [ ] Pontos de contato por squad estão identificados
- [ ] Cadência de sync entre squads está definida
- [ ] Processo de escalação cross-squad está acordado
- [ ] SLAs de resposta entre squads estão estabelecidos

---

## Critérios de Aprovação
- **Mínimo**: Handoffs relevantes ao projeto e Acordos de Responsabilidade completos
- **Recomendado**: Todos os itens aplicáveis marcados
- **Bloqueante**: RACI não definido ou squad crítico não comunicado

## Sinais de Alerta (Red Flags)
- Handoff é um email com documento anexo sem walkthrough
- Squad afetado descobre mudanças quando já estão em produção
- Nenhum ponto de contato definido ("fala com o time de X")
- C-Level descobre problemas pelo canal de incidentes, não proativamente
- Design e Engineering com versões diferentes do escopo

## Agente Responsável
**Agente de Final Review & Handoff** — responsável por coordenar handoffs com todos os squads envolvidos.
