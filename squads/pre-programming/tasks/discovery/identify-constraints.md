# Task: Identificar Restrições

## Objetivo
Mapear todas as restrições que limitam as opções de solução do projeto, categorizá-las e avaliar seu impacto nas decisões de escopo e arquitetura.

## Input Necessário
- Project Brief aprovado.
- Informações de stakeholders sobre prazos e orçamento.
- Contexto tecnológico da organização.
- Requisitos regulatórios aplicáveis.

## Agentes Envolvidos
- **Agente de Discovery:** Conduz o levantamento de restrições.
- **Agente de Arquitetura:** Identifica restrições técnicas.
- **Agente de Risco:** Avalia impacto das restrições.
- **Stakeholders de Compliance/Segurança:** Fornecem restrições regulatórias.

## Passos

### 1. Levantar Restrições por Categoria
- **Tempo:** Deadlines, datas de lançamento, dependências de cronograma.
- **Orçamento:** Limites financeiros, custo de infraestrutura.
- **Tecnologia:** Stack obrigatório, proibições, licenças.
- **Equipe:** Tamanho, skills disponíveis, disponibilidade.
- **Regulatório:** LGPD, PCI-DSS, normas setoriais.
- **Infraestrutura:** Ambientes disponíveis, capacidade, região.
- **Organizacional:** Processos de aprovação, cultura, políticas.

### 2. Validar Cada Restrição
- Para cada restrição, verificar: é real ou percebida?
- Confirmar com a fonte original.
- Questionar restrições herdadas de projetos anteriores.

### 3. Avaliar Impacto
- Para cada restrição confirmada, avaliar:
  - Impacto no escopo (o que não podemos fazer).
  - Impacto na arquitetura (como limita o design).
  - Impacto no cronograma (como afeta prazos).

### 4. Classificar Negociabilidade
- Inegociável: não pode ser alterada (ex: lei, deadline externo).
- Negociável com esforço: pode ser mudada com aprovação.
- Preferência: pode ser ajustada com facilidade.

### 5. Documentar
- Preencher o template `constraint-map-template.md`.
- Vincular restrições às decisões que elas afetam.

## Output Esperado
- Mapa de restrições completo e categorizado.
- Classificação de negociabilidade para cada restrição.
- Análise de impacto documentada.

## Checklist de Validação
- [ ] Todas as categorias de restrição foram avaliadas.
- [ ] Cada restrição tem uma fonte identificável.
- [ ] Restrições foram validadas (não são apenas percepções).
- [ ] Impacto de cada restrição está documentado.
- [ ] Negociabilidade está classificada.
- [ ] Restrições regulatórias foram validadas com compliance.
- [ ] O mapa está vinculado a decisões de escopo e arquitetura.
