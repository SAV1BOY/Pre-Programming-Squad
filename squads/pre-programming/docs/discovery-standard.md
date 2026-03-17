# Standard para Fase de Descoberta (Discovery)

## Propósito

Definir o processo e os critérios de qualidade para a fase de descoberta técnica e de negócio. O discovery transforma um pedido de projeto em entendimento profundo do problema, contexto e restrições — base para todas as decisões subsequentes.

## Escopo

Projetos classificados como M, G ou XG na triagem. Projetos P podem pular discovery se o escopo já estiver claro no intake.

## Definições

| Termo | Definição |
|---|---|
| Discovery | Fase de investigação que visa entender profundamente o problema, o contexto técnico, os stakeholders e as restrições antes de definir escopo |
| Spike Técnico | Investigação prática (código, prototipagem) para reduzir incerteza técnica específica |
| Mapa de Stakeholders | Identificação de todas as pessoas e times impactados ou que influenciam o projeto |

## Processo

### 1. Preparação (Dia 1)

- Revisar toda documentação existente (intake, PRD, RFCs anteriores, tickets relacionados)
- Identificar stakeholders para entrevistas
- Preparar perguntas-guia organizadas por tema
- Agendar sessões de discovery

### 2. Investigação de Negócio (Dias 2-3)

**Atividades:**
- Entrevista com PM/solicitante sobre o problema e contexto de negócio
- Coleta de métricas de negócio (impacto, volume, custo atual)
- Mapeamento de jornada do usuário impactada
- Identificação de restrições de negócio (prazo, orçamento, regulatório)

**Perguntas-guia:**
- Qual é o problema real? (não a solução proposta, o problema subjacente)
- Quem é afetado e com que frequência?
- Qual o custo de não fazer nada?
- Qual o critério de sucesso mensurável?
- Existem restrições de prazo não negociáveis? Por quê?

### 3. Investigação Técnica (Dias 3-5)

**Atividades:**
- Mapeamento do estado atual dos sistemas envolvidos
- Identificação de dependências técnicas (serviços, APIs, bancos, infra)
- Avaliação de dívida técnica relevante ao projeto
- Análise de viabilidade técnica das abordagens cogitadas
- Spike técnico para áreas de alta incerteza (quando necessário)

**Perguntas-guia:**
- Quais sistemas são impactados? Como se comunicam hoje?
- Existe dívida técnica que bloqueia ou dificulta este projeto?
- Quais são as restrições de infraestrutura (capacidade, região, compliance)?
- Alguém já tentou algo similar? O que aconteceu?
- Existem integrações externas envolvidas? Qual o SLA e a documentação delas?

### 4. Síntese (Dia 5-6)

Consolidar descobertas em documento de discovery com:

- **Problema:** Descrição precisa e quantificada do problema
- **Contexto:** Estado atual técnico e de negócio
- **Stakeholders:** Mapa com papel e interesse de cada um
- **Restrições:** Limitações identificadas (técnicas, negócio, regulatórias)
- **Riscos iniciais:** Riscos percebidos durante discovery
- **Perguntas abertas:** O que não foi possível descobrir, com plano para resolver
- **Recomendação:** Prosseguir para scoping / pedir mais investigação / recomendar não fazer

### 5. Validação

- Apresentar síntese ao solicitante e stakeholders-chave
- Confirmar que o entendimento está correto
- Obter aceite para prosseguir ao scoping

## Critérios de Qualidade

- Documento de discovery endereça todas as seções listadas na síntese
- Nenhuma afirmação quantitativa sem fonte de dados
- Pelo menos 2 stakeholders entrevistados (negócio + técnico)
- Perguntas abertas têm owner e prazo para resolução
- Spike técnico realizado quando incerteza técnica é alta
- Solicitante valida a síntese antes de prosseguir

## Responsáveis

| Papel | Responsabilidade |
|---|---|
| Membro do squad (analista) | Conduzir discovery, documentar achados, facilitar sessões |
| Solicitante | Participar ativamente, fornecer contexto e acesso a stakeholders |
| Tech Lead | Orientar profundidade da investigação, revisar síntese |
| Stakeholders técnicos | Fornecer informações sobre sistemas existentes |

## Referências

- Standard de Intake: `docs/project-intake-standard.md`
- Standard de Scoping: `docs/scoping-standard.md`
- Standard de Revisão de Riscos: `docs/risk-review-standard.md`
