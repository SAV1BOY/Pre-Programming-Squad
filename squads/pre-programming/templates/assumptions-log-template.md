# Template: Registro de Premissas

## Título
Assumptions Log — Registro e Rastreamento de Premissas

## Propósito
Documentar todas as premissas feitas durante o planejamento do projeto, rastrear sua validação e identificar riscos associados a premissas não confirmadas.

## Quando Usar
- Sempre que uma decisão for baseada em algo não confirmado.
- Quando informações estão indisponíveis e é necessário avançar com suposições.
- Em revisões periódicas para validar ou invalidar premissas anteriores.

## Seções

### 1. Informações Gerais
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| Responsável | `[nome]` |
| Data da Última Revisão | `[YYYY-MM-DD]` |

### 2. Registro de Premissas
| ID | Premissa | Categoria | Base | Impacto se Falsa | Status | Validada Por | Data |
|----|----------|-----------|------|-------------------|--------|-------------|------|
| A-01 | `[premissa assumida]` | `[Técnica/Negócio/Recursos/Prazo]` | `[evidência ou razão]` | `[consequência se estiver errada]` | `[Pendente/Validada/Invalidada]` | `[nome]` | `[data]` |

### 3. Premissas Críticas (Alto Impacto se Falsas)
| ID | Premissa | Impacto se Falsa | Plano de Validação | Prazo de Validação |
|----|----------|-------------------|-------------------|-------------------|
| `[ID]` | `[premissa]` | `[consequência grave]` | `[como validar]` | `[até quando]` |

### 4. Premissas Invalidadas
| ID | Premissa Original | Realidade Descoberta | Impacto no Projeto | Ação Tomada |
|----|-------------------|---------------------|--------------------|-|
| `[ID]` | `[o que assumimos]` | `[o que descobrimos]` | `[como afetou]` | `[o que fizemos]` |

### 5. Dependências de Premissas
| Premissa | Decisões Dependentes | Artefatos Afetados |
|----------|---------------------|-------------------|
| `[premissa]` | `[decisões que dependem dela]` | `[documentos, designs, estimativas]` |

## Exemplo de Preenchimento

### 2. Registro de Premissas
| ID | Premissa | Categoria | Base | Impacto se Falsa | Status | Validada Por | Data |
|----|----------|-----------|------|-------------------|--------|-------------|------|
| A-01 | A API do parceiro suporta batch de até 1000 registros | Técnica | Documentação pública (v2.3) | Precisaremos implementar paginação, +2 semanas | Validada | Carlos | 2026-03-10 |
| A-02 | O time de DBA consegue provisionar o banco em 1 semana | Recursos | Conversa informal com o líder | Atraso de 2 semanas no início do dev | Pendente | — | — |
| A-03 | Não haverá mudanças regulatórias no Q2 | Negócio | Cenário atual estável | Retrabalho de compliance, +3 semanas | Pendente | — | — |

## Dicas de Qualidade
- **Registre imediatamente:** Premissa não documentada é premissa esquecida.
- **Valide as críticas primeiro:** Priorize a validação das premissas com maior impacto.
- **Vincule a decisões:** Toda premissa deve estar conectada às decisões que a utilizam.
- **Revise semanalmente:** Premissas mudam. O que era verdade pode não ser mais.
- **Não confunda premissa com fato:** Se está confirmado, é fato. Se não, é premissa.
