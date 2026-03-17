# Legacy Refactor Readiness Framework

## Título e Propósito

O **Legacy Refactor Readiness Framework** é um checklist para avaliar se um projeto de refatoração ou modernização de sistema legado está preparado para iniciar. O propósito é evitar o padrão onde equipes mergulham em código legado sem entender o sistema, seus riscos e suas dependências — resultando em refactors que quebram funcionalidades existentes ou que nunca terminam.

## Quando Usar

- Antes de iniciar qualquer refatoração significativa de código legado
- Em projetos de modernização (strangler fig, big bang rewrite, incremental)
- Quando a equipe precisa mudar código que ninguém da equipe atual escreveu
- Ao avaliar se vale a pena refatorar vs. conviver com o legado
- Para estimar esforço realista de projetos de modernização

## Conceitos-Chave

1. **Cobertura de Testes do Legado**: Antes de mudar, precisa testar. Se não há testes, o primeiro passo é criar testes de caracterização.
2. **Testes de Caracterização**: Testes que documentam o comportamento atual do sistema, mesmo comportamento "errado". São a rede de segurança.
3. **Mapa de Dependências**: Quem depende desse código? Mudá-lo pode quebrar o quê?
4. **Fronteira de Refactor**: Até onde vai o refactor? Sem fronteira clara, ele se expande indefinidamente.
5. **Critério de Sucesso**: Como saber que o refactor foi bem-sucedido? "Código mais limpo" não é mensurável.

## Processo / Passos

### Passo 1 — Mapear o Sistema Existente
Entenda o que o sistema faz hoje: funcionalidades, fluxos, integrações, dados. Documente o que descobrir.

### Passo 2 — Mapear Dependências
Quem depende desse código? Outros serviços, jobs, relatórios, integrações? Mudanças podem afetar todos.

### Passo 3 — Avaliar Cobertura de Testes
Que testes existem? Qual a cobertura? Se insuficiente, o primeiro trabalho é criar testes de caracterização.

### Passo 4 — Definir Fronteira do Refactor
Até onde vai? O que é "dentro do escopo" e "fora do escopo"? Sem fronteira, o refactor vira rewrite.

### Passo 5 — Definir Critério de Sucesso
Métricas: tempo de deploy, frequência de bugs, performance, manutenibilidade (medida por tempo de onboarding).

### Passo 6 — Escolher Estratégia
Strangler fig (gradual), big bang rewrite (arriscado), refactor incremental (contínuo). A estratégia depende do contexto.

### Passo 7 — Definir Plano de Rollback
Se o refactor causar problemas em produção, como reverter para o comportamento anterior?

## Perguntas de Ativação

- "Temos testes suficientes para refatorar sem medo de quebrar funcionalidades?"
- "Quem depende desse código e sabe que vamos mudá-lo?"
- "Onde termina o refactor? Qual é a fronteira?"
- "Se o refactor causar regressão em produção, como revertemos?"
- "Quanto tempo estimamos vs. quanto tempo projetos similares levaram na realidade?"
- "Estamos refatorando porque agrega valor ou porque o código é 'feio'?"

## Output Esperado

Avaliação de readiness cobrindo: mapeamento do legado, dependências, cobertura de testes, fronteira de refactor, critérios de sucesso, estratégia escolhida, plano de rollback.

## Armadilhas Comuns

1. **Refatorar sem testes**: Mudar código sem rede de segurança é criar bugs, não eliminá-los.
2. **Refactor infinito**: Sem fronteira, o refator se expande para "reescrever tudo" e nunca termina.
3. **Subestimar o legado**: "É só limpar esse código" — legado acumula regras de negócio implícitas que ninguém documentou.
4. **Big bang rewrite**: Reescrever do zero parece atraente mas quase sempre falha (Joel Spolsky, Joel on Software).
5. **Não comunicar dependências**: Refatorar sem avisar quem depende do código quebra integrações.
6. **Métricas erradas**: Medir sucesso por "linhas de código removidas" em vez de impacto real em manutenibilidade.
