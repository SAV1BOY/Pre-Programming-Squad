# Google Design Docs — Fonte de Referência

## Fonte

**Organização**: Google
**Prática**: Design Docs como pré-requisito para projetos de engenharia
**Referências Principais**:
- "Design Docs at Google" — artigo de engenharia interna amplamente referenciado
- "Software Engineering at Google" (Livro, O'Reilly, 2020) — Capítulo sobre Design Docs
- Blog de engenharia do Google (research.google / developers.google.com)

## URL de Referência

- https://www.industrialempathy.com/posts/design-docs-at-google/
- https://abseil.io/resources/swe-book (Software Engineering at Google)

---

## O que Aprender

### A Cultura do Design Doc

No Google, nenhum projeto significativo começa sem um design doc aprovado. Isso cria uma cultura onde pensar antes de codificar é a norma, não a exceção. O design doc não é burocracia — é a principal ferramenta de comunicação técnica.

### Estrutura que Funciona

O template do Google é intencionalmente flexível, mas contém seções essenciais:

1. **Context & Scope**: Por que este projeto existe e quais são seus limites
2. **Goals and Non-Goals**: O que faz e explicitamente o que não faz
3. **Design**: A proposta técnica detalhada
4. **Alternatives Considered**: O que mais foi avaliado e por que foi descartado
5. **Cross-cutting Concerns**: Segurança, privacidade, acessibilidade

### O Processo de Revisão

Design docs no Google são revisados por peers, não apenas gestores. Qualquer engenheiro pode comentar. Isso gera:
- Diversidade de perspectivas
- Identificação precoce de problemas
- Alinhamento entre times
- Transfer de conhecimento

### O Papel dos Non-Goals

A seção de "Non-Goals" é considerada tão importante quanto "Goals". Ela previne scope creep e alinha expectativas sobre o que deliberadamente não será abordado.

---

## Práticas Relevantes para Pré-Programação

1. **Design doc como gate obrigatório**: Nenhum projeto passa para codificação sem design doc aprovado. Adotar como prática do squad.

2. **Revisão por pares técnicos**: Não apenas o tech lead revisa — outros engenheiros do time e de times adjacentes devem revisar. Encontram problemas de integração e compartilham contexto.

3. **Alternativas como requisito**: Proibir design docs que apresentam uma única opção. Mínimo de 2-3 alternativas avaliadas com prós e contras.

4. **Non-goals explícitos**: Toda feature e todo projeto devem declarar o que NÃO farão. Adotar como campo obrigatório nos templates do squad.

5. **Documentos vivos durante o design, imutáveis após aprovação**: O design doc pode ser alterado durante a revisão. Após aprovação, mudanças geram novo documento ou addendum.

6. **Tamanho adequado**: Google sugere que design docs tenham entre 3-20 páginas. Menos que 3 provavelmente não tem profundidade suficiente. Mais que 20 provavelmente tenta resolver problemas demais em um único documento.

7. **Diagramas são obrigatórios**: Arquitetura sem diagrama é ficção. Incluir pelo menos: diagrama de componentes, fluxo de dados e modelo de dados.
