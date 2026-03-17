# Template: Definição de Escopo

## Título
Scope Definition — Definição Clara do Escopo do Projeto

## Propósito
Estabelecer limites claros e acordados sobre o que será e o que não será entregue, prevenindo scope creep e alinhando expectativas entre todas as partes.

## Quando Usar
- Após a fase de discovery e clarificação de requisitos.
- Quando for necessário formalizar o que está dentro e fora do escopo.
- Antes de iniciar arquitetura e estimativas.

## Seções

### 1. Informações Gerais
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| Versão do Escopo | `[v1.0]` |
| Data | `[YYYY-MM-DD]` |
| Aprovadores | `[lista de aprovadores]` |

### 2. Objetivo do Escopo
`[Em 1-2 frases, o que este escopo cobre e qual o resultado esperado.]`

### 3. Funcionalidades Incluídas (In-Scope)
| ID | Funcionalidade | Descrição | Prioridade | Critério de Aceite |
|----|----------------|-----------|------------|-------------------|
| F-01 | `[nome]` | `[descrição concisa]` | `[Must/Should/Could]` | `[critério testável]` |

### 4. Itens Explicitamente Fora do Escopo (Out-of-Scope)
| Item | Motivo da Exclusão | Quando Pode Ser Incluído |
|------|--------------------|-------------------------|
| `[funcionalidade/requisito]` | `[justificativa]` | `[Fase 2 / Nunca / A avaliar]` |

### 5. Faseamento
| Fase | Funcionalidades | Critério de Entrada | Critério de Saída |
|------|----------------|--------------------|--------------------|
| MVP / Fase 1 | `[F-01, F-02, ...]` | `[condição]` | `[entregável]` |
| Fase 2 | `[F-05, F-06, ...]` | `[condição]` | `[entregável]` |

### 6. Premissas do Escopo
- `[Premissa que, se mudar, altera o escopo]`

### 7. Limites e Interfaces
| Sistema/Área | Tipo de Interface | Responsável | Escopo da Integração |
|-------------|------------------|-------------|---------------------|
| `[sistema externo]` | `[API/Evento/Arquivo]` | `[equipe]` | `[o que entra e o que sai]` |

### 8. Critérios de Mudança de Escopo
`[Descreva o processo para solicitar mudanças no escopo após aprovação.]`
- Quem pode solicitar: `[papéis]`
- Quem aprova: `[papéis]`
- Processo: `[descrição do fluxo]`

### 9. Assinaturas
| Nome | Papel | Concordância | Data |
|------|-------|-------------|------|
| `[nome]` | `[papel]` | `[Sim/Não]` | `[data]` |

## Exemplo de Preenchimento

### 3. Funcionalidades Incluídas
| ID | Funcionalidade | Descrição | Prioridade | Critério de Aceite |
|----|----------------|-----------|------------|-------------------|
| F-01 | Login com SSO | Autenticação via SAML 2.0 com IdP corporativo | Must | Usuário autentica em < 3s sem criar nova senha |
| F-02 | Dashboard de pedidos | Visualização dos últimos 100 pedidos com filtros | Must | Carrega em < 2s com filtros por data e status |
| F-03 | Exportar para CSV | Download de pedidos filtrados em CSV | Should | Arquivo gerado em < 10s para até 10k registros |

### 4. Itens Explicitamente Fora do Escopo
| Item | Motivo da Exclusão | Quando Pode Ser Incluído |
|------|--------------------|-------------------------|
| App mobile | Orçamento e prazo insuficientes | Fase 2, Q3 2026 |
| Relatórios customizáveis | Complexidade alta, baixa demanda inicial | A avaliar após MVP |

## Dicas de Qualidade
- **Seja explícito sobre o "não":** Listar o que está fora é tão importante quanto listar o que está dentro.
- **Use priorização MoSCoW:** Distinguir Must de Should evita que tudo seja "prioridade máxima".
- **Vincule ao Project Brief:** O escopo deve derivar dos objetivos documentados no brief.
- **Proteja contra scope creep:** Defina processo claro de mudança de escopo.
- **Revise com todos os stakeholders:** Escopo não validado é escopo que vai mudar.
