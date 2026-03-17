# Task: Classificar o Projeto

## Objetivo
Categorizar o projeto por tipo, complexidade, risco e domínio, determinando qual workflow de pré-programação deve ser seguido e qual nível de rigor é adequado.

## Input Necessário
- Project Brief aprovado.
- Clarificações de requisitos.
- Contexto sobre sistemas existentes e equipe disponível.

## Agentes Envolvidos
- **Agente de Intake:** Realiza a classificação inicial.
- **Agente de Arquitetura:** Valida a classificação técnica.
- **Agente de Risco:** Avalia a complexidade e o risco.

## Passos

### 1. Classificar por Tipo
- Identificar a natureza principal do projeto:
  - Novo sistema (greenfield)
  - Evolução de sistema existente
  - Migração / Modernização
  - Integração entre sistemas
  - Refatoração técnica
  - Automação de processo
  - Projeto de AI/ML

### 2. Avaliar Complexidade
- Usar matriz de complexidade:
  | Fator | Peso | Valor (1-5) |
  |-------|------|-------------|
  | Número de integrações | 3 | `[valor]` |
  | Incerteza de requisitos | 4 | `[valor]` |
  | Tamanho da equipe necessária | 2 | `[valor]` |
  | Restrições regulatórias | 3 | `[valor]` |
  | Impacto em sistemas legados | 3 | `[valor]` |
  | Novidade tecnológica | 2 | `[valor]` |
- Score total: Baixa (≤30), Média (31-50), Alta (>50)

### 3. Avaliar Nível de Risco
- Identificar fatores de risco:
  - Impacto financeiro de falha
  - Número de usuários afetados
  - Dados sensíveis envolvidos
  - Prazo agressivo
  - Dependências externas

### 4. Selecionar Workflow Adequado
- Com base no tipo e complexidade, selecionar o workflow principal:
  - Projetos simples → Workflow simplificado (intake → escopo → handoff)
  - Projetos médios → Workflow padrão (todos os gates)
  - Projetos complexos → Workflow completo (com revisões adicionais)

### 5. Documentar Classificação
- Registrar a classificação no Project Brief.
- Definir o nível de rigor para cada artefato (obrigatório/recomendado/opcional).

## Output Esperado
- Classificação do projeto documentada (tipo, complexidade, risco).
- Workflow de pré-programação selecionado e justificado.
- Mapa de artefatos obrigatórios para este projeto.

## Checklist de Validação
- [ ] O tipo do projeto está definido e justificado.
- [ ] A complexidade foi avaliada com critérios objetivos.
- [ ] O nível de risco foi documentado.
- [ ] O workflow adequado foi selecionado.
- [ ] Os artefatos obrigatórios estão listados.
- [ ] A equipe de pré-programação concorda com a classificação.
- [ ] O stakeholder foi informado sobre o nível de rigor e o que isso implica em prazo.
