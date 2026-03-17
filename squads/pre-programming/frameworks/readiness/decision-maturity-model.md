# Decision Maturity Model

## Título e Propósito

O **Decision Maturity Model** é um framework para avaliar o grau de maturidade das decisões tomadas durante a pré-programação — desde intuições cruas até decisões validadas com dados. O propósito é garantir que decisões críticas tenham o nível adequado de maturidade antes que a equipe se comprometa com implementação, enquanto decisões de baixo impacto podem avançar com menos rigor.

## Quando Usar

- Para avaliar se as decisões do projeto estão maduras o suficiente para implementar
- Quando há desconforto sobre a base de uma decisão mas é difícil articular por quê
- Em revisões de projeto para verificar quais decisões precisam de mais trabalho
- Quando decisões estão sendo tomadas sob pressão de tempo e é preciso avaliar o risco
- Para calibrar o nível de esforço de validação proporcional ao impacto da decisão

## Conceitos-Chave

1. **Maturidade da Decisão**: O grau de confiança justificável na decisão, baseado na qualidade da informação e análise.
2. **Níveis de Maturidade**: De L0 (palpite) a L4 (validado em produção). Cada nível oferece mais confiança e custa mais esforço.
3. **Maturidade Adequada**: Nem toda decisão precisa de L4. O nível necessário depende do impacto e reversibilidade.
4. **Gap de Maturidade**: Diferença entre o nível atual e o nível necessário. Gaps em decisões críticas são riscos.
5. **Custo de Maturação**: O esforço para subir de nível. Às vezes é uma conversa; às vezes é um protótipo de 2 semanas.

## Processo / Passos

### Passo 1 — Listar Decisões Tomadas
Compile todas as decisões relevantes do projeto: tecnologia, arquitetura, escopo, priorização, design.

### Passo 2 — Classificar Nível Atual de Cada Decisão
- **L0 — Palpite**: Baseado em intuição sem dados. "Acho que funciona."
- **L1 — Opinião Informada**: Baseado em experiência relevante ou referência. "Em projetos similares, funcionou."
- **L2 — Análise**: Baseado em investigação estruturada: comparação de opções, avaliação de trade-offs. "Analisamos 3 opções e escolhemos por critérios."
- **L3 — Validação**: Baseado em evidência concreta: spike técnico, protótipo, teste com usuários, dados de produção. "Testamos e os dados mostram."
- **L4 — Comprovação em Produção**: Baseado em resultados reais em produção. "Está rodando e os resultados confirmam."

### Passo 3 — Definir Nível Necessário
Para cada decisão, defina o nível mínimo de maturidade necessário baseado em:
- Impacto se errada (alto → mais maturidade)
- Reversibilidade (irreversível → mais maturidade)
- Custo de estar errado (alto → mais maturidade)

### Passo 4 — Identificar Gaps
Compare nível atual com nível necessário. Decisões com gap são riscos.

### Passo 5 — Planejar Maturação
Para cada gap, defina como subir de nível: conversa com especialista (L0→L1), análise estruturada (L1→L2), spike/protótipo (L2→L3).

### Passo 6 — Executar
Dedique tempo explícito para maturar decisões críticas antes de implementar.

### Passo 7 — Aceitar Riscos Residuais
Algumas decisões não podem ser maturadas antes da implementação. Documente o risco aceito.

## Perguntas de Ativação

- "Em que nível de maturidade está essa decisão? Palpite, opinião, análise ou validação?"
- "Qual é a base dessa decisão — intuição, experiência, dados ou teste?"
- "Se essa decisão estiver errada, qual é o custo?"
- "Podemos subir o nível de maturidade dessa decisão antes de implementar?"
- "Quanto esforço é necessário para validar isso com um spike ou protótipo?"
- "Estamos confortáveis com o nível de maturidade atual para o risco envolvido?"

## Output Esperado

| Decisão | Nível Atual | Nível Necessário | Gap | Impacto se Errada | Custo de Maturação | Ação |
|---|---|---|---|---|---|---|
| Usar PostgreSQL | L2 (análise comparativa) | L2 | OK | Alto (migração) | — | Nenhuma |
| Modelo de dados de pedidos | L1 (experiência anterior) | L3 | GAP | Alto (refactor extenso) | 3 dias (protótipo) | Fazer spike com dados reais |
| Feature de busca com Elasticsearch | L0 (CTO sugeriu) | L2 | GAP | Médio (pode trocar) | 1 dia (análise) | Comparar com alternativas |
| Framework frontend: React | L3 (equipe já usa em produção) | L2 | OK (acima) | Baixo (reversível) | — | Nenhuma |
| SLA de 99.9% | L0 (stakeholder pediu) | L2 | GAP | Alto (custo de infra) | 4h (análise de custo vs. necessidade) | Analisar se 99.9% é realmente necessário |

**Resumo**: 5 decisões, 3 gaps identificados. 2 gaps podem ser fechados em 1 semana de trabalho focado.

## Armadilhas Comuns

1. **Decidir por palpite em questões críticas**: L0 é aceitável para decisões de baixo impacto. Para decisões críticas, é negligência.
2. **Exigir L4 para tudo**: Nem tudo pode ou precisa ser validado em produção antes de decidir. Calibre o nível ao impacto.
3. **Confundir opinião forte com evidência**: "Tenho certeza que funciona" não é L3. L3 requer dados.
4. **Não investir em maturação**: Saber que a decisão está em L0 e avançar mesmo assim sem tentar subir.
5. **Falsa maturidade**: "Fizemos uma análise" que na verdade foi uma conversa informal de 5 minutos não é L2.
6. **Maturidade como burocracia**: Se o processo de maturar decisões atrasa o projeto sem reduzir risco, está mal calibrado.
