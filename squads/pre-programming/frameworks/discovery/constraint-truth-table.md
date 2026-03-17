# Constraint Truth Table

## Título e Propósito

A **Constraint Truth Table** é um framework para verificar sistematicamente se as restrições declaradas de um projeto são reais, negociáveis ou imaginárias. O propósito é separar restrições genuínas de suposições disfarçadas — porque equipes frequentemente operam sob restrições que ninguém validou, limitando desnecessariamente o espaço de soluções.

## Quando Usar

- No início de projetos quando restrições são declaradas por stakeholders
- Quando o espaço de soluções parece injustificadamente estreito
- Quando alguém diz "não podemos" sem evidência clara
- Em revisões de viabilidade antes de comprometer com uma abordagem
- Quando o projeto parece impossível — talvez algumas restrições não sejam reais

## Conceitos-Chave

1. **Restrição Verdadeira**: Limite que existe independente de quem acredita nele. Verificável com dados ou autoridade.
2. **Restrição Assumida**: Algo que a equipe trata como restrição mas que nunca foi verificado. Pode ser ou não real.
3. **Restrição Herdada**: Vem de projetos anteriores ou de "como sempre fizemos". O contexto pode ter mudado.
4. **Restrição Política**: Existe por razões organizacionais, não técnicas. Pode ser negociada com a pessoa certa.
5. **Valor-Verdade**: Para cada restrição, o resultado da verificação: **Verdadeira** (confirmada), **Falsa** (refutada), **Parcial** (verdadeira com nuances), **Desconhecida** (não verificável agora).

## Processo / Passos

### Passo 1 — Coletar Todas as Restrições Declaradas
Liste tudo que a equipe acredita ser uma restrição: técnica, de prazo, de orçamento, regulatória, de equipe, de infraestrutura.

### Passo 2 — Para Cada Restrição, Identificar a Fonte
Quem declarou essa restrição? Com base em quê? Quando? O contexto pode ter mudado.

### Passo 3 — Classificar o Tipo
Para cada restrição, classifique: técnica, regulatória, contratual, organizacional, de recursos, temporal.

### Passo 4 — Verificar o Valor-Verdade
Para cada restrição, busque verificação:
- **Técnica**: Teste, spike, documentação oficial
- **Regulatória**: Texto da lei ou regulação, opinião jurídica
- **Contratual**: Leitura do contrato
- **Organizacional**: Confirmação com quem tem autoridade
- **De recursos**: Confirmação com RH, financeiro, infra

### Passo 5 — Registrar Resultado
Para cada restrição, registre: valor-verdade, evidência, data de verificação, implicação para o projeto.

### Passo 6 — Reclassificar o Espaço de Soluções
Com restrições falsas removidas e parciais ajustadas, reavalie: que soluções agora são viáveis que antes não eram?

### Passo 7 — Monitorar Restrições Temporais
Algumas restrições são verdadeiras agora mas mudam. Estabeleça revisão periódica.

## Perguntas de Ativação

- "Quem disse que não podemos fazer isso? Essa pessoa tem autoridade para definir essa restrição?"
- "Essa restrição existia no projeto anterior. Ainda é válida neste contexto?"
- "Se eu perguntasse ao jurídico/infra/negócio, eles confirmariam essa restrição?"
- "Quando foi a última vez que alguém verificou se isso é realmente uma limitação?"
- "Se essa restrição não existisse, que solução teríamos?"
- "Estamos tratando uma preferência como uma restrição?"

## Output Esperado

| Restrição Declarada | Fonte | Tipo | Valor-Verdade | Evidência | Implicação |
|---|---|---|---|---|---|
| "Não podemos usar cloud pública" | CTO em 2022 | Organizacional | **Parcial** — pode usar para workloads não-sensíveis | Conversa com CTO em março/2024 | Abre opção de cloud para serviços stateless |
| "LGPD proíbe armazenar CPF" | Dev sênior | Regulatória | **Falsa** — LGPD permite com base legal e consentimento | Parecer jurídico | Remove bloqueio no módulo de cadastro |
| "API do parceiro não suporta batch" | Documentação v2 | Técnica | **Verdadeira** — confirmado com parceiro | Email do suporte técnico | Mantém processamento individual, projetar para async |
| "Prazo de 6 semanas é fixo" | Diretor de Produto | Temporal | **Verdadeira** — launch vinculado a evento | Confirmação em reunião | Ajustar escopo para caber no prazo |
| "O time de dados não pode ajudar" | PM | Organizacional | **Falsa** — time de dados tem capacidade | Conversa com lead de dados | Incluir no planejamento |

**Resultado**: 2 de 5 restrições eram falsas. Espaço de soluções significativamente expandido.

## Armadilhas Comuns

1. **Aceitar sem verificar**: A armadilha mais comum. "Alguém disse que não pode" vira restrição eterna sem ninguém questionar.
2. **Medo de questionar**: Desafiar restrições declaradas por superiores pode parecer insubordinação. Formule como "quero garantir que estou entendendo corretamente."
3. **Restrição como identidade**: A equipe se identifica com certas restrições ("somos on-premise") e resiste a questioná-las.
4. **Verificação superficial**: "Perguntei e disseram que sim" não é verificação robusta para restrições de alto impacto.
5. **Contexto desatualizado**: Restrições que eram verdadeiras quando definidas mas que o contexto mudou. Ninguém reavaliou.
6. **Remover restrição real**: O oposto — questionar uma restrição genuína e agir como se não existisse, criando risco real.
