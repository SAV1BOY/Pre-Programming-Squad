# Padrões Ruins de Estimativa — Exemplos Anotados

## Introdução

Estimativas ruins são epidêmicas em engenharia de software. Não porque engenheiros sejam incompetentes, mas porque estimativas são inerentemente difíceis e os vieses cognitivos que as corrompem são universais. Este documento cataloga os padrões mais comuns de estimativas falhas, com exemplos reais e estratégias para a pré-programação mitigar cada um.

---

## Exemplo 1 — Viés de Otimismo ("Vai ser rápido")

### O Padrão

> Estimativa do desenvolvedor: "2 semanas, fácil."
> Realidade: 8 semanas.
> O dev estimou o caminho feliz: código novo, tudo funciona de primeira, sem bugs, sem mudança de requisito, sem dependência bloqueada.

### Por que falha

- **Ignora o desconhecido**: Estimativa considera apenas o que já sabe. Não conta com descobertas durante a implementação.
- **Esquece o overhead**: Code review, testes, documentação, deploy, bugs encontrados em QA, refactoring.
- **Assume disponibilidade total**: Não desconta reuniões, suporte a produção, interrupções, contexto switch.
- **Fator real**: Trabalho útil de codificação é ~4-5h por dia de 8h. Estimativa de "2 semanas de código" precisa de 3+ semanas de calendário.

### Mitigação na pré-programação

- Multiplicar estimativa do dev por 2-3x (regra de Hofstadter)
- Decompor em tarefas de máximo 2 dias — tarefas maiores escondem complexidade
- Incluir buffer explícito para "descobertas" (20-30% do total)

---

## Exemplo 2 — Estimativa por Analogia Falsa ("Foi rápido da última vez")

### O Padrão

> "Fizemos algo parecido no projeto anterior em 3 semanas. Deve levar o mesmo tempo."
> Realidade: O projeto anterior usava stack conhecida, banco existente e equipe experiente. Este usa stack nova, banco novo e metade da equipe é nova.

### Por que falha

- **"Parecido" esconde diferenças críticas**: Contexto, stack, time, escala — tudo muda entre projetos
- **Survivorship bias**: Lembram do projeto que deu certo em 3 semanas. Esquecem dos 5 que atrasaram
- **Curva de aprendizado ignorada**: Stack nova ou domínio novo multiplicam o tempo

### Mitigação na pré-programação

- Ao usar analogia, listar explicitamente diferenças entre projetos
- Adicionar fator de ajuste para cada diferença significativa
- Verificar se a estimativa original do projeto análogo era precisa (ou se também atrasou)

---

## Exemplo 3 — Estimativa por Pressão ("O prazo é esse, se virem")

### O Padrão

> Gerente: "O cliente precisa para dia 15. Dá?"
> Time: "...dá." (não dá, mas ninguém quer ser o pessimista)
> Resultado: Entrega no dia 15 com metade das features cortadas, zero testes e código que será reescrito em 3 meses.

### Por que falha

- **Confunde desejo com realidade**: O prazo é uma restrição de negócio, não uma estimativa técnica
- **Incentivo perverso**: Quem dá más notícias é "negativo". Quem promete o impossível é "comprometido"
- **Dívida técnica oculta**: Para cumprir o prazo, cortam testes, documentação e qualidade — custo transferido para o futuro

### Mitigação na pré-programação

- Separar estimativa de compromisso: "A estimativa é 8 semanas. Se o prazo é 4, precisamos cortar escopo"
- Apresentar opções: "Em 4 semanas entregamos X. Em 8 semanas, X+Y+Z"
- Documentar trade-offs aceitos: Se cortar testes para cumprir prazo, registrar o risco

---

## Exemplo 4 — Estimativa Sem Decomposição ("Chute de alto nível")

### O Padrão

> "O projeto todo deve levar uns 4 meses."
> Sem breakdown de tarefas. Sem identificação de dependências. Sem mapeamento de riscos.

### Por que falha

- **Lei dos grandes números não se aplica**: Estimativas de alto nível não se cancelam — vieses são sistemáticos, não aleatórios
- **Esconde complexidade**: "4 meses" para um projeto com 15 componentes, 8 integrações e 3 migrações é ficção
- **Impossível de acompanhar**: Sem decomposição, não há como saber no mês 2 se está no caminho certo

### Mitigação na pré-programação

- Decompor até tarefas de 1-3 dias
- Identificar caminho crítico
- Somar tarefas + dependências + buffer = estimativa bottom-up
- Comparar bottom-up com top-down — a diferença revela pontos cegos

---

## Exemplo 5 — Estimativa Ignorando Integração

### O Padrão

> "Serviço A: 3 semanas. Serviço B: 2 semanas. Integração: 1 dia. Total: 5 semanas e 1 dia."
> Realidade: Integração levou 3 semanas adicionais.

### Por que falha

- **Integração é onde mora a complexidade**: Formatos incompatíveis, edge cases não previstos, race conditions, handling de erros entre serviços
- **Estimativa proporcional é mentira**: Integração não é proporcional ao tamanho dos componentes. Dois serviços simples podem ter integração complexa
- **Ambiente de teste**: Testar integração requer ambientes completos, dados realistas e cenários de falha

### Mitigação na pré-programação

- Estimar integração separadamente, com seus próprios cenários e riscos
- Definir contratos de API antes da implementação
- Planejar testes de integração como atividade explícita com tempo dedicado

---

## Lições Extraídas

1. **Multiplique por pi**: Estimativa do dev × 3.14 é surpreendentemente preciso (semi-sério, semi-verdade)
2. **Decomponha obsessivamente**: Tarefas de mais de 3 dias escondem incógnitas
3. **Separe estimativa de compromisso**: Uma é técnica, outra é de negócio
4. **Inclua buffer explícito**: 20-30% para "surpresas" não é pessimismo, é realismo
5. **Estime a integração como primeiro-classe**: Não é "1 dia no final"
6. **Use histórico real**: Quanto levou de verdade nos últimos 5 projetos?
7. **Três pontos**: Melhor caso, caso provável, pior caso — a média ponderada é mais realista
8. **Revise conforme aprende**: Reestime quando novas informações surgirem, não espere o final
