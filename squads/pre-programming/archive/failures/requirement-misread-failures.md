# Falhas por Leitura Incorreta de Requisitos

## Objetivo

Catalogar casos reais onde requisitos foram mal interpretados na fase de pré-programação, resultando em retrabalho significativo. Cada caso inclui análise de causa raiz e medidas preventivas.

---

## Caso 1: "Exportar para CSV" vs. "Relatório Exportável"

### O Que Aconteceu
O PRD dizia "usuário deve poder exportar dados para análise externa". O time implementou um botão de export CSV simples. O stakeholder esperava um relatório formatado com cabeçalhos, totais, filtros aplicados e formatação condicional — essencialmente um Excel complexo, não um CSV raw.

### O Que Deu Errado
- A palavra "exportar" foi interpretada como dump de dados
- "Análise externa" foi interpretada como "vai abrir no Excel" quando significava "vai apresentar para diretoria"
- Nenhuma pergunta de clarificação foi feita sobre formato ou audiência final

### Causa Raiz
**Ambiguidade não desafiada.** O requisito usava linguagem vaga ("exportar dados") e o time assumiu a interpretação mais simples em vez de perguntar. Não houve sessão de refinamento entre produto e engenharia.

### Como Prevenir
1. Quando um requisito contém verbos genéricos (exportar, visualizar, gerenciar), criar lista de interpretações possíveis e validar com stakeholder
2. Perguntar "quem é o consumidor final do output?" — isso revela expectativas de formato
3. Pedir mockup ou exemplo do output esperado, mesmo que em rascunho

### Checklist Atualizado
- [ ] Verbos genéricos no PRD foram desambiguados?
- [ ] O consumidor final do output está identificado?
- [ ] Existe exemplo ou mockup do resultado esperado?
- [ ] As interpretações alternativas do requisito foram listadas e eliminadas?

---

## Caso 2: "Tempo Real" — Interpretações Divergentes

### O Que Aconteceu
Requisito: "Dashboard deve mostrar dados em tempo real". Engenharia implementou WebSocket com updates a cada 100ms. Produto esperava refresh a cada 30 segundos. Infraestrutura custou 5x mais do que o necessário.

### O Que Deu Errado
- "Tempo real" tem significados completamente diferentes para produto e engenharia
- Nenhuma definição de latência aceitável foi estabelecida
- O custo de infraestrutura não foi estimado antes da implementação

### Causa Raiz
**Jargão técnico sem definição compartilhada.** "Tempo real" é um dos termos mais perigosos em requisitos porque cada disciplina tem uma definição diferente. Sem SLA de latência explícito, engenharia otimizou para o cenário extremo.

### Como Prevenir
1. Banir termos como "tempo real", "rápido", "escalável" sem definição numérica
2. Sempre traduzir para SLA: "dados atualizados a cada X segundos" ou "latência máxima de Xms"
3. Incluir estimativa de custo de infraestrutura para cada nível de "realtime"

### Checklist Atualizado
- [ ] Termos subjetivos (tempo real, rápido, escalável) foram substituídos por métricas?
- [ ] SLAs de latência estão definidos com valores numéricos?
- [ ] O custo incremental de cada nível de performance foi estimado?

---

## Caso 3: Requisito Implícito de Multi-idioma

### O Que Aconteceu
Sistema implementado inteiramente em português. Três meses depois, cliente Enterprise exigiu inglês e espanhol, o que estava mencionado em uma nota de rodapé do contrato comercial. Refatoração de todas as strings hardcoded levou 6 semanas.

### O Que Deu Errado
- Requisito de internacionalização estava no contrato comercial, não no PRD
- Time de produto não comunicou restrição contratual
- Strings foram hardcoded em toda a aplicação
- Sem framework de i18n desde o início, refactor foi invasivo

### Causa Raiz
**Fontes de requisitos não consolidadas.** Requisitos vinham de PRD, contratos comerciais e conversas em Slack. Não havia processo de consolidação que garantisse que todas as fontes fossem revisadas.

### Como Prevenir
1. Checklist de fontes de requisitos: PRD, contratos, regulação, SLAs comerciais, feedback de vendas
2. Perguntar explicitamente: "existem requisitos contratuais que afetam esta feature?"
3. Para qualquer texto visível ao usuário, sempre perguntar sobre i18n na fase de design

### Checklist Atualizado
- [ ] Fontes além do PRD foram consultadas (contratos, regulação, SLAs)?
- [ ] Requisitos contratuais foram identificados e incorporados?
- [ ] Necessidade de internacionalização foi avaliada?
- [ ] Strings são externalizadas desde o início?

---

## Caso 4: "Igual ao Concorrente" — Requisito por Referência

### O Que Aconteceu
PRD dizia "funcionalidade de agendamento similar ao Calendly". Time implementou agendamento básico com slots fixos. Stakeholder esperava: timezone automático, buffer entre reuniões, round-robin entre atendentes, integração com Google Calendar e link de videoconferência automático. Escopo real era 5x maior.

### O Que Deu Errado
- Requisito por referência ("similar ao X") não decompõe o que exatamente é similar
- Cada pessoa tem uma percepção diferente do que o concorrente faz
- Não houve análise detalhada das funcionalidades do Calendly antes da estimativa

### Causa Raiz
**Requisito por analogia sem decomposição.** "Igual ao X" parece claro mas esconde dezenas de decisões e funcionalidades implícitas. Sem decomposição feature-by-feature, o escopo é uma surpresa.

### Como Prevenir
1. Quando o requisito referencia um produto concorrente, fazer decomposição feature-by-feature
2. Classificar cada feature como: "deve ter", "nice to have" ou "fora do escopo"
3. Documentar explicitamente o que NÃO será implementado da referência

### Checklist Atualizado
- [ ] Referências a produtos externos foram decompostas em features individuais?
- [ ] Cada feature foi classificada (must have / nice to have / out of scope)?
- [ ] O que NÃO será copiado da referência está documentado?

---

## Resumo de Padrões

| Padrão | Frequência | Impacto Médio |
|--------|------------|---------------|
| Verbo genérico não desambiguado | Alta | 2-4 semanas de retrabalho |
| Termo subjetivo sem métrica | Alta | Custo de infra 2-5x maior |
| Requisito em fonte não consultada | Média | 4-8 semanas de refactor |
| Requisito por referência sem decomposição | Média | Escopo 3-5x maior |

---

## Checklist Consolidado — Leitura de Requisitos

- [ ] Verbos genéricos foram desambiguados com exemplos concretos?
- [ ] Termos subjetivos foram substituídos por métricas?
- [ ] Todas as fontes de requisitos foram consultadas?
- [ ] Referências a produtos externos foram decompostas?
- [ ] O consumidor final de cada output está identificado?
- [ ] Existe exemplo ou mockup para funcionalidades ambíguas?
- [ ] Requisitos contratuais e regulatórios foram verificados?
- [ ] O não-escopo está explícito e validado com stakeholder?
