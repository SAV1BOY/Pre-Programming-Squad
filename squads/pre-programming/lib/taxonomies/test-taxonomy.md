# Taxonomia de Testes

## Categorias

### 1. Testes Funcionais (TF)
Verificam se o sistema faz o que deveria fazer.

#### Subcategorias
- **TF-UNIT:** Teste unitário - valida componente isolado
- **TF-INTG:** Teste de integração - valida interação entre componentes
- **TF-E2E:** Teste end-to-end - valida fluxo completo do usuário
- **TF-SMOK:** Teste smoke - verificação rápida das funcionalidades críticas
- **TF-SANI:** Teste sanity - verificação focada após mudança específica
- **TF-REGR:** Teste de regressão - garante que mudanças não quebraram existente
- **TF-ACEI:** Teste de aceite - valida critérios de aceite do requisito

#### Definições
| Subcategoria | Escopo | Velocidade | Quem Executa | Automatização |
|---|---|---|---|---|
| TF-UNIT | Função/classe | Milissegundos | Desenvolvedor | Obrigatória |
| TF-INTG | 2+ componentes | Segundos | Desenvolvedor | Obrigatória |
| TF-E2E | Fluxo completo | Minutos | QA/Automação | Recomendada |
| TF-SMOK | Funcionalidades críticas | Minutos | CI/CD | Obrigatória |
| TF-SANI | Área de mudança | Minutos | QA | Recomendada |
| TF-REGR | Sistema inteiro | Horas | Automação | Obrigatória |
| TF-ACEI | Requisito específico | Variável | PO/QA | Opcional |

### 2. Testes Não-Funcionais (TNF)
Verificam como o sistema se comporta em diferentes condições.

#### Subcategorias
- **TNF-PERF:** Teste de performance - mede tempos de resposta e throughput
- **TNF-CARG:** Teste de carga - valida comportamento sob carga esperada
- **TNF-ESTR:** Teste de stress - identifica limites do sistema
- **TNF-RESI:** Teste de resiliência - valida recuperação de falhas
- **TNF-SECU:** Teste de segurança - identifica vulnerabilidades
- **TNF-ACES:** Teste de acessibilidade - verifica conformidade WCAG
- **TNF-COMP:** Teste de compatibilidade - valida em diferentes plataformas

#### Definições
| Subcategoria | Objetivo | Ferramentas Típicas | Frequência |
|---|---|---|---|
| TNF-PERF | Medir latência e throughput | k6, JMeter, Gatling | A cada release |
| TNF-CARG | Validar sob carga nominal | k6, Locust | A cada release |
| TNF-ESTR | Encontrar ponto de ruptura | k6, Artillery | Trimestral |
| TNF-RESI | Validar recuperação | Chaos Monkey, Litmus | Mensal |
| TNF-SECU | Identificar vulnerabilidades | OWASP ZAP, Burp Suite | A cada release |
| TNF-ACES | Verificar WCAG | Axe, Lighthouse, Pa11y | A cada release |
| TNF-COMP | Testar em browsers/OS | BrowserStack, Playwright | A cada release |

### 3. Testes Exploratórios (TE)
Testes não-scriptados baseados na experiência do testador.

#### Subcategorias
- **TE-SESS:** Teste exploratório baseado em sessão (SBET)
- **TE-TOUR:** Tour exploratório guiado por heurística
- **TE-PARS:** Teste por pares (pair testing)

#### Definições
| Subcategoria | Abordagem | Duração Típica | Quando Usar |
|---|---|---|---|
| TE-SESS | Sessão timeboxada com charter definido | 60-90 minutos | Funcionalidade nova |
| TE-TOUR | Percorrer o sistema com perspectiva específica | 30-60 minutos | Após integração |
| TE-PARS | Dev + QA testam juntos | 30-60 minutos | Funcionalidade complexa |

### 4. Testes de Contrato (TC)
Verificam conformidade de interfaces entre serviços.

#### Subcategorias
- **TC-CONS:** Contrato do consumidor (consumer-driven)
- **TC-PROV:** Contrato do provedor (provider verification)
- **TC-SCHE:** Validação de schema (estrutura de dados)

#### Definições
| Subcategoria | Definição | Ferramenta Típica |
|---|---|---|
| TC-CONS | Consumidor define expectativas, provedor verifica | Pact, Spring Cloud Contract |
| TC-PROV | Provedor publica contrato, consumidor valida | OpenAPI, Swagger |
| TC-SCHE | Valida formato de dados contra schema | JSON Schema, Avro |

### 5. Testes de Dados (TD)
Verificam integridade e qualidade dos dados.

#### Subcategorias
- **TD-MIGR:** Teste de migração de dados
- **TD-QUAL:** Teste de qualidade de dados
- **TD-VOLM:** Teste com volume realista de dados

## Exemplos por Categoria

### TF-UNIT: Teste Unitário
```
Cenário: Cálculo de desconto progressivo
Tipo: TF-UNIT
Prioridade: Crítica
Pré-condições: Nenhuma dependência externa

Casos de teste:
  1. Cliente com histórico de R$ 500 -> desconto 0%
  2. Cliente com histórico de R$ 1.000 -> desconto 5%
  3. Cliente com histórico de R$ 5.000 -> desconto 10%
  4. Cliente com histórico de R$ 10.000 -> desconto 15%
  5. Cliente com histórico de R$ 0 -> desconto 0%
  6. Valor negativo -> lançar exceção
  7. Valor no limite exato (R$ 999.99) -> desconto 0%
  8. Valor no limite exato (R$ 1.000.00) -> desconto 5%

Automatizado: Sim (obrigatório)
Cobertura: 100% dos branches da função
```

### TNF-RESI: Teste de Resiliência
```
Cenário: Indisponibilidade do serviço de pagamento
Tipo: TNF-RESI
Prioridade: Alta

Teste 1: Circuit breaker abre após 3 falhas
  Ação: Simular timeout do serviço de pagamento
  Esperado: Após 3 timeouts, circuit breaker abre
  Verificar: Requisições subsequentes retornam erro imediato
  Verificar: Alerta disparado

Teste 2: Recuperação após restabelecimento
  Ação: Restabelecer serviço de pagamento
  Esperado: Circuit breaker fecha após 30s (half-open)
  Verificar: Próxima requisição tenta o serviço real
  Verificar: Fluxo normaliza sem intervenção manual

Automatizado: Sim (Chaos Engineering pipeline)
```

### TC-CONS: Teste de Contrato do Consumidor
```
Cenário: Order Service consome User Service
Tipo: TC-CONS
Ferramenta: Pact

Contrato do consumidor (Order Service espera):
  GET /api/users/{id}
  Resposta 200:
    {
      "id": string,
      "nome": string (min 1 caractere),
      "email": string (formato email),
      "ativo": boolean
    }

Verificação:
  - Executado no pipeline do User Service
  - Falha se contrato não for atendido
  - Bloqueia deploy do User Service se quebrar contrato
```
