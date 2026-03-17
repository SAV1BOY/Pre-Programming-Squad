# Workshop Kit — Design Doc

## Objetivo

Capacitar membros do squad e times de desenvolvimento na criação de design docs eficazes. Ao final do workshop, os participantes serão capazes de escrever um design doc completo que comunique contexto, decisões, alternativas e trade-offs de forma clara e estruturada. O workshop combina teoria (o que faz um bom design doc) com prática (escrever um design doc real).

---

## Duração

**4 horas** (meio período), divididas em:
- 45min — Teoria e exemplos
- 30min — Análise de design docs bons e ruins
- 15min — Intervalo
- 90min — Exercício prático (escrita de design doc)
- 30min — Revisão por pares
- 30min — Retrospectiva e discussão

---

## Participantes

- **Mínimo**: 4 pessoas | **Máximo**: 12 pessoas
- **Perfil ideal**: Engenheiros seniores, tech leads, arquitetos, membros do Pre-Programming Squad
- **Pré-requisito**: Experiência mínima de 1 ano em desenvolvimento de software
- **Facilitador**: Membro experiente do squad ou arquiteto sênior

---

## Agenda Detalhada

### Bloco 1 — Teoria e Exemplos (45 min)

1. **Por que Design Docs existem** (10 min)
   - Comunicação assíncrona de decisões técnicas
   - Registro histórico do raciocínio por trás da arquitetura
   - Ferramenta de revisão antes do código existir
   - Referência do Google: design docs como gate obrigatório

2. **Anatomia de um Design Doc** (20 min)
   - Contexto e Escopo: O problema e os limites
   - Objetivos e Não-Objetivos: O que faz e deliberadamente não faz
   - Design Proposto: A solução técnica detalhada
   - Alternativas Consideradas: O que mais foi avaliado
   - Trade-offs: Custos conscientes da decisão
   - Plano de Migração/Rollout: Como sair de A para B
   - Riscos e Mitigações: O que pode dar errado

3. **Erros Comuns** (15 min)
   - Design doc que é só a decisão sem alternativas
   - Design doc sem não-objetivos (convite para scope creep)
   - Design doc sem diagramas (texto puro é insuficiente)
   - Design doc escrito após a implementação (pós-racionalization)

### Bloco 2 — Análise de Exemplos (30 min)

Dividir em grupos de 3-4 pessoas. Cada grupo recebe:
- 1 design doc "bom" (do swipe file)
- 1 design doc "ruim" (com problemas plantados)

Tarefa: Identificar 5 pontos fortes do bom e 5 problemas do ruim. Apresentar em 5 minutos.

### Intervalo (15 min)

### Bloco 3 — Exercício Prático (90 min)

Cada grupo recebe um cenário fictício (mas realista) e deve escrever um design doc completo.

**Cenários sugeridos**:
- A: Projetar sistema de filas de atendimento com priorização por SLA
- B: Projetar migração de autenticação de sessão para JWT
- C: Projetar sistema de notificações multi-canal com preferências do usuário
- D: Projetar cache distribuído para catálogo de produtos com 500K SKUs

Template fornecido com seções obrigatórias. Grupos devem preencher todas as seções.

### Bloco 4 — Revisão por Pares (30 min)

Grupos trocam design docs e fazem revisão escrita:
- Está claro o que será construído?
- As alternativas são convincentes?
- Os trade-offs são honestos?
- Faltou algum cenário de falha?
- O diagrama é compreensível?

### Bloco 5 — Retrospectiva (30 min)

Discussão aberta:
- O que foi mais difícil de escrever?
- Que seção gerou mais debate no grupo?
- Como adaptar o template para nosso contexto?
- Quais critérios de qualidade adotar para design docs do squad?

---

## Exercícios

1. **Exercício de Não-Objetivos**: Dado um requisito de projeto, cada pessoa escreve 3 não-objetivos. Comparar — diversidade revela ambiguidades.

2. **Exercício de Alternativas**: Dado um design proposto, cada pessoa deve propor uma alternativa radicalmente diferente em 10 minutos. Discutir trade-offs.

3. **Exercício de "Destruição"**: Dado um design doc, cada pessoa tenta encontrar o cenário de falha que o autor não considerou. Quem encontrar mais ganha.

4. **Exercício de Diagrama**: Mesma arquitetura descrita por diferentes pessoas. Comparar diagramas — diferenças revelam ambiguidades na descrição textual.

---

## Outputs Esperados

- Cada participante sai com habilidade prática de escrever design docs
- Template de design doc adaptado para o contexto do squad
- Checklist de revisão de design doc acordado pelo grupo
- Catálogo de "erros comuns" específico da organização
- Pelo menos 3-4 design docs de prática que podem servir como exemplos futuros
