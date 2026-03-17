# Workflow 04: Da Arquitetura à Revisão de Riscos

## Objetivo
Revisar a arquitetura proposta sob a perspectiva de riscos, modos de falha e premissas, garantindo que o design é resiliente e os riscos são tratáveis.

## Trigger
- Arquitetura v1 documentada no workflow 03.

## Agentes Envolvidos
- Agente de Risco
- Agente de Arquitetura
- Agente de Qualidade

## Passos

### 1. Revisar Modos de Falha
- Preencher template `failure-mode-review-template.md`.
- Identificar como cada componente pode falhar.
- Calcular RPN (Risk Priority Number) para cada modo.
- **Output:** Análise de modos de falha completa.

### 2. Revisar Premissas
- Preencher template `assumptions-log-template.md`.
- Listar todas as premissas feitas durante a arquitetura.
- Validar premissas críticas imediatamente.
- **Output:** Log de premissas com plano de validação.

### 3. Atualizar Registro de Riscos
- Adicionar riscos técnicos descobertos na análise de falha.
- Reavaliar severidade dos riscos existentes com base na arquitetura.
- **Output:** Risk register atualizado.

### 4. Definir Estratégias de Resiliência
- Para os modos de falha mais críticos, definir:
  - Circuit breakers, retries, fallbacks.
  - Redundância e failover.
  - Graceful degradation.
- **Output:** Estratégias de resiliência documentadas.

### 5. Revisar Arquitetura (se necessário)
- Se riscos inaceitáveis foram encontrados, ajustar a arquitetura.
- Documentar mudanças e justificativas.
- **Output:** Arquitetura v2 (se alterada).

## Gates de Qualidade
- [ ] Modos de falha de todos os componentes críticos foram analisados.
- [ ] Top 5 modos de falha (por RPN) têm plano de mitigação.
- [ ] Premissas críticas estão identificadas e com plano de validação.
- [ ] Registro de riscos foi atualizado com riscos técnicos.
- [ ] Estratégias de resiliência estão documentadas.
- [ ] Não há riscos inaceitáveis sem plano de ação.

## Output
- Failure mode review completo.
- Assumptions log preenchido.
- Risk register atualizado.
- Estratégias de resiliência documentadas.

## Próximo Workflow
→ `05-risk-review-to-test-design.md`
