# Team Topologies

## Informações Gerais

- **Titulo:** Team Topologies: Organizing Business and Technology Teams for Fast Flow
- **Autores:** Matthew Skelton, Manuel Pais
- **Ano:** 2019

## Tese Central

A forma como equipes sao organizadas determina a arquitetura do software que elas produzem (Lei de Conway). Em vez de lutar contra Conway, devemos usa-la estrategicamente: organizar equipes intencionalmente para que a comunicacao necessaria entre elas resulte na arquitetura desejada. Quatro tipos fundamentais de equipes e tres modos de interacao fornecem um vocabulario preciso para design organizacional.

## Conceitos-Chave para Pre-Programacao

### 1. Lei de Conway e Manobra Inversa de Conway
A Lei de Conway afirma que sistemas espelham a estrutura de comunicacao das organizacoes que os produzem. A manobra inversa propoe organizar equipes para produzir a arquitetura desejada. Na pre-programacao, a estrutura das equipes deve ser considerada como restricao arquitetural.

### 2. Quatro Tipos Fundamentais de Equipes
- **Stream-aligned team:** Alinhada a um fluxo de negocio. Entrega valor diretamente ao usuario. E o tipo principal.
- **Enabling team:** Ajuda stream-aligned teams a superar obstaculos. Detecta gaps e oferece capacitacao.
- **Complicated-subsystem team:** Gerencia subsistemas que requerem expertise especializada.
- **Platform team:** Fornece servicos internos que reduzem carga cognitiva de stream-aligned teams.

### 3. Tres Modos de Interacao
- **Collaboration:** Duas equipes trabalham juntas por um periodo definido. Bom para descoberta.
- **X-as-a-Service:** Uma equipe fornece algo que outra consome com minima interacao. Bom para previsibilidade.
- **Facilitating:** Uma equipe ajuda outra a crescer. Bom para capacitacao.

### 4. Carga Cognitiva
O limite cognitivo de uma equipe determina o tamanho do dominio que ela pode gerenciar eficazmente. Tipos: intrinseca (complexidade do dominio), extrinseca (ferramentas, processos) e germana (aprendizado do dominio). O objetivo e minimizar extrinseca e maximizar germana.

### 5. Fluxo de Mudancas (Flow of Change)
O objetivo primario e otimizar o fluxo de mudancas do conceito ao deploy. Decisoes organizacionais e arquiteturais devem ser avaliadas pelo impacto no fluxo.

### 6. Limites de Equipe como Limites de Software
Os limites entre equipes devem coincidir com limites de software (APIs, contratos). Se duas equipes precisam mudar o mesmo codigo frequentemente, ou ha um problema de organizacao ou de arquitetura.

## Como Aplicar no Squad

### Na Avaliacao de Viabilidade Organizacional
- Mapear a estrutura de equipes atual e como ela afeta a arquitetura proposta.
- Identificar se o design requer comunicacao entre equipes que nao existe.
- Avaliar a carga cognitiva de cada equipe com o design proposto.
- Recomendar ajustes organizacionais quando necessario para viabilizar a arquitetura.

### Na Definicao de Limites de Servico
- Alinhar limites de servico com limites de equipe.
- Definir contratos claros entre servicos/equipes (X-as-a-Service).
- Identificar areas que requerem colaboracao temporaria entre equipes.
- Planejar transicao de collaboration para X-as-a-Service apos periodo de discovery.

### Na Avaliacao de Impacto em Fluxo
- Para cada design, avaliar: "Quantas equipes precisam ser coordenadas para entregar uma mudanca?"
- Preferir designs que minimizam dependencias inter-equipe.
- Identificar gargalos de comunicacao que impactam o fluxo de entrega.

### Nos Criterios de Readiness
- "A estrutura de equipes suporta a arquitetura proposta?"
- "A carga cognitiva por equipe e gerenciavel?"
- "Limites de servico estao alinhados com limites de equipe?"
- "Modos de interacao entre equipes estao definidos?"

## Citacoes Importantes

> "Choose software boundaries that match team cognitive load."

> "Team-first architecture means designing the software architecture to fit the team, not the other way around."

> "If the architecture of the system and the architecture of the organization are at odds, the organization wins."

> "Minimize cognitive load on stream-aligned teams so they can focus on delivering value."

> "The purpose of a platform team is to enable stream-aligned teams to deliver work with substantial autonomy."

## Relacao com Outros Livros de Referencia

- **Accelerate:** Team Topologies expande a dimensao organizacional que Accelerate identifica como critica.
- **DDD (Evans):** Bounded contexts alinham-se com limites de stream-aligned teams.
- **Fundamentals of Software Architecture:** O quantum arquitetural de Richards/Ford frequentemente corresponde ao dominio de uma stream-aligned team.
