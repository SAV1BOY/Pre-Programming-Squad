# Goldratt: Theory of Constraints

## Título e Propósito

Framework baseado no trabalho de **Eliyahu Goldratt** (*The Goal*). A tese central: **o throughput de qualquer sistema é determinado por seu gargalo (constraint)** — e melhorar qualquer parte que não é o gargalo é desperdício. O propósito é aplicar esse pensamento para identificar e aliviar o gargalo real em projetos e sistemas de software.

## Quando Usar

- Quando a equipe trabalha muito mas entrega pouco (throughput baixo)
- Para identificar o que realmente limita a velocidade do projeto
- Ao otimizar pipelines de CI/CD, processos de deploy ou fluxos de trabalho
- Em análise de performance de sistemas onde nem tudo precisa ser otimizado
- Quando há debate sobre onde investir esforço de melhoria

## Conceitos-Chave

1. **Constraint (Gargalo)**: O recurso ou processo mais lento que limita o throughput do sistema inteiro. Pode ser técnico, organizacional ou processual.
2. **Five Focusing Steps**: (1) Identificar o gargalo, (2) Explorar o gargalo (maximizar uso), (3) Subordinar tudo ao gargalo, (4) Elevar o gargalo (aumentar capacidade), (5) Repetir (o gargalo move).
3. **Throughput**: A taxa de entrega de valor do sistema. Não é busyness (estar ocupado) — é output real.
4. **Local vs. Global Optimization**: Otimizar uma parte pode piorar o todo se não é o gargalo. Exemplo: acelerar desenvolvimento quando o gargalo é deploy.
5. **Work in Progress (WIP)**: Trabalho iniciado mas não concluído. WIP excessivo é sintoma de gargalo — e causa de mais gargalo (Lei de Little).

## Processo / Passos

### Passo 1 — Mapear o Fluxo de Valor
Mapeie o fluxo completo: ideia → discovery → design → implementação → review → teste → deploy → produção. Cada etapa é um nó.

### Passo 2 — Medir Tempo em Cada Etapa
Para cada etapa, meça: tempo de processamento (ativo) e tempo de espera (em fila). O gargalo é onde a fila é mais longa.

### Passo 3 — Identificar o Gargalo
O gargalo é a etapa com maior fila e/ou maior tempo de espera. Não é necessariamente a mais lenta — é a que limita o fluxo.

### Passo 4 — Explorar o Gargalo
Maximize o uso do gargalo: elimine interrupções, reduza waste, garanta que nunca fique ocioso. Exemplo: se code review é gargalo, priorize reviews sobre novo código.

### Passo 5 — Subordinar ao Gargalo
Não produza mais rápido nas etapas anteriores ao gargalo — isso só aumenta a fila. Sincronize o ritmo com a capacidade do gargalo.

## Perguntas de Ativação

- "O que está impedindo a equipe de entregar mais rápido? Onde está a fila mais longa?"
- "Se pudéssemos melhorar apenas uma etapa do nosso processo, qual teria mais impacto?"
- "Estamos otimizando algo que não é o gargalo?"
- "O gargalo é técnico (infra, testes) ou organizacional (aprovações, comunicação)?"
- "Quanto trabalho está iniciado mas não concluído? Isso é sinal de gargalo."

## Output Esperado

Mapa do fluxo de valor com tempos por etapa, gargalo identificado, plano de exploração e elevação do gargalo.

## Armadilhas Comuns

1. **Otimização local**: Acelerar o desenvolvimento quando o gargalo é deploy ou aprovação. Gera mais WIP, não mais entrega.
2. **Gargalo invisível**: O gargalo pode ser "esperar resposta do PO" ou "aprovação de segurança" — não aparece no board.
3. **Gargalo moveu**: Após aliviar um gargalo, o próximo mais lento se torna o novo gargalo. É processo contínuo.
4. **WIP como produtividade**: Equipes que iniciam 10 coisas em paralelo acham que são produtivas. Na verdade, estão alimentando filas.
5. **Gargalo de pessoas**: Quando uma pessoa é gargalo, a solução não é "trabalhar mais" — é disseminar conhecimento e redistribuir.
