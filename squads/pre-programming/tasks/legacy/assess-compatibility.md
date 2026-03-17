# Task: Avaliar Compatibilidade

## Objetivo
Verificar se o sistema novo é compatível com o sistema legado em termos de dados, interfaces, processos e infraestrutura, identificando pontos de incompatibilidade que precisam ser tratados.

## Input Necessário
- Análise do sistema existente.
- Esboço de arquitetura do sistema novo.
- Contratos de API planejados.
- Modelo de dados novo.

## Agentes Envolvidos
- **Agente de Legado:** Conduz a avaliação de compatibilidade.
- **Agente de Arquitetura:** Compara arquiteturas nova e antiga.
- **DBA:** Avalia compatibilidade de dados.
- **Equipe do legado:** Valida a análise.

## Passos

### 1. Comparar Modelos de Dados
- Mapear entidades do legado para o novo modelo.
- Identificar campos que mudam de tipo, nome ou semântica.
- Identificar dados que existem no legado mas não no novo (e vice-versa).
- Avaliar necessidade de transformação de dados.

### 2. Comparar Interfaces
- Mapear APIs/interfaces do legado para as novas.
- Identificar breaking changes em contratos.
- Verificar se consumidores existentes serão afetados.
- Avaliar necessidade de camada de compatibilidade.

### 3. Avaliar Coexistência
- O sistema novo e o legado podem rodar ao mesmo tempo?
- Como manter dados consistentes entre ambos durante a transição?
- Quais funcionalidades serão duplicadas temporariamente?

### 4. Identificar Incompatibilidades
- Para cada incompatibilidade encontrada, documentar:
  - O que é incompatível.
  - Impacto se não for tratada.
  - Opções de resolução (adapter, migration, deprecation).
  - Esforço estimado.

### 5. Documentar Plano de Compatibilidade
- Atualizar o template `legacy-impact-template.md`.
- Definir estratégia para cada incompatibilidade.

## Output Esperado
- Matriz de compatibilidade entre sistema novo e legado.
- Lista de incompatibilidades com plano de resolução.
- Estratégia de coexistência durante a transição.

## Checklist de Validação
- [ ] Modelos de dados foram comparados campo a campo.
- [ ] Interfaces/APIs foram comparadas.
- [ ] Breaking changes estão identificadas.
- [ ] Impacto em consumidores existentes está avaliado.
- [ ] Estratégia de coexistência está definida.
- [ ] Cada incompatibilidade tem plano de resolução.
- [ ] A equipe do legado validou a análise.
