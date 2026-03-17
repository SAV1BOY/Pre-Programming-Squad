# Task: Projetar Estratégia de Testes

## Objetivo
Definir a estratégia completa de testes do projeto antes da implementação, incluindo pirâmide de testes, ferramentas, ambientes, dados e critérios de qualidade.

## Input Necessário
- Requisitos funcionais e não-funcionais.
- Arquitetura definida.
- Edge cases mapeados.
- Definition of Done acordada.

## Agentes Envolvidos
- **Agente de Qualidade:** Desenha a estratégia de testes.
- **Agente de Arquitetura:** Valida testabilidade da arquitetura.
- **Equipe de Dev:** Confirma viabilidade da estratégia.

## Passos

### 1. Definir Pirâmide de Testes
- Proporção desejada: unitários > integração > E2E.
- Definir o que cada nível cobre neste projeto.
- Definir cobertura mínima por nível.

### 2. Selecionar Ferramentas
- Para cada nível de teste, escolher ferramenta.
- Considerar: experiência da equipe, integração com CI/CD, custo.
- Padronizar para evitar fragmentação.

### 3. Desenhar Cenários Críticos
- Priorizar cenários de teste para funcionalidades Must.
- Incluir happy path, sad path e edge cases.
- Definir critérios de aceite testáveis.

### 4. Planejar Testes Não-Funcionais
- Performance: quais cenários e metas.
- Segurança: quais verificações.
- Acessibilidade: se aplicável.
- Compatibilidade: browsers, dispositivos.

### 5. Definir Estratégia de Dados
- Como gerar dados de teste (factories, fixtures, seed).
- Necessidade de anonimização para dados de produção.
- Gestão de estado entre testes.

### 6. Documentar
- Preencher o template `test-design-template.md`.
- Vincular cenários a requisitos.

## Output Esperado
- Estratégia de testes documentada e completa.
- Pirâmide de testes definida com ferramentas.
- Cenários críticos de teste desenhados.
- Plano de testes não-funcionais.

## Checklist de Validação
- [ ] A pirâmide de testes está definida com proporções.
- [ ] Ferramentas de teste estão selecionadas para cada nível.
- [ ] Cenários críticos estão desenhados com critérios de aceite.
- [ ] Testes não-funcionais estão planejados (performance, segurança).
- [ ] Estratégia de dados de teste está definida.
- [ ] A equipe de dev revisou e concordou com a estratégia.
- [ ] Ambientes de teste estão planejados.
- [ ] Cobertura mínima de código está definida.
