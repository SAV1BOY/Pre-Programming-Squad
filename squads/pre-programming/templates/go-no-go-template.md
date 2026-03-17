# Template: Go/No-Go

## Título
Go/No-Go — Decisão de Prosseguir ou Parar

## Propósito
Fornecer uma estrutura formal para a decisão de prosseguir (Go) ou parar (No-Go) em pontos críticos do projeto, com base em critérios objetivos e evidências documentadas.

## Quando Usar
- Antes de iniciar desenvolvimento (gate pré-programação → dev).
- Antes de deploy em produção.
- Em qualquer ponto de decisão crítica onde parar é uma opção viável.

## Seções

### 1. Informações Gerais
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| Gate | `[nome do checkpoint — ex: Pré-Dev, Pré-Prod, Fase 2]` |
| Data | `[YYYY-MM-DD]` |
| Facilitador | `[nome]` |
| Decisor Final | `[nome e papel]` |
| Resultado | `[GO / NO-GO / GO COM CONDIÇÕES]` |

### 2. Critérios de Go
| # | Critério | Peso | Status | Evidência |
|---|----------|------|--------|-----------|
| 1 | `[critério obrigatório]` | Must | `[Verde/Amarelo/Vermelho]` | `[evidência]` |
| 2 | `[critério obrigatório]` | Must | `[Verde/Amarelo/Vermelho]` | `[evidência]` |
| 3 | `[critério desejável]` | Should | `[Verde/Amarelo/Vermelho]` | `[evidência]` |

### 3. Resumo do Status
| Categoria | Verdes | Amarelos | Vermelhos |
|-----------|--------|----------|-----------|
| Must | `[N]` | `[N]` | `[N]` |
| Should | `[N]` | `[N]` | `[N]` |
| **Total** | `[N]` | `[N]` | `[N]` |

**Regra:** Go requer TODOS os Must em Verde ou Amarelo com plano de ação, e ZERO vermelhos em Must.

### 4. Riscos Não Resolvidos
| Risco | Severidade | Impacto no Go/No-Go | Plano |
|-------|-----------|---------------------|-------|
| `[risco]` | `[Alta/Média/Baixa]` | `[Bloqueia Go / Não bloqueia]` | `[como resolver]` |

### 5. Condições para Go (se Go com Condições)
| Condição | Responsável | Prazo | Consequência se Não Cumprir |
|----------|-------------|-------|-----------------------------|
| `[condição]` | `[nome]` | `[data]` | `[o que acontece]` |

### 6. Motivos para No-Go (se No-Go)
| Motivo | Impacto | O que Precisa Mudar | Prazo para Reavaliação |
|--------|---------|--------------------|-----------------------|
| `[motivo]` | `[consequência de prosseguir]` | `[ação necessária]` | `[data]` |

### 7. Decisão e Assinaturas
| Nome | Papel | Voto | Justificativa | Data |
|------|-------|------|--------------|------|
| `[nome]` | `[papel]` | `[Go/No-Go]` | `[razão breve]` | `[data]` |

**Decisão Final:** `[GO / NO-GO / GO COM CONDIÇÕES]`
**Assinatura do Decisor:** `[nome]` — `[data]`

## Exemplo de Preenchimento

### 2. Critérios de Go
| # | Critério | Peso | Status | Evidência |
|---|----------|------|--------|-----------|
| 1 | Requisitos documentados e aprovados | Must | Verde | Doc aprovado em 2026-03-15 |
| 2 | Arquitetura revisada pelo Tech Lead | Must | Verde | Review em 2026-03-16 |
| 3 | Ambientes de dev prontos | Must | Amarelo | CI/CD pronto; staging em 2 dias |
| 4 | Sandbox do parceiro de pagamento disponível | Should | Vermelho | Aguardando credenciais |
| 5 | Equipe 100% alocada | Must | Verde | Confirmado com gestores |

### 3. Resumo
| Categoria | Verdes | Amarelos | Vermelhos |
|-----------|--------|----------|-----------|
| Must | 3 | 1 | 0 |
| Should | 0 | 0 | 1 |
| **Total** | **3** | **1** | **1** |

**Resultado: GO COM CONDIÇÕES** — Staging deve estar pronto até 2026-03-22. Sandbox do parceiro não bloqueia sprint 1.

## Dicas de Qualidade
- **Critérios antes da reunião:** Defina o que é Go antes de avaliar. Evite mover a trave.
- **Baseie-se em evidências:** "Acho que está pronto" não é evidência. Links, datas e artefatos são.
- **No-Go não é fracasso:** Parar quando não está pronto é melhor que avançar e fracassar.
- **Go com Condições é temporário:** As condições devem ter prazo e consequência clara.
- **Registre votos e justificativas:** Transparência protege todos e melhora decisões futuras.
