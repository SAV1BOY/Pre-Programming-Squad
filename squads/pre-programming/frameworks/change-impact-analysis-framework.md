# Change Impact Analysis Framework

## Propósito
Avaliar sistematicamente o impacto de mudanças propostas em sistemas existentes, equipes e processos antes de implementar, evitando efeitos colaterais não previstos.

## Problema que Resolve
Toda mudança tem efeitos de segunda e terceira ordem. Alterar um schema de database pode quebrar 5 serviços downstream. Mudar um API endpoint afeta 3 consumidores. Este framework mapeia todos os impactos antes de começar.

## Quando Usar
- Em todo projeto que modifica sistemas existentes
- Obrigatório para projetos porte G/XG
- Quando Legacy Impact Auditor identifica áreas de risco
- Antes de migrations, refactorings ou mudanças de API

## Dimensões de Impacto

### 1. Técnico
- **Código:** Quais módulos/serviços são modificados diretamente?
- **Dados:** Schemas alterados? Migração necessária? Backward compatible?
- **APIs:** Contratos quebram? Novos endpoints? Deprecações?
- **Infraestrutura:** Novos serviços? Mais recursos? Mudança de topologia?

### 2. Organizacional
- **Times:** Quais times são afetados e precisam ser informados?
- **Processos:** Algum processo operacional muda?
- **Treinamento:** Alguém precisa aprender algo novo?
- **Comunicação:** Quem precisa ser informado e quando?

### 3. Operacional
- **Disponibilidade:** Há janela de downtime necessária?
- **Monitoramento:** Alertas precisam ser ajustados?
- **Rollback:** O que acontece se der errado?
- **Suporte:** Volume de tickets pode aumentar?

## Processo

### Passo 1 — Definir a Mudança
Descrever em 2-3 frases o que vai mudar e por quê.

### Passo 2 — Mapear Impactos Diretos
| Componente Afetado | Tipo de Impacto | Severidade | Ação Necessária |
|-------------------|----------------|-----------|----------------|
| user-service | Schema change | Alta | Migration script + rollback |
| payment-api | New endpoint | Média | Contract update, notify consumers |
| dashboard-frontend | New data field | Baixa | UI update |

### Passo 3 — Mapear Impactos Indiretos (Cascata)
Para cada impacto direto, perguntar: "O que depende deste componente?"
Repetir até não haver mais dependências.

### Passo 4 — Avaliar Blast Radius
```
Blast Radius = Número de componentes afetados × Severidade média × Reversibilidade
```
- **Baixo:** ≤3 componentes, todos reversíveis
- **Médio:** 4-10 componentes ou 1+ irreversível
- **Alto:** >10 componentes ou múltiplos irreversíveis

### Passo 5 — Planejar Mitigação
Para cada impacto de severidade média/alta:
- Ação de mitigação específica
- Responsável e prazo
- Critério de verificação

## Armadilhas
- **Subestimar cascata** → O impacto de segunda ordem é quase sempre maior que o de primeira
- **Avaliar apenas cenário ideal** → Incluir cenário de falha (e se a migration falhar no meio?)
- **Não consultar times afetados** → Eles conhecem dependências ocultas
- **Blast radius "é pequeno" sem análise** → Quantificar sempre
