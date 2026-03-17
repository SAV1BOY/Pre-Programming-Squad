# Reversible vs. Irreversible Decisions

## Título e Propósito

O **Reversible vs. Irreversible Decisions** é um framework para calibrar o nível de análise e deliberação de acordo com a reversibilidade da decisão. O propósito é evitar dois erros opostos: gastar semanas analisando decisões facilmente reversíveis (paralisia) e tomar decisões irreversíveis sem análise suficiente (imprudência).

## Quando Usar

- Em qualquer ponto de decisão técnica ou arquitetural
- Quando a equipe está paralisada por análise excessiva ("analysis paralysis")
- Quando alguém propõe uma mudança com consequências potencialmente permanentes
- Na escolha de tecnologias, fornecedores, contratos ou arquiteturas
- Quando há pressão para decidir rápido mas o risco não está claro

## Conceitos-Chave

1. **Decisão Tipo 1 (Irreversível)**: Porta de mão única. Uma vez tomada, reverter é extremamente caro, lento ou impossível. Exige análise rigorosa.
2. **Decisão Tipo 2 (Reversível)**: Porta de duas mãos. Se não funcionar, podemos voltar atrás com custo baixo. Pode ser tomada rapidamente.
3. **Custo de Reversão**: O esforço real (tempo, dinheiro, complexidade) para desfazer a decisão. Quanto maior, mais análise é necessária.
4. **Custo de Atraso**: O custo de não decidir — oportunidades perdidas, equipe parada, mercado mudando. Deve ser pesado contra o risco.
5. **Janela de Decisão**: O período em que a decisão pode ser adiada sem custo significativo. Após a janela, o adiamento se torna uma decisão implícita.

## Processo / Passos

### Passo 1 — Identificar a Decisão
Articule claramente o que está sendo decidido. Muitas vezes, a equipe debate sem ter a decisão formulada.

### Passo 2 — Avaliar Reversibilidade
Pergunte: "Se tomarmos essa decisão e ela se provar errada em 3 meses, o que é necessário para reverter?" Avalie o custo de reversão em tempo, dinheiro e complexidade.

### Passo 3 — Classificar a Decisão
- **Tipo 1**: Custo de reversão alto (meses de retrabalho, contratos de longo prazo, mudanças de schema com dados em produção)
- **Tipo 2**: Custo de reversão baixo (mudança de biblioteca, feature flag, configuração)

### Passo 4 — Calibrar a Análise
- Para Tipo 1: Análise profunda, múltiplas perspectivas, prototipagem, consulta a especialistas, documentação da decisão
- Para Tipo 2: Decidir rápido, experimentar, coletar dados e ajustar. "Bom o suficiente" é o padrão.

### Passo 5 — Avaliar Custo de Atraso
Mesmo para Tipo 1, não adie indefinidamente. Calcule: "Quanto custa cada semana que não decidimos?"

### Passo 6 — Decidir e Documentar
Registre a decisão, a classificação (Tipo 1 ou 2), os fatores considerados e o critério para reconsiderar.

### Passo 7 — Definir Trigger de Revisão
Para Tipo 2, defina quando e sob que condições a decisão será revisitada. Para Tipo 1, documente os sinais que indicariam que a decisão precisa ser mitigada.

## Perguntas de Ativação

- "Se essa decisão se provar errada, quanto custa reverter?"
- "Estamos gastando uma semana decidindo algo que poderíamos reverter em um dia?"
- "Essa decisão fecha portas permanentemente ou é ajustável?"
- "Qual é o custo de não decidir agora?"
- "Podemos tomar essa decisão de forma incremental em vez de tudo de uma vez?"
- "Existe uma versão menor dessa decisão que podemos testar primeiro?"

## Output Esperado

| Decisão | Tipo | Custo de Reversão | Custo de Atraso | Nível de Análise | Prazo para Decidir |
|---|---|---|---|---|---|
| Escolher banco de dados principal | Tipo 1 | Meses de migração | Equipe parada | Profundo: spike + benchmark | 1 semana |
| Framework CSS | Tipo 2 | Dias de refactor | Baixo | Rápido: escolher e seguir | 1 dia |
| Contrato de 3 anos com cloud provider | Tipo 1 | Multa + migração | Desconto perdido | Profundo: análise financeira + técnica | 2 semanas |
| Estrutura de pastas do projeto | Tipo 2 | Horas de rename | Nenhum | Rápido: convenção do time | 30 min |

## Armadilhas Comuns

1. **Tratar tudo como Tipo 1**: Analisar cada decisão como se fosse irreversível paralisa a equipe e mata a velocidade.
2. **Tratar tudo como Tipo 2**: Tomar decisões arquiteturais irreversíveis sem análise gera dívida técnica catastrófica.
3. **Ignorar custo de atraso**: Análise interminável para decisões Tipo 1 é tão caro quanto decidir errado.
4. **Não reclassificar**: Uma decisão que parece Tipo 1 pode ser convertida em Tipo 2 com feature flags, abstrações ou contratos curtos.
5. **Decisão por omissão**: Não decidir é decidir manter o status quo — que pode ser a pior opção.
6. **Falsa reversibilidade**: Classificar como Tipo 2 algo que parece fácil de reverter mas que na prática envolve migração de dados, retreino de usuários ou reputação comprometida.
