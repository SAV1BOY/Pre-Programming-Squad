# Padrões de Decomposição

## Nome do Padrão
Padrões para Decomposição de Sistemas e Problemas Complexos

## Problema que Resolve
Sistemas complexos tratados como um bloco monolítico resultam em: dificuldade de estimativa, paralelização limitada de trabalho, testes de integração frágeis, deploys arriscados e evolução lenta. A decomposição adequada durante a pré-programação permite entregas incrementais e paralelas.

## Solução

### 1. Decomposição por Capacidade de Negócio
Dividir o sistema com base nas capacidades de negócio que ele suporta, alinhando componentes técnicos com funções organizacionais.

**Aplicação prática:**
- Identificar capacidades de negócio (ex: gerenciar pedidos, processar pagamentos)
- Cada capacidade mapeia para um ou mais componentes
- Equipes organizadas por capacidade (ownership claro)
- Comunicação entre capacidades via eventos ou APIs

### 2. Decomposição por Subdomain (DDD)
Usar Domain-Driven Design para identificar subdomínios core, supporting e generic, aplicando diferentes níveis de investimento em cada um.

**Aplicação prática:**
- **Core Domain:** Diferencial competitivo, máximo investimento em design
- **Supporting Domain:** Necessário mas não diferenciador, design pragmático
- **Generic Domain:** Commodity, usar soluções prontas (SaaS, bibliotecas)
- Documentar classificação e justificativa

### 3. Fatias Verticais (Vertical Slicing)
Decompor trabalho em fatias que atravessam todas as camadas (UI, API, lógica, dados), entregando funcionalidades completas e testáveis.

**Aplicação prática:**
- Cada fatia entrega valor ao usuário
- Uma fatia é implementável em 1-3 dias
- Inclui: interface, lógica, persistência, testes
- Priorizar fatias por valor de negócio

### 4. Decomposição por Volatilidade
Separar partes do sistema que mudam frequentemente daquelas que são estáveis, isolando a volatilidade.

**Aplicação prática:**
- Identificar eixos de mudança (regras de negócio, integrações, UI)
- Separar componentes voláteis dos estáveis
- Interfaces estáveis entre componentes
- Componentes voláteis com deploy independente

## Quando Usar

- No planejamento de qualquer projeto com mais de 2 semanas de duração
- Ao estruturar trabalho para equipes paralelas
- Na definição de limites de microsserviços
- Ao planejar entregas incrementais
- Quando o sistema tem múltiplos domínios de negócio

## Quando NÃO Usar

- Em projetos triviais com escopo bem definido e pequeno
- Quando a decomposição gera mais complexidade de coordenação do que valor
- Em sistemas fortemente acoplados onde decomposição quebraria transações ACID necessárias
- Quando a equipe é muito pequena (1-2 pessoas) para se beneficiar de paralelização

## Exemplos

### Exemplo 1: Decomposição por Capacidade - Marketplace
```
Capacidades de negócio identificadas:
  1. Gestão de Catálogo (equipe: Catálogo)
     - Cadastro de produtos, categorias, busca
  2. Gestão de Vendedores (equipe: Seller)
     - Onboarding, perfil, comissões
  3. Processamento de Pedidos (equipe: Orders)
     - Carrinho, checkout, status
  4. Pagamentos (equipe: Payments)
     - Processamento, estorno, split
  5. Logística (equipe: Shipping)
     - Cálculo de frete, rastreamento, devolução

Comunicação:
  Catálogo -> Orders: ProductSelected event
  Orders -> Payments: OrderPlaced command
  Payments -> Orders: PaymentConfirmed event
  Orders -> Shipping: OrderPaid event
```

### Exemplo 2: Fatias Verticais - Sistema de RH
```
Épico: Gestão de Férias

Fatia 1 (3 dias): "Solicitar férias"
  - Formulário de solicitação (UI)
  - Endpoint POST /api/ferias (API)
  - Validação de saldo de dias (Lógica)
  - Tabela de solicitações (Dados)
  - Testes: unitário + integração + e2e

Fatia 2 (2 dias): "Aprovar férias"
  - Tela de aprovação do gestor (UI)
  - Endpoint PATCH /api/ferias/:id/aprovar (API)
  - Regras de aprovação (Lógica)
  - Notificação por e-mail (Integração)

Fatia 3 (2 dias): "Visualizar calendário de férias"
  - Componente de calendário (UI)
  - Endpoint GET /api/ferias/equipe (API)
  - Filtros por equipe/período (Lógica)
```

### Exemplo 3: Decomposição por Volatilidade
```
Componentes estáveis (muda raramente):
  - Modelo de dados core (Usuário, Produto)
  - Autenticação e autorização
  - Infraestrutura de logging e monitoramento

Componentes voláteis (muda frequentemente):
  - Regras de precificação e descontos
  - Algoritmo de recomendação
  - Layouts e fluxos de UI
  - Integrações com parceiros

Decisão: Componentes voláteis deployáveis independentemente
  - Regras de precificação: engine com hot-reload
  - Recomendação: serviço separado com A/B testing
  - UI: micro-frontends com deploy independente
```
