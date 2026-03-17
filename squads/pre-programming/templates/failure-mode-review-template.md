# Template: Revisão de Modos de Falha

## Título
Failure Mode Review — Análise de Modos de Falha do Sistema

## Propósito
Identificar sistematicamente como o sistema pode falhar, avaliar o impacto de cada modo de falha e definir estratégias de prevenção e recuperação antes da implementação.

## Quando Usar
- Após o esboço de arquitetura estar definido.
- Antes de finalizar o design de componentes críticos.
- Em revisões de resiliência e confiabilidade do sistema.

## Seções

### 1. Informações Gerais
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| Componente/Serviço | `[escopo da revisão]` |
| Responsável | `[nome]` |
| Data | `[YYYY-MM-DD]` |

### 2. Registro de Modos de Falha
| ID | Componente | Modo de Falha | Causa Provável | Efeito | Severidade | Probabilidade | Detecção | RPN |
|----|-----------|---------------|----------------|--------|-----------|---------------|----------|-----|
| FM-01 | `[componente]` | `[como falha]` | `[por quê]` | `[impacto no sistema/usuário]` | `[1-10]` | `[1-10]` | `[1-10]` | `[S×P×D]` |

> RPN = Risk Priority Number = Severidade × Probabilidade × Dificuldade de Detecção

### 3. Análise Detalhada (Top 5 por RPN)

#### FM-`[XX]`: `[Modo de Falha]`
- **Componente:** `[onde ocorre]`
- **Cenário:** `[descrição detalhada do cenário de falha]`
- **Impacto no Usuário:** `[o que o usuário experimenta]`
- **Impacto no Negócio:** `[consequência financeira ou operacional]`
- **Prevenção:** `[como evitar]`
- **Detecção:** `[como detectar rapidamente]`
- **Recuperação:** `[como restaurar o funcionamento]`
- **Tempo de Recuperação Estimado:** `[minutos/horas]`

### 4. Estratégias de Resiliência
| Estratégia | Modos de Falha Cobertos | Implementação |
|------------|------------------------|---------------|
| `[Circuit Breaker / Retry / Fallback / Redundância / etc.]` | `[IDs dos modos]` | `[como implementar]` |

### 5. Testes de Falha Planejados
| Teste | Modo de Falha | Método | Critério de Sucesso |
|-------|---------------|--------|---------------------|
| `[nome do teste]` | `[FM-XX]` | `[chaos engineering / teste manual / simulação]` | `[resultado esperado]` |

### 6. Plano de Ação
| Ação | Prioridade | Responsável | Prazo | Status |
|------|-----------|-------------|-------|--------|
| `[ação corretiva/preventiva]` | `[Alta/Média/Baixa]` | `[nome]` | `[data]` | `[status]` |

## Exemplo de Preenchimento

### 2. Registro de Modos de Falha
| ID | Componente | Modo de Falha | Causa Provável | Efeito | Sev. | Prob. | Det. | RPN |
|----|-----------|---------------|----------------|--------|------|-------|------|-----|
| FM-01 | Payment Service | Timeout na API de pagamento | Instabilidade do provedor | Pedido fica em estado inconsistente | 9 | 4 | 3 | 108 |
| FM-02 | Database | Conexões esgotadas | Pool mal dimensionado sob carga | Sistema retorna 500 para todos os requests | 8 | 3 | 5 | 120 |
| FM-03 | Cache (Redis) | Redis indisponível | Falha de memória ou rede | Latência aumenta 10x, possível cascata | 7 | 2 | 2 | 28 |

## Dicas de Qualidade
- **Pense como um pessimista:** A pergunta é "como isso pode falhar?", não "isso vai funcionar?".
- **Foque no impacto ao usuário:** A severidade deve refletir a experiência do usuário final.
- **Teste os modos de falha:** Uma falha não testada é uma falha que vai surpreender em produção.
- **Priorize por RPN:** Nem todos os modos de falha precisam de ação imediata.
- **Revise após mudanças:** Cada mudança na arquitetura pode introduzir novos modos de falha.
