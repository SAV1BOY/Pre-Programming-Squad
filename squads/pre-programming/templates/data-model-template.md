# Template: Modelo de Dados

## Título
Data Model — Modelagem de Dados do Sistema

## Propósito
Definir a estrutura de dados do sistema, incluindo entidades, atributos, relacionamentos, índices e estratégias de persistência, servindo como referência para a implementação do banco de dados.

## Quando Usar
- Após definição do modelo de domínio e contratos de API.
- Antes de implementar a camada de persistência.
- Quando múltiplas equipes precisam concordar sobre a estrutura de dados.

## Seções

### 1. Informações Gerais
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| Banco de Dados | `[PostgreSQL/MongoDB/etc.]` |
| Responsável | `[nome]` |
| Data | `[YYYY-MM-DD]` |
| Versão | `[v1.0]` |

### 2. Diagrama ER (Entidade-Relacionamento)
```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   [Tabela A] │──1:N──│  [Tabela B]  │──N:M──│  [Tabela C]  │
└──────────────┘     └──────────────┘     └──────────────┘
```

### 3. Tabelas / Coleções

#### `[nome_da_tabela]`
| Coluna | Tipo | Nullable | Default | Descrição |
|--------|------|----------|---------|-----------|
| `[coluna]` | `[tipo SQL]` | `[Sim/Não]` | `[valor padrão]` | `[descrição]` |

**Chave Primária:** `[coluna(s)]`
**Índices:**
| Nome | Colunas | Tipo | Justificativa |
|------|---------|------|---------------|
| `[nome]` | `[colunas]` | `[B-tree/Hash/GIN/etc.]` | `[consulta que otimiza]` |

**Constraints:**
| Nome | Tipo | Expressão | Motivo |
|------|------|-----------|--------|
| `[nome]` | `[UNIQUE/CHECK/FK]` | `[expressão]` | `[regra de negócio]` |

### 4. Relacionamentos
| Tabela Origem | Tabela Destino | Tipo | FK | On Delete | On Update |
|---------------|---------------|------|-------|-----------|-----------|
| `[tabela]` | `[tabela]` | `[1:1/1:N/N:M]` | `[coluna]` | `[CASCADE/SET NULL/RESTRICT]` | `[CASCADE/NO ACTION]` |

### 5. Estratégia de Migração
| Versão | Mudança | Script | Reversível? |
|--------|---------|--------|-------------|
| `[v001]` | `[descrição da mudança]` | `[nome do script]` | `[Sim/Não]` |

### 6. Volumetria e Performance
| Tabela | Volume Inicial | Crescimento/Mês | Consultas Frequentes |
|--------|---------------|-----------------|---------------------|
| `[tabela]` | `[registros]` | `[registros/mês]` | `[queries principais]` |

### 7. Dados Sensíveis e LGPD
| Tabela | Coluna | Classificação | Criptografia | Retenção |
|--------|--------|---------------|-------------|----------|
| `[tabela]` | `[coluna]` | `[Pessoal/Sensível/Público]` | `[Sim/Não — método]` | `[prazo de retenção]` |

### 8. Estratégia de Backup e Recovery
| Aspecto | Valor |
|---------|-------|
| Frequência de Backup | `[diário/horário]` |
| Retenção | `[dias]` |
| RPO (Recovery Point Objective) | `[tempo]` |
| RTO (Recovery Time Objective) | `[tempo]` |

## Exemplo de Preenchimento

### 3. Tabelas
#### `orders`
| Coluna | Tipo | Nullable | Default | Descrição |
|--------|------|----------|---------|-----------|
| id | UUID | Não | gen_random_uuid() | Identificador único |
| customer_id | UUID | Não | — | FK para customers |
| status | VARCHAR(20) | Não | 'pending' | Estado do pedido |
| total_amount | DECIMAL(10,2) | Não | 0.00 | Valor total |
| created_at | TIMESTAMPTZ | Não | now() | Data de criação |
| updated_at | TIMESTAMPTZ | Não | now() | Última atualização |

## Dicas de Qualidade
- **Normalize com bom senso:** Nem tudo precisa estar na 3FN. Pense em performance.
- **Índices com propósito:** Todo índice deve ter uma query que o justifique.
- **Pense em LGPD desde o início:** Dados pessoais devem ser identificados e protegidos.
- **Planeje migrações:** Todo schema vai mudar. Tenha estratégia desde o dia 1.
- **Documente volumetria:** Decisões de design dependem do volume esperado de dados.
