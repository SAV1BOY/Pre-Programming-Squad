# Pre-Bug Risk Forecast

## Título e Propósito

O **Pre-Bug Risk Forecast** é um framework para prever onde bugs são mais prováveis de aparecer antes que o código seja escrito. O propósito é direcionar atenção, testes e cuidado de design para as áreas de maior risco — porque a distribuição de bugs não é uniforme: 80% dos bugs vêm de 20% do código, e essas áreas são frequentemente previsíveis.

## Quando Usar

- No planejamento de testes e QA antes da implementação
- Ao identificar componentes que merecem design extra cuidadoso
- Em revisões de arquitetura para antecipar fragilidades
- Quando recursos de QA são limitados e precisam ser focados
- Para calibrar estimativas — código de alto risco leva mais tempo

## Conceitos-Chave

1. **Indicadores de Risco de Bug**: Fatores que aumentam a probabilidade de bugs: complexidade ciclomática, acoplamento, código legado, equipe inexperiente, requisitos ambíguos.
2. **Hotspot de Bugs**: Área do código onde bugs se concentram. Geralmente são: lógica de negócio complexa, integrações, transformações de dados, concorrência.
3. **Risco Combinado**: Quando múltiplos indicadores convergem no mesmo componente, o risco é multiplicativo, não aditivo.
4. **Prevenção vs. Detecção**: Prevenir bugs no design é mais barato que detectá-los em teste e muito mais barato que corrigi-los em produção.
5. **Bug de Design vs. Bug de Implementação**: Bugs de design afetam a estrutura e são caros de corrigir. Bugs de implementação são localizados e mais baratos.

## Processo / Passos

### Passo 1 — Mapear Componentes do Projeto
Liste todos os componentes que serão implementados: módulos, serviços, integrações, fluxos.

### Passo 2 — Avaliar Indicadores de Risco
Para cada componente, avalie (1-5):
- Complexidade da lógica
- Número de integrações
- Ambiguidade dos requisitos
- Experiência da equipe com o domínio
- Presença de concorrência/estado
- Manipulação de dados sensíveis

### Passo 3 — Identificar Hotspots
Componentes com score alto em múltiplos indicadores são hotspots. Eles receberão atenção especial.

### Passo 4 — Projetar Prevenção
Para cada hotspot, defina medidas preventivas: design reviews, pair programming, testes mais rigorosos, prototipação, spike técnico.

### Passo 5 — Definir Estratégia de Teste Diferenciada
Hotspots recebem: mais testes unitários, testes de integração, testes de cenários de borda. Componentes de baixo risco recebem cobertura proporcional.

### Passo 6 — Ajustar Estimativas
Componentes de alto risco levam mais tempo para implementar com qualidade. Reflita isso nas estimativas.

### Passo 7 — Monitorar em Produção
Após deploy, monitore se bugs realmente se concentram nos hotspots previstos. Calibre o modelo para projetos futuros.

## Perguntas de Ativação

- "Onde bugs são mais prováveis de aparecer nesse projeto?"
- "Qual componente tem a lógica mais complexa ou os requisitos mais ambíguos?"
- "Temos experiência com esse tipo de integração ou é território novo?"
- "Se tivéssemos que apostar onde vai dar problema primeiro, onde seria?"
- "Esse componente envolve concorrência, estado compartilhado ou transformação complexa de dados?"
- "Quanto do nosso esforço de teste está focado nos hotspots vs. distribuído uniformemente?"

## Output Esperado

| Componente | Complexidade | Integrações | Ambiguidade | Experiência | Concorrência | Score | Classificação | Medidas Preventivas |
|---|---|---|---|---|---|---|---|---|
| Motor de desconto | 5 | 2 | 4 | 3 | 1 | 15 | HOTSPOT | Design review, testes extensivos de edge cases, pair programming |
| Sincronização de estoque | 3 | 4 | 2 | 2 | 5 | 16 | HOTSPOT | Spike para testar concorrência, idempotência, testes de carga |
| CRUD de usuários | 1 | 1 | 1 | 5 | 1 | 5 | Baixo risco | Testes padrão |
| Integração com ERP | 2 | 5 | 3 | 1 | 2 | 13 | Alto risco | Spike de integração, mock robusto, testes de contrato |
| Dashboard de métricas | 2 | 2 | 3 | 4 | 1 | 8 | Médio risco | Testes de dados agregados |

**Previsão**: 70% dos bugs concentrados em Motor de Desconto e Sincronização de Estoque.

## Armadilhas Comuns

1. **Distribuição uniforme de esforço de teste**: Testar tudo com a mesma intensidade subestima hotspots e desperdiça em áreas de baixo risco.
2. **Confiança excessiva em "código simples"**: Código que parece simples mas tem edge cases sutis (datas, moeda, unicode, timezones).
3. **Ignorar a experiência da equipe**: Uma equipe experiente no domínio terá menos bugs que uma equipe nova, mesmo com a mesma complexidade.
4. **Não ajustar estimativas**: Saber que um componente é hotspot mas não dar tempo extra para implementá-lo com cuidado.
5. **Previsão como certeza**: O forecast é probabilístico. Hotspots são mais prováveis de ter bugs, não certezas.
6. **Não calibrar**: Não comparar previsão com realidade para melhorar o modelo em projetos futuros.
