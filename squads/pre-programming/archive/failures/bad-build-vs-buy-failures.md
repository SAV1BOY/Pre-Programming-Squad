# Falhas em Decisões Build vs. Buy

## Objetivo

Catalogar casos onde a decisão de construir internamente ou comprar/adotar solução pronta foi errada, gerando custo desnecessário, atraso ou dependência perigosa.

---

## Caso 1: Construir Motor de Busca Interno (Deveria Ter Comprado)

### O Que Aconteceu
E-commerce decidiu construir motor de busca próprio "para ter controle total". Após 6 meses de desenvolvimento com 3 devs, o motor suportava busca textual básica. Sem: fuzzy search, sinônimos, facets, boosting, analytics de busca. Enquanto isso, concorrentes usando Algolia ou Elasticsearch entregavam experiência de busca superior. Após 1 ano, abandonaram o motor próprio e migraram para Elasticsearch.

### O Que Deu Errado
- Custo de construir subestimado em 5x (estimativa: 2 meses, real: 12+ meses para chegar em paridade)
- "Controle total" era requisito emocional, não técnico — funcionalidades necessárias eram padrão
- 3 devs dedicados por 1 ano = custo de oportunidade enorme
- Motor próprio nunca atingiu paridade de features com soluções existentes

### Causa Raiz
**Viés de "Not Invented Here".** O time preferiu construir porque subestimou a complexidade do domínio (search é difícil) e superestimou a necessidade de customização. "Controle total" é raramente necessário quando soluções maduras têm APIs de extensibilidade.

### Como Prevenir
1. Estimar honestamente o tempo para atingir paridade de features com soluções existentes
2. Listar funcionalidades necessárias e verificar quais são cobertas por soluções prontas
3. Calcular custo real: devs x meses + custo de manutenção futura vs. licença da solução

### Checklist Atualizado
- [ ] Custo de construir foi estimado incluindo manutenção de 2 anos?
- [ ] Funcionalidades necessárias foram comparadas feature-by-feature com soluções prontas?
- [ ] "Controle total" foi decomposto em necessidades concretas de customização?
- [ ] Custo de oportunidade (o que os devs fariam em vez disso) foi considerado?

---

## Caso 2: Adotar SaaS de Workflow sem Avaliar Lock-in (Deveria Ter Construído)

### O Que Aconteceu
Time adotou SaaS de workflow (no-code) para automatizar processos internos. Após 18 meses, 47 workflows críticos rodavam na plataforma. Quando o SaaS aumentou preço em 300% e removeu funcionalidades do plano atual, migração era inviável no curto prazo — todos os workflows estavam em formato proprietário sem export.

### O Que Deu Errado
- Nenhuma avaliação de lock-in antes da adoção
- Formato proprietário sem opção de export ou portabilidade
- Custo crescente não previsto em projeção financeira
- Sem plano de contingência para mudança de vendor

### Causa Raiz
**Lock-in não avaliado.** A decisão de "buy" não considerou o custo de saída. Quanto mais processos migram para a plataforma, mais difícil e caro é sair. O custo total inclui não só a licença, mas o custo de exit.

### Como Prevenir
1. Antes de adotar SaaS, avaliar: portabilidade de dados, formatos de export, APIs de migração
2. Calcular custo de saída (exit cost) como parte do TCO
3. Definir limite de dependência: máximo de processos críticos em uma única plataforma
4. Manter abstração mínima que permita trocar vendor sem reescrever lógica de negócio

### Checklist Atualizado
- [ ] Portabilidade de dados e formatos de export foram avaliados?
- [ ] Custo de saída (exit cost) foi estimado e incluído no TCO?
- [ ] Existe limite definido para processos críticos em plataforma única?
- [ ] Cláusulas contratuais de preço e continuidade foram analisadas?

---

## Caso 3: Construir Framework de UI Interno (Deveria Ter Comprado)

### O Que Aconteceu
Time decidiu construir design system e component library próprios "porque nenhum framework atende 100%". Após 8 meses, a biblioteca tinha 30 componentes com qualidade inconsistente. Faltavam: acessibilidade, responsividade, internacionalização, temas. Time de produto frustrado com velocidade de entrega. Migração para Material UI + customização teria levado 3 semanas.

### O Que Deu Errado
- Requisito de "100% custom" não era real — 90% dos componentes eram padrão (botão, input, tabela)
- Acessibilidade e responsividade subestimadas (cada uma é projeto próprio)
- Manutenção de component library virou tempo integral de 1 dev
- Qualidade inconsistente entre componentes criados por diferentes devs

### Causa Raiz
**Subestimação da complexidade de fundação.** Bibliotecas de UI parecem simples na superfície, mas incluem acessibilidade, i18n, temas, responsividade, testes cross-browser e performance. Construir isso é produto próprio, não tarefa lateral.

### Como Prevenir
1. Listar requisitos não-funcionais de componentes (a11y, i18n, responsive, performance)
2. Avaliar frameworks existentes com base nesses requisitos, não apenas design visual
3. Preferir framework existente + customização sobre construção from scratch
4. Se construir, tratar como produto com roadmap, testes e ownership

### Checklist Atualizado
- [ ] Requisitos não-funcionais (a11y, i18n, responsive) foram incluídos na avaliação?
- [ ] Frameworks existentes foram avaliados com critérios objetivos?
- [ ] Custo de manutenção contínua da solução interna foi projetado?

---

## Caso 4: Comprar Ferramenta de Observabilidade Errada (Deveria Ter Avaliado Melhor)

### O Que Aconteceu
Time comprou licença enterprise de ferramenta de APM por R$180K/ano baseado em demo do vendor. Após 3 meses de implementação, descobriram que: (1) agent consumia 15% de CPU, (2) integração com stack existente (Kafka, Redis) era parcial, (3) dashboards custom eram limitados. Solução open-source (Grafana + Prometheus + Jaeger) atendia 95% dos requisitos por custo 10x menor.

### O Que Deu Errado
- Decisão baseada em demo do vendor (cenário otimista) sem PoC no ambiente real
- Sem avaliação de alternativas open-source
- Contrato de 1 ano assinado antes de validar integração com stack existente
- Overhead de agent não testado em produção

### Causa Raiz
**Decisão de compra sem Proof of Concept.** Demos de vendors mostram o melhor cenário. Sem PoC no ambiente real, problemas de integração e performance só aparecem após a compra.

### Como Prevenir
1. Toda decisão de compra > R$50K requer PoC de no mínimo 2 semanas no ambiente real
2. Avaliar pelo menos 2 alternativas (incluindo open-source)
3. Testar integração com stack existente antes de assinar contrato
4. Negociar período de trial ou cláusula de saída no contrato

### Checklist Atualizado
- [ ] PoC foi realizado no ambiente real (não apenas demo do vendor)?
- [ ] Alternativas (incluindo open-source) foram avaliadas?
- [ ] Integração com stack existente foi testada?
- [ ] Contrato inclui período de trial ou cláusula de saída?

---

## Resumo de Padrões

| Padrão | Frequência | Impacto Médio |
|--------|------------|---------------|
| Build quando deveria Buy (NIH) | Alta | 6-12 meses de atraso |
| Buy sem avaliar lock-in | Média | Dependência cara e arriscada |
| Build subestimando complexidade | Alta | 3-5x custo estimado |
| Buy sem PoC no ambiente real | Média | R$50K-200K desperdiçados |

---

## Checklist Consolidado — Build vs. Buy

- [ ] A decisão tem análise de custo completa (build + manutenção vs. licença + integração)?
- [ ] "Controle total" foi decomposto em necessidades concretas?
- [ ] Lock-in e custo de saída foram avaliados para opções de compra?
- [ ] PoC foi realizado no ambiente real para soluções a serem compradas?
- [ ] Alternativas (incluindo open-source) foram comparadas?
- [ ] Custo de oportunidade dos desenvolvedores foi considerado?
- [ ] Requisitos não-funcionais foram incluídos na comparação?
- [ ] Projeção de custo de 2 anos foi feita para ambos cenários?
