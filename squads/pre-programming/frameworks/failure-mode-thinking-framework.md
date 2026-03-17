# Failure Mode Thinking Framework

## Título e Propósito

O **Failure Mode Thinking Framework** é uma abordagem sistemática para antecipar como um sistema pode falhar antes de construí-lo. O propósito é mudar o mindset de "como isso vai funcionar?" para "como isso vai quebrar?" — porque sistemas em produção passam mais tempo lidando com falhas do que operando no happy path.

## Quando Usar

- Durante design de arquitetura, antes de implementar
- Em revisões técnicas de soluções propostas
- Ao projetar integrações com sistemas externos
- Antes de definir SLAs e SLOs
- Na preparação para lançamentos de features críticas
- Em post-mortems, para prevenir reincidência

## Conceitos-Chave

1. **Modo de Falha**: Uma maneira específica pela qual o sistema pode falhar. Exemplo: timeout na API de pagamento.
2. **Efeito da Falha**: O que acontece para o usuário/sistema quando o modo de falha se materializa.
3. **Severidade**: O impacto do efeito da falha — de cosmético a catastrófico.
4. **Probabilidade**: Quão provável é que esse modo de falha ocorra em condições normais e adversas.
5. **Detectabilidade**: Quão fácil é perceber que a falha ocorreu. Falhas silenciosas são as mais perigosas.
6. **Cascata de Falhas**: Quando uma falha em um componente causa falhas em componentes dependentes.

## Processo / Passos

### Passo 1 — Mapear Componentes
Liste todos os componentes do sistema e suas dependências: serviços internos, APIs externas, bancos de dados, filas, caches, etc.

### Passo 2 — Para Cada Componente, Perguntar "E Se?"
Sistematicamente pergunte: "E se esse componente ficar lento? Indisponível? Retornar dados errados? Perder dados? Ficar sobrecarregado?"

### Passo 3 — Mapear Efeitos
Para cada modo de falha, trace o efeito: o que acontece com os componentes dependentes? E com o usuário final?

### Passo 4 — Avaliar Severidade × Probabilidade × Detectabilidade
Para cada modo de falha, classifique (1-5) cada dimensão. O produto dos três é o **Número de Prioridade de Risco (RPN)**.

### Passo 5 — Identificar Cascatas
Verifique se a falha de um componente pode causar falhas em cadeia. Mapeie caminhos de cascata.

### Passo 6 — Projetar Mitigações
Para modos de falha com RPN alto, projete: timeout, retry, circuit breaker, fallback, graceful degradation, alertas.

### Passo 7 — Documentar Modos Aceitos
Para modos de falha com RPN baixo, documente explicitamente que o risco é aceito e por quê.

## Perguntas de Ativação

- "O que acontece quando esse serviço não responde em 5 segundos?"
- "Se o banco de dados ficar indisponível por 10 minutos, perdemos dados?"
- "Como o usuário fica sabendo que algo deu errado?"
- "Uma falha aqui pode derrubar outros componentes?"
- "Temos como detectar essa falha automaticamente ou só quando o usuário reclamar?"
- "Já simulamos esse cenário de falha em ambiente de teste?"

## Output Esperado

| Componente | Modo de Falha | Efeito | Severidade (1-5) | Probabilidade (1-5) | Detectabilidade (1-5) | RPN | Mitigação |
|---|---|---|---|---|---|---|---|
| API de Pagamento | Timeout | Checkout travado | 5 | 3 | 2 | 30 | Circuit breaker + fallback para fila |
| Cache Redis | Indisponibilidade | Aumento de latência 10x | 3 | 2 | 1 | 6 | Fallback para DB + alerta |
| Serviço de Email | Dados corrompidos | Email com informação errada | 4 | 1 | 5 | 20 | Validação de payload + queue DLQ |
| CDN | Expiração de cache | Assets desatualizados | 2 | 3 | 4 | 24 | Versionamento de assets |

## Armadilhas Comuns

1. **Otimismo sistêmico**: Assumir que dependências externas "sempre funcionam". Toda dependência vai falhar eventualmente.
2. **Foco apenas em falhas totais**: Falhas parciais (lentidão, dados inconsistentes, perda parcial) são mais comuns e mais difíceis de detectar.
3. **Ignorar cascatas**: Tratar cada componente isoladamente sem considerar efeitos em cadeia.
4. **Mitigação excessiva**: Tentar mitigar todo modo de falha possível adiciona complexidade que gera novos modos de falha.
5. **Falhas silenciosas**: O modo de falha mais perigoso é aquele que ninguém percebe — dados corrompidos silenciosamente por semanas.
6. **"Isso nunca acontece"**: Em escala suficiente, todo modo de falha teoricamente possível vai acontecer.
