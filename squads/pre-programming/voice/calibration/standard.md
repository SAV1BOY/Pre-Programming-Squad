# Modo Padrão

## Nível de Detalhe

Balanceado entre contexto e conclusão. Inclui o raciocínio por trás das decisões, evidências que sustentam as recomendações e implicações identificadas. Suficiente para que alguém que não participou da discussão entenda o "porquê", não apenas o "o quê".

**Proporção alvo:** 30% contexto, 40% análise/decisão, 30% implicações e próximos passos.

## Quando Usar

- **Documentos de decisão** (ADRs, RFCs) — quando a justificativa precisa ser registrada
- **Revisões técnicas** — apresentar achados com evidência e recomendação
- **Análises de viabilidade** — quando produto ou liderança precisa entender trade-offs
- **Comunicação cross-squad** — quando a audiência tem contexto parcial
- **Handoffs entre fases** — quando o próximo grupo precisa entender premissas e restrições
- **Relatórios de risco** — quando o impacto e a probabilidade precisam de fundamentação

**Não usar quando:**
- A audiência já sabe tudo e quer apenas a decisão final (use conciso)
- O tema exige análise profunda com múltiplos cenários detalhados (use deep-dive)
- É uma auditoria formal com requisitos de compliance (use audit-mode)

## Extensão Esperada

- **ADR/RFC:** 1-2 páginas (contexto, opções, decisão, consequências)
- **Revisão técnica:** 1 página por tópico (achado, evidência, recomendação, severidade)
- **Análise de viabilidade:** 1-2 páginas (cenários, comparação, recomendação)
- **Total:** Tipicamente entre 200-600 palavras

## Exemplo

```
## Revisão Técnica — Serviço de Busca de Produtos

### Contexto
O serviço de busca atual usa PostgreSQL com full-text search para
catálogo de ~500k produtos. O time de produto reporta que a relevância
dos resultados está abaixo do aceitável: taxa de "busca sem clique"
subiu de 15% para 28% nos últimos 3 meses, indicando que usuários
não encontram o que procuram.

### Análise

Identificamos dois problemas distintos:

**1. Relevância** — O ranking atual usa ts_rank do PostgreSQL sem
customização. Não considera popularidade do produto, histórico de
vendas ou sinônimos. Resultado: buscar "notebook" não retorna
"laptop" e produtos fora de estoque aparecem no topo.

Evidência: análise das 100 buscas mais frequentes mostra que 35%
retornam resultados irrelevantes no top 3.

**2. Latência** — p95 de 1.8s para buscas com mais de 2 termos.
Causa: full-text search no PostgreSQL faz sequential scan em
consultas complexas porque o índice GIN não cobre todos os campos
buscáveis.

Evidência: query plan mostra Seq Scan em 40% das buscas com
filtros combinados.

### Opções Avaliadas

| Critério | Otimizar PG atual | Elasticsearch | Typesense |
|---|---|---|---|
| Relevância | Limitada | Excelente | Boa |
| Latência | Melhoria parcial | < 100ms | < 50ms |
| Esforço | 1 sprint | 3-4 sprints | 2 sprints |
| Custo operacional | Zero adicional | +$800/mês | +$200/mês |
| Sinônimos/typos | Manual | Nativo | Nativo |

### Recomendação

Adotar Typesense. Oferece o melhor equilíbrio entre melhoria de
relevância, esforço de implementação e custo operacional. O time
já tem experiência com Typesense no projeto interno de documentação.

O Elasticsearch é mais poderoso, mas o overhead operacional não se
justifica para o volume atual do catálogo.

### Próximos Passos
1. Spike de 3 dias para validar Typesense com subset do catálogo
2. Definir pipeline de sincronização PostgreSQL → Typesense
3. A/B test comparando busca atual vs. Typesense por 2 semanas
4. Decisão final baseada em métricas de "busca sem clique" e latência
```
