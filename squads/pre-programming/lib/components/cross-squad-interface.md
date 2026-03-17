# Cross-Squad Interface Component

## Propósito
Componente reutilizável para estruturar interfaces de comunicação entre o Pre-Programming Squad e outros squads do MMOS.

## Interface Padrão

### Input (do outro squad)
```yaml
source_squad: string
request_type: enum[input_request, review_request, handoff, escalation]
priority: enum[low, medium, high, critical]
deadline: date
context: text
artifacts: list[artifact]
```

### Output (para o outro squad)
```yaml
target_squad: string
response_type: enum[input_provided, review_complete, handoff_delivered, escalation_response]
status: enum[complete, partial, blocked]
artifacts: list[artifact]
notes: text
next_steps: list[action]
```

## Squads Integrados
- Coding Squad: handoff de pacote de implementação
- Design Squad: input de UX/UI e design system
- Data Squad: requisitos de dados e analytics
- Cybersecurity Squad: validação de segurança
- DeepResearch Squad: pesquisa de mercado e técnica
- C-Level Squad: aprovações e priorização estratégica
- Advisory Board Squad: consultoria especializada
- Traffic Squad: requisitos de performance e escala
- Storytelling Squad: comunicação e documentação externa
