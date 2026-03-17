# Workflow 03: Do Escopo à Arquitetura

## Objetivo
Transformar o escopo aprovado em decisões arquiteturais documentadas, incluindo componentes, contratos, modelo de dados e fronteiras do sistema.

## Trigger
- Escopo aprovado no workflow 02.

## Agentes Envolvidos
- Agente de Arquitetura
- Agente de Domínio
- Agente de Risco
- Tech Lead

## Passos

### 1. Comparar Opções de Solução
- Executar task `compare-solution-options.md`.
- Preencher template `solution-options-template.md`.
- Se aplicável, preencher template `build-vs-buy-template.md`.
- **Output:** Decisão de solução documentada.

### 2. Esboçar Arquitetura v1
- Executar task `sketch-architecture-v1.md`.
- Preencher template `architecture-sketch-template.md`.
- **Output:** Esboço arquitetural com diagrama.

### 3. Modelar Domínio
- Preencher template `domain-model-template.md`.
- Definir Ubiquitous Language.
- **Output:** Modelo de domínio documentado.

### 4. Definir Fronteiras
- Executar task `define-boundaries.md`.
- Definir bounded contexts e relações.
- **Output:** Mapa de fronteiras do sistema.

### 5. Definir Contratos
- Executar task `define-contracts.md`.
- Preencher template `api-contract-template.md`.
- **Output:** Contratos de API especificados.

### 6. Modelar Dados
- Preencher template `data-model-template.md`.
- **Output:** Modelo de dados documentado.

### 7. Mapear Integrações
- Preencher template `integration-map-template.md`.
- **Output:** Mapa de integrações completo.

### 8. Registrar Decisões
- Preencher template `decision-memo-template.md` para cada decisão significativa.
- **Output:** ADRs documentados.

## Gates de Qualidade
- [ ] Opções de solução foram comparadas com critérios objetivos.
- [ ] Arquitetura está documentada com diagrama de componentes.
- [ ] Modelo de domínio reflete o entendimento do negócio.
- [ ] Bounded contexts estão definidos.
- [ ] Contratos de API estão especificados.
- [ ] Modelo de dados está definido.
- [ ] Integrações estão mapeadas.
- [ ] Decisões técnicas estão documentadas com justificativa.
- [ ] A arquitetura foi revisada por pelo menos um par.

## Output
- Architecture sketch completo.
- Domain model documentado.
- API contracts especificados.
- Data model definido.
- Integration map preenchido.
- Decision memos registrados.

## Próximo Workflow
→ `04-architecture-to-risk-review.md`
