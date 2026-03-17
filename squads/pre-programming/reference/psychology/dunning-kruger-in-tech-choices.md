# Dunning-Kruger em Escolhas Tecnologicas

## Vies/Efeito

**Efeito Dunning-Kruger:** Pessoas com pouco conhecimento em um dominio tendem a superestimar sua competencia, enquanto especialistas tendem a subestimar a sua. Identificado por Dunning e Kruger (1999).

## Descricao

O efeito opera em quatro estagios: (1) Incompetencia inconsciente — nao sabemos o que nao sabemos. (2) Incompetencia consciente — percebemos nossas lacunas. (3) Competencia consciente — sabemos, mas com esforço. (4) Competencia inconsciente — dominio automatico. O perigo esta no estagio 1, onde a confianca e maxima e o conhecimento e minimo.

## Como se Manifesta em Pre-Programacao

### Na Escolha de Tecnologias
- **"Li o tutorial de Kubernetes, vamos usar em producao."** Kubernetes resolve problemas reais, mas sua complexidade operacional e subestimada por quem acabou de aprender.
- **"MongoDB e mais simples que PostgreSQL."** Para o caso de uso errado, MongoDB pode ser mais complexo. A percepcao de simplicidade vem do desconhecimento dos problemas que surgirao.
- **"Event sourcing resolve tudo."** Entusiasmo com um padrao recen-aprendido, sem entender os custos operacionais.

### Na Avaliacao de Complexidade
- **"Microservicos sao simples — cada um faz uma coisa."** Subestimar a complexidade distribuida (network, consistency, observability, deployment).
- **"GraphQL e so um endpoint."** Ignorar complexidade de N+1, caching, authorization, schema management.
- **"Serveless — nao precisa de ops."** Subestimar cold starts, limites de concorrencia, debugging, custos inesperados.

### Na Revisao de Design
- **Junior propoe arquitetura over-engineered** sem perceber que esta adicionando complexidade desnecessaria.
- **Senior recusa nova tecnologia sem avaliar** porque "ja viu isso antes" (outro lado do espectro).

## Como Mitigar

### 1. Exigir Experiencia em Producao
Para adotar uma tecnologia nova, exigir que pelo menos um membro da equipe tenha experiencia em producao com ela, ou que um spike substancial seja conduzido.

### 2. Escala de Maturidade Tecnologica
Classificar o conhecimento da equipe sobre cada tecnologia:
- **Nivel 0:** Leu blog posts e tutoriais.
- **Nivel 1:** Completou um projeto pessoal ou prova de conceito.
- **Nivel 2:** Usou em um projeto profissional.
- **Nivel 3:** Operou em producao por > 6 meses.
- **Nivel 4:** Debugou problemas complexos em producao.

Para decisoes criticas, exigir nivel >= 2 na equipe ou mitigar com consultoria/spike.

### 3. Perguntas Calibradoras
Antes de adotar uma tecnologia, a equipe deve responder:
- "Quais sao as 3 maiores limitacoes dessa tecnologia?"
- "Em que cenarios essa tecnologia e uma MA escolha?"
- "Qual e o custo operacional mensal estimado?"
- "Como debugamos problemas nessa tecnologia as 3h da manha?"

Se ninguem consegue responder, a equipe esta no estagio 1 de Dunning-Kruger.

### 4. Proof of Failure, nao Proof of Concept
Alem de provar que funciona (PoC), provar que falha graciosamente. O que acontece quando a tecnologia falha? Como recuperamos?

### 5. Anti-Resumo de Tecnologia
Para cada tecnologia proposta, documentar: "Quando NAO usar esta tecnologia." Se a equipe nao consegue articular anti-patterns, nao conhece a tecnologia profundamente.

## Exemplo Real

**Contexto:** Equipe de 4 desenvolvedores com experiencia em monolito Django decide adotar stack completa de microservicos: Kubernetes, Kafka, gRPC, Redis, Elasticsearch.

**Manifestacao do Dunning-Kruger:**
- Toda a equipe assistiu a um curso online de Kubernetes (40h). Confianca alta.
- Ninguem operou Kubernetes em producao. Desconhecem problemas de networking, resource limits, node draining.
- "Kafka e simples — publica e consome mensagens." Nao entendem consumer lag, rebalancing, exactly-once semantics.
- "gRPC e mais rapido que REST." Sem entender HTTP/2 load balancing, debugging com ferramentas limitadas.

**Resultado:** 6 meses de luta com infraestrutura, zero features entregues, 3 desenvolvedores frustrados, rollback parcial para monolito.

**O que deveria ter acontecido na pre-programacao:**
- Avaliar nivel de maturidade da equipe: nivel 0-1 para toda a stack nova.
- Propor adocao incremental: manter Django, extrair UM servico critico, operar por 3 meses, avaliar.
- Exigir consultoria ou contratacao de alguem com nivel 3+ em Kubernetes.
- Spike de 2 semanas em Kubernetes antes de comprometer a arquitetura.
