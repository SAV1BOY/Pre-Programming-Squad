# Task: Dividir em Fases

## Objetivo
Organizar o escopo completo do projeto em fases incrementais e coerentes, definindo critérios claros de transição entre cada fase e garantindo entrega de valor progressivo.

## Input Necessário
- Definição de MVP aprovada.
- Lista completa de funcionalidades priorizadas.
- Mapa de dependências entre funcionalidades.
- Restrições de prazo e recursos.

## Agentes Envolvidos
- **Agente de Escopo:** Conduz a divisão em fases.
- **Agente de Arquitetura:** Valida viabilidade técnica de cada fase.
- **Stakeholder de Produto:** Confirma valor de negócio de cada fase.

## Passos

### 1. Mapear Dependências
- Identificar dependências técnicas entre funcionalidades.
- Identificar dependências de negócio (o que precisa existir antes).
- Criar grafo de dependências para visualizar a ordem natural.

### 2. Agrupar em Fases
- Fase 1 = MVP (já definido).
- Para fases subsequentes, agrupar funcionalidades que:
  - Pertencem ao mesmo domínio/módulo.
  - Têm dependências entre si.
  - Formam um incremento de valor coerente.

### 3. Definir Critérios de Transição
- Para cada fase, definir:
  - Critério de entrada (o que precisa estar pronto).
  - Critério de saída (o que é entregue).
  - Métricas de sucesso específicas da fase.

### 4. Validar Independência
- Cada fase deve poder ser entregue e gerar valor independentemente.
- Se uma fase posterior não for feita, a anterior ainda faz sentido.

### 5. Documentar Roadmap
- Documentar as fases no template `scope-definition-template.md`.
- Incluir estimativa de esforço e duração para cada fase.
- Indicar pontos de decisão (gates) entre fases.

## Output Esperado
- Roadmap de fases com funcionalidades atribuídas a cada uma.
- Critérios de transição entre fases.
- Estimativa de esforço por fase.
- Mapa de dependências entre fases.

## Checklist de Validação
- [ ] Cada fase entrega valor de negócio independente.
- [ ] Dependências técnicas estão respeitadas na sequência.
- [ ] Critérios de entrada e saída de cada fase estão definidos.
- [ ] Estimativas de esforço existem para cada fase.
- [ ] O stakeholder validou a priorização das fases.
- [ ] Há pontos de decisão (gates) entre fases.
- [ ] A fase 1 (MVP) é autossuficiente.
