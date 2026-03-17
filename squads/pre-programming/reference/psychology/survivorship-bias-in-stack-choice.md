# Vies de Sobrevivencia em Escolha de Stack

## Vies/Efeito

**Vies de Sobrevivencia (Survivorship Bias):** A tendencia de focar nos casos de sucesso (que "sobreviveram") e ignorar os fracassos (que sao invisiveis), levando a conclusoes distorcidas. Popularizado pela analise de Abraham Wald sobre blindagem de avioes na Segunda Guerra.

## Descricao

Wald percebeu que os militares queriam reforcar as areas dos avioes com mais impactos de bala. Mas os avioes que retornaram com buracos eram os sobreviventes — os avioes que levaram impactos em areas criticas nao voltaram para ser analisados. O vies de sobrevivencia nos faz estudar os vencedores e ignorar os perdedores, distorcendo nossa compreensao de causalidade.

## Como se Manifesta em Pre-Programacao

### Na Escolha de Tecnologias
- **"Netflix usa microservicos e e bem-sucedida, logo microservicos levam ao sucesso."** Nao vemos as centenas de empresas que adotaram microservicos e fracassaram — elas nao publicam blog posts sobre seus fracassos.
- **"Varias startups unicornio usam Node.js."** Nao vemos as milhares de startups que usaram Node.js e faliram. A tecnologia nao foi o fator determinante.
- **"O Spotify usa squads e e bem-sucedido."** O proprio Spotify publicou que o modelo teve problemas significativos.

### Na Avaliacao de Arquiteturas
- **Case studies e conferencias:** Apresentacoes em conferencias sao quase exclusivamente de projetos bem-sucedidos. Os fracassos nao sao apresentados.
- **Blog posts de empresas:** Empresas publicam quando algo funciona, raramente quando falha. A amostra disponivel de informacao e distorcida.
- **Stack Overflow / Reddit:** Respostas tendem a vir de quem teve sucesso. Quem falhou silenciosamente nao responde.

### Na Analise de Riscos
- **"Nunca tivemos problema com essa abordagem."** Talvez os projetos que tiveram problemas foram cancelados ou transferidos para outras equipes, e os problemas nao sao visiveis.
- **"Todas as equipes que conheco usam X e esta tudo bem."** Voce conhece equipes que usam X e sobreviveram para contar. As que falharam podem ter migrado silenciosamente.

## Como Mitigar

### 1. Buscar Ativamente Fracassos
Para cada case de sucesso citado, perguntar: "Quem usou a mesma abordagem e fracassou? Por que?" Buscar postmortems, artigos criticos, discussoes sobre problemas.

### 2. Base Rate Analysis
Em vez de focar em exemplos especificos, buscar a taxa base: "De todas as empresas que adotaram microservicos, quantas tiveram sucesso? Quantas reverteram?"

### 3. Desconfiar de Unanimidade em Cases
Se todos os cases disponiveis sao positivos, provavelmente ha vies de sobrevivencia. Resultados genuinamente bons tem distribuicao de resultados, nao unanimidade.

### 4. Pre-Mortem com Base em Fracassos
Em vez de imaginar fracasso abstratamente, buscar casos reais de fracasso com a mesma tecnologia/abordagem e avaliar: "Isso pode acontecer conosco?"

### 5. Avaliar Contexto, nao Resultado
O sucesso da Netflix com microservicos e resultado de investimento massivo em plataforma, tooling e engenharia. Copiar a arquitetura sem copiar o investimento e receita para fracasso.

### 6. Ler Postmortems Publicos
Fontes como failure.wiki, postmortems.info e HackerNews threads sobre "what went wrong" oferecem a perspectiva dos fracassos que normalmente sao invisiveis.

## Exemplo Real

**Contexto:** Equipe avalia adotar Event Sourcing para sistema de e-commerce. Leram 5 blog posts e assistiram 3 talks sobre Event Sourcing. Todos positivos.

**Manifestacao do vies de sobrevivencia:**
- Os 5 blog posts sao de empresas que implementaram Event Sourcing com sucesso.
- Os 3 talks sao de arquitetos que se especializaram em Event Sourcing (e portanto tem interesse em promove-lo).
- Nenhuma pesquisa sobre empresas que tentaram Event Sourcing e reverteram.
- Nenhuma analise de quando Event Sourcing NAO e adequado.

**Informacoes invisiveis (nao buscadas):**
- Equipe X reverteu ES apos 8 meses porque a complexidade de queries era ingerenciavel.
- Equipe Y descobriu que event replay levava 4 horas, tornando testes impraticaveis.
- Equipe Z gastou 6 meses construindo projecoes que um CRUD + audit log resolveria.
- Pesquisa informal mostra que ~40% das equipes que tentam ES nao concluem a implementacao.

**O que deveria ter acontecido na pre-programacao:**
- Pesquisar "event sourcing problems" e "event sourcing migration back" alem de "event sourcing success."
- Listar pre-requisitos de sucesso: equipe experiente, dominio adequado, tooling maduro.
- Avaliar honestamente: a equipe e o dominio atendem os pre-requisitos?
- Conversar com alguem que REVERTEU event sourcing, nao apenas com quem adotou.
