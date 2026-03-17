# Taxonomia de Requisitos

## Categorias

### 1. Requisitos Funcionais (RF)
Descrevem o que o sistema deve fazer em termos de comportamento e funcionalidades.

#### Subcategorias
- **RF-CRUD:** Operações de criação, leitura, atualização e exclusão de dados
- **RF-PROC:** Processamento e transformação de dados (cálculos, validações, workflows)
- **RF-INTG:** Integrações com sistemas externos (APIs, mensageria, arquivos)
- **RF-BUSN:** Regras de negócio específicas do domínio
- **RF-RPRT:** Relatórios, dashboards e visualizações de dados
- **RF-NOTF:** Notificações, alertas e comunicações com usuário
- **RF-SRCH:** Busca, filtragem e ordenação de informações

#### Definições
| Subcategoria | Definição | Critério de Classificação |
|---|---|---|
| RF-CRUD | Operação básica de manipulação de entidade | Envolve criar, ler, atualizar ou excluir registro |
| RF-PROC | Lógica de processamento | Envolve transformação, cálculo ou validação complexa |
| RF-INTG | Comunicação com sistema externo | Requer protocolo de comunicação com outro serviço |
| RF-BUSN | Regra de domínio | Implementa política ou regra específica do negócio |
| RF-RPRT | Apresentação de dados agregados | Gera visualização ou relatório para tomada de decisão |
| RF-NOTF | Envio de informação ao usuário | Dispara mensagem, e-mail, push ou alerta |
| RF-SRCH | Recuperação de informação | Permite localizar dados com critérios dinâmicos |

### 2. Requisitos Não-Funcionais (RNF)
Descrevem como o sistema deve se comportar em termos de qualidade.

#### Subcategorias
- **RNF-PERF:** Performance e tempo de resposta
- **RNF-SCAL:** Escalabilidade e capacidade
- **RNF-SECU:** Segurança e proteção de dados
- **RNF-AVAI:** Disponibilidade e resiliência
- **RNF-MANT:** Manutenibilidade e testabilidade
- **RNF-USAB:** Usabilidade e acessibilidade
- **RNF-COMP:** Compatibilidade e portabilidade
- **RNF-OBSV:** Observabilidade e monitoramento

#### Definições
| Subcategoria | Definição | Exemplo de Métrica |
|---|---|---|
| RNF-PERF | Limites de tempo de resposta e throughput | Latência p99 < 200ms |
| RNF-SCAL | Capacidade de crescimento do sistema | Suportar 10x usuários sem redesign |
| RNF-SECU | Proteção contra ameaças e compliance | OWASP Top 10 mitigado, LGPD compliance |
| RNF-AVAI | Tempo de operação e recuperação | SLA 99.9%, RTO < 15min |
| RNF-MANT | Facilidade de manutenção e evolução | Cobertura de testes > 80% |
| RNF-USAB | Experiência do usuário e acessibilidade | WCAG 2.1 nível AA |
| RNF-COMP | Compatibilidade com plataformas | Chrome, Firefox, Safari últimas 2 versões |
| RNF-OBSV | Capacidade de monitorar e diagnosticar | Logs estruturados, traces distribuídos |

### 3. Requisitos de Interface (RI)
Descrevem como o sistema interage com usuários e outros sistemas.

#### Subcategorias
- **RI-UI:** Interface com o usuário (telas, formulários, fluxos)
- **RI-API:** Interface programática (REST, GraphQL, gRPC)
- **RI-DATA:** Interface de dados (importação, exportação, sincronização)
- **RI-HW:** Interface com hardware (dispositivos, sensores)

### 4. Requisitos de Restrição (RR)
Limitações impostas ao projeto.

#### Subcategorias
- **RR-TECH:** Restrições técnicas (linguagem, framework, infraestrutura)
- **RR-REGUL:** Restrições regulatórias (LGPD, PCI-DSS, SOX)
- **RR-ORCAM:** Restrições orçamentárias
- **RR-PRAZO:** Restrições de prazo

## Exemplos por Categoria

### RF-BUSN: Regra de Negócio
```
ID: RF-BUSN-001
Título: Cálculo de desconto progressivo
Descrição: O sistema deve aplicar desconto progressivo baseado no
  volume de compras do cliente nos últimos 12 meses:
  - 0-999 reais: sem desconto
  - 1000-4999 reais: 5% de desconto
  - 5000-9999 reais: 10% de desconto
  - 10000+ reais: 15% de desconto
Critério de aceite: Desconto calculado corretamente para cada faixa
Prioridade: Alta
```

### RNF-PERF: Performance
```
ID: RNF-PERF-001
Título: Tempo de resposta da API de busca
Descrição: O endpoint de busca deve retornar resultados em:
  - p50 < 100ms
  - p95 < 300ms
  - p99 < 500ms
  Para queries de até 200 caracteres com até 1000 resultados indexados.
Critério de aceite: Medições em ambiente de staging com carga simulada
Prioridade: Alta
```

### RI-API: Interface de API
```
ID: RI-API-001
Título: Contrato da API de Pedidos
Descrição: Endpoint REST para criação de pedidos.
  POST /api/v1/pedidos
  Content-Type: application/json
  Autenticação: Bearer Token (JWT)
  Corpo: { items: [...], endereco_entrega: {...}, pagamento: {...} }
  Resposta 201: { pedido_id, status, estimativa_entrega }
  Resposta 400: { erros: [...] }
  Resposta 409: { conflito: "estoque insuficiente" }
Prioridade: Crítica
```
