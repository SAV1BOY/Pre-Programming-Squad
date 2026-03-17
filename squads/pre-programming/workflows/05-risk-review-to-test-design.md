# Workflow 05: Da Revisão de Riscos ao Design de Testes

## Objetivo
Traduzir os riscos identificados, modos de falha e requisitos em uma estratégia de testes abrangente que cubra cenários críticos e edge cases.

## Trigger
- Revisão de riscos e modos de falha completa no workflow 04.

## Agentes Envolvidos
- Agente de Qualidade
- Agente de Arquitetura
- Equipe de QA (se disponível)

## Passos

### 1. Mapear Edge Cases
- Executar task `map-edge-cases.md`.
- Usar modos de falha como fonte de cenários de teste.
- **Output:** Lista de edge cases classificados.

### 2. Projetar Estratégia de Testes
- Executar task `design-test-strategy.md`.
- Preencher template `test-design-template.md`.
- **Output:** Estratégia de testes completa.

### 3. Definir Definition of Done
- Preencher template `definition-of-done-template.md`.
- Alinhar com equipe de desenvolvimento.
- **Output:** DoD acordada.

### 4. Planejar Estimativas
- Preencher template `estimation-template.md`.
- Incluir esforço de testes na estimativa.
- **Output:** Estimativas revisadas.

## Gates de Qualidade
- [ ] Edge cases foram mapeados sistematicamente.
- [ ] Pirâmide de testes está definida com proporções.
- [ ] Cenários críticos de teste estão desenhados.
- [ ] Testes não-funcionais estão planejados.
- [ ] Definition of Done está acordada com o dev.
- [ ] Estimativas incluem esforço de testes.

## Output
- Test design completo.
- Definition of Done aprovada.
- Estimation template preenchido.

## Próximo Workflow
→ `06-test-design-to-readiness.md`
