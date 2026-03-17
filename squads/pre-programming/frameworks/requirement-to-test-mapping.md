# Requirement-to-Test Mapping

## Título e Propósito

O **Requirement-to-Test Mapping** é um framework para criar rastreabilidade direta entre cada requisito e os testes que o validam. O propósito é garantir que nenhum requisito fique sem verificação e nenhum teste exista sem justificativa — eliminando tanto lacunas de cobertura quanto testes órfãos que consomem tempo sem valor.

## Quando Usar

- Durante a fase de pré-programação, ao transformar requisitos em plano de testes
- Quando a equipe precisa demonstrar cobertura de requisitos para compliance ou auditoria
- Quando bugs em produção revelam requisitos que não tinham testes associados
- Em projetos com requisitos regulatórios onde rastreabilidade é obrigatória
- Quando o test suite cresceu organicamente e perdeu conexão com os requisitos

## Conceitos-Chave

1. **Rastreabilidade Bidirecional**: De cada requisito, saber quais testes o cobrem. De cada teste, saber qual requisito justifica sua existência.
2. **Requisito Testável**: Um requisito escrito de forma que seja possível definir um teste que o valide ou refute. Requisitos vagos não são testáveis.
3. **Cobertura de Requisitos**: Percentual de requisitos que têm pelo menos um teste associado. Diferente de cobertura de código.
4. **Teste Órfão**: Teste que não valida nenhum requisito atual. Pode ser legado, redundante ou desnecessário.
5. **Gap de Cobertura**: Requisito sem teste associado. É um risco explícito que precisa ser endereçado ou aceito.

## Processo / Passos

### Passo 1 — Listar Todos os Requisitos
Compile requisitos funcionais e não-funcionais. Numere cada um para referência.

### Passo 2 — Avaliar Testabilidade
Para cada requisito, pergunte: "Como eu verificaria se isso foi implementado corretamente?" Se não houver resposta clara, o requisito precisa ser reescrito.

### Passo 3 — Definir Testes por Requisito
Para cada requisito testável, defina um ou mais testes: unitário, integração, e2e, performance, manual. Cada teste recebe um ID.

### Passo 4 — Construir a Matriz de Rastreabilidade
Crie a matriz requisito × teste. Identifique: requisitos sem teste (gaps) e testes sem requisito (órfãos).

### Passo 5 — Resolver Gaps
Para cada gap, decida: criar teste, reformular requisito ou aceitar o risco explicitamente.

### Passo 6 — Resolver Órfãos
Para cada teste órfão, decida: associar a um requisito existente, documentar requisito implícito ou remover o teste.

### Passo 7 — Manter Viva
A matriz deve ser atualizada quando requisitos mudam, são adicionados ou removidos.

## Perguntas de Ativação

- "Qual teste prova que esse requisito foi atendido?"
- "Esse requisito está escrito de forma que eu possa verificar se foi implementado?"
- "Há requisitos sem nenhum teste? Estamos confortáveis com esse risco?"
- "Esse teste valida qual requisito? Se nenhum, por que ele existe?"
- "Se esse teste falhar, qual requisito foi violado?"
- "Nossos testes cobrem os requisitos ou cobrem a implementação?"

## Output Esperado

| ID Requisito | Requisito | Testável? | Testes Associados | Tipo de Teste | Status |
|---|---|---|---|---|---|
| REQ-001 | Usuário pode criar conta com email válido | Sim | T-001, T-002 | Unitário, E2E | Coberto |
| REQ-002 | Sistema deve responder em < 200ms (p95) | Sim | T-010 | Performance | Coberto |
| REQ-003 | Interface deve ser "intuitiva" | Não | — | — | Reescrever requisito |
| REQ-004 | Dados pessoais criptografados em repouso | Sim | T-015 | Integração | Coberto |
| REQ-005 | Notificação por email ao completar pedido | Sim | — | — | GAP — criar teste |

**Resumo**: 25 requisitos, 22 testáveis, 20 cobertos, 2 gaps, 3 testes órfãos.

## Armadilhas Comuns

1. **Requisitos vagos**: "O sistema deve ser rápido" não é testável. Reescreva antes de mapear.
2. **Mapeamento 1:1 forçado**: Nem todo requisito precisa de exatamente um teste. Alguns precisam de vários, outros compartilham testes.
3. **Matriz como burocracia**: Se a matriz vira documento que ninguém consulta, ela perdeu o propósito. Deve ser ferramenta viva.
4. **Cobertura como meta**: 100% de requisitos cobertos não significa que os testes são bons. Qualidade dos testes importa mais que quantidade.
5. **Ignorar requisitos não-funcionais**: Performance, segurança e acessibilidade frequentemente ficam sem testes na matriz.
6. **Não atualizar**: Requisitos mudam, testes são adicionados/removidos. Uma matriz desatualizada é pior que não ter matriz.
