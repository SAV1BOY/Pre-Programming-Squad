# Estimation Under Uncertainty Framework

## Título e Propósito

O **Estimation Under Uncertainty Framework** é um sistema para produzir estimativas mais honestas e úteis quando a incerteza é alta. O propósito é substituir a falsa precisão de estimativas pontuais ("vai levar 3 semanas") por ranges que comunicam explicitamente o nível de confiança — porque estimativas precisas em contextos incertos são ficção.

## Quando Usar

- Em qualquer estimativa de esforço ou prazo para projetos de software
- Quando há alta incerteza técnica, de escopo ou de dependências
- Quando estimativas anteriores falharam consistentemente
- Para comunicar realismo a stakeholders sem gerar frustração
- Na priorização de projetos que competem por recursos

## Conceitos-Chave

1. **Estimativa em Range**: Em vez de "3 semanas", use "2-5 semanas, mais provavelmente 3". Comunica incerteza explicitamente.
2. **Cone de Incerteza**: No início do projeto, a incerteza é 4x. Após design, 2x. Após implementação parcial, 1.25x. A estimativa refina com o tempo.
3. **Nível de Confiança**: A probabilidade de entregar dentro do range. Range de 50% é otimista; 90% é conservador mas mais confiável.
4. **Referência por Analogia**: Estimar comparando com projetos anteriores similares, não inventando números.
5. **Viés de Otimismo**: A tendência universal de subestimar esforço e superestimar velocidade. Corrigir conscientemente.

## Processo / Passos

### Passo 1 — Decompor o Trabalho
Quebre em componentes mensuráveis. Componentes menores são mais fáceis de estimar.

### Passo 2 — Estimar em Três Pontos
Para cada componente, estime:
- **Otimista**: Se tudo der certo (10% de chance)
- **Provável**: O cenário mais realista (50% de chance)
- **Pessimista**: Se as coisas derem errado (90% de chance)

### Passo 3 — Calcular a Estimativa PERT
E = (Otimista + 4×Provável + Pessimista) ÷ 6. Isso pondera mais o cenário provável.

### Passo 4 — Buscar Referências
Pergunte: "Já fizemos algo parecido? Quanto levou?" Dados reais superam estimativas teóricas.

### Passo 5 — Adicionar Incerteza Explícita
Comunique o range, não apenas o ponto: "Estimamos entre X e Y, com confiança de Z%."

### Passo 6 — Documentar Premissas
Liste o que foi assumido para chegar à estimativa. Quando premissas mudam, a estimativa muda.

### Passo 7 — Re-estimar à Medida que Avança
Atualize estimativas conforme incerteza diminui. Re-estimar não é falha — é responsabilidade.

## Perguntas de Ativação

- "Essa estimativa assume que tudo dá certo na primeira tentativa?"
- "Já fizemos algo parecido? Quanto tempo realmente levou (não quanto estimamos)?"
- "Qual é nosso nível de confiança nessa estimativa — 50%? 80%? 90%?"
- "Se um dev sênior e um júnior estimassem, a diferença seria grande? Isso é um sinal."
- "Quais premissas sustentam essa estimativa?"
- "Estamos estimando o trabalho de implementação ou o trabalho total (incluindo review, testes, deploy)?"

## Output Esperado

| Componente | Otimista | Provável | Pessimista | PERT | Premissas |
|---|---|---|---|---|---|
| Integração com API de pagamento | 2 dias | 5 dias | 12 dias | 5.7 dias | API documentada e sandbox funcional |
| CRUD de produtos | 1 dia | 2 dias | 3 dias | 2 dias | Schema definido, sem regras complexas |
| Motor de busca | 3 dias | 7 dias | 15 dias | 7.7 dias | Elasticsearch já configurado |
| Testes e QA | 2 dias | 4 dias | 8 dias | 4.3 dias | Ambiente de staging disponível |
| **Total** | **8 dias** | **18 dias** | **38 dias** | **19.7 dias** | |

**Comunicação ao stakeholder**: "Estimamos entre 3 e 4 semanas, com 80% de confiança em 4 semanas. Pode chegar a 6+ semanas se [riscos X, Y] se materializarem."

## Armadilhas Comuns

1. **Precisão falsa**: "Vai levar 17 dias" transmite falsa certeza. O mundo real não funciona assim.
2. **Estimar apenas o happy path**: Não contabilizar testes, code review, deploy, bugs, reuniões, interrupções.
3. **Viés de ancoragem**: O primeiro número mencionado "ancora" todas as estimativas seguintes. Estime independentemente primeiro.
4. **Pressão para reduzir**: Stakeholder pede "menos tempo". Reduzir estimativa não reduz trabalho — reduz honestidade.
5. **Não re-estimar**: Manter a estimativa original mesmo quando novas informações mudam o cenário.
6. **Ignorar dados históricos**: Estimar "no feeling" quando há dados reais de projetos anteriores disponíveis.
