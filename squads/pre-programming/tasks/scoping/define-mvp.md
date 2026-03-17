# Task: Definir o MVP

## Objetivo
Determinar o escopo mínimo viável (MVP) que entrega valor ao usuário e valida as hipóteses mais críticas do projeto, separando o essencial do desejável.

## Input Necessário
- Discovery completa com declaração do problema.
- Requisitos clarificados com priorização MoSCoW.
- Critérios de sucesso definidos.
- Mapa de restrições (especialmente prazo e equipe).

## Agentes Envolvidos
- **Agente de Escopo:** Conduz a definição do MVP.
- **Stakeholder de Produto:** Valida que o MVP entrega valor.
- **Agente de Arquitetura:** Confirma viabilidade técnica do recorte.
- **Agente de Risco:** Avalia riscos do escopo reduzido.

## Passos

### 1. Listar Todas as Funcionalidades
- Consolidar todos os requisitos funcionais identificados.
- Agrupar por tema ou módulo.

### 2. Aplicar Filtro de MVP
- Para cada funcionalidade, perguntar:
  - O sistema tem utilidade sem esta funcionalidade?
  - Esta funcionalidade valida uma hipótese crítica?
  - O usuário consegue completar a jornada principal sem ela?
- Classificar: Essencial para MVP / Pode esperar / Nice-to-have.

### 3. Validar Coerência
- Verificar que o MVP forma um conjunto coerente e funcional.
- Confirmar que o fluxo principal do usuário está completo.
- Garantir que os critérios de sucesso mínimos podem ser atendidos.

### 4. Estimar Esforço do MVP
- Fazer estimativa de alto nível apenas do escopo MVP.
- Comparar com as restrições de prazo e equipe.
- Ajustar se necessário (reduzir mais ou realocar prazo).

### 5. Documentar Escopo MVP
- Preencher o template `scope-definition-template.md` com foco no MVP.
- Listar explicitamente o que fica FORA do MVP e quando será abordado.

## Output Esperado
- Definição clara do escopo MVP com funcionalidades listadas.
- Lista do que está fora do MVP com justificativa e horizonte.
- Estimativa de alto nível do esforço para o MVP.
- Validação de que o MVP atende critérios mínimos de sucesso.

## Checklist de Validação
- [ ] O MVP entrega valor real ao usuário (não é apenas uma fundação técnica).
- [ ] O fluxo principal do usuário está completo no MVP.
- [ ] O escopo MVP é realizável dentro das restrições de prazo e equipe.
- [ ] Itens fora do MVP estão documentados com justificativa.
- [ ] Stakeholder de produto validou que o MVP é "viável" do ponto de vista de negócio.
- [ ] A equipe técnica confirmou que o MVP é tecnicamente coerente.
- [ ] Não há dependências circulares entre itens do MVP e itens fora dele.
