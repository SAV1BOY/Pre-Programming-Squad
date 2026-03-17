# Workflow 09: Prontidão API-First

## Objetivo
Garantir que projetos centrados em APIs sejam planejados com contratos definidos primeiro, permitindo desenvolvimento paralelo entre produtores e consumidores.

## Trigger
- Projeto classificado como "Integração entre sistemas" ou com múltiplas APIs como entrega principal.

## Agentes Envolvidos
- Agente de Arquitetura
- Equipes consumidoras das APIs
- Equipes produtoras das APIs
- Agente de Qualidade

## Passos

### 1. Identificar Todas as APIs Necessárias
- Mapear todas as interfaces que serão expostas.
- Identificar consumidores de cada API.
- **Output:** Inventário de APIs planejadas.

### 2. Definir Contratos (Contract-First)
- Executar task `define-contracts.md`.
- Preencher template `api-contract-template.md` para cada API.
- Incluir schemas, códigos de erro e paginação.
- **Output:** Contratos de API especificados.

### 3. Validar com Consumidores
- Compartilhar contratos com equipes consumidoras.
- Coletar feedback e ajustar.
- Obter aceite formal.
- **Output:** Contratos validados e aceitos.

### 4. Definir Estratégia de Versionamento
- Escolher estratégia (URL path, header, query param).
- Definir política de deprecação.
- **Output:** Política de versionamento documentada.

### 5. Planejar Mock Server
- Configurar mock server para consumidores iniciarem desenvolvimento.
- Validar que mocks refletem os contratos.
- **Output:** Mock server disponível.

### 6. Definir Contract Testing
- Escolher ferramenta de contract testing (Pact, etc.).
- Configurar no CI/CD.
- **Output:** Contract testing configurado.

### 7. Planejar Documentação
- Escolher ferramenta (Swagger/OpenAPI, Redoc, etc.).
- Configurar geração automática a partir dos contratos.
- **Output:** Documentação de API automatizada.

## Gates de Qualidade
- [ ] Todos os endpoints têm contrato definido antes da implementação.
- [ ] Consumidores revisaram e aceitaram os contratos.
- [ ] Estratégia de versionamento está definida.
- [ ] Mock server está disponível e funcional.
- [ ] Contract testing está configurado no CI/CD.
- [ ] Documentação de API será gerada automaticamente.

## Output
- Contratos de API completos e aceitos.
- Mock server funcional.
- Contract testing configurado.
- Documentação automatizada.

## Próximo Workflow
→ Retorna ao workflow principal (06-test-design-to-readiness).
