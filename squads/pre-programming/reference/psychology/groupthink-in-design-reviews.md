# Groupthink em Design Reviews

## Vies/Efeito

**Groupthink (Pensamento de Grupo):** A tendencia de membros de um grupo coeso a buscar consenso acima da analise critica, suprimindo opinioes dissidentes e alternativas para manter harmonia. Identificado por Irving Janis (1972).

## Descricao

Groupthink ocorre quando a coesao do grupo se torna mais importante que a qualidade da decisao. Sintomas classicos: ilusao de invulnerabilidade, racionalizacao coletiva, crenca na moralidade inerente do grupo, estereotipificacao de dissidentes, pressao para conformidade, auto-censura, ilusao de unanimidade e "guardioes da mente" que protegem o grupo de informacoes contrarias.

## Como se Manifesta em Pre-Programacao

### Em Design Reviews
- **Concordancia prematura:** O tech lead propoe uma solucao, todos concordam em 5 minutos. Nenhuma alternativa e discutida.
- **Auto-censura:** Um junior tem uma preocupacao valida mas nao verbaliza porque "todo mundo parece concordar."
- **Pressao social:** Quem questiona e rotulado como "negativo" ou "bloqueador."
- **Deferencia a autoridade:** "Se o arquiteto diz que e a melhor opcao, deve ser."

### Na Escolha de Tecnologias
- **Efeito bandwagon:** "Todo mundo esta usando Kubernetes, devemos usar tambem." Nenhuma analise critica.
- **Identidade do grupo:** "Nos somos uma equipe moderna, usamos microservicos." Tecnologia como identidade.

### Na Avaliacao de Riscos
- **Ilusao de invulnerabilidade:** "Somos uma equipe senior, nao cometemos esses erros."
- **Racionalizacao coletiva:** "Se todas as big techs usam essa abordagem, nao pode dar errado."
- **Minimizacao de dissidencia:** "Voce esta sendo pessimista, va ficar tudo bem."

## Como Mitigar

### 1. Advocacia do Diabo Formal
Designar um membro da equipe como "advogado do diabo" em cada design review. Sua funcao explicita e encontrar problemas e defender alternativas. Rotacionar o papel.

### 2. Escrita antes de Fala
Em design reviews, cada participante escreve feedback por escrito ANTES da discussão em grupo. Isso previne ancoragem e auto-censura.

### 3. Votacao Anonima
Para decisoes significativas, usar votacao anonima antes de abrir discussao. Revela se o consenso e real ou fabricado.

### 4. Convidar Outsiders
Incluir revisores de fora da equipe que nao tem pressao social para concordar. Eles trazem perspectiva fresca e nao temem desafiar o consenso.

### 5. Valorizar Dissidencia
Criar cultura explicita onde discordar e valorizado. Em retrospectivas, celebrar momentos em que alguem discordou e estava certo. Frase util: "Discordancia e um presente para a equipe."

### 6. Regra dos "Tres Porques"
Antes de aceitar uma decisao como consenso, perguntar "Por que?" tres vezes. Consenso superficial se revela quando nao sobrevive a tres niveis de questionamento.

### 7. Tempo de Reflexao
Nao tomar decisoes arquiteturais significativas na mesma reunião em que sao apresentadas. Dar 24-48h para reflexao individual.

## Exemplo Real

**Contexto:** Equipe de 8 pessoas em design review para novo sistema de pagamentos. O arquiteto sênior apresenta proposta de event sourcing com CQRS.

**Manifestacao do groupthink:**
- O arquiteto e respeitado e articulado. A apresentacao e convincente.
- 2 desenvolvedores tem duvidas sobre a complexidade, mas nao verbalizam.
- 1 desenvolvedor pergunta timidamente "Nao e complexo demais?" e recebe a resposta "E o padrao correto para esse dominio." A conversa muda de assunto.
- Todos "concordam" em 15 minutos.
- O PM registra: "Decisao unanime por event sourcing + CQRS."

**Resultado:** Implementacao 3x mais complexa que o necessario. O dominio nao exigia auditoria historica completa (principal justificativa para event sourcing). Apos 6 meses, a equipe simplifica para CRUD com audit log — que teria sido suficiente desde o inicio.

**O que deveria ter acontecido:**
- Design doc enviado 48h antes da review. Cada pessoa escreve feedback por escrito.
- Um membro designado como advogado do diabo argumenta contra event sourcing.
- Votacao anonima: "Quao confiante voce esta de que event sourcing e a melhor escolha?" Resultado revelaria que 4 de 8 tinham duvidas.
- Discussão aberta das duvidas, com dados: "Quais requisitos especificos exigem event sourcing? CRUD + audit log atende?"
- Decisao informada com trade-offs explicitos.
