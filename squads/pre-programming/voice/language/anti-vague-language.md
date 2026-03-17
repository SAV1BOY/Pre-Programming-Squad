# Linguagem Anti-Vagueza

## Propósito

Eliminar ambiguidade e imprecisão na comunicação técnica do squad. Cada afirmação deve ser específica, mensurável e verificável. Vagueza em documentação pré-programação propaga incerteza para o time de implementação, gerando retrabalho, decisões inconsistentes e estimativas incorretas.

## Palavras-chave

`específico`, `mensurável`, `verificável`, `quantificado`, `concreto`, `rastreável`, `definido`, `delimitado`, `exemplificado`, `evidenciado`

## Frases Modelo

### Substituições Obrigatórias

| Vago (proibido) | Específico (usar) |
|---|---|
| "Melhorar a performance" | "Reduzir latência p99 de 1.2s para 400ms no endpoint /checkout" |
| "Vários usuários afetados" | "~15.000 usuários (23% da base ativa) afetados entre 14h e 16h" |
| "Em breve" | "Até 15/março" ou "em 5 dias úteis" |
| "Sistema lento" | "Tempo de resposta acima do SLA de 500ms em 35% dos requests" |
| "Impacto significativo" | "Queda de 12% na taxa de conversão do checkout" |
| "Grande volume" | "~2M de eventos/dia, com pico de 500 eventos/segundo às 20h" |
| "Alguns problemas" | "3 problemas identificados: [listar]" |
| "Quase pronto" | "7 de 9 critérios de aceitação atendidos; faltam X e Y" |
| "Complexo" | "Envolve 4 serviços, 2 bancos de dados e integração com parceiro externo" |
| "Boas práticas" | "Conforme padrão X definido em [referência], especificamente: A, B, C" |

### Frases de Precisão

- "O impacto medido é [número] em [métrica], afetando [quem] durante [período]."
- "A causa raiz identificada é [X], confirmada por [evidência Y]."
- "O escopo inclui [lista explícita] e exclui [lista explícita]."
- "A estimativa é de [N] dias, com margem de [M] dias para [risco específico]."
- "O critério de sucesso é [métrica] atingindo [valor] medido por [ferramenta] no período [janela]."

### Frases de Delimitação

- "Quando digo [termo], refiro-me especificamente a [definição precisa]."
- "Esse número considera [premissas] e não considera [exclusões]."
- "Válido para o cenário de [contexto]; em [outro contexto], o comportamento é [diferente]."

## Anti-Padrões Linguísticos

### 1. Adjetivos sem Escala
**Errado:** "O sistema está instável."
**Correto:** "O sistema apresentou 12 erros 5xx nas últimas 2 horas, contra baseline de 0-2 por hora."

### 2. Pronomes Ambíguos
**Errado:** "Isso precisa ser resolvido antes daquilo."
**Correto:** "O bug de autenticação (JIRA-1234) precisa ser resolvido antes da migração de banco (JIRA-1235)."

### 3. Quantificadores Indefinidos
**Errado:** "Muitos clientes reclamaram."
**Correto:** "47 tickets abertos no Zendesk na última semana sobre timeout no checkout."

### 4. Prazos Elásticos
**Errado:** "Deve ficar pronto nas próximas semanas."
**Correto:** "Estimativa de conclusão: 22/março. Risco de atraso de até 5 dias se integração com parceiro X atrasar."

### 5. Causalidade Implícita
**Errado:** "O deploy causou o problema."
**Correto:** "O deploy das 14h (commit abc123) introduziu query N+1 que saturou o connection pool; confirmado por correlação temporal no APM e reproduzido em staging."

### 6. Escopo Aberto
**Errado:** "Precisamos melhorar a segurança."
**Correto:** "Precisamos implementar: (1) rate limiting no endpoint de login, (2) rotação automática de secrets, (3) scan de dependências no CI. Priorizados nessa ordem."
