# Internal Tooling Readiness Framework

## Título e Propósito

O **Internal Tooling Readiness Framework** é um checklist para projetos de ferramentas internas — admin panels, dashboards operacionais, scripts de automação, ferramentas de suporte. O propósito é evitar que ferramentas internas sejam tratadas como cidadãos de segunda classe — sem design, sem testes, sem manutenção — apesar de serem críticas para operações e frequentemente as mais usadas pela equipe.

## Quando Usar

- Ao planejar desenvolvimento de admin panels ou backoffice
- Em projetos de dashboards operacionais ou de business intelligence
- Ao construir ferramentas de suporte ao cliente (internal CRUD, ferramentas de debug)
- Em automações de processos internos (scripts, jobs, pipelines)
- Para decidir se build vs. buy para ferramentas internas (Retool, AppSmith vs. custom)

## Conceitos-Chave

1. **Ferramenta Interna como Produto**: Ferramentas internas têm usuários (operadores, suporte, devs) que merecem experiência funcional.
2. **80/20 de Features**: 80% do valor vem de 20% das funcionalidades. Foque no essencial, não em polish.
3. **Segurança Interna**: Ferramentas internas frequentemente têm acesso privilegiado a dados. Segurança é mais, não menos, importante.
4. **Manutenção Sustentável**: Ferramentas internas tendem a crescer organicamente sem governance. Planeje manutenção.
5. **Build vs. Buy**: Retool, AppSmith, Metabase cobrem muitos casos. Custom só quando necessário.

## Processo / Passos

### Passo 1 — Definir Usuários e Casos de Uso
Quem usa a ferramenta? Para quê? Com que frequência? Quanto tempo gasta hoje fazendo isso manualmente?

### Passo 2 — Avaliar Build vs. Buy
Ferramentas no-code/low-code (Retool, AppSmith) atendem? Se sim, o custo é menor e a entrega mais rápida.

### Passo 3 — Definir Escopo Mínimo
Quais funcionalidades são essenciais? Resistir à tentação de "já que estamos fazendo, vamos adicionar..."

### Passo 4 — Projetar Segurança e Auditoria
Quem pode acessar? Quais ações são logadas? Há dados sensíveis expostos? RBAC é necessário?

### Passo 5 — Definir Nível de Qualidade
Ferramentas internas não precisam de pixel-perfect design, mas precisam: funcionar corretamente, não perder dados, ter tratamento de erros.

### Passo 6 — Planejar Manutenção
Quem mantém quando APIs mudam? Quem adiciona features? Sem dono, a ferramenta apodrece.

### Passo 7 — Documentar para Operadores
Documentação mínima para operadores: o que a ferramenta faz, como usar, limitações conhecidas.

## Perguntas de Ativação

- "Uma ferramenta no-code resolveria 80% desse problema?"
- "Quem é responsável por manter essa ferramenta depois de entregue?"
- "Essa ferramenta interna tem acesso a dados de produção? A segurança é adequada?"
- "Quanto tempo os operadores gastam hoje fazendo isso manualmente?"
- "Se essa ferramenta der dados errados, alguém percebe antes de tomar decisão errada?"
- "Qual é o escopo mínimo que resolve o problema?"

## Output Esperado

Avaliação build vs. buy, escopo mínimo definido, segurança projetada, plano de manutenção, documentação para operadores.

## Armadilhas Comuns

1. **Ferramenta eterna "temporária"**: Script quick-and-dirty que vira ferramenta oficial usada por 3 anos.
2. **Sem segurança**: "É só interno" — mas tem acesso a todos os dados de produção sem controle.
3. **Sem dono**: Ferramenta que ninguém mantém, com bugs que ninguém corrige, com dados que ninguém valida.
4. **Over-engineering**: Aplicar padrões de produto externo a ferramenta interna. Funcional basta; perfeito é desperdício.
5. **Build quando buy resolve**: Construir custom quando Retool/AppSmith resolveriam em 1/10 do tempo.
6. **Sem auditoria**: Ações administrativas (deletar dados, mudar status) sem log de quem fez e quando.
