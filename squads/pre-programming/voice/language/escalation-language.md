# Linguagem de Escalonamento

## Propósito

Comunicar escalonamentos de forma clara, estruturada e sem carga emocional. O escalonamento é uma ferramenta legítima de gestão — não um sinal de falha. A linguagem de escalonamento garante que o nível correto de decisão receba a informação necessária para agir, com contexto suficiente e urgência calibrada.

## Palavras-chave

`escalonamento`, `nível de decisão`, `bloqueio`, `urgência`, `impacto`, `ação necessária`, `owner`, `prazo`, `tentativas anteriores`, `recomendação`

## Frases Modelo

### Declaração de Escalonamento

- "Escalono [assunto] para [nível/pessoa] porque [motivo: excede autonomia do squad / bloqueio cross-team / impacto acima do threshold / prazo em risco]."
- "Tentativas anteriores de resolução: [lista do que já foi feito]. Resultado: [insuficiente porque X]."
- "A decisão necessária é [descrição específica], de [quem], até [quando]. Sem essa decisão, o impacto é [consequência]."

### Níveis de Urgência

- **Urgência crítica:** "Bloqueio imediato. Impacto em produção/receita/segurança agora. Necessário: [ação] de [quem] em [horas]."
- **Urgência alta:** "Bloqueio que afetará entrega em [prazo]. Necessário: [decisão/recurso] de [quem] até [data]. Sem resolução, [consequência]."
- **Urgência média:** "Risco identificado que pode se tornar bloqueio em [prazo]. Necessário: [alinhamento/priorização] com [quem] até [data]."
- **Urgência informativa:** "Sinalizando [situação] que pode requerer ação futura. Nenhuma ação imediata necessária. Próximo check-in: [data]."

### Estrutura de Escalonamento

- "**O quê:** [situação em 1-2 frases]. **Por quê escalo:** [motivo]. **O que já fizemos:** [ações]. **O que precisamos:** [ação específica de quem até quando]. **Se não resolvido:** [consequência]."
- "Solicito [decisão/recurso/priorização] de [nível]. O squad esgotou as opções dentro da sua autonomia: [lista]. A decisão requer [autoridade/visibilidade/recurso] que está fora do nosso escopo."

### Frases de Desescalonamento

- "O escalonamento de [assunto] está resolvido. Resolução: [o que foi feito]. Impacto residual: [se houver]. Ações preventivas: [para evitar recorrência]."
- "Rebaixo a urgência de [crítica] para [média] porque [mudança de situação]. Novo prazo para resolução: [data]."

## Anti-Padrões Linguísticos

### 1. Escalonamento Emocional
**Errado:** "Ninguém está nos ajudando! O time de infra não responde e estamos desesperados."
**Correto:** "O squad está bloqueado desde segunda por dependência do time de infra (ticket INFRA-789). Tentativas de contato: Slack (seg 10h), email (seg 15h), reunião (terça cancelada por eles). Impacto: entrega de [projeto X] atrasará 3 dias por dia de bloqueio. Solicito mediação do EM para priorização."

### 2. Escalonamento sem Tentativa Prévia
**Errado:** "O time de dados não fez o que pedimos. Escalando para o diretor."
**Correto:** "Antes de escalonar, as seguintes tentativas foram feitas: (1) pedido direto ao tech lead em [data], (2) alinhamento em weekly cross-team em [data], (3) proposta de priorização compartilhada em [data]. Nenhuma resultou em comprometimento. Escalono para [nível] com recomendação de [ação]."

### 3. Escalonamento Vago
**Errado:** "Temos um problema com o projeto."
**Correto:** "O projeto [nome] está em risco de atrasar 2 semanas. Causa: [específica]. Decisão necessária: [aprovação de horas extras / repriorização de escopo / alocação de recurso adicional]. Prazo para decisão: [data]."

### 4. Escalonamento sem Recomendação
**Errado:** "O que vocês acham que devemos fazer?"
**Correto:** "Recomendamos [opção A] por [razão]. Alternativa: [opção B] com [trade-off]. Solicito aprovação de [quem] para prosseguir com [opção recomendada]."

### 5. Sobre-escalonamento
**Errado:** *Levar ao VP uma decisão que o tech lead pode resolver.*
**Correto:** Antes de escalonar, perguntar: "Essa decisão pode ser tomada no meu nível? No nível do meu lead? Precisa de alguém acima?" Escalonar para o nível mínimo necessário.

### 6. Escalonamento como Punição
**Errado:** "Vou escalar porque o time X não coopera."
**Correto:** "Escalono para alinhar prioridades entre squads, pois os objetivos [nosso: X] e [deles: Y] estão em conflito para o recurso Z. Recomendo: [proposta de resolução]."
