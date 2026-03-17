# Ousterhout: Complexity Management

## Título e Propósito

Framework baseado no trabalho de **John Ousterhout** (*A Philosophy of Software Design*). A tese central: **complexidade é o inimigo número um do desenvolvimento de software**. O propósito é aplicar os princípios de Ousterhout na fase de pré-programação para projetar sistemas que minimizem complexidade desde o design, antes que ela se acumule no código.

## Quando Usar

- Em decisões de design e arquitetura onde há escolha entre abordagens simples e complexas
- Quando o sistema existente sofre de complexidade acidental que impede evolução
- Na definição de interfaces entre módulos e serviços
- Em code reviews para avaliar se uma solução está adicionando complexidade desnecessária
- Ao projetar APIs e contratos entre componentes

## Conceitos-Chave

1. **Complexidade é Incremental**: Ninguém decide "vamos tornar o sistema complexo". Cada decisão adiciona um pouco. O acúmulo é que mata.
2. **Deep Modules**: Módulos com interface simples e implementação rica. Poucos métodos públicos que escondem muita funcionalidade. Oposto: shallow modules que expõem complexidade.
3. **Information Hiding**: A implementação de um módulo não deve vazar para quem o usa. Decisões de design ficam dentro do módulo.
4. **Complexidade como Sintomas**: Mudanças amplificadas (mudar uma coisa exige mudar muitas outras), carga cognitiva (muito para entender), e unknowns (não é óbvio o que precisa ser feito).
5. **Tactical vs. Strategic Programming**: Tático resolve o problema imediato (rápido, mas acumula complexidade). Estratégico investe um pouco mais agora para manter simplicidade a longo prazo.

## Processo / Passos

### Passo 1 — Identificar Fontes de Complexidade
Para cada componente do sistema, avalie: há mudanças amplificadas? Alta carga cognitiva? Unknowns?

### Passo 2 — Projetar Deep Modules
Para cada componente, minimize a interface pública. Cada método/endpoint/contrato deve esconder o máximo de complexidade possível.

### Passo 3 — Aplicar Information Hiding
Para cada fronteira entre componentes, pergunte: "Estou expondo detalhes de implementação?" Se sim, redesenhe.

### Passo 4 — Escolher Abordagem Estratégica
Invista 10-20% mais em design para evitar complexidade futura. Não é over-engineering — é investimento proporcional.

### Passo 5 — Avaliar Trade-offs de Complexidade
Para cada decisão de design, pergunte: "Isso adiciona ou remove complexidade do sistema como um todo?"

## Perguntas de Ativação

- "Esse módulo tem interface simples e implementação rica, ou o contrário?"
- "Se eu mudar esse componente internamente, algo externo precisa mudar?"
- "Um novo membro da equipe conseguiria entender essa interface sem ler a implementação?"
- "Estamos resolvendo o problema imediato (tático) ou investindo em simplicidade (estratégico)?"
- "Essa decisão adiciona complexidade que teremos que pagar depois?"

## Output Esperado

Avaliação de cada componente crítico quanto a: profundidade (deep vs. shallow), information hiding, fontes de complexidade, e decisões estratégicas vs. táticas documentadas.

## Armadilhas Comuns

1. **Complexidade justificada por "boas práticas"**: Adicionar camadas de abstração, patterns e indireção porque "é o jeito certo" quando a simplicidade resolveria.
2. **Shallow modules**: Muitos métodos públicos que expõem detalhes internos. A interface é tão complexa quanto a implementação.
3. **Tático como padrão**: Sempre escolher o caminho mais rápido porque "não temos tempo" acumula dívida técnica exponencial.
4. **Confundir simplicidade com superficialidade**: Código simples não é código que faz pouco. É código que faz muito com interface clara.
5. **Complexity creep**: Aceitar "só mais uma flag" ou "só mais um parâmetro" até que a interface se torne incompreensível.
