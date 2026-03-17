# Template: Modelo de Domínio

## Título
Domain Model — Modelagem do Domínio de Negócio

## Propósito
Capturar as entidades, relacionamentos e regras de negócio do domínio do projeto, criando uma linguagem comum entre negócio e tecnologia (Ubiquitous Language).

## Quando Usar
- Durante ou após a discovery, quando o domínio já foi compreendido.
- Antes de desenhar modelo de dados ou APIs.
- Quando múltiplas equipes precisam concordar sobre conceitos do negócio.

## Seções

### 1. Informações Gerais
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| Domínio | `[área de negócio]` |
| Responsável | `[nome]` |
| Data | `[YYYY-MM-DD]` |

### 2. Glossário do Domínio (Ubiquitous Language)
| Termo | Definição | Sinônimos a Evitar |
|-------|-----------|-------------------|
| `[termo do domínio]` | `[definição precisa]` | `[termos ambíguos que não devem ser usados]` |

### 3. Entidades Principais
| Entidade | Descrição | Atributos-Chave | Identificador |
|----------|-----------|-----------------|---------------|
| `[nome]` | `[o que representa]` | `[atributos principais]` | `[como é identificada]` |

### 4. Objetos de Valor (Value Objects)
| Objeto de Valor | Descrição | Composto Por |
|-----------------|-----------|-------------|
| `[nome]` | `[o que representa]` | `[atributos]` |

### 5. Agregados
| Agregado | Raiz | Entidades Internas | Invariantes |
|----------|------|-------------------|-------------|
| `[nome]` | `[entidade raiz]` | `[entidades agrupadas]` | `[regras que devem ser sempre verdadeiras]` |

### 6. Relacionamentos
```
[Entidade A] ──1:N──▶ [Entidade B]
[Entidade B] ──N:M──▶ [Entidade C]
```

| Origem | Destino | Cardinalidade | Descrição |
|--------|---------|---------------|-----------|
| `[entidade]` | `[entidade]` | `[1:1, 1:N, N:M]` | `[natureza do relacionamento]` |

### 7. Regras de Negócio
| ID | Regra | Entidade | Exceções |
|----|-------|----------|----------|
| RN-01 | `[regra de negócio]` | `[entidade afetada]` | `[exceções conhecidas]` |

### 8. Eventos de Domínio
| Evento | Gatilho | Dados | Consequência |
|--------|---------|-------|-------------|
| `[nome do evento]` | `[o que causa]` | `[dados contidos]` | `[o que acontece depois]` |

### 9. Bounded Contexts
| Contexto | Responsabilidade | Entidades | Interface com Outros Contextos |
|----------|-----------------|-----------|-------------------------------|
| `[nome]` | `[o que gerencia]` | `[entidades neste contexto]` | `[como se comunica]` |

## Exemplo de Preenchimento

### 2. Glossário do Domínio
| Termo | Definição | Sinônimos a Evitar |
|-------|-----------|-------------------|
| Pedido | Solicitação de compra feita pelo cliente com itens e valor total | Ordem, Requisição, Compra |
| Item de Pedido | Produto específico dentro de um pedido com quantidade e preço unitário | Linha, Produto |
| Fulfillment | Processo de separação, empacotamento e envio do pedido | Entrega, Despacho |

### 7. Regras de Negócio
| ID | Regra | Entidade | Exceções |
|----|-------|----------|----------|
| RN-01 | Pedido não pode ser cancelado após início do fulfillment | Pedido | Admin pode cancelar com justificativa |
| RN-02 | Desconto máximo de 30% por item sem aprovação gerencial | Item de Pedido | Campanhas promocionais aprovadas pelo marketing |

## Dicas de Qualidade
- **Use a linguagem do negócio:** O modelo deve ser compreensível para não-técnicos.
- **Defina limites claros:** Bounded Contexts evitam que conceitos se misturem.
- **Valide com especialistas do domínio:** Desenvolvedores sozinhos não entendem todas as nuances.
- **Documente eventos:** Eventos de domínio são fundamentais para arquiteturas orientadas a eventos.
- **Itere com a equipe:** O modelo evolui conforme o entendimento do domínio melhora.
