# Task: Definir Contratos

## Objetivo
Especificar contratos de API e eventos entre componentes e sistemas antes da implementação, permitindo que equipes trabalhem em paralelo contra interfaces acordadas.

## Input Necessário
- Esboço de arquitetura com componentes e comunicação.
- Bounded contexts definidos.
- Requisitos funcionais detalhados.
- Modelo de domínio.

## Agentes Envolvidos
- **Agente de Arquitetura:** Define a estrutura dos contratos.
- **Equipes consumidoras:** Validam que os contratos atendem suas necessidades.
- **Equipes produtoras:** Confirmam viabilidade de implementação.
- **Agente de Qualidade:** Revisa completude e consistência.

## Passos

### 1. Identificar Todas as Interfaces
- Listar todas as comunicações entre componentes.
- Listar todas as integrações com sistemas externos.
- Identificar eventos de domínio que cruzam fronteiras.

### 2. Definir Contratos de API
- Para cada endpoint, especificar:
  - Método HTTP e path.
  - Request payload com tipos e validações.
  - Response payload para sucesso e erros.
  - Códigos de resposta e seus significados.
  - Autenticação e autorização necessárias.
- Usar o template `api-contract-template.md`.

### 3. Definir Contratos de Eventos
- Para cada evento, especificar:
  - Nome e tópico/fila.
  - Schema do payload.
  - Produtor e consumidor(es).
  - Garantias de entrega (at-least-once, exactly-once).

### 4. Definir Schemas Compartilhados
- Modelar objetos que aparecem em múltiplos contratos.
- Usar formato padronizado (JSON Schema, Protobuf, Avro).
- Versionamento de schemas.

### 5. Revisar com Consumidores
- Apresentar contratos para as equipes que vão consumi-los.
- Coletar feedback e ajustar.
- Obter aceite formal dos contratos.

### 6. Registrar em Repositório
- Armazenar contratos em local versionado e acessível.
- Configurar validação automática de contratos (contract testing) se possível.

## Output Esperado
- Contratos de API especificados e aceitos por produtores e consumidores.
- Contratos de eventos especificados.
- Schemas compartilhados documentados.
- Aceite formal das equipes envolvidas.

## Checklist de Validação
- [ ] Todos os endpoints planejados têm contrato definido.
- [ ] Todos os eventos planejados têm schema definido.
- [ ] Request e response payloads incluem tipos e validações.
- [ ] Códigos de erro estão documentados com cenários.
- [ ] Consumidores revisaram e aceitaram os contratos.
- [ ] Produtores confirmaram viabilidade de implementação.
- [ ] Estratégia de versionamento está definida.
- [ ] Contratos estão em local acessível e versionado.
