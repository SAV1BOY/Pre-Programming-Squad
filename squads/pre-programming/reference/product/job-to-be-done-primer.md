# Jobs to Be Done (JTBD) - Primer

## O que e Jobs to Be Done

Jobs to Be Done e um framework de inovacao criado por Clayton Christensen e desenvolvido por Tony Ulwick e Bob Moesta. A premissa central e que pessoas nao compram produtos — elas "contratam" produtos para realizar um "trabalho" (job) em suas vidas. Entender o job que o usuario esta tentando realizar e mais importante do que entender as features que ele pede.

## A Frase Classica

> "As pessoas nao querem uma furadeira de 1/4 de polegada. Elas querem um buraco de 1/4 de polegada." — Theodore Levitt

E indo alem:

> "Elas nao querem nem o buraco. Elas querem pendurar um quadro na parede para que sua sala fique bonita."

## Anatomia de um Job

### Estrutura
```
Quando [situacao/contexto],
eu quero [motivacao/necessidade],
para que [resultado desejado].
```

### Dimensoes de um Job
- **Funcional:** O que o usuario esta tentando fazer objetivamente.
- **Emocional (pessoal):** Como o usuario quer se sentir.
- **Social:** Como o usuario quer ser percebido por outros.

### Exemplo Completo: App de Transferencia Bancaria
**Funcional:** "Quando preciso pagar um fornecedor que esta em outro banco, quero transferir dinheiro de forma confiavel, para que o pagamento seja confirmado e eu nao tenha problemas com o fornecedor."

**Emocional:** "Quero me sentir seguro de que o dinheiro chegou ao destino certo."

**Social:** "Quero ser visto como um pagador confiavel e pontual pelo fornecedor."

## JTBD na Pre-Programacao

### Por que JTBD e Relevante para Pre-Programacao

Na pre-programacao, frequentemente recebemos requisitos na forma de solucoes ("precisamos de um microservico de notificacoes"). JTBD nos forca a voltar ao problema real:

- **Qual job o usuario esta tentando realizar?**
- **Quais sao as circunstancias desse job?**
- **Quais resultados o usuario espera?**
- **Quais sao as barreiras atuais para realizar esse job?**

Entender o job permite questionar se a solucao proposta e realmente a melhor forma de realizar o trabalho.

### Exemplo Pratico

**Requisito recebido:** "Precisamos de um dashboard de analytics em tempo real."

**Analise JTBD:**
- **Job funcional:** "Quando um incidente acontece, o engenheiro de plantao precisa identificar a causa raiz rapidamente para restaurar o servico."
- **Circunstancia:** Sob pressao, as 3h da manha, com informacao espalhada em 5 ferramentas diferentes.
- **Resultado desejado:** Identificar causa raiz em menos de 10 minutos.
- **Barreiras:** Dados espalhados, falta de correlacao entre metricas, alertas sem contexto.

**Insight:** O job nao e "ver um dashboard" — e "encontrar a causa raiz rapidamente." Talvez a solucao nao seja um dashboard, mas alertas com contexto automatico e runbooks integrados.

## Framework de Outcome-Driven Innovation (ODI)

Tony Ulwick estendeu JTBD com o framework ODI, que sistematiza a descoberta de oportunidades:

### 1. Definir o Job
Mapear o job completo, nao apenas um passo dele.

### 2. Mapear o Job Map
Decompor o job em 8 passos universais:
1. **Definir:** O que preciso realizar?
2. **Localizar:** Onde encontro o que preciso?
3. **Preparar:** O que preciso antes de comecar?
4. **Confirmar:** Estou pronto para comecar?
5. **Executar:** Realizar o trabalho.
6. **Monitorar:** Esta funcionando?
7. **Modificar:** Preciso ajustar algo?
8. **Concluir:** O trabalho esta feito?

### 3. Identificar Desired Outcomes
Para cada passo do job map, identificar resultados que o usuario deseja:
- "Minimizar o tempo para [passo]."
- "Minimizar a probabilidade de [problema]."
- "Maximizar a capacidade de [acao]."

### 4. Encontrar Oportunidades
Outcomes que sao muito importantes mas pouco satisfeitos representam oportunidades de inovacao.

## Como Aplicar no Squad

### Na Avaliacao de PRDs
- Verificar se o PRD articula o job do usuario, nao apenas a feature.
- Perguntar: "Qual trabalho o usuario esta contratando nosso produto para fazer?"
- Validar que a solucao proposta atende o job, nao apenas o requisito aparente.

### Na Definicao de Criterios de Aceitacao
- Formular criterios em termos de outcomes do job, nao de funcionalidades.
- Exemplo: Em vez de "o botao deve funcionar", usar "o usuario deve conseguir completar a transferencia em menos de 30 segundos."

### Na Priorizacao
- Priorizar features que atendem jobs com alta importancia e baixa satisfacao.
- Usar a matriz importancia x satisfacao para identificar oportunidades.

### Na Avaliacao de Alternativas
- Para cada design proposto, avaliar: "Qual design realiza melhor o job do usuario?"
- Considerar competing solutions: como o usuario resolve o job hoje sem nosso produto?

## Switch Interview: Entendendo Motivacoes de Troca

Bob Moesta propoe a Switch Interview para entender por que usuarios trocam de solucao:

### Quatro Forcas da Troca
1. **Push:** Insatisfacao com a solucao atual.
2. **Pull:** Atracao pela nova solucao.
3. **Habito:** Inércia de continuar com a solucao atual.
4. **Ansiedade:** Medo de mudar para algo novo.

Para que a troca aconteca: Push + Pull > Habito + Ansiedade.

### Aplicacao na Pre-Programacao
- Se estamos substituindo um sistema existente, mapear as 4 forcas.
- Projetar para minimizar ansiedade (migracoes graduais, rollback facil).
- Projetar para maximizar pull (beneficios claros e imediatos).
- Reconhecer que habito e real (treinar usuarios, migrar dados).
