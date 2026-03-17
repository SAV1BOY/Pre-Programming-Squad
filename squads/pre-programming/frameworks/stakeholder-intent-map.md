# Stakeholder Intent Map

## Título e Propósito

O **Stakeholder Intent Map** é um framework para mapear as intenções reais (não apenas declaradas) de cada stakeholder envolvido em um projeto. O propósito é revelar motivações ocultas, conflitos de interesse e alinhamentos necessários antes de começar a construir — porque requisitos conflitantes de stakeholders diferentes são a causa número um de retrabalho em projetos de software.

## Quando Usar

- No início de projetos com múltiplos stakeholders ou áreas envolvidas
- Quando requisitos parecem contraditórios entre diferentes fontes
- Quando há pressão política sobre decisões técnicas
- Antes de apresentar opções arquiteturais que afetam diferentes áreas
- Quando um projeto "muda de direção" repetidamente sem explicação clara

## Conceitos-Chave

1. **Intenção Declarada vs. Real**: O que o stakeholder diz que quer vs. o que realmente precisa ou deseja. Nem sempre há má-fé — frequentemente o stakeholder não articulou sua própria necessidade.
2. **Poder de Decisão**: Quem de fato pode aprovar, vetar ou bloquear decisões relevantes.
3. **Critério de Sucesso Individual**: O que cada stakeholder usará para julgar se o projeto foi bem-sucedido — e esses critérios podem conflitar.
4. **Zona de Conflito**: Áreas onde as intenções de dois ou mais stakeholders são incompatíveis.
5. **Aliança de Interesse**: Stakeholders cujos interesses estão naturalmente alinhados e que podem ser abordados juntos.

## Processo / Passos

### Passo 1 — Listar Todos os Stakeholders
Identifique todos que têm interesse no projeto: quem pede, quem aprova, quem usa, quem mantém, quem paga, quem é afetado indiretamente.

### Passo 2 — Mapear Intenções Declaradas
Para cada stakeholder, registre o que eles dizem que querem. Use as palavras deles.

### Passo 3 — Inferir Intenções Reais
Para cada stakeholder, pergunte: "O que essa pessoa realmente precisa? O que a faria declarar sucesso? O que a faria declarar fracasso?" Considere incentivos de carreira, métricas pelas quais são avaliados, medos e aspirações.

### Passo 4 — Mapear Poder de Decisão
Classifique cada stakeholder: **Decide** (poder de veto), **Influencia** (voz mas não veto), **Afetado** (impactado mas sem voz formal).

### Passo 5 — Identificar Conflitos
Cruze as intenções reais. Onde dois stakeholders querem coisas incompatíveis? Documente cada conflito explicitamente.

### Passo 6 — Propor Resoluções
Para cada conflito, proponha: compromisso, priorização, escalonamento ou reformulação que acomode ambos.

### Passo 7 — Validar o Mapa
Compartilhe as intenções declaradas (não as inferidas) com os stakeholders para confirmar que você entendeu corretamente.

## Perguntas de Ativação

- "O que essa pessoa faria se o projeto fosse cancelado amanhã — ficaria aliviada ou preocupada?"
- "Por qual métrica essa pessoa é avaliada pelo chefe dela?"
- "Quem perde poder ou relevância se esse projeto for bem-sucedido?"
- "Há alguém que não está na mesa mas deveria estar?"
- "Se pudéssemos atender apenas um stakeholder perfeitamente, quem seria e por quê?"
- "Quais decisões do projeto cada stakeholder acredita que são suas para tomar?"

## Output Esperado

| Stakeholder | Intenção Declarada | Intenção Real (Inferida) | Poder | Critério de Sucesso | Conflitos |
|---|---|---|---|---|---|
| Diretor de Produto | "Precisamos de um dashboard analítico" | Quer mostrar resultados para o board no Q2 | Decide | Dashboard apresentável em 6 semanas | Conflita com CTO sobre prazo vs. qualidade |
| CTO | "Precisa ser escalável" | Não quer dívida técnica que caia no colo dele depois | Decide | Arquitetura que não precise ser refeita em 1 ano | Conflita com Diretor sobre prazo |
| Equipe de Suporte | "Os clientes reclamam muito" | Quer reduzir volume de tickets para poder respirar | Afetado | Menos tickets sobre dados incorretos | Alinhado com Diretor |

## Armadilhas Comuns

1. **Aceitar tudo ao pé da letra**: Assumir que o que o stakeholder diz é exatamente o que ele precisa. Sempre investigue a intenção por trás do pedido.
2. **Ignorar stakeholders silenciosos**: Quem não fala nas reuniões ainda pode ter poder de veto ou ser criticamente afetado.
3. **Evitar conflitos**: Documentar conflitos é desconfortável mas essencial. Conflitos não resolvidos explodem durante a implementação.
4. **Mapa estático**: Intenções mudam conforme o contexto muda. O mapa deve ser revisitado em marcos importantes.
5. **Confundir volume com poder**: O stakeholder que fala mais alto nem sempre é o que tem poder de decisão real.
6. **Não validar**: Inferências sobre intenções reais podem estar erradas. Valide hipóteses com perguntas indiretas.
