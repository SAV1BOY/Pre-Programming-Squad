# Heuristica de Disponibilidade em Risco

## Vies/Efeito

**Heuristica de Disponibilidade (Availability Heuristic):** A tendencia de julgar a probabilidade de um evento com base na facilidade com que exemplos vem a mente, em vez de dados estatisticos reais. Identificada por Tversky e Kahneman (1973).

## Descricao

Eventos vividos recentemente, dramaticos ou emocionalmente carregados sao mais "disponiveis" na memoria e, portanto, percebidos como mais provaveis. Apos um acidente de aviao, as pessoas superestimam o risco de voar — mesmo que dirigir continue sendo estatisticamente mais perigoso. O inverso tambem e verdadeiro: riscos que nunca experimentamos parecem improvaveis.

## Como se Manifesta em Pre-Programacao

### Na Avaliacao de Riscos Tecnicos
- **Superestimação de riscos recentes:** Se a equipe teve um incidente de DDoS recentemente, todos os designs serao avaliados com paranoia sobre DDoS, mesmo quando o risco real e baixo.
- **Subestimação de riscos nao experimentados:** Se a equipe nunca teve problema com data corruption, esse risco sera minimizado no design — mesmo sendo catastrofico.
- **Vies de midia tecnica:** Riscos que aparecem frequentemente em blog posts e conferencias (ex: "microservicos sao dificeis") recebem atencao desproporcional.

### Na Escolha de Tecnologias
- **Experiencia pessoal domina:** "PostgreSQL deu problema naquele projeto, vamos usar MongoDB." Um incidente pessoal supera dados objetivos de confiabilidade.
- **Historias de sucesso vividas:** "Usamos Redis com sucesso no projeto X, vamos usar para tudo." Generalizar experiencia especifica para contextos diferentes.

### Na Estimativa de Impacto
- **Incidentes dramaticos:** Um downtime de 4 horas que virou manchete pesa mais que 100 pequenos bugs que ninguem notou — mesmo que os 100 bugs custem mais no total.
- **Memoria seletiva:** Lembrar do projeto que deu certo com a tecnologia X e esquecer os tres que deram errado.

## Como Mitigar

### 1. Registro Sistematico de Incidentes
Manter um banco de dados de incidentes com classificacao por tipo, severidade e causa raiz. Usar dados do registro para avaliar riscos, nao memorias.

### 2. Matriz de Riscos com Dados
Para cada risco identificado, exigir dados que fundamentem a avaliacao de probabilidade e impacto. "Qual e a evidencia de que esse risco e provavel?"

### 3. Checklist de Riscos Padronizada
Usar uma lista padrao de categorias de risco (seguranca, performance, disponibilidade, dados, integracao, compliance) para que riscos "nao disponiveis" na memoria ainda sejam considerados.

### 4. Consultar Fontes Externas
Verificar relatorios de incidentes publicos (DORA reports, postmortems publicos) para calibrar a percepcao de risco com dados da industria.

### 5. Pre-Mortem Estruturado
Em vez de perguntar "Quais riscos voces veem?", usar categorias: "Quais riscos de seguranca? De performance? De dados? De integracao? De compliance?" Isso ativa categorias que nao viriam a mente espontaneamente.

### 6. Separar Vivencia de Probabilidade
Reconhecer explicitamente: "Estamos preocupados com X porque aconteceu recentemente, ou porque e objetivamente provavel?"

## Exemplo Real

**Contexto:** Apos um incidente grave de performance em producao causado por N+1 queries, a equipe esta projetando um novo servico.

**Manifestacao da heuristica:**
- 80% do tempo da design review e gasto discutindo otimizacao de queries e caching.
- Ninguem menciona seguranca — o servico manipula dados financeiros.
- Ninguem menciona resiliencia — o servico depende de 3 APIs externas.
- Ninguem menciona migracao de dados — o novo servico substituira dados de um sistema legado.
- O risco de performance e real, mas ocupa espaco desproporcional porque e o mais "disponivel" na memoria.

**O que deveria ter acontecido:**
- Usar checklist de riscos padronizada:
  - Performance: Sim, N+1 e risco real. Mitigacao: DataLoader, indexes, monitoring.
  - Seguranca: Dados financeiros requerem encriptacao em trânsito e repouso, auditoria, RBAC.
  - Resiliencia: 3 APIs externas precisam de timeout, circuit breaker, fallback.
  - Dados: Migracao de legado requer plano detalhado com validacao.
  - Compliance: Dados financeiros podem ter requisitos regulatorios.
- Alocar tempo da review proporcionalmente ao risco real, nao a memoria recente.
