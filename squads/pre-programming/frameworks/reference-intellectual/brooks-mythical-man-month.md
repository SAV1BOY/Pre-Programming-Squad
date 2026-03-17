# Brooks: The Mythical Man-Month

## Título e Propósito

Framework baseado no trabalho de **Fred Brooks** (*The Mythical Man-Month*). A tese central: **adicionar pessoas a um projeto atrasado o atrasa mais** — porque comunicação cresce exponencialmente com o tamanho da equipe, e novas pessoas precisam ser treinadas por quem já está produzindo. O propósito é aplicar esses insights no planejamento e gestão de projetos de software.

## Quando Usar

- Quando há pressão para "adicionar mais gente" para cumprir prazo
- No planejamento de equipe e distribuição de trabalho
- Para calibrar expectativas sobre velocidade de ramp-up de novos membros
- Em estimativas que envolvem equipes crescendo durante o projeto
- Quando comunicação entre equipe está consumindo mais tempo que produção

## Conceitos-Chave

1. **Lei de Brooks**: Adicionar pessoas a um projeto atrasado o atrasa mais. Os novos precisam de onboarding (que consome tempo dos existentes) e criam novos canais de comunicação.
2. **Mês-Homem Mítico**: O "mês-homem" assume que trabalho é divisível e pessoas são intercambiáveis. Ambas as premissas são falsas em software.
3. **Canais de Comunicação**: Em equipe de N pessoas, há N(N-1)/2 canais. De 4 para 8 pessoas: de 6 para 28 canais. Comunicação cresce quadraticamente.
4. **Second-System Effect**: A segunda versão de um sistema tende a ser over-engineered porque a equipe tenta compensar todas as limitações da primeira.
5. **No Silver Bullet**: Não existe tecnologia ou processo que multiplique produtividade em 10x. Melhorias são incrementais.

## Processo / Passos

### Passo 1 — Avaliar se "Mais Gente" Resolve
Antes de adicionar pessoas, pergunte: o gargalo é capacidade de implementação ou outra coisa (requisitos, decisões, infraestrutura)?

### Passo 2 — Calcular Custo de Onboarding
Cada pessoa nova consome X horas/semana de quem já está produzindo. Com 4 devs adicionando 2, são 8 horas/semana de produção perdidas durante ramp-up.

### Passo 3 — Avaliar Paralelizabilidade
O trabalho pode ser dividido em partes independentes? Se há muita dependência entre tarefas, mais pessoas não aceleram — criam espera.

### Passo 4 — Manter Equipes Pequenas
Prefira equipes de 3-7 pessoas. Acima disso, os custos de comunicação superam os ganhos de capacidade.

### Passo 5 — Se Precisar Escalar, Particione
Em vez de uma equipe grande, crie equipes pequenas com fronteiras claras (bounded contexts) e contratos definidos.

## Perguntas de Ativação

- "Adicionar mais gente vai acelerar ou atrasar? Onde está o gargalo real?"
- "Quanto tempo leva para um novo membro ser produtivo neste projeto?"
- "O trabalho é paralelizável ou há dependências que criam espera?"
- "Quantos canais de comunicação nossa equipe tem? É gerenciável?"
- "Estamos construindo o segundo sistema e over-engineering?"

## Output Esperado

Avaliação de paralelizabilidade do trabalho, cálculo de custo de onboarding, recomendação sobre tamanho de equipe, estratégia de particionamento se escalar for necessário.

## Armadilhas Comuns

1. **"Jogar gente no problema"**: Reação instintiva de gerência a atraso. Quase nunca funciona em software.
2. **Pessoa = capacidade linear**: Assumir que 2x pessoas = 2x velocidade. Na prática, é frequentemente 1.5x ou menos.
3. **Ignorar ramp-up**: Assumir que novos membros são produtivos no dia 1. Ramp-up realista é 2-8 semanas.
4. **Second-system effect**: Após o sucesso da v1, over-engineering da v2 por excesso de confiança e ambição.
5. **Comunicação como overhead**: Não contabilizar reuniões, alinhamentos, code reviews e pair programming no cálculo de capacidade.
