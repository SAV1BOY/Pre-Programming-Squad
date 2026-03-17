# Constraints-Led Design

## Título e Propósito

O **Constraints-Led Design** é um framework que inverte a lógica tradicional de design: em vez de começar pela solução ideal e depois acomodar restrições, começa pelas restrições e deixa que elas guiem o espaço de soluções viáveis. O propósito é eliminar retrabalho causado por soluções bonitas que esbarram na realidade.

## Quando Usar

- Quando o projeto opera sob restrições severas (prazo, orçamento, equipe reduzida, tecnologia legada)
- Quando a equipe tende a projetar soluções ideais que nunca cabem no contexto real
- Em projetos de migração ou modernização com restrições de compatibilidade
- Quando há restrições regulatórias ou de compliance que limitam opções
- Em contextos de startup com recursos limitados e pressão de mercado

## Conceitos-Chave

1. **Restrição Dura**: Limite que não pode ser negociado — regulação, contrato, limitação física. Viola-la é impossível ou ilegal.
2. **Restrição Mole**: Limite que pode ser negociado com esforço — prazo, orçamento, escopo. Pode ser alterada com trade-offs.
3. **Espaço de Soluções**: O conjunto de todas as soluções possíveis. Cada restrição reduz esse espaço. O design emerge das opções restantes.
4. **Restrição Generativa**: Uma restrição que, paradoxalmente, facilita o design ao eliminar opções e forçar criatividade dentro de limites claros.
5. **Conflito de Restrições**: Quando duas restrições são mutuamente exclusivas, algo precisa ceder — e essa decisão precisa ser explícita.

## Processo / Passos

### Passo 1 — Inventariar Todas as Restrições
Liste todas as restrições conhecidas em categorias: técnicas, de negócio, regulatórias, de equipe, de infraestrutura, de prazo e de orçamento.

### Passo 2 — Classificar: Dura vs. Mole
Para cada restrição, pergunte: "Isso pode ser negociado?" Se sim, é mole. Se não, é dura. Registre quem confirmou a classificação.

### Passo 3 — Identificar Conflitos
Cruze as restrições: "Há duas restrições que não podem ser satisfeitas simultaneamente?" Documente cada conflito.

### Passo 4 — Resolver Conflitos
Para cada conflito, escalone para quem tem autoridade de decisão. Registre a resolução e qual restrição foi relaxada.

### Passo 5 — Desenhar Dentro do Espaço Restante
Com as restrições mapeadas e conflitos resolvidos, projete soluções que caibam dentro do espaço viável. Não tente expandir o espaço — trabalhe dentro dele.

### Passo 6 — Testar Contra as Restrições
Para cada solução proposta, verifique sistematicamente se ela respeita cada restrição. Use uma checklist explícita.

### Passo 7 — Documentar Restrições Relaxadas
Se alguma restrição foi relaxada durante o processo, documente quem decidiu, por quê e quais riscos foram aceitos.

## Perguntas de Ativação

- "Quais restrições são absolutas e quais podemos negociar?"
- "Se tivéssemos que entregar em metade do prazo, o que cortaríamos?"
- "Essa restrição foi validada ou é percepção da equipe?"
- "Qual restrição está mais limitando nosso espaço de soluções?"
- "Há restrições que estamos ignorando e que vão nos surpreender depois?"
- "Essa restrição é permanente ou temporária?"

## Output Esperado

| Restrição | Tipo | Categoria | Fonte | Impacto no Design | Conflitos | Resolução |
|---|---|---|---|---|---|---|
| LGPD — dados pessoais não podem sair do Brasil | Dura | Regulatória | Jurídico | Elimina provedores cloud sem região BR | Nenhum | — |
| Prazo de 8 semanas | Mole | Negócio | Diretor de Produto | Limita escopo a MVP | Conflita com "precisa ser escalável" | Escopo MVP + arquitetura extensível |
| Sistema legado não pode ser alterado | Dura | Técnica | CTO | Integração via API/eventos, sem acesso ao banco | Nenhum | — |
| Equipe de 3 devs | Mole | Equipe | RH | Limita paralelismo e complexidade | Conflita com prazo | Priorizar features de maior impacto |

## Armadilhas Comuns

1. **Ignorar restrições no início**: Projetar a "solução ideal" e depois tentar encaixar restrições gera retrabalho e frustração.
2. **Tratar tudo como restrição dura**: Nem toda limitação é absoluta. Questione a rigidez de cada restrição.
3. **Tratar tudo como restrição mole**: Algumas limitações realmente não podem ser negociadas. Tentar relaxar restrições duras gera risco legal ou técnico.
4. **Restrições invisíveis**: Restrições organizacionais (política, silos, processos) que ninguém menciona mas que bloqueiam a implementação.
5. **Otimismo sobre negociação**: Assumir que uma restrição mole "certamente será relaxada" sem ter feito a negociação.
6. **Design que encosta nos limites**: Projetar uma solução que funciona exatamente no limite das restrições não deixa margem para imprevistos.
