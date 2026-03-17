# O que é "Bom" em Cada Entregável do Squad

## Propósito

Definir padrões de qualidade explícitos para cada tipo de entregável produzido pelo Pre-Programming Squad. Serve como referência para auto-avaliação antes da entrega e como critério de revisão entre pares. "Bom" significa: completo, claro, acionável e que não gera dúvidas evitáveis para o receptor.

## Escopo

Todos os entregáveis produzidos pelo Pre-Programming Squad durante o ciclo de preparação de qualquer projeto.

## Definições

| Termo | Definição |
|---|---|
| Bom | Entregável que o receptor consegue usar sem precisar de esclarecimentos adicionais |
| Excelente | "Bom" + antecipa dúvidas do receptor e as responde proativamente |
| Insuficiente | Entregável que gera mais de 2 perguntas de esclarecimento do receptor |

## Processo

Antes de entregar qualquer artefato, o membro do squad revisa contra os critérios abaixo. Na revisão entre pares, o revisor assume o papel do receptor e avalia se conseguiria agir baseado apenas no documento.

---

### 1. Documento de Discovery

**Bom parece assim:**
- Problema de negócio descrito em linguagem que produto e engenharia entendem
- Usuários afetados quantificados (não "vários", mas "~15k MAU")
- Contexto técnico atual documentado (o que existe hoje, como funciona, onde dói)
- Restrições identificadas (prazo, orçamento, tecnologia, regulatório)
- Perguntas respondidas e perguntas em aberto listadas com owner e prazo
- Fontes de dados citadas para cada afirmação quantitativa

**Sinais de insuficiência:**
- "Muitos usuários reclamam" sem dados
- Contexto técnico ausente ou superficial
- Restrições não mapeadas
- Sem distinção entre fato e suposição

### 2. Definição de Escopo

**Bom parece assim:**
- Lista explícita de "inclui" e "não inclui" (não apenas o que faz, mas o que NÃO faz)
- Cada item de escopo com critério de aceitação verificável
- Dependências listadas com status (resolvida / pendente / em risco)
- Premissas declaradas com impacto se forem falsas
- Escopo dimensionado (tamanho P/M/G/XG com justificativa)

**Sinais de insuficiência:**
- Escopo definido apenas pelo "inclui" sem "não inclui"
- Critérios de aceitação subjetivos ("funcionar bem")
- Dependências não mapeadas
- Tamanho estimado sem justificativa

### 3. Revisão de Arquitetura

**Bom parece assim:**
- Achados classificados por severidade com critérios consistentes
- Cada achado tem: observação + evidência + impacto + recomendação
- Alternativas avaliadas com trade-offs explícitos para cada decisão
- Pontos positivos reconhecidos (não apenas problemas)
- Veredicto claro (aprovado / aprovado com condições / não aprovado)
- Plano de ação com owners e prazos para cada achado

**Sinais de insuficiência:**
- Achados sem evidência ("acho que isso pode dar problema")
- Severidade inconsistente entre achados similares
- Apenas críticas, sem reconhecimento de acertos
- Sem plano de ação concreto

### 4. Design de Testes

**Bom parece assim:**
- Cenários derivados dos requisitos (rastreabilidade requisito → teste)
- Cobertura de happy path, edge cases e cenários de erro
- Dados de teste definidos ou critérios para geração
- Tipos de teste especificados (unitário, integração, e2e, carga)
- Critérios de aceitação quantificados (cobertura mínima, latência máxima)

**Sinais de insuficiência:**
- Apenas happy path coberto
- Cenários vagos ("testar se funciona")
- Sem dados de teste definidos
- Sem critérios quantitativos

### 5. Revisão de Riscos

**Bom parece assim:**
- Riscos com probabilidade, impacto e justificativa para a classificação
- Plano de mitigação concreto para cada risco médio/alto
- Riscos aceitos documentados com justificativa e revisor
- Indicadores antecedentes definidos para monitoramento
- Data de revisão programada

**Sinais de insuficiência:**
- Riscos genéricos ("pode ter bugs")
- Sem probabilidade ou impacto estimados
- Mitigação vaga ("vamos monitorar")
- Sem owner para mitigação

### 6. Estimativa de Esforço

**Bom parece assim:**
- Estimativa por fase/componente (não apenas total)
- Três cenários: melhor caso, esperado, pior caso
- Premissas explícitas com impacto na estimativa se falharem
- Fatores de incerteza identificados (complexidade, dependência, experiência do time)
- Comparação com projetos similares passados quando possível

**Sinais de insuficiência:**
- Número único sem faixa
- Sem premissas declaradas
- Sem decomposição por fase
- "Chute" sem fundamentação

### 7. Pacote de Handoff

**Bom parece assim:**
- Auto-contido: receptor consegue iniciar sem reunião de esclarecimento
- Sequência de implementação clara com dependências
- Edge cases documentados com comportamento esperado
- Contratos de API com exemplos de request/response e erros
- Critérios de aceitação verificáveis para cada entregável
- Referências e links todos funcionais e acessíveis

**Sinais de insuficiência:**
- Receptor precisa de mais de 2 perguntas de esclarecimento
- Contratos incompletos ou ambíguos
- "TBD" sem owner e prazo
- Links quebrados ou artefatos inacessíveis

## Critérios de Qualidade

- Todo entregável é auto-avaliado contra estes critérios antes da entrega
- Revisão entre pares confirma aderência
- Feedback do receptor confirma que o entregável foi "bom" ou melhor
- Critérios são atualizados a cada trimestre com base em feedback acumulado

## Responsáveis

| Papel | Responsabilidade |
|---|---|
| Autor do entregável | Auto-avaliação contra critérios antes de submeter para revisão |
| Par revisor | Avaliar assumindo o papel do receptor |
| Tech Lead | Manter critérios atualizados e calibrados |

## Referências

- Definição de Readiness: `docs/readiness-definition.md`
- Cada standard específico em `docs/`
