# Edge Case Explosion Framework

## Título e Propósito

O **Edge Case Explosion Framework** é um sistema para identificar, catalogar e priorizar edge cases antes da implementação. O propósito é tornar visível o volume real de casos de borda que um requisito aparentemente simples esconde — e decidir conscientemente quais tratar, quais aceitar como limitação e quais adiar.

## Quando Usar

- Durante refinamento de requisitos e histórias de usuário
- Quando um requisito parece "simples" mas a equipe suspeita de complexidade oculta
- Em design de APIs, validações e fluxos de dados
- Antes de estimar esforço — edge cases são onde mora o esforço real
- Quando bugs em produção revelam edge cases não considerados

## Conceitos-Chave

1. **Edge Case**: Cenário que ocorre nos limites das condições esperadas — valores extremos, combinações incomuns, timing inesperado.
2. **Corner Case**: Cenário que ocorre quando múltiplas condições de borda se combinam simultaneamente.
3. **Explosão Combinatória**: O número de edge cases cresce exponencialmente com o número de variáveis e seus possíveis estados.
4. **Cobertura Pragmática**: Não é possível cobrir todos os edge cases. O objetivo é cobrir os de maior impacto e probabilidade.
5. **Boundary Value Analysis**: Técnica de focar testes nos limites de cada variável, onde erros são mais prováveis.

## Processo / Passos

### Passo 1 — Identificar Variáveis
Liste todas as variáveis relevantes do requisito: inputs do usuário, estados do sistema, dados de integração, condições temporais.

### Passo 2 — Para Cada Variável, Listar Valores de Borda
Para cada variável, identifique: valor mínimo, máximo, zero, nulo, vazio, negativo, muito grande, formato inesperado, caracteres especiais, Unicode.

### Passo 3 — Identificar Combinações Perigosas
Cruze variáveis que interagem entre si. Exemplo: desconto de 100% + frete grátis + cupom = preço negativo?

### Passo 4 — Avaliar Impacto de Cada Edge Case
Para cada edge case, classifique o impacto se não for tratado: **Crítico** (perda de dados/dinheiro), **Alto** (erro visível), **Médio** (comportamento inesperado), **Baixo** (cosmético).

### Passo 5 — Avaliar Probabilidade
Qual a chance de um usuário real encontrar esse edge case? Dados históricos, se disponíveis, ajudam.

### Passo 6 — Decidir: Tratar, Aceitar ou Adiar
- **Tratar**: Implementar lógica para lidar com o caso
- **Aceitar**: Documentar como limitação conhecida
- **Adiar**: Colocar no backlog para versão futura

### Passo 7 — Atualizar Estimativas
Revise a estimativa de esforço incluindo os edge cases que serão tratados. Este é frequentemente o momento em que "2 dias" vira "2 semanas".

## Perguntas de Ativação

- "O que acontece se o usuário enviar esse campo vazio? Nulo? Com 10.000 caracteres?"
- "E se duas pessoas fizerem a mesma ação ao mesmo tempo?"
- "O que acontece na virada de mês? De ano? No horário de verão?"
- "E se a API externa retornar dados em formato diferente do esperado?"
- "Quantas combinações de estado são possíveis aqui?"
- "Qual edge case, se ignorado, causaria o maior estrago?"

## Output Esperado

| Edge Case | Variáveis Envolvidas | Impacto | Probabilidade | Decisão | Justificativa |
|---|---|---|---|---|---|
| Quantidade negativa no carrinho | input.quantidade | Crítico (cobrança negativa) | Baixa (mas explorável) | Tratar | Risco financeiro e de segurança |
| Nome com emoji/Unicode | input.nome | Baixo (visual) | Média | Aceitar | Não afeta funcionalidade |
| Dois pedidos simultâneos para último item | estoque + concorrência | Alto (venda sem estoque) | Média | Tratar | Impacto operacional direto |
| Timezone diferente entre client e server | timestamp + timezone | Médio (dados inconsistentes) | Alta | Tratar | Afeta relatórios |
| CPF com formatação inconsistente | input.cpf | Médio (duplicação de cadastro) | Alta | Tratar | Impacta integridade de dados |

**Resumo**: 23 edge cases identificados, 12 tratados, 6 aceitos como limitação, 5 adiados.
**Impacto na estimativa**: +40% sobre estimativa original.

## Armadilhas Comuns

1. **"O usuário nunca faria isso"**: Usuários fazem coisas inesperadas. Atacantes fazem deliberadamente. Nunca assuma comportamento ideal.
2. **Tentar cobrir tudo**: A explosão combinatória torna impossível cobrir 100% dos edge cases. Priorize por impacto × probabilidade.
3. **Edge cases tardios**: Descobrir edge cases durante o code review ou em produção é 10x mais caro que durante o design.
4. **Subestimar combinações**: 5 variáveis com 3 estados cada = 243 combinações. A maioria será irrelevante, mas algumas serão críticas.
5. **Não atualizar estimativas**: Identificar edge cases e não ajustar prazo/esforço é receita para atraso.
6. **Edge case como bug**: Tratar edge cases descobertos em produção como "bugs" quando na verdade são cenários nunca considerados.
