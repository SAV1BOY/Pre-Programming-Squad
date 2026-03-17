# E-commerce - Readiness Primer

## Contexto da Industria

E-commerce abrange vendas online de produtos e servicos: B2C, B2B, D2C, marketplaces. No Brasil, o mercado cresce consistentemente e inclui particularidades como Pix como meio de pagamento dominante, boleto bancario, parcelamento sem juros, e logistica complexa em um pais continental. Eventos de pico como Black Friday podem gerar 10-50x do trafego normal.

## Desafios Especificos de Pre-Programacao

### Picos de Trafego Extremos
Black Friday, datas comemorativas e flash sales geram picos de 10-50x. Na pre-programacao, o design deve ser avaliado para capacidade de pico, nao para media. Auto-scaling, caching agressivo e graceful degradation sao essenciais.

### Catalogo e Busca
Catalogos com milhoes de SKUs, atributos variados, imagens, precos dinamicos. Busca deve ser rapida (<300ms), relevante e tolerante a erros. Na pre-programacao, a estrategia de busca (Elasticsearch, Algolia) e indexacao deve ser definida.

### Precificacao e Promocoes
Regras complexas de precificacao: descontos por quantidade, cupons, cashback, precos por regiao, parcelamento, frete gratis condicional. Na pre-programacao, o motor de precificacao e uma area de alto risco que requer modelagem cuidadosa.

### Estoque e Logistica
Consistencia de estoque em tempo real, reserva de estoque durante checkout, multiplos centros de distribuicao, calculo de frete por CEP, estimativa de entrega. Na pre-programacao, a estrategia de consistencia de estoque e critica.

### Checkout e Pagamentos
Conversao no checkout e a metrica mais valiosa. Cada segundo de latencia ou campo extra reduz conversao. Multiplos meios de pagamento (Pix, cartao, boleto, wallet). Na pre-programacao, o fluxo de checkout deve ser projetado para minimizar fricção.

## Regulacoes Relevantes

| Regulacao | Escopo | Impacto no Design |
|---|---|---|
| CDC (Codigo Defesa Consumidor) | Direitos do consumidor | Direito de arrependimento 7 dias, informacoes claras |
| LGPD | Dados pessoais | Consentimento, cookies, tracking |
| PCI-DSS | Dados de cartao | Tokenizacao, encriptacao, segmentacao |
| Decreto 7.962/2013 | E-commerce | Informacoes obrigatorias, atendimento, SAC |
| Nota Fiscal Eletronica | Fiscal | Integracao com SEFAZ, emissao automatica |

## Padroes de Readiness

### Checklist de Pre-Programacao para E-commerce

**Performance e Escalabilidade:**
- [ ] Estimativas de pico de trafego documentadas (QPS, concurrent users).
- [ ] Estrategia de caching definida (CDN, application cache, database cache).
- [ ] Auto-scaling configurado e testado.
- [ ] Graceful degradation definida (o que desligar primeiro sob carga).
- [ ] Plano de load testing antes de eventos de pico.

**Catalogo e Busca:**
- [ ] Engine de busca definida e justificada.
- [ ] Estrategia de indexacao definida (tempo de propagacao).
- [ ] Tolerancia a erros de busca (typos, sinonimos).
- [ ] Filtros e facetas definidos.

**Checkout e Pagamentos:**
- [ ] Fluxo de checkout mapeado com latencia maxima por etapa.
- [ ] Meios de pagamento definidos (Pix, cartao, boleto).
- [ ] Estrategia de parcelamento definida.
- [ ] Idempotencia em operacoes de pagamento.
- [ ] PCI-DSS compliance avaliada.

**Estoque:**
- [ ] Estrategia de consistencia de estoque definida (reserva, timeout).
- [ ] Tratamento de overselling definido.
- [ ] Integracao com multiplos CDs/warehouses planejada.

**Fiscal:**
- [ ] Integracao com emissao de NF-e planejada.
- [ ] Calculo de impostos por estado (ICMS, ST) definido.
- [ ] Contingencia para SEFAZ indisponivel planejada.

## Riscos Tipicos

1. **Indisponibilidade em Black Friday:** Perda financeira direta de milhoes, dano reputacional.
2. **Erro de preco em promocao:** Obrigacao legal de vender pelo preco anunciado (CDC).
3. **Overselling:** Vender produto sem estoque, cancelamento gera insatisfacao.
4. **Pagamento duplicado:** Cobrar duas vezes, estorno manual custoso.
5. **Problema fiscal:** NF-e nao emitida, multa da Receita Federal.
6. **Fraude em pagamento:** Chargebacks, perda financeira direta.
