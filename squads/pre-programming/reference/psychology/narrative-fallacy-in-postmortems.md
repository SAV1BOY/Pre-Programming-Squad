# Falacia Narrativa em Postmortems

## Vies/Efeito

**Falacia Narrativa (Narrative Fallacy):** A tendencia de construir narrativas coerentes e simplificadas para explicar eventos complexos, atribuindo causalidade onde ha apenas correlacao e impondo ordem linear a processos caoticos. Descrita por Nassim Taleb em "The Black Swan" (2007).

## Descricao

Nosso cerebro e uma maquina de criar historias. Diante de eventos complexos, construimos uma narrativa que "faz sentido" — com inicio, meio e fim, herois e viloes, causa e efeito claros. Mas a realidade e mais complexa: incidentes de software resultam de multiplas causas interagindo de formas nao-lineares, nao de uma unica "causa raiz."

## Como se Manifesta em Pre-Programacao

### Em Postmortems que Informam Design
- **Causa raiz unica:** "O incidente foi causado por falta de timeout na API." Na realidade, o incidente resulta de: ausencia de timeout + ausencia de circuit breaker + ausencia de alerta + deploys na sexta-feira + feriado na equipe de ops.
- **Narrativa heroica:** "O engenheiro de plantao salvou o dia identificando o problema em 30 minutos." Ignorando que o sistema deveria ter self-healing, e que depender de heroismo e um risco.
- **Historias causais falsas:** "Adotamos microservicos E tivemos mais incidentes, logo microservicos causam incidentes." Correlacao nao e causalidade.

### Na Construcao de Justificativas de Design
- **Cherry-picking de historias:** "O Spotify usa essa arquitetura e e bem-sucedido." Ignorando que o contexto do Spotify e radicalmente diferente.
- **Post-hoc rationalization:** Construir uma narrativa convincente para justificar uma decisao ja tomada por intuicao.
- **Simplificacao excessiva:** "O projeto X falhou porque usaram tecnologia Y." Projetos falham por dezenas de razoes interconectadas.

### Na Analise de Projetos Anteriores
- **Vies de hindsight:** "Era obvio que ia dar errado." Nao era obvio na epoca — e facil ver padroes olhando para tras.
- **Atribuicao de agencia:** "O tech lead tomou uma decisao ruim." Decisoes ruins sao frequentemente decisoes razoaveis com informacao incompleta.

## Como Mitigar

### 1. Causalidade Multipla
Em postmortems e analises, exigir a identificacao de multiplos fatores contribuintes, nao uma "causa raiz" unica. Usar frameworks como "5 Whys" com ramificacoes, nao lineares.

### 2. Fatos antes de Narrativa
Em postmortems, primeiro documentar a timeline factual (o que aconteceu, quando, em que ordem). So depois tentar explicar por que. Separar observacao de interpretacao.

### 3. Contra-factuais
Para cada explicacao causal, perguntar: "Se removermos esse fator, o incidente ainda teria ocorrido?" Se a resposta e "possivelmente sim," o fator nao e a unica causa.

### 4. Complexidade Respeitada
Aceitar que alguns eventos sao resultado de interacoes complexas sem causa unica identificavel. "Nao sabemos exatamente por que, mas sabemos quais fatores contribuiram" e uma resposta honesta.

### 5. Desconfiar de Narrativas Limpas
Se a explicacao e simples, elegante e satisfatória demais, provavelmente e uma simplificacao excessiva. Realidade e confusa.

### 6. Dados Quantitativos
Complementar narrativas com dados: metricas de antes e depois, estatisticas de incidentes, tendencias temporais. Dados sao menos susceptiveis a falacia narrativa que historias.

## Exemplo Real

**Contexto:** Postmortem de um incidente de indisponibilidade de 2 horas no sistema de pagamentos.

**Narrativa simplificada:**
"O incidente foi causado por um deploy defeituoso que nao foi testado adequadamente. O desenvolvedor que fez o deploy nao seguiu o processo de code review."

**Realidade complexa (fatores contribuintes):**
1. A mudanca de codigo tinha um bug sutil em tratamento de null.
2. O teste unitario nao cobria o caso especifico (null em campo opcional).
3. O teste de integracao estava desabilitado ha 2 semanas por flakiness.
4. O code review foi feito, mas o reviewer estava sob pressao de prazo.
5. O canary deployment detectou o problema, mas o alerta foi ignorado porque o canal de alertas tinha ruido (alert fatigue).
6. O rollback automatico nao funcionou porque a migration de banco nao era reversivel.
7. O playbook de rollback manual estava desatualizado.

**Aplicacao na pre-programacao:**
- Nao usar o postmortem simplificado para justificar "precisamos de mais code review."
- Usar a analise complexa para informar o design: reversibilidade de migrations, tratamento de nullability, estrategia de alertas, testes de integracao confiaveis.
- Abordar multiplos fatores sistemicamente, nao buscar uma "bala de prata."
