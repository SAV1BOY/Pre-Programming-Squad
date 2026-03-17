# Linguagem de Decisão

## Propósito

Estruturar e comunicar decisões técnicas com clareza sobre o quê foi decidido, por quem, com base em quê, e quais as consequências. Toda decisão do squad deve ser rastreável, contestável e revisável. A linguagem de decisão elimina ambiguidade sobre o estado de uma decisão (proposta, aprovada, implementada, revisada).

## Palavras-chave

`decisão registrada`, `contexto da decisão`, `alternativas avaliadas`, `critério de decisão`, `consequências aceitas`, `reversibilidade`, `validade`, `owner da decisão`, `data de revisão`, `status da decisão`

## Frases Modelo

### Status de Decisão

- "Decisão **proposta**: [descrição]. Aguardando revisão de [quem] até [data]."
- "Decisão **aprovada**: [descrição]. Aprovada por [quem] em [data] com base em [evidência/critério]."
- "Decisão **implementada**: [descrição]. Em produção desde [data]. Métricas de validação: [lista]."
- "Decisão **revisada**: [descrição original] reavaliada em [data]. Nova decisão: [atualização]. Motivo da revisão: [mudança de contexto]."
- "Decisão **revertida**: [descrição original] revertida em [data]. Motivo: [evidência que invalidou a premissa original]."

### Estrutura de Decisão

- "A decisão é [ação]. O contexto é [situação]. As alternativas avaliadas foram [lista]. O critério determinante foi [fator]. As consequências aceitas são [lista]."
- "Decidimos [X] e não [Y] porque [razão principal]. Se [condição] mudar, devemos reconsiderar."
- "Esta decisão é válida enquanto [premissa] se mantiver. Gatilho de revisão: [evento ou data]."

### Frases de Delegação de Decisão

- "Esta decisão está dentro da autonomia de [papel/pessoa]. Não requer aprovação adicional."
- "Esta decisão requer alinhamento de [stakeholders] porque afeta [escopo cross-team]."
- "Escalo esta decisão para [nível] porque [impacto excede autonomia do squad / envolve orçamento acima de X / afeta SLA contratual]."

### Frases de Decisão sob Incerteza

- "Decidimos [X] com informação parcial. Se a premissa [Y] for invalidada, o plano B é [Z] com custo de transição de [esforço]."
- "Adiamos a decisão sobre [X] até [data] quando teremos [dados necessários]. Isso não bloqueia [próximos passos] porque [razão]."
- "Decisão reversível: optamos por [X] sabendo que podemos mudar para [Y] em [prazo] com custo de [esforço]. Não justifica análise exaustiva."

### Frases de Não-Decisão

- "Deliberadamente não decidimos sobre [X] agora porque [razão: informação insuficiente, prioridade menor, dependência externa]. Revisão programada: [data]."
- "Este ponto não requer decisão formal — segue o padrão [X] já estabelecido em [referência]."

## Anti-Padrões Linguísticos

### 1. Decisão sem Owner
**Errado:** "Foi decidido que usaremos PostgreSQL."
**Correto:** "A equipe técnica decidiu usar PostgreSQL, com aprovação do Tech Lead @pedro em 10/mar. ADR-052 registra a justificativa."

### 2. Decisão sem Alternativas
**Errado:** "Vamos usar Kafka."
**Correto:** "Avaliamos Kafka, RabbitMQ e SQS. Kafka foi escolhido porque [critério A, B]. RabbitMQ descartado por [motivo]. SQS descartado por [motivo]."

### 3. Decisão sem Data de Validade
**Errado:** "Nosso padrão é REST para todas as APIs."
**Correto:** "Nosso padrão atual é REST para APIs externas (decisão ADR-031, mar/2024). Revisão programada para set/2025 considerando adoção de gRPC para comunicação interna."

### 4. Decisão por Omissão
**Errado:** *Silêncio sobre a escolha do banco de dados — o time simplesmente começa a usar MongoDB.*
**Correto:** "Decisão: usar MongoDB para o serviço X. Razão: [justificativa]. Registrado em ADR-055. Owner: @fulano."

### 5. Decisão Vaga
**Errado:** "Vamos melhorar a arquitetura."
**Correto:** "Decisão: extrair o módulo de pagamentos em serviço independente até Q2. Motivação: permitir deploy independente e escala diferenciada. Owner: @fulana. Critério de sucesso: serviço operando em produção com SLA de 99.9%."

### 6. Reabertura Infinita
**Errado:** *Rediscutir a mesma decisão em toda reunião sem informação nova.*
**Correto:** "Esta decisão foi tomada em [data] com base em [evidência]. Para reabrir, é necessário apresentar: (1) evidência nova que invalide uma premissa, ou (2) mudança material de contexto. Sem isso, a decisão permanece."
