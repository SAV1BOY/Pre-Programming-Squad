# Amazon Working Backwards — Fonte de Referência

## Fonte

**Organização**: Amazon
**Prática**: Working Backwards — partir da experiência do cliente para definir o que construir
**Referências Principais**:
- "Working Backwards" (Livro, Colin Bryar & Bill Carr, 2021)
- "The Amazon Way" (John Rossman)
- PR/FAQ como documento fundacional de projetos na Amazon

## URL de Referência

- https://www.aboutamazon.com/news/workplace/working-backwards
- https://www.productplan.com/glossary/working-backward-amazon-method/

---

## O que Aprender

### O Conceito de Working Backwards

Em vez de começar pela tecnologia e perguntar "o que podemos construir?", a Amazon começa pelo cliente e pergunta "o que o cliente precisa?". O processo força o time a articular o valor para o cliente antes de discutir implementação.

### O PR/FAQ (Press Release / FAQ)

Antes de iniciar qualquer projeto, a Amazon exige um documento no formato de press release fictício anunciando o produto como se já estivesse lançado. Esse exercício:

- Força clareza sobre o benefício para o cliente
- Elimina jargão técnico — o PR é escrito para o público
- Revela se o projeto realmente resolve um problema que importa
- O FAQ (interno e externo) antecipa objeções e questões práticas

### Narrativas em vez de Slides

A Amazon proíbe PowerPoint em reuniões de decisão. Em vez disso, usa documentos narrativos de 6 páginas que são lidos em silêncio nos primeiros 20 minutos da reunião. Isso garante:

- Profundidade de pensamento (escrever é pensar)
- Que todos leram o mesmo material
- Discussões baseadas em conteúdo, não em habilidade de apresentação

### O Mecanismo do "Bar Raiser"

Revisões são feitas por alguém de fora do time (Bar Raiser) que não tem viés emocional sobre o projeto. Essa pessoa tem poder de veto e garante qualidade consistente.

---

## Práticas Relevantes para Pré-Programação

1. **PR/FAQ como primeiro artefato**: Antes de design doc ou ADR, escrever um "comunicado de imprensa" fictício do projeto. Se não consegue articular o benefício em linguagem simples, o projeto não está claro o suficiente.

2. **Narrativa sobre slides**: Para readiness reviews e go/no-go, usar documentos escritos em vez de apresentações. Força pensamento estruturado e permite que todos absorvam o conteúdo.

3. **FAQ antecipando objeções**: A seção de FAQ do PR/FAQ é diretamente aplicável ao handoff. Antecipar as 15-20 perguntas mais prováveis do time de desenvolvimento.

4. **Revisor externo (Bar Raiser)**: Para decisões críticas de arquitetura, trazer um revisor de fora do squad — alguém sem viés emocional que possa questionar premissas.

5. **Começar pelo cliente, não pela tecnologia**: Toda pesquisa de stack e decisão de arquitetura deve ser justificada por um benefício ao usuário final, não por preferência técnica.

6. **Métricas de sucesso do cliente**: Definir métricas que medem impacto no cliente (NPS, tempo de tarefa, taxa de erro do usuário), não apenas métricas técnicas (uptime, latência).

7. **Documento de 6 páginas**: Adaptar o formato para briefs do squad. 6 páginas é suficiente para cobrir problema, solução, escopo, riscos e plano sem ser superficial.
