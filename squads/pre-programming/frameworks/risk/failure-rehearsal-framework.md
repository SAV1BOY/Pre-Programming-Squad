# Failure Rehearsal Framework

## Título e Propósito

O **Failure Rehearsal Framework** é um sistema para ensaiar falhas antes que elas aconteçam em produção. O propósito é transformar falhas de eventos inesperados e caóticos em cenários praticados e controlados — porque equipes que ensaiaram a resposta a incidentes respondem mais rápido, cometem menos erros e sofrem menos impacto.

## Quando Usar

- Antes de lançamentos de funcionalidades críticas
- Periodicamente (trimestral) para manter a equipe preparada
- Quando novos membros entram na equipe e precisam aprender a responder a incidentes
- Após post-mortems que revelaram falhas na resposta
- Quando o sistema cresceu em complexidade desde o último ensaio

## Conceitos-Chave

1. **Ensaio de Falha**: Simulação controlada de um cenário de falha para praticar a resposta da equipe.
2. **Game Day**: Sessão dedicada onde falhas são injetadas (ou simuladas) e a equipe responde como em incidente real.
3. **Chaos Engineering**: Prática de introduzir falhas deliberadas em sistemas para descobrir vulnerabilidades.
4. **Tabletop Exercise**: Exercício de simulação mental onde a equipe discute "e se?" sem realmente quebrar nada.
5. **Runbook**: Documento com passos detalhados para diagnosticar e resolver tipos específicos de incidente.
6. **Tempo Médio de Recuperação (MTTR)**: Tempo entre início do incidente e resolução. O ensaio visa reduzir o MTTR.

## Processo / Passos

### Passo 1 — Identificar Cenários de Falha
Liste os cenários mais prováveis e mais impactantes: banco de dados indisponível, API externa fora do ar, pico de tráfego, perda de dados, breach de segurança.

### Passo 2 — Priorizar por Impacto e Probabilidade
Classifique cenários e comece pelos de maior risco. Não tente ensaiar tudo de uma vez.

### Passo 3 — Escolher o Formato
- **Tabletop**: Discussão em grupo. Bom para cenários que não podem ser simulados (breach, perda de data center).
- **Simulation**: Injetar falhas em ambiente de staging. Bom para falhas técnicas.
- **Game Day**: Injetar falhas em produção (com controle). Bom para equipes maduras.

### Passo 4 — Preparar o Cenário
Defina: o que vai falhar, como vai falhar, quais são os sinais que a equipe deveria detectar, qual é a resolução esperada.

### Passo 5 — Executar o Ensaio
Execute o cenário. Observe: quanto tempo leva para detectar? Para diagnosticar? Para resolver? Quais problemas surgiram?

### Passo 6 — Debrief
Após o ensaio, discuta: o que funcionou? O que falhou? Quais gaps foram descobertos nos runbooks, monitoramento, comunicação?

### Passo 7 — Atualizar Runbooks e Processos
Incorpore os aprendizados: atualize runbooks, melhore alertas, corrija gaps de monitoramento, treine a equipe nos pontos fracos.

## Perguntas de Ativação

- "Se o banco de dados principal ficasse indisponível agora, a equipe saberia o que fazer?"
- "Temos runbooks atualizados para os incidentes mais prováveis?"
- "Quando foi a última vez que praticamos resposta a incidente?"
- "Novos membros da equipe sabem como responder a falhas críticas?"
- "Nosso monitoramento detectaria [cenário X] em menos de 5 minutos?"
- "Se a pessoa que normalmente resolve incidentes estivesse de férias, alguém mais conseguiria?"

## Output Esperado

```
ENSAIO DE FALHA — [Data]

CENÁRIO: API de pagamento indisponível por 15 minutos

FORMATO: Simulation (staging)

CRONOLOGIA DO ENSAIO:
- T+0: Falha injetada (API de pagamento retornando 503)
- T+2min: Alerta disparado — "Taxa de erro gateway > 5%"
- T+4min: Dev de plantão investigando
- T+8min: Diagnóstico correto — identificou API de pagamento down
- T+10min: Circuit breaker ativado, pedidos redirecionados para fila
- T+15min: API restaurada, fila processada, operação normalizada

MTTR: 10 minutos (até ativação do circuit breaker)

O QUE FUNCIONOU:
- Alerta disparou em 2 minutos ✓
- Circuit breaker funcionou como projetado ✓
- Fila processou pedidos sem perda ✓

O QUE FALHOU:
- Runbook desatualizado — referenciava dashboard antigo ✗
- Dev demorou 4min para identificar a causa — log confuso ✗
- Comunicação com stakeholders não aconteceu ✗

AÇÕES:
1. Atualizar runbook com dashboards corretos — Resp: [nome] — Prazo: [data]
2. Melhorar mensagem de log do circuit breaker — Resp: [nome] — Prazo: [data]
3. Criar template de comunicação para incidente de pagamento — Resp: [nome] — Prazo: [data]
```

## Armadilhas Comuns

1. **Nunca ensaiar**: "Não temos tempo para simulação" — até que um incidente real prove que o tempo de resposta é 10x maior do que deveria.
2. **Ensaiar apenas em staging**: Staging não é produção. Algumas falhas só se manifestam com dados e tráfego reais.
3. **Ensaio sem debrief**: Fazer o exercício mas não discutir os aprendizados. O valor está na reflexão, não apenas na prática.
4. **Cenários irrealistas**: Simular falhas que não correspondem a riscos reais do sistema.
5. **Runbooks de gaveta**: Runbooks escritos uma vez e nunca atualizados. Após cada ensaio, atualize.
6. **Dependência de heróis**: Se apenas uma pessoa sabe responder a incidentes, o ensaio deve treinar outros.
