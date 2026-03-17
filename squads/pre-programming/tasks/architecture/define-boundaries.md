# Task: Definir Fronteiras do Sistema

## Objetivo
Estabelecer claramente as fronteiras do sistema — o que está dentro, o que está fora, onde começa e termina cada componente, e como se comunicam com o mundo externo.

## Input Necessário
- Esboço de arquitetura v1.
- Modelo de domínio.
- Mapa de integrações.
- Escopo definido.

## Agentes Envolvidos
- **Agente de Arquitetura:** Define e documenta as fronteiras.
- **Agente de Domínio:** Valida bounded contexts do domínio.
- **Agente de Integração:** Mapeia fronteiras com sistemas externos.

## Passos

### 1. Definir Fronteira Externa do Sistema
- O que o sistema faz vs. o que é responsabilidade de outros.
- Onde o sistema começa (inputs) e onde termina (outputs).
- Quais interfaces expõe e quais consome.

### 2. Definir Bounded Contexts
- Identificar contextos de domínio distintos.
- Para cada contexto, definir:
  - Entidades que pertencem a ele.
  - Linguagem específica do contexto.
  - Responsabilidades exclusivas.

### 3. Definir Relações entre Contextos
- Upstream/Downstream: quem depende de quem.
- Padrão de integração: Shared Kernel, Anti-Corruption Layer, Open Host.
- Tradução de modelos entre contextos.

### 4. Definir Fronteiras de Serviço (se microserviços)
- Cada serviço = um bounded context (idealmente).
- Definir o que cada serviço faz e o que não faz.
- Garantir que serviços podem evoluir independentemente.

### 5. Documentar Contratos de Fronteira
- Para cada fronteira, documentar o contrato de comunicação.
- Usar o template `api-contract-template.md` para APIs.
- Definir quem é "dono" de cada contrato.

## Output Esperado
- Mapa de fronteiras do sistema (interno e externo).
- Bounded contexts definidos com responsabilidades.
- Contratos de fronteira documentados.
- Modelo de domínio atualizado com bounded contexts.

## Checklist de Validação
- [ ] A fronteira externa do sistema está claramente definida.
- [ ] Bounded contexts estão identificados e descritos.
- [ ] Relações entre contextos estão documentadas (upstream/downstream).
- [ ] Cada contexto tem entidades e responsabilidades definidas.
- [ ] Contratos de fronteira estão documentados.
- [ ] Não há responsabilidade ambígua entre contextos.
- [ ] A equipe de domínio validou os bounded contexts.
