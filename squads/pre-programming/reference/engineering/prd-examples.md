# Exemplos de Product Requirements Documents (PRDs)

## O que e um PRD

Um Product Requirements Document (PRD) descreve o que construir e por que, sem prescrever como. Define o problema, os usuarios-alvo, os requisitos funcionais e nao-funcionais, metricas de sucesso e restricoes. E a ponte entre product discovery e engenharia.

## Template Padrao

```markdown
# PRD: [Nome da Feature/Projeto]

**Autor:** [Product Manager]
**Ultima atualizacao:** [Data]
**Status:** Rascunho | Em Revisao | Aprovado | Em Desenvolvimento | Lancado

## 1. Problema e Oportunidade

### Problema
[Qual problema dos usuarios estamos resolvendo?]

### Evidencias
[Dados que demonstram que o problema existe: metricas, pesquisas, feedback.]

### Oportunidade
[Qual o impacto esperado de resolver o problema?]

## 2. Usuarios-Alvo

### Persona Primaria
[Quem e o usuario principal? Contexto, necessidades, comportamento.]

### Persona Secundaria
[Outros usuarios impactados.]

## 3. Objetivos e Metricas de Sucesso

### Objetivos
[O que queremos alcancar? Objetivos mensuráveis.]

### Metricas de Sucesso (KPIs)
[Como saberemos que deu certo? Metricas especificas com targets.]

### Metricas de Guarda (Guardrails)
[Metricas que nao devem piorar com a mudanca.]

## 4. Requisitos Funcionais

### Must-have (P0)
[Funcionalidades essenciais sem as quais o projeto nao tem valor.]

### Should-have (P1)
[Funcionalidades importantes mas nao bloqueantes para o lancamento.]

### Nice-to-have (P2)
[Funcionalidades desejaveis para versoes futuras.]

## 5. Requisitos Nao-Funcionais
[Performance, seguranca, escalabilidade, acessibilidade, compliance.]

## 6. Restricoes e Dependencias
[Limitacoes tecnicas, de prazo, regulatorias. Dependencias de outras equipes.]

## 7. Escopo Negativo (Fora de Escopo)
[O que explicitamente nao esta incluido.]

## 8. Timeline e Fases
[Marcos principais e entregas esperadas.]
```

## Exemplo 1: Sistema de Busca de Produtos

```markdown
# PRD: Busca Inteligente de Produtos

**Autor:** Ana Oliveira (PM)
**Status:** Aprovado

## 1. Problema e Oportunidade

### Problema
A busca atual do e-commerce tem taxa de "busca sem resultado" de 23%.
Usuarios que encontram resultados irrelevantes abandonam o site —
a taxa de bounce pos-busca e 45%. Perda estimada: R$ 2.1M/mes em
vendas perdidas.

### Evidencias
- Analytics: 23% das buscas retornam 0 resultados (ultimos 90 dias).
- Sessoes com busca: 45% bounce rate vs. 28% navegação direta.
- NPS de busca: 32 (medido em survey in-app, n=1.200).
- Top queries sem resultado: "tenis corrida", "notebook gamer", "fone bluetooth".

### Oportunidade
Reduzir busca sem resultado para < 5% e bounce pos-busca para < 25%
geraria estimado R$ 800k-1.2M/mes em receita incremental.

## 2. Usuarios-Alvo

### Persona Primaria: Comprador Direto
Sabe o que quer comprar. Usa busca como atalho. Frustra-se com resultados
irrelevantes. 60% do trafego de busca.

### Persona Secundaria: Explorador
Busca por categorias amplas ("presente para mae"). Precisa de sugestoes
e refinamento. 25% do trafego de busca.

## 3. Objetivos e Metricas de Sucesso

### Metricas de Sucesso
- Taxa de busca sem resultado: de 23% para < 5% em 90 dias.
- Bounce pos-busca: de 45% para < 25% em 90 dias.
- Conversao pos-busca: de 3.2% para > 5% em 90 dias.
- NPS de busca: de 32 para > 50 em 180 dias.

### Guardrails
- Latencia de busca p99 < 300ms (atual: 180ms).
- Custo de infra de busca: aumento maximo de 30%.
- Taxa de cliques no primeiro resultado nao deve cair abaixo de 25%.

## 4. Requisitos Funcionais

### Must-have (P0)
- Tolerancia a erros de digitacao (typo correction).
- Busca por sinonimos (ex: "tenis" = "calcado esportivo").
- Autocomplete com sugestoes baseadas em popularidade.
- Resultados ranqueados por relevancia + popularidade + margem.

### Should-have (P1)
- Filtros dinamicos baseados nos resultados (faceted search).
- "Voce quis dizer..." para queries ambiguas.
- Busca por atributos (ex: "notebook 16gb ram").

### Nice-to-have (P2)
- Busca por imagem (visual search).
- Busca em linguagem natural ("notebook bom e barato para trabalho").
- Personalizacao baseada em historico de compras.

## 5. Requisitos Nao-Funcionais
- Latencia p99: < 300ms.
- Disponibilidade: 99.95%.
- Escala: suportar 500 queries/segundo em pico (Black Friday: 2.000 qps).
- Indexacao: novos produtos disponiveis em busca em < 5 minutos.
- Acessibilidade: WCAG 2.1 AA para interface de busca.

## 6. Restricoes
- Solucao deve rodar em AWS (nossa cloud atual).
- Budget de infra adicional: ate R$ 15k/mes.
- Equipe disponivel: 2 backend + 1 frontend + 0.5 data engineer.
- Deadline desejavel: MVP em 6 semanas, full rollout em 12 semanas.

## 7. Fora de Escopo
- Reformulacao visual da pagina de resultados (projeto separado).
- Busca em conteudo editorial (blog, guias de compra).
- Recomendacoes na homepage (projeto de personalizacao separado).
```

## Exemplo 2: Sistema de Notificacoes Transacionais

```markdown
# PRD: Notificacoes Transacionais Multi-Canal

**Autor:** Pedro Lima (PM)
**Status:** Em Revisao

## 1. Problema
Usuarios reportam que nao recebem atualizacoes de status de pedido.
Suporte recebe ~800 chamados/mes sobre "onde esta meu pedido" que
poderiam ser evitados com notificacoes proativas. Custo de suporte:
~R$ 45/chamado = R$ 36k/mes.

## 3. Metricas de Sucesso
- Chamados "onde esta meu pedido": reduzir 60% em 90 dias.
- Taxa de abertura de notificacoes: > 40% para email, > 60% para push.
- NPS do processo de entrega: de 41 para > 55.

### Guardrails
- Taxa de unsubscribe: < 2%.
- Notificacoes por usuario por dia: maximo 5.

## 4. Requisitos Funcionais P0
- Notificacao automatica em cada mudanca de status do pedido.
- Canais: email e push notification.
- Preferencias de canal gerenciaveis pelo usuario.
- Templates com dados do pedido (itens, valor, prazo estimado).
- Link direto para rastreamento no corpo da notificacao.
```

## O que o Squad de Pre-Programacao Deve Avaliar no PRD

### Completude
- Todos os requisitos funcionais P0 estao especificados?
- Requisitos nao-funcionais estao quantificados (nao "deve ser rapido")?
- Metricas de sucesso sao mensuráveis?
- Restricoes tecnicas estao documentadas?

### Viabilidade
- Os requisitos nao-funcionais sao atingiveis com o budget e equipe disponíveis?
- Existem dependencias tecnicas nao mencionadas?
- O timeline e realista para o escopo?

### Testabilidade
- Cada requisito P0 pode ser traduzido em criterios de aceitacao verificaveis?
- As metricas de sucesso podem ser medidas com a infraestrutura atual?

### Ambiguidade
- Ha requisitos que podem ser interpretados de multiplas formas?
- Termos subjetivos ("rapido", "facil", "intuitivo") estao quantificados?
- Cenarios de erro estao especificados?
