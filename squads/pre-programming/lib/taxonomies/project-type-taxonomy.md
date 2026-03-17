# Taxonomia de Tipos de Projeto

## Categorias

### 1. Novo Produto (NP)
Desenvolvimento de um produto ou sistema completamente novo.

#### Subcategorias
- **NP-MVP:** Produto mínimo viável - validação de hipótese de mercado
- **NP-V1:** Primeira versão completa - funcionalidades core
- **NP-PLAT:** Plataforma nova - base para múltiplos produtos
- **NP-INTL:** Produto interno - ferramenta para uso da organização

#### Definições
| Subcategoria | Características | Nível de Planejamento | Risco Típico |
|---|---|---|---|
| NP-MVP | Escopo mínimo, velocidade prioritária, validação rápida | Leve (foco em hipóteses) | Médio (pivot frequente) |
| NP-V1 | Escopo definido, qualidade importa, lançamento público | Completo | Alto (muitas incertezas) |
| NP-PLAT | Extensibilidade crítica, múltiplos consumidores | Extensivo (arquitetura) | Muito alto |
| NP-INTL | Usuários conhecidos, requisitos mais flexíveis | Moderado | Baixo-Médio |

### 2. Evolução de Produto (EP)
Adição de funcionalidades ou melhorias a um produto existente.

#### Subcategorias
- **EP-FEAT:** Nova funcionalidade - feature isolada
- **EP-ENHC:** Melhoria de funcionalidade existente
- **EP-REFR:** Refatoração - reestruturação sem mudança de comportamento
- **EP-OTIM:** Otimização de performance ou custos
- **EP-ESCL:** Escalabilidade - preparar para crescimento

#### Definições
| Subcategoria | Características | Nível de Planejamento | Risco Típico |
|---|---|---|---|
| EP-FEAT | Feature nova no sistema existente | Moderado (impacto analisado) | Médio |
| EP-ENHC | Melhoria incremental de UX ou funcionalidade | Leve | Baixo |
| EP-REFR | Mudança interna sem alterar comportamento externo | Moderado (regressão) | Médio |
| EP-OTIM | Foco em métricas de performance ou custo | Focado (benchmarks) | Baixo-Médio |
| EP-ESCL | Preparar infraestrutura para escala | Extensivo (capacidade) | Alto |

### 3. Migração (MG)
Transição entre tecnologias, plataformas ou fornecedores.

#### Subcategorias
- **MG-TECH:** Migração de tecnologia (linguagem, framework)
- **MG-INFR:** Migração de infraestrutura (on-premise para cloud)
- **MG-DATA:** Migração de banco de dados ou storage
- **MG-FORN:** Migração de fornecedor ou provedor
- **MG-ARQT:** Migração arquitetural (monolito para microsserviços)

#### Definições
| Subcategoria | Complexidade | Duração Típica | Risco Típico |
|---|---|---|---|
| MG-TECH | Alta | 3-12 meses | Alto (regressão) |
| MG-INFR | Alta | 2-6 meses | Alto (downtime) |
| MG-DATA | Muito alta | 1-6 meses | Muito alto (perda de dados) |
| MG-FORN | Média-Alta | 1-3 meses | Médio (feature gap) |
| MG-ARQT | Muito alta | 6-18 meses | Muito alto |

### 4. Integração (IG)
Conexão entre sistemas ou adoção de plataformas externas.

#### Subcategorias
- **IG-API:** Integração com API de terceiros
- **IG-SAAS:** Adoção de SaaS (CRM, ERP, pagamento)
- **IG-B2B:** Integração business-to-business
- **IG-LEGC:** Integração com sistema legado

#### Definições
| Subcategoria | Complexidade | Duração Típica | Risco Típico |
|---|---|---|---|
| IG-API | Baixa-Média | 1-4 semanas | Baixo-Médio |
| IG-SAAS | Média | 1-3 meses | Médio (customização) |
| IG-B2B | Alta | 2-6 meses | Alto (coordenação) |
| IG-LEGC | Muito alta | 2-6 meses | Muito alto |

### 5. Manutenção e Suporte (MS)
Correção de problemas e suporte operacional.

#### Subcategorias
- **MS-CORR:** Correção de bugs
- **MS-SECU:** Correção de vulnerabilidade de segurança
- **MS-OPER:** Melhoria operacional (monitoramento, alertas)
- **MS-DEBT:** Pagamento de débito técnico

## Exemplos por Categoria

### NP-MVP: Novo Produto MVP
```
Projeto: App de delivery para restaurantes locais
Tipo: NP-MVP

Características:
  Duração estimada: 6 semanas
  Equipe: 2 devs + 1 designer
  Escopo: Apenas pedido e entrega (sem pagamento online)
  Validação: 50 restaurantes parceiros, 500 pedidos/semana

Abordagem de planejamento:
  - Project brief simplificado (1 página)
  - Arquitetura: monolito simples
  - Riscos: foco nos 3 principais
  - Testes: smoke + manuais
  - Handoff: informal
```

### MG-ARQT: Migração Arquitetural
```
Projeto: Decomposição do monolito em microsserviços
Tipo: MG-ARQT

Características:
  Duração estimada: 12 meses
  Equipe: 4 squads de 4-5 pessoas
  Escopo: 15 módulos do monolito -> 8 microsserviços
  Estratégia: Strangler fig pattern

Abordagem de planejamento:
  - Project brief extenso com business case
  - Notas de arquitetura para cada serviço
  - Registro de riscos completo (20+ riscos)
  - Plano de testes com regressão automatizada
  - Plano de rollout em fases com rollback
  - Readiness review a cada fase
  - Handoff formal com documentação completa
```

### EP-FEAT: Nova Funcionalidade
```
Projeto: Adicionar busca full-text ao catálogo
Tipo: EP-FEAT

Características:
  Duração estimada: 4 sprints
  Equipe: 2 devs + 1 QA
  Escopo: Busca por texto em produtos com filtros
  Impacto: Endpoint novo + componente de UI

Abordagem de planejamento:
  - Nota de arquitetura (escolha do engine de busca)
  - 3-4 riscos identificados
  - Plano de testes com cenários de performance
  - Feature flag para lançamento gradual
  - Handoff leve (ADR + critérios de aceite)
```
