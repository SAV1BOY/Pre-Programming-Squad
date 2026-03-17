# Custo Afundado em Arquitetura

## Vies/Efeito

**Falacia do Custo Afundado (Sunk Cost Fallacy):** A tendencia de continuar investindo em algo por causa do que ja foi investido (tempo, dinheiro, esforco), mesmo quando evidencias indicam que seria melhor parar ou mudar de direcao.

## Descricao

O custo afundado e racional se os investimentos passados geram retorno futuro. Mas se tornam uma falacia quando continuamos investindo simplesmente porque "ja gastamos muito para parar agora." Arkes e Blumer (1985) demonstraram que pessoas preferem usar um ingresso para um show ruim se pagaram mais caro por ele — mesmo que a experiencia seja negativa independente do preco pago.

## Como se Manifesta em Pre-Programacao

### Em Decisoes Arquiteturais
- **"Ja investimos 6 meses nessa arquitetura, nao podemos mudar agora."** O tempo investido e irrelevante para a decisao futura — o que importa e o custo de continuar vs. o custo de mudar.
- **"Escolhemos essa tecnologia e toda a equipe ja se capacitou."** O treinamento ja aconteceu. A pergunta correta e: "Essa tecnologia e a melhor para o proximo ano?"
- **"O design doc ja foi aprovado, nao vamos reabrir a discussao."** Novas informacoes surgem. Decisoes devem ser reversiveis quando o contexto muda.

### Em Projetos de Migracao
- **Continuar migracao para microservicos** mesmo quando evidencias mostram que o monolito refatorado seria suficiente — porque "ja migramos 3 servicos."
- **Insistir em ferramenta X** mesmo quando ferramenta Y se provou superior — porque "ja customizamos X extensivamente."

### Em Reescritas
- **"Ja reescrevemos 60% do sistema, nao podemos parar."** Talvez os 40% restantes sejam os mais complexos e a reescrita completa nunca entregue valor.

### Em Debates Tecnicos
- **Defender uma posicao tecnica porque voce a defendeu publicamente** antes, mesmo com novas evidencias. O ego se torna um custo afundado.

## Como Mitigar

### 1. Perguntar: "Se estivessemos comecando do zero hoje, fariamos a mesma escolha?"
Se a resposta e "nao," o investimento passado e irrelevante. O que importa e a melhor decisao daqui para frente.

### 2. Kill Criteria Pre-Definidos
Antes de iniciar um projeto ou migracao, definir criterios claros para abortar. Exemplos: "Se em 8 semanas nao atingimos X, reavaliamos." "Se o custo exceder Y, pausamos."

### 3. Revisoes Periodicas de Direcao
Checkpoints obrigatorios onde a equipe pergunta: "Ainda faz sentido continuar?" Nao como formalidade, mas com disposicao genuina de mudar.

### 4. Separar Investimento Passado de Decisao Futura
Em reunioes de decisao, proibir argumentos baseados em investimento passado. Focar em: "Qual opcao tem melhor custo-beneficio DAQUI PARA FRENTE?"

### 5. Normalizar Mudanca de Direcao
Criar cultura onde mudar de direcao baseado em novas evidencias e celebrado, nao punido. "Pivotamos cedo" deve ser motivo de orgulho.

## Exemplo Real

**Contexto:** Uma equipe investiu 9 meses migrando um monolito para 12 microservicos. Apos migrar 5 servicos, descobriram que a complexidade operacional triplicou, o custo de infra dobrou e a latencia piorou por causa de chamadas entre servicos.

**Manifestacao do custo afundado:**
- "Ja migramos 5 servicos. Parar agora seria desperdicio."
- "A equipe aprendeu muito. Nao podemos jogar esse aprendizado fora."
- "Os stakeholders ja viram a apresentacao do plano. Voltar atras seria constrangedor."

**O que deveria ter acontecido:**
- Nos kill criteria definidos no inicio: "Se apos 3 servicos migrados o custo operacional exceder 2x, reavaliamos."
- Na revisao do mes 6: "O custo dobrou, a latencia piorou, e a complexidade triplicou. Se comecassemos hoje, escolheriamos um modular monolith."
- Decisao: Parar a migracao, manter os 5 servicos estabilizados, adotar modular monolith para o restante.
- Aprendizado preservado: A experiencia com microservicos ainda e valiosa para os 5 servicos existentes e para decisoes futuras.
