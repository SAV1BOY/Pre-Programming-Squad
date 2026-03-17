# Template: Impacto em Sistema Legado

## Título
Legacy Impact — Análise de Impacto em Sistemas Legados

## Propósito
Avaliar como o projeto novo ou mudança afeta sistemas legados existentes, identificando riscos de compatibilidade, necessidades de migração e estratégias de coexistência.

## Quando Usar
- Quando o projeto interage com sistemas legados.
- Antes de modificar ou substituir funcionalidades existentes.
- Em projetos de modernização ou migração.

## Seções

### 1. Informações Gerais
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| Sistema(s) Legado(s) | `[nomes dos sistemas]` |
| Responsável | `[nome]` |
| Data | `[YYYY-MM-DD]` |

### 2. Inventário de Sistemas Legados Afetados
| Sistema | Tecnologia | Idade | Proprietário | Criticidade | Documentação |
|---------|-----------|-------|-------------|-------------|-------------|
| `[nome]` | `[stack]` | `[anos]` | `[equipe]` | `[Alta/Média/Baixa]` | `[Boa/Parcial/Inexistente]` |

### 3. Análise de Impacto por Sistema
#### Sistema: `[Nome]`
| Aspecto | Impacto | Detalhes |
|---------|---------|---------|
| Dados | `[Alto/Médio/Baixo/Nenhum]` | `[como os dados são afetados]` |
| APIs/Interfaces | `[Alto/Médio/Baixo/Nenhum]` | `[mudanças em contratos]` |
| Processos de Negócio | `[Alto/Médio/Baixo/Nenhum]` | `[fluxos alterados]` |
| Infraestrutura | `[Alto/Médio/Baixo/Nenhum]` | `[recursos compartilhados]` |
| Usuários | `[Alto/Médio/Baixo/Nenhum]` | `[mudança na experiência]` |

### 4. Dependências Bidirecionais
| Nosso Sistema Depende De | Sistema Legado Depende de Nós |
|--------------------------|------------------------------|
| `[funcionalidade/dado do legado]` | `[funcionalidade/dado que fornecemos]` |

### 5. Riscos de Compatibilidade
| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| `[risco de incompatibilidade]` | `[Alta/Média/Baixa]` | `[Alto/Médio/Baixo]` | `[estratégia]` |

### 6. Estratégia de Coexistência
- **Período de Coexistência:** `[duração esperada]`
- **Abordagem:** `[Strangler Fig / Parallel Run / Big Bang / Branch by Abstraction]`
- **Sincronização de Dados:** `[como manter dados consistentes entre sistemas]`
- **Roteamento de Tráfego:** `[como direcionar usuários]`

### 7. Plano de Migração (se aplicável)
| Fase | Escopo | Duração | Critério de Sucesso | Rollback |
|------|--------|---------|--------------------|-|
| `[fase]` | `[o que migra]` | `[prazo]` | `[como validar]` | `[como reverter]` |

### 8. Plano de Descomissionamento (se aplicável)
| Etapa | Ação | Pré-requisito | Data Alvo |
|-------|------|-------------|----------|
| `[etapa]` | `[ação para desligar o legado]` | `[condição]` | `[data]` |

## Exemplo de Preenchimento

### 2. Inventário
| Sistema | Tecnologia | Idade | Proprietário | Criticidade | Documentação |
|---------|-----------|-------|-------------|-------------|-------------|
| ERP Financeiro | Java 8 + Oracle | 12 anos | Equipe Legado | Alta | Parcial |
| Portal do Cliente v1 | PHP 7.2 + MySQL | 6 anos | Equipe Web | Média | Boa |

### 6. Estratégia de Coexistência
- **Período:** 6 meses (Q2-Q3 2026)
- **Abordagem:** Strangler Fig — migrar funcionalidades gradualmente
- **Sincronização:** CDC (Change Data Capture) do Oracle para PostgreSQL
- **Roteamento:** Feature flag por empresa cliente

## Dicas de Qualidade
- **Respeite o legado:** Sistemas legados funcionam. Entenda por que antes de mudar.
- **Mapeie dependências ocultas:** Sistemas legados têm integrações que ninguém documenta.
- **Teste em paralelo:** Execute o sistema novo e o legado lado a lado antes de migrar.
- **Planeje o descomissionamento:** Um legado que "nunca será desligado" consome recursos para sempre.
- **Converse com quem mantém:** A equipe do legado tem conhecimento que a documentação não tem.
