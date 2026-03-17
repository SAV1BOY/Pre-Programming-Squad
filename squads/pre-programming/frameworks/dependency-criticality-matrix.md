# Dependency Criticality Matrix

## Título e Propósito

A **Dependency Criticality Matrix** é um framework para mapear, classificar e gerenciar dependências de um projeto com base em sua criticidade. O propósito é tornar visível quais dependências podem bloquear, atrasar ou comprometer o projeto — e definir estratégias de mitigação antes que se tornem problemas reais.

## Quando Usar

- No início de projetos que envolvem integrações com sistemas externos
- Quando o projeto depende de outras equipes, fornecedores ou serviços
- Na avaliação de risco de cronograma
- Quando uma dependência falha e é preciso entender o impacto
- Em revisões de arquitetura para avaliar acoplamento

## Conceitos-Chave

1. **Dependência Técnica**: Bibliotecas, APIs, serviços, bancos de dados dos quais o sistema depende para funcionar.
2. **Dependência Organizacional**: Outras equipes, aprovações, decisões que precisam acontecer para o projeto avançar.
3. **Criticidade**: Combinação de impacto (se falhar) × probabilidade de falha × disponibilidade de alternativa.
4. **Dependência Bloqueante**: Sem ela, o trabalho não pode avançar. Deve ser resolvida ou desbloqueada primeiro.
5. **Plano de Contingência**: O que fazer se a dependência falhar, atrasar ou não entregar o esperado.

## Processo / Passos

### Passo 1 — Inventariar Dependências
Liste todas as dependências: técnicas (APIs, libs, infra), organizacionais (outras equipes, aprovações), externas (fornecedores, terceiros).

### Passo 2 — Classificar por Tipo
Categorize: **Hard** (sem ela, impossível prosseguir), **Soft** (sem ela, funciona com degradação), **Nice-to-have** (melhora mas não é necessária).

### Passo 3 — Avaliar Confiabilidade
Para cada dependência, avalie: SLA histórico, maturidade, estabilidade da equipe responsável, frequência de mudanças breaking.

### Passo 4 — Avaliar Substituibilidade
Pergunte: "Se essa dependência desaparecer amanhã, podemos substituí-la? Com que custo e tempo?"

### Passo 5 — Calcular Criticidade
Criticidade = Tipo (Hard > Soft > Nice) × (1 - Confiabilidade) × (1 - Substituibilidade). Quanto maior, mais crítica.

### Passo 6 — Definir Planos de Contingência
Para dependências de alta criticidade, defina: alternativa técnica, workaround temporário, escalonamento, ou redesign que elimina a dependência.

### Passo 7 — Monitorar Ativamente
Estabeleça checkpoints regulares para verificar o status de dependências críticas. Não espere até precisar delas para descobrir que estão indisponíveis.

## Perguntas de Ativação

- "Se essa API/equipe/serviço não entregar no prazo, qual é nosso plano B?"
- "Temos controle sobre essa dependência ou estamos à mercê de outro time?"
- "Qual a última vez que essa dependência nos causou problema?"
- "Podemos redesenhar para eliminar ou reduzir essa dependência?"
- "Quem é nosso ponto de contato para essa dependência e ele sabe que dependemos dele?"
- "Se essa biblioteca for descontinuada, quanto trabalho é migrar?"

## Output Esperado

| Dependência | Tipo | Categoria | Confiabilidade | Substituibilidade | Criticidade | Plano de Contingência |
|---|---|---|---|---|---|---|
| API de CEP (ViaCEP) | Técnica | Hard | Média (85% uptime) | Alta (várias alternativas) | Média | Fallback para segunda API + cache local |
| Equipe de Infra (provisionar K8s) | Organizacional | Hard | Baixa (frequentes atrasos) | Baixa (única equipe) | Crítica | Pré-agendar com 3 semanas, escalar para CTO se atrasar |
| Biblioteca de gráficos (D3.js) | Técnica | Soft | Alta (projeto maduro) | Média | Baixa | — (risco aceito) |
| Aprovação jurídica de termos | Organizacional | Hard | Desconhecida | Nenhuma | Crítica | Iniciar processo em paralelo ao desenvolvimento |

## Armadilhas Comuns

1. **Dependências invisíveis**: Dependências que ninguém mapeou porque "sempre funcionaram" — até pararem.
2. **Otimismo sobre outras equipes**: "Eles disseram que entregam na semana que vem" não é garantia. Verifique independentemente.
3. **Sem plano de contingência**: Identificar a dependência crítica mas não ter plano B é análise sem ação.
4. **Dependência de pessoa**: Quando o conhecimento está em uma única pessoa que pode sair de férias, adoecer ou sair da empresa.
5. **Não comunicar dependência**: A outra equipe nem sabe que você depende dela. Comunique explicitamente e cedo.
6. **Lock-in não reconhecido**: Dependência técnica que parece substituível mas que na prática envolve migração de dados, retreino ou reescrita.
