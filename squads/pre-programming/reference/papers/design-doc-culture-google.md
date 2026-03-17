# Cultura de Design Docs no Google

## Titulo

Design Document Culture at Google and Its Impact on Software Quality

## Resumo

O Google adota uma cultura onde toda mudanca significativa de software requer um design doc escrito e revisado antes da implementacao. Essa pratica, documentada em "Software Engineering at Google" (Winters et al., 2020) e em diversos artigos internos do Google, demonstra que a escrita e revisao de design docs melhora a qualidade do software, dissemina conhecimento, cria documentacao historica de decisoes e previne desperdicio de esforco em abordagens equivocadas. A pratica nao e burocracia — e uma ferramenta de pensamento.

## Insight Principal

Escrever um design doc nao e documentar uma decisao ja tomada — e o processo de pensar rigorosamente sobre o problema. O ato de escrever forca clareza, expoe lacunas no raciocinio e cria um artefato revisavel. A revisao por pares traz perspectivas diversas e previne vieses individuais. O design doc e, portanto, uma ferramenta de design, nao apenas de documentacao.

## Estrutura Tipica de um Design Doc (Google)

### 1. Context and Scope
Qual e o problema? Quem e afetado? Qual e o escopo da mudanca?

### 2. Goals and Non-Goals
O que esta e o que nao esta no escopo. Non-goals sao tao importantes quanto goals — previnem scope creep.

### 3. Design Overview
Descricao de alto nivel da solucao proposta. Diagramas de arquitetura, fluxos de dados, componentes principais.

### 4. Detailed Design
Detalhamento tecnico: APIs, modelos de dados, algoritmos, fluxos de erro. Nivel de detalhe suficiente para que outro engenheiro possa implementar.

### 5. Alternatives Considered
Pelo menos duas alternativas genuinas com pros e contras de cada. Explica por que a opcao escolhida e preferida.

### 6. Cross-cutting Concerns
Seguranca, privacidade, acessibilidade, internacionalizacao, observabilidade.

### 7. Migration / Rollout Plan
Como a mudanca sera implantada. Feature flags, migracoes de dados, rollback plan.

## Principios da Cultura de Design Doc

### Escrever para Pensar
O objetivo primario nao e produzir um documento — e forcar o pensamento rigoroso. Se voce nao consegue explicar por escrito, provavelmente nao entende bem o suficiente.

### Revisao como Colaboracao
A revisao nao e um gate de aprovacao — e uma conversa colaborativa para melhorar o design. Revisores trazem perspectivas diferentes e identificam pontos cegos.

### Proporcionalidade
O tamanho do design doc deve ser proporcional ao impacto e risco da mudanca. Mudancas pequenas precisam de docs pequenos. Mudancas significativas precisam de docs detalhados.

### Documento Vivo
Design docs sao atualizados durante a implementacao quando o design muda. Eles nao sao contratos imutaveis — sao artefatos de pensamento que evoluem.

## Aplicacao ao Squad

### Como Ferramenta de Pre-Programacao
- Adotar design docs como artefato principal de saida do squad de pre-programacao.
- Usar a estrutura do Google como template adaptavel.
- Exigir "Alternatives Considered" como secao obrigatoria.
- Incluir "Non-Goals" para prevenir scope creep.

### Como Processo de Revisao
- Toda decisao arquitetural significativa requer design doc revisado.
- Definir niveis de revisao baseados em impacto (self-review, peer review, architectural review).
- Revisores devem incluir representantes de equipes impactadas.
- Feedback deve ser construtivo e focado em melhorar o design.

### Como Registro Historico
- Design docs se tornam ADRs (Architecture Decision Records) implicitos.
- Manter um indice de design docs para consulta futura.
- Vincular design docs a PRs e tickets de implementacao.

## Referencias

- Winters, T., Manshreck, T., Wright, H. (2020). "Software Engineering at Google." O'Reilly.
- Larson, W. (2019). "Design Docs at Google." Staff Engineer blog.
- Hynes, C. (2020). "Writing Technical Design Documents." Google Engineering Practices.
