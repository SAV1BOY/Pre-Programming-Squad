# Workflow 11: Prontidão Frontend

## Objetivo
Garantir que projetos com componente frontend significativo tenham design system, padrões de UI/UX, APIs mockadas e infraestrutura de build prontos para implementação.

## Trigger
- Projeto classificado com componente frontend significativo (web app, SPA, portal).

## Agentes Envolvidos
- Agente de Arquitetura (Frontend)
- Designer de UI/UX
- Agente de Qualidade
- Equipe de DevOps

## Passos

### 1. Validar Protótipos/Wireframes
- Verificar que telas principais estão desenhadas.
- Validar fluxos de navegação.
- Confirmar responsividade planejada.
- **Output:** Protótipos validados.

### 2. Definir Design System/Componentes
- Identificar componentes reutilizáveis.
- Definir padrões de design (cores, tipografia, espaçamento).
- Escolher biblioteca de componentes (se aplicável).
- **Output:** Design system ou guidelines definidos.

### 3. Configurar Projeto Frontend
- Boilerplate do projeto configurado.
- Linter e formatação configurados.
- Estrutura de pastas definida.
- **Output:** Projeto frontend inicializado.

### 4. Configurar Mock APIs
- Mock server configurado com contratos de API.
- Dados de teste realistas.
- **Output:** Frontend pode desenvolver sem depender do backend.

### 5. Planejar Gestão de Estado
- Escolher estratégia (Context, Redux, Zustand, etc.).
- Definir padrões de acesso a dados.
- **Output:** Estratégia de estado definida.

### 6. Planejar Testes Frontend
- Testes unitários de componentes.
- Testes de integração de páginas.
- Testes E2E de fluxos críticos.
- Testes de acessibilidade.
- **Output:** Estratégia de testes frontend.

### 7. Configurar Performance Frontend
- Orçamento de performance definido (bundle size, TTFB, LCP).
- Code splitting planejado.
- Estratégia de cache de assets.
- **Output:** Metas de performance frontend.

## Gates de Qualidade
- [ ] Protótipos das telas principais estão disponíveis.
- [ ] Design system ou guidelines estão definidos.
- [ ] Projeto frontend está inicializado e rodando.
- [ ] Mock APIs estão disponíveis.
- [ ] Estratégia de gestão de estado está definida.
- [ ] Testes frontend estão planejados.
- [ ] Orçamento de performance está definido.

## Output
- Frontend pronto para implementação.
- Design system definido.
- Mock APIs funcionais.

## Próximo Workflow
→ Retorna ao workflow principal (06-test-design-to-readiness).
