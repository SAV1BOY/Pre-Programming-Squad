# Marketplace - Readiness Primer

## Contexto da Industria

Marketplaces conectam oferta e demanda: vendedores e compradores (Mercado Livre, Amazon), prestadores e consumidores de servico (iFood, Uber), profissionais e clientes (GetNinjas). O modelo e fundamentalmente diferente de e-commerce proprio: o marketplace nao controla o estoque, a qualidade do produto/servico ou a entrega — ele facilita a transacao e garante confianca.

## Desafios Especificos de Pre-Programacao

### O Problema do Chicken-and-Egg
Marketplace sem vendedores nao atrai compradores. Sem compradores, nao atrai vendedores. Na pre-programacao, o design deve suportar crescimento desequilibrado e bootstrapping de um dos lados.

### Multi-Sided Platform
Cada lado do marketplace (buyer, seller, e frequentemente um terceiro como entregador) tem necessidades, interfaces e fluxos diferentes. Na pre-programacao, modelar o dominio de cada lado e suas interacoes.

### Trust & Safety
O marketplace e responsavel por garantir confianca: reviews, ratings, disputas, moderacao, prevencao de fraude. Na pre-programacao, projetar o sistema de trust desde o inicio, nao como afterthought.

### Take Rate e Financeiro
O modelo de receita envolve comissao (take rate) sobre transacoes. Fluxo financeiro complexo: buyer paga, marketplace retém comissao, repassa ao seller (split payment). Na pre-programacao, o motor financeiro e critico.

### Matching e Discovery
Conectar o buyer certo ao seller certo: algoritmos de ranking, busca, recomendacao, precificacao dinamica. Na pre-programacao, a estrategia de matching influencia toda a arquitetura.

## Regulacoes Relevantes

| Regulacao | Escopo | Impacto no Design |
|---|---|---|
| CDC | Responsabilidade solidaria | Marketplace pode ser responsavel pelo produto/servico |
| LGPD | Dados de compradores e vendedores | Dois lados de dados pessoais para gerenciar |
| BACEN (se intermediacao financeira) | Split payment, escrow | Regulacao de pagamento, limites |
| Lei do Marketplace (PL em andamento) | Responsabilidades do marketplace | Obrigacoes de transparencia, moderacao |
| Regulacoes setoriais | Depende do vertical | Alimentacao (ANVISA), transporte (regulacao local) |

## Padroes de Readiness

### Checklist de Pre-Programacao para Marketplace

**Modelo de Negocio:**
- [ ] Lados do marketplace identificados (buyer, seller, delivery, etc.).
- [ ] Fluxo financeiro mapeado (pagamento, retencao, split, repasse).
- [ ] Take rate e modelo de comissao definidos.
- [ ] Regras de cancelamento e reembolso especificadas por lado.

**Trust & Safety:**
- [ ] Sistema de ratings/reviews projetado.
- [ ] Fluxo de disputas definido (abertura, mediacao, resolucao).
- [ ] Moderacao de conteudo planejada (anuncios, reviews, mensagens).
- [ ] Prevencao de fraude: identidade falsa, transacoes fraudulentas.
- [ ] KYC para sellers/prestadores definido.

**Matching e Discovery:**
- [ ] Algoritmo de ranking/matching definido (criterios, pesos).
- [ ] Estrategia de busca definida.
- [ ] Personalizacao planejada.
- [ ] Metricas de qualidade do match definidas.

**Financeiro:**
- [ ] Split payment implementado ou integrado.
- [ ] Escrow (retenção ate confirmacao) se aplicavel.
- [ ] Conciliacao financeira entre lados.
- [ ] Tratamento de chargebacks e disputas financeiras.

**Escalabilidade:**
- [ ] Design suporta crescimento assimetrico dos lados.
- [ ] Onboarding de sellers escalavel (self-service).
- [ ] Cataloging/listing escalavel.

## Riscos Tipicos

1. **Fraude entre participantes:** Seller fantasma, buyer fraudulento, conluio.
2. **Desequilibrio de lados:** Excesso de sellers sem buyers (ou vice-versa) degrada experiencia.
3. **Problema financeiro:** Split payment errado, repasse atrasado, comissao calculada incorretamente.
4. **Disputa mal resolvida:** Perda de confianca de um ou ambos os lados.
5. **Qualidade do supply:** Sellers de baixa qualidade degradam a plataforma inteira.
6. **Desintermediacao:** Participantes transacionam fora da plataforma para evitar comissao.
