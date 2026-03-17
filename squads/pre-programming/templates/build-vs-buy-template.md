# Template: Build vs. Buy

## Título
Build vs. Buy — Análise de Construir vs. Comprar/Adotar

## Propósito
Avaliar de forma estruturada se é melhor construir uma solução internamente ou adquirir/adotar uma solução pronta (SaaS, biblioteca, serviço gerenciado), considerando custos, riscos e alinhamento estratégico.

## Quando Usar
- Quando há uma solução de mercado que resolve parte do problema.
- Antes de decidir construir algo que pode ser comprado.
- Em decisões de uso de bibliotecas open-source vs. implementação própria.

## Seções

### 1. Informações Gerais
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| Componente em Análise | `[funcionalidade ou módulo]` |
| Responsável | `[nome]` |
| Data | `[YYYY-MM-DD]` |
| Decisor Final | `[nome e papel]` |

### 2. Necessidade
`[Descreva claramente o que precisa ser resolvido, sem viés para build ou buy.]`

### 3. Opção Build (Construir)
| Aspecto | Avaliação |
|---------|-----------|
| Descrição | `[o que seria construído]` |
| Esforço Estimado | `[pessoa-dias/semanas]` |
| Custo de Desenvolvimento | `[R$]` |
| Custo de Manutenção (anual) | `[R$]` |
| Time to Market | `[prazo]` |
| Personalização | `[nível de customização]` |
| Dependência de Equipe | `[skills necessários]` |
| Riscos | `[riscos de construir]` |

### 4. Opção Buy (Comprar/Adotar)
| Aspecto | Avaliação |
|---------|-----------|
| Solução(ões) Avaliada(s) | `[nomes dos produtos/serviços]` |
| Custo de Licença/Assinatura | `[R$/mês ou ano]` |
| Custo de Integração | `[R$ e esforço]` |
| Time to Market | `[prazo]` |
| Personalização | `[nível de customização possível]` |
| Vendor Lock-in | `[grau de dependência]` |
| Suporte e SLA | `[o que oferecem]` |
| Riscos | `[riscos de comprar]` |

### 5. Comparação
| Critério | Peso | Build | Buy |
|----------|------|-------|-----|
| Custo total (3 anos) | `[1-5]` | `[nota 1-5]` | `[nota 1-5]` |
| Time to Market | `[1-5]` | `[nota 1-5]` | `[nota 1-5]` |
| Personalização | `[1-5]` | `[nota 1-5]` | `[nota 1-5]` |
| Manutenção | `[1-5]` | `[nota 1-5]` | `[nota 1-5]` |
| Risco técnico | `[1-5]` | `[nota 1-5]` | `[nota 1-5]` |
| Alinhamento estratégico | `[1-5]` | `[nota 1-5]` | `[nota 1-5]` |
| **Total Ponderado** | | `[total]` | `[total]` |

### 6. Recomendação
- **Opção Recomendada:** `[Build/Buy]`
- **Justificativa:** `[por que esta opção é melhor]`
- **Condições:** `[condições para a recomendação ser válida]`

### 7. Decisão
| Campo | Valor |
|-------|-------|
| Decisão | `[Build/Buy — qual solução]` |
| Decidido Por | `[nome]` |
| Data | `[YYYY-MM-DD]` |
| Revisão Programada | `[data para reavaliar]` |

## Exemplo de Preenchimento

### 5. Comparação
| Critério | Peso | Build (In-house) | Buy (Auth0) |
|----------|------|-----------------|-------------|
| Custo total (3 anos) | 4 | 3 (R$180k dev + R$60k/ano manutenção) | 4 (R$36k/ano licença) |
| Time to Market | 5 | 2 (8 semanas) | 5 (1 semana) |
| Personalização | 3 | 5 (total controle) | 3 (limitado ao que Auth0 oferece) |
| Manutenção | 4 | 2 (equipe interna mantém) | 5 (gerenciado pelo vendor) |
| Risco técnico | 4 | 2 (segurança é difícil) | 4 (especialistas em auth) |
| **Total Ponderado** | | **56** | **86** |

## Dicas de Qualidade
- **Pense em TCO (Total Cost of Ownership):** O custo de construir não é só o desenvolvimento inicial.
- **Considere manutenção:** Software próprio precisa de manutenção contínua.
- **Avalie vendor lock-in:** Quanto custa trocar de fornecedor no futuro?
- **Pergunte "é core business?":** Se não é diferencial competitivo, provavelmente não vale construir.
- **Faça um PoC:** Antes de decidir, teste a solução de mercado com um caso real.
