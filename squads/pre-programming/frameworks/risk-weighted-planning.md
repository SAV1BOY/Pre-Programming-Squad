# Risk-Weighted Planning

## Título e Propósito

O **Risk-Weighted Planning** é um framework para incorporar riscos explicitamente no planejamento de projetos, ajustando estimativas, prioridades e sequenciamento com base no perfil de risco de cada componente. O propósito é substituir o planejamento otimista ("se tudo der certo, entregamos em 6 semanas") por planejamento realista que antecipa e absorve problemas.

## Quando Usar

- No planejamento de sprints, ciclos ou projetos
- Quando estimativas precisam refletir incerteza real, não cenários ideais
- Para priorizar a ordem de implementação baseada em risco
- Quando projetos anteriores consistentemente atrasaram
- Em projetos com alta incerteza técnica ou dependências externas

## Conceitos-Chave

1. **Risco Técnico**: Incerteza sobre se a solução técnica vai funcionar como esperado.
2. **Risco de Integração**: Incerteza sobre o comportamento de dependências externas.
3. **Risco de Escopo**: Probabilidade de que requisitos mudem ou cresçam durante a execução.
4. **Buffer de Risco**: Tempo adicional no plano para absorver riscos materializados. Não é "folga" — é gestão de incerteza.
5. **Sequenciamento por Risco**: Implementar primeiro os componentes de maior risco para falhar cedo e barato.

## Processo / Passos

### Passo 1 — Decompor o Trabalho
Quebre o projeto em componentes ou tarefas estimáveis. Cada componente deve ser independente o suficiente para ter seu próprio perfil de risco.

### Passo 2 — Estimar sem Risco (Base)
Para cada componente, estime o esforço no cenário otimista: "Se tudo der certo e não houver surpresas."

### Passo 3 — Identificar Riscos por Componente
Para cada componente, liste riscos específicos: técnico, integração, escopo, dependência de pessoas, etc.

### Passo 4 — Atribuir Multiplicador de Risco
Para cada componente, atribua um multiplicador baseado no perfil de risco:
- **1.0x**: Trabalho bem entendido, sem dependências, equipe experiente
- **1.3x**: Alguma incerteza técnica ou dependência controlável
- **1.5x**: Incerteza significativa ou dependência externa
- **2.0x**: Alta incerteza, tecnologia nova, integração complexa
- **3.0x**: Território desconhecido, pesquisa necessária

### Passo 5 — Calcular Estimativa Ajustada
Estimativa Ajustada = Base × Multiplicador. Some todos os componentes para o total do projeto.

### Passo 6 — Sequenciar por Risco
Ordene: componentes de maior risco primeiro. Isso maximiza o tempo disponível para lidar com surpresas e permite pivotar se necessário.

### Passo 7 — Definir Checkpoints de Risco
Estabeleça pontos no cronograma onde riscos serão reavaliados e o plano ajustado se necessário.

## Perguntas de Ativação

- "Se essa tarefa der problema, quanto tempo a mais vai levar?"
- "Estamos sequenciando pelo que é mais fácil ou pelo que é mais arriscado?"
- "Qual componente, se falhar, compromete todo o projeto?"
- "Nossa estimativa assume que tudo dá certo na primeira tentativa?"
- "Onde está nosso buffer? Se não tem buffer, onde vamos cortar quando algo der errado?"
- "Já fizemos algo parecido antes ou estamos estimando no escuro?"

## Output Esperado

| Componente | Estimativa Base | Riscos | Multiplicador | Estimativa Ajustada | Prioridade de Execução |
|---|---|---|---|---|---|
| Integração com gateway de pagamento | 3 dias | API mal documentada, sandbox instável | 2.0x | 6 dias | 1 (maior risco) |
| Motor de regras de desconto | 5 dias | Lógica complexa, edge cases | 1.5x | 7.5 dias | 2 |
| CRUD de usuários | 2 dias | Bem entendido | 1.0x | 2 dias | 4 (menor risco) |
| Relatório analítico | 3 dias | Requisitos em flux | 1.5x | 4.5 dias | 3 |
| **Total** | **13 dias** | | | **20 dias** | |

**Buffer global adicional**: 10% = 2 dias → **Total planejado: 22 dias**

## Armadilhas Comuns

1. **Planejamento otimista**: Estimar baseado no melhor cenário é a causa número um de atrasos.
2. **Buffer escondido**: Cada dev adiciona buffer individual invisível. Melhor ter buffer explícito e gerenciado.
3. **Sequenciamento por conforto**: Começar pelo que é fácil e deixar o risco para o final — quando não há mais tempo para absorver surpresas.
4. **Multiplicador uniforme**: Usar o mesmo multiplicador para tudo anula o propósito de ponderação por risco.
5. **Buffer como escopo extra**: Stakeholders que veem buffer e adicionam features no "tempo que sobrou".
6. **Não revisitar**: O perfil de risco muda conforme o projeto avança. Reavalie nos checkpoints.
