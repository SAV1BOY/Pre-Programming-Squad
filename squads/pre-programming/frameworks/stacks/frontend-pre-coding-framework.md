# Frontend Pre-Coding Framework

## Título e Propósito

O **Frontend Pre-Coding Framework** é um checklist estruturado para garantir que todas as decisões específicas de frontend estejam tomadas antes de implementar. O propósito é endereçar dimensões como gestão de estado, performance percebida, acessibilidade, responsividade e experiência offline que geram retrabalho significativo quando não planejadas.

## Quando Usar

- Antes de iniciar implementação de features ou páginas frontend
- Em projetos com interfaces ricas ou SPAs complexas
- Ao definir design system ou padrões de componentes
- Em migrações de framework ou biblioteca de UI
- Como checklist de readiness para trabalho frontend

## Conceitos-Chave

1. **Gestão de Estado**: Onde o estado vive (local, global, server), como é atualizado e como se mantém consistente.
2. **Performance Percebida**: Não apenas velocidade real, mas a experiência que o usuário tem — loading states, skeleton screens, transições.
3. **Acessibilidade (a11y)**: O sistema é usável por pessoas com deficiências visuais, motoras, cognitivas? Não é feature — é requisito.
4. **Responsividade**: O layout funciona em mobile, tablet e desktop? Touch e mouse? Landscape e portrait?
5. **Contrato com Backend**: O frontend consome APIs. O contrato deve estar definido antes de implementar qualquer chamada.

## Processo / Passos

### Passo 1 — Definir Estrutura de Componentes
Mapeie a hierarquia de componentes. Quais são reutilizáveis? Quais são específicos de página? Qual o design system?

### Passo 2 — Definir Gestão de Estado
Decida: estado local (useState/component state), estado global (Redux/Zustand/Context), estado do servidor (React Query/SWR). Para cada tipo de dado, defina onde vive.

### Passo 3 — Definir Contrato com Backend
Quais APIs são consumidas? O contrato está definido? Há mock disponível para desenvolvimento independente?

### Passo 4 — Planejar Performance
Bundle size, code splitting, lazy loading, image optimization, caching, CDN. Defina budget de performance.

### Passo 5 — Definir Estratégia de Loading e Erro
Para cada chamada async: loading state, error state, empty state, retry. O usuário nunca deve ficar sem feedback.

### Passo 6 — Planejar Acessibilidade
Semântica HTML, ARIA labels, navegação por teclado, contraste de cores, screen reader compatibility.

### Passo 7 — Definir Responsividade
Breakpoints, layout adaptativo, touch targets, viewport testing. Defina quais dispositivos são prioritários.

## Perguntas de Ativação

- "Onde o estado de [X] vive? Local, global ou server?"
- "O que o usuário vê enquanto os dados estão carregando?"
- "Essa interface funciona em mobile? Com touch? Com screen reader?"
- "Qual é o tamanho do bundle para essa página? É aceitável?"
- "Se a API demorar 5 segundos, o que acontece na tela?"
- "O contrato da API está definido ou vamos descobrir durante a implementação?"

## Output Esperado

Checklist preenchido cobrindo: componentes definidos, estado mapeado, contrato de API definido, performance budget, loading/error states, a11y requirements, responsividade.

## Armadilhas Comuns

1. **Estado global para tudo**: Colocar todo estado em Redux/Zustand quando a maioria deveria ser local ou server state.
2. **Implementar sem mock**: Esperar o backend ficar pronto em vez de trabalhar contra mock do contrato.
3. **Acessibilidade como afterthought**: Adicionar ARIA labels depois é mais difícil que projetar com semântica desde o início.
4. **Performance ignorada**: Bundle de 5MB em mobile porque ninguém mediu. Defina budget antes.
5. **Apenas happy path no UI**: Projetar a tela com dados e esquecer: loading, erro, vazio, sem permissão.
6. **Responsividade tardia**: "Depois fazemos funcionar no mobile" é receita para redesign.
