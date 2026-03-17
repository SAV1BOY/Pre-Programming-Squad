# Architecture Decision Record (ADR) Framework

## Título e Propósito

O **Architecture Decision Record Framework** é um sistema para documentar decisões arquiteturais de forma leve, padronizada e pesquisável. O propósito é criar memória institucional sobre o "porquê" das decisões — porque código mostra o que foi feito, commits mostram quando, mas nada mostra por que aquela opção foi escolhida e quais foram rejeitadas.

## Quando Usar

- Em qualquer decisão arquitetural que afeta múltiplos componentes ou equipes
- Ao escolher tecnologias, padrões ou abordagens com impacto duradouro
- Quando uma decisão anterior precisa ser revisitada e ninguém lembra o contexto
- Na onboarding de novos membros da equipe
- Quando há debate sobre mudar uma decisão existente

## Conceitos-Chave

1. **Decisão Arquitetural**: Escolha que afeta a estrutura, comportamento, qualidade ou interação do sistema de forma significativa.
2. **Contexto**: As circunstâncias, restrições e forças que levaram à decisão. Muda com o tempo.
3. **Consequências**: Efeitos da decisão — positivos, negativos e neutros. Toda decisão tem trade-offs.
4. **Status**: Proposed, Accepted, Deprecated, Superseded. ADRs não são deletados, são superseded.
5. **Imutabilidade**: Um ADR aceito não é editado. Se a decisão muda, cria-se novo ADR que supersede o anterior.

## Processo / Passos

### Passo 1 — Identificar a Decisão
Reconheça que uma decisão arquitetural está sendo tomada. Nem toda escolha técnica é arquitetural — foque nas de impacto significativo.

### Passo 2 — Documentar o Contexto
Descreva: qual o problema que motivou a decisão? Quais forças estão em jogo (requisitos, restrições, premissas)?

### Passo 3 — Listar Opções Consideradas
Para cada opção, descreva brevemente: abordagem, pontos fortes e fracos.

### Passo 4 — Registrar a Decisão
Declare a opção escolhida de forma clara e direta: "Usaremos X para resolver Y."

### Passo 5 — Documentar Consequências
Liste consequências positivas, negativas e neutras. Seja honesto sobre os trade-offs.

### Passo 6 — Definir Status e Metadados
Data, autor, status (proposed/accepted), relação com outros ADRs.

### Passo 7 — Armazenar com o Código
ADRs vivem no repositório, junto ao código que afetam. Versionados e pesquisáveis.

## Perguntas de Ativação

- "Se alguém perguntar 'por que fizemos assim?' daqui a 1 ano, teremos a resposta documentada?"
- "Essa decisão afeta a estrutura do sistema ou apenas um detalhe de implementação?"
- "Quais opções foram consideradas e por que foram rejeitadas?"
- "Quais são os trade-offs que estamos aceitando?"
- "Sob que condições revisitaríamos essa decisão?"
- "Quem precisa saber sobre essa decisão?"

## Output Esperado

```
# ADR-001: Usar PostgreSQL como banco de dados principal

## Status
Accepted — 2024-03-15

## Contexto
O sistema precisa de um banco relacional para transações de pedidos com ACID.
Volume esperado: 1000 transações/hora no primeiro ano, crescendo para 10.000.
A equipe tem experiência com PostgreSQL e MySQL.

## Opções Consideradas
1. **PostgreSQL**: Robusto, extensível, bom suporte a JSON, comunidade ativa.
2. **MySQL**: Familiar, amplo suporte de hosting, performance em reads.
3. **MongoDB**: Flexibilidade de schema, mas fraco em transações multi-documento.

## Decisão
Usaremos PostgreSQL como banco de dados principal para todas as operações transacionais.

## Consequências
### Positivas
- ACID completo para transações financeiras
- JSONB para dados semi-estruturados sem precisar de banco NoSQL separado
- Equipe já tem expertise

### Negativas
- Scaling horizontal mais complexo que MongoDB
- Requer mais cuidado com vacuuming e tuning

### Neutras
- Custo similar às alternativas em cloud managed

## Condições de Revisão
Revisitar se volume ultrapassar 100.000 transações/hora ou se necessidade de multi-region aparecer.
```

## Armadilhas Comuns

1. **Não documentar**: A maioria das decisões arquiteturais vive apenas na cabeça das pessoas — que saem da empresa.
2. **Documentação pesada**: ADRs devem ser leves (1-2 páginas). Se é pesado, ninguém escreve.
3. **Documentar depois**: ADRs escritos semanas depois perdem o contexto. Documente na hora da decisão.
4. **Editar em vez de superseder**: Editar um ADR aceito destrói a história. Crie novo ADR que referencia o anterior.
5. **Fora do repositório**: ADRs em wiki ou Google Docs são esquecidos. No repositório, vivem junto ao código.
6. **Decisões triviais**: Não toda escolha técnica merece um ADR. Foque nas que têm impacto significativo e duradouro.
