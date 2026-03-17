# Ambiguity Burn-Down System

## Título e Propósito

O **Ambiguity Burn-Down System** é um framework para identificar, quantificar e reduzir sistematicamente a ambiguidade em um projeto ao longo do tempo. O propósito é tornar visível o que a equipe não sabe, não entende ou não concordou — e queimar essas ambiguidades antes que se tornem surpresas durante a implementação.

## Quando Usar

- No início de projetos com alta incerteza ou escopo nebuloso
- Quando a equipe sente que "não sabe o que não sabe"
- Em projetos onde requisitos vêm de múltiplas fontes com linguagem inconsistente
- Quando estimativas variam muito entre membros da equipe (sinal de ambiguidade)
- Como ferramenta contínua de acompanhamento durante discovery

## Conceitos-Chave

1. **Ambiguidade**: Situação onde múltiplas interpretações são possíveis e a equipe não convergiu sobre qual é correta.
2. **Ambiguidade Técnica**: Incerteza sobre como implementar (tecnologia, padrão, viabilidade).
3. **Ambiguidade de Requisitos**: Incerteza sobre o que implementar (escopo, comportamento esperado, critérios de aceite).
4. **Ambiguidade Organizacional**: Incerteza sobre quem decide, quem faz, quem aprova.
5. **Burn-Down de Ambiguidade**: Gráfico que mostra redução de itens ambíguos ao longo do tempo. Análogo ao burn-down de tarefas mas para incerteza.

## Processo / Passos

### Passo 1 — Inventariar Ambiguidades
Reúna a equipe e pergunte: "O que não está claro?" Para cada área do projeto (requisitos, arquitetura, integração, infraestrutura, processo), liste todos os pontos ambíguos.

### Passo 2 — Classificar por Tipo e Impacto
Categorize cada ambiguidade: técnica, requisitos, organizacional. Avalie impacto se não for resolvida: **Bloqueante** (impede trabalho), **Significativo** (causa retrabalho), **Menor** (incomoda mas não bloqueia).

### Passo 3 — Definir Responsável e Método de Resolução
Para cada ambiguidade, defina: quem vai resolver, como (conversa, spike técnico, prototipo, pesquisa), e até quando.

### Passo 4 — Executar Resolução
Dedique tempo explícito na sprint/ciclo para resolver ambiguidades. Não trate como overhead — é trabalho essencial.

### Passo 5 — Atualizar o Burn-Down
À medida que ambiguidades são resolvidas, atualize o gráfico. Novas ambiguidades descobertas são adicionadas.

### Passo 6 — Verificar Convergência
O gráfico deve mostrar tendência de queda. Se ambiguidades crescem mais rápido que são resolvidas, há problema de escopo ou comunicação.

### Passo 7 — Gate de Implementação
Não inicie implementação com ambiguidades bloqueantes abertas. Use o burn-down como critério de readiness.

## Perguntas de Ativação

- "Se 5 devs da equipe implementassem isso independentemente, fariam a mesma coisa?"
- "Quais perguntas estamos evitando fazer porque a resposta pode ser complicada?"
- "Quais termos usamos que pessoas diferentes interpretam de forma diferente?"
- "Se começássemos a implementar agora, onde travaríamos por falta de clareza?"
- "O que o stakeholder quis dizer com [termo vago]?"
- "Nossas ambiguidades estão diminuindo ao longo do tempo ou crescendo?"

## Output Esperado

```
BURN-DOWN DE AMBIGUIDADE — Semana 3

Total inicial: 28 ambiguidades
Resolvidas: 19
Adicionadas: 4
Restantes: 13
Bloqueantes: 2

| ID | Ambiguidade | Tipo | Impacto | Responsável | Método | Prazo | Status |
|---|---|---|---|---|---|---|---|
| A-01 | O que "usuário premium" significa exatamente? | Requisitos | Bloqueante | PO | Conversa com negócio | Seg | Resolvida |
| A-02 | API do parceiro suporta webhook? | Técnica | Significativo | Dev Lead | Spike + contato com parceiro | Qua | Em andamento |
| A-03 | Quem aprova mudanças no fluxo de pagamento? | Organizacional | Bloqueante | PM | Reunião com diretor | Qui | Pendente |
| A-04 | Performance aceitável para relatório pesado? | Técnica | Significativo | Dev | Prototipo com dados reais | Sex | Pendente |

GRÁFICO: [28] → [22] → [18] → [13] (tendência de queda — saudável)
```

## Armadilhas Comuns

1. **Ambiguidade invisível**: A equipe não sabe que está ambígua porque todos assumem que entendem — cada um entende diferente.
2. **Listar sem resolver**: Criar o inventário e não dedicar tempo para resolver. O valor está na resolução, não na lista.
3. **Resolver com mais ambiguidade**: "Vamos fazer o que fizer sentido" não resolve ambiguidade — desloca para o implementador.
4. **Burn-down crescente**: Se o gráfico sobe consistentemente, o escopo está mal definido ou a comunicação é insuficiente.
5. **Não incluir ambiguidades organizacionais**: "Quem decide?" e "quem faz?" são tão importantes quanto "o que fazer?".
6. **Perfeccionismo**: Tentar resolver 100% das ambiguidades antes de qualquer implementação paralisa. Foque nas bloqueantes.
