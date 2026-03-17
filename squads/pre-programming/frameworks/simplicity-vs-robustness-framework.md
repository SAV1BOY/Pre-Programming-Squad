# Simplicity vs. Robustness Framework

## Título e Propósito

O **Simplicity vs. Robustness Framework** é um modelo de decisão para navegar o trade-off fundamental entre manter as coisas simples e torná-las robustas. O propósito é ajudar equipes a fazer escolhas conscientes sobre quando aceitar simplicidade (com seus riscos) e quando investir em robustez (com sua complexidade), em vez de deixar essa decisão ser implícita.

## Quando Usar

- Em decisões de design onde há tensão entre "fazer simples" e "fazer direito"
- Quando a equipe debate se deve adicionar tratamento de erros, retry, circuit breaker, etc.
- Na definição do nível de maturidade aceitável para um MVP vs. produto em produção madura
- Quando um componente simples precisa ser endurecido para produção
- Em revisões arquiteturais para avaliar se a complexidade adicionada é justificada

## Conceitos-Chave

1. **Simplicidade Essencial**: Complexidade que não pode ser removida sem perder funcionalidade. É intrínseca ao problema.
2. **Complexidade Acidental**: Complexidade adicionada pela solução, não pelo problema. Deve ser minimizada.
3. **Robustez**: Capacidade do sistema de continuar funcionando corretamente sob condições adversas (falhas, carga, dados inválidos).
4. **Complexidade Justificada**: Complexidade adicionada para robustez onde o custo de falha justifica o investimento.
5. **YAGNI Estratégico**: "You Ain't Gonna Need It" — mas aplicado com discernimento. Às vezes, você vai precisar sim.

## Processo / Passos

### Passo 1 — Identificar o Componente
Defina claramente qual parte do sistema está sendo avaliada.

### Passo 2 — Avaliar Custo de Falha
Pergunte: "Se esse componente falhar, qual é o impacto?" Classifique: **Catastrófico** (perda de dados, impacto financeiro), **Significativo** (degradação de serviço), **Tolerável** (inconveniência menor), **Irrelevante** (ninguém nota).

### Passo 3 — Avaliar Probabilidade de Falha
Quais cenários podem causar falha? Qual a probabilidade de cada um? Use dados históricos se disponíveis.

### Passo 4 — Mapear Opções no Espectro
Para cada decisão de design, identifique as opções do mais simples ao mais robusto:
- **Nível 0**: Happy path apenas
- **Nível 1**: Tratamento básico de erros
- **Nível 2**: Retry, timeout, validação
- **Nível 3**: Circuit breaker, fallback, graceful degradation
- **Nível 4**: Auto-healing, redundância, chaos engineering

### Passo 5 — Escolher o Nível Adequado
Use a matriz: Custo de Falha × Probabilidade de Falha = Nível de robustez necessário. Catastrófico + provável = Nível 3-4. Tolerável + improvável = Nível 0-1.

### Passo 6 — Documentar a Decisão
Registre o nível escolhido, a justificativa e os cenários explicitamente não cobertos.

## Perguntas de Ativação

- "Se esse componente falhar às 3h da manhã de domingo, alguém precisa acordar?"
- "Estamos adicionando complexidade por paranoia ou por dados?"
- "Qual é o custo real de uma falha aqui vs. o custo de preveni-la?"
- "Essa robustez é para agora ou para um volume que teremos em 2 anos?"
- "Podemos começar simples e adicionar robustez quando tivermos dados de produção?"
- "Estamos tratando esse componente com o mesmo nível que todos os outros, quando deveria ser diferente?"

## Output Esperado

| Componente | Custo de Falha | Probabilidade | Nível Escolhido | Justificativa | Cenários Não Cobertos |
|---|---|---|---|---|---|
| Processamento de pagamentos | Catastrófico | Médio | Nível 3 | Perda financeira direta | Falha total do provider (aceito: SLA do provider cobre) |
| Feed de notificações | Tolerável | Baixo | Nível 1 | Usuário pode recarregar | Perda de notificações em pico (aceito: não crítico) |
| Sincronização de inventário | Significativo | Alto | Nível 3 | Venda de item sem estoque | — |
| Página "Sobre Nós" | Irrelevante | Muito baixo | Nível 0 | Conteúdo estático | Qualquer falha (aceito: impacto zero) |

## Armadilhas Comuns

1. **Robustez uniforme**: Tratar todos os componentes com o mesmo nível de robustez desperdiça esforço em áreas de baixo risco.
2. **Simplicidade como desculpa**: Usar "YAGNI" para evitar robustez necessária em componentes críticos.
3. **Robustez prematura**: Adicionar circuit breakers e auto-healing antes de ter dados sobre padrões reais de falha.
4. **Complexidade oculta**: A robustez adicionada introduz novos modos de falha que também precisam ser tratados.
5. **Não revisitar**: O que era tolerável com 100 usuários pode ser catastrófico com 100.000.
6. **Consenso por medo**: A equipe escolhe o nível mais robusto por medo de ser responsabilizada por uma falha, mesmo quando o custo não justifica.
