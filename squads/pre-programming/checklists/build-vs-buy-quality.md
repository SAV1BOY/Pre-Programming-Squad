# Checklist: Qualidade da Análise Build vs Buy

## Propósito
Garantir que a decisão entre construir internamente, reutilizar componentes existentes ou adquirir soluções prontas é fundamentada em critérios claros de ROI, manutenção e risco.

## Quando Usar
- Quando surge a necessidade de uma funcionalidade que pode existir como produto/serviço
- Antes de iniciar desenvolvimento de componentes genéricos
- Quando há pressão para "usar a ferramenta X" sem análise

---

## Checklist

### Reuso Interno
- [ ] Soluções internas existentes foram pesquisadas antes de build ou buy
- [ ] Componentes compartilhados (libs, serviços) do ecossistema foram avaliados
- [ ] Custo de adaptação de solução interna existente foi estimado
- [ ] Responsabilidade de manutenção da solução interna está clara
- [ ] Capacidade da solução interna de atender os requisitos foi avaliada

### Dependências e Lock-in
- [ ] Nível de acoplamento com vendor/ferramenta está avaliado
- [ ] Custo de migração futura (saída do vendor) está estimado
- [ ] Padrões abertos vs proprietários foram considerados
- [ ] Riscos de descontinuação do produto/vendor foram avaliados
- [ ] Alternativas de mercado existem caso o vendor falhe

### Manutenção
- [ ] Custo de manutenção de solução build está estimado (time, infra)
- [ ] Custo de manutenção de solução buy está estimado (licença, suporte)
- [ ] Responsabilidade por atualizações e patches está definida
- [ ] Suporte disponível para a opção escolhida está avaliado
- [ ] Curva de aprendizado do time para cada opção está estimada

### ROI (Retorno sobre Investimento)
- [ ] Custo total de propriedade (TCO) está calculado para cada opção (3-5 anos)
- [ ] Time-to-market de cada opção está comparado
- [ ] Valor diferencial de build custom vs commodity está avaliado
- [ ] Custo de oportunidade (o que o time deixa de fazer) está considerado
- [ ] Breakeven point entre build e buy está identificado

### Adequação
- [ ] A opção buy atende pelo menos 80% dos requisitos out-of-the-box
- [ ] Customizações necessárias no buy estão mapeadas e viáveis
- [ ] A opção build justifica-se como diferencial competitivo
- [ ] Requisitos de segurança e compliance são atendidos pela opção escolhida
- [ ] Escalabilidade da opção escolhida atende a projeções futuras

---

## Critérios de Aprovação
- **Mínimo**: ROI e Dependências/Lock-in completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Decisão sem análise de TCO ou lock-in não avaliado

## Sinais de Alerta (Red Flags)
- "Vamos construir porque podemos" (síndrome do Not Invented Here)
- Buy de ferramenta que atende 30% dos requisitos com "customizações futuras"
- Lock-in total em vendor sem plano de saída
- Análise de ROI que ignora custo de manutenção contínua
- Decisão baseada apenas em experiência prévia do time com a ferramenta

## Agente Responsável
**Agente de Solution Architecture** — responsável por análise técnica e financeira de build vs buy.
