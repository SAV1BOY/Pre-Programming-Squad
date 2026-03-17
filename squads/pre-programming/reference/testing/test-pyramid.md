# Piramide de Testes

## O que e a Piramide de Testes

A piramide de testes, introduzida por Mike Cohn e popularizada por Martin Fowler, e um modelo que guia a distribuicao de testes automatizados em tres (ou mais) camadas. A base larga e composta por testes unitarios (rapidos, baratos, muitos), o meio por testes de integracao (moderados), e o topo por testes end-to-end (lentos, caros, poucos).

## Camadas da Piramide

### Camada 1: Testes Unitarios (Base)
**Quantidade:** Muitos (70-80% do total)
**Velocidade:** Milissegundos por teste
**Escopo:** Uma unica funcao, classe ou modulo isoladamente
**Dependencias:** Mockadas/stubadas
**Feedback:** Imediato (segundos para toda a suite)

**O que testar:**
- Logica de negocio pura.
- Transformacoes de dados.
- Validacoes.
- Casos de borda e cenarios de erro.
- Algoritmos.

**O que nao testar unitariamente:**
- Integracao com banco de dados.
- Chamadas HTTP reais.
- File system.
- Configuracao de framework.

### Camada 2: Testes de Integracao (Meio)
**Quantidade:** Moderada (15-20% do total)
**Velocidade:** Segundos por teste
**Escopo:** Interacao entre 2 ou mais componentes
**Dependencias:** Reais quando possivel (testcontainers), mocadas quando necessario

**O que testar:**
- Queries de banco de dados.
- Serializacao/desserializacao de APIs.
- Contract testing entre servicos.
- Integracao com message brokers.
- Repositories e data access.

**Ferramentas uteis:**
- Testcontainers (bancos, Redis, Kafka em containers).
- Pact (contract testing).
- WireMock (mock de APIs externas).

### Camada 3: Testes End-to-End (Topo)
**Quantidade:** Poucos (5-10% do total)
**Velocidade:** Minutos por teste
**Escopo:** Fluxo completo do usuario, todos os sistemas integrados
**Dependencias:** Ambiente completo (staging ou similar)

**O que testar:**
- Fluxos criticos de negocio (happy path).
- Smoke tests pos-deploy.
- Cenarios que envolvem multiplos servicos.

**O que nao testar E2E:**
- Casos de borda (testar unitariamente).
- Todas as combinacoes (combinatoria explode).
- Cenarios de erro de baixo nivel.

## A Piramide na Pre-Programacao

### Definir Estrategia de Testes no Design Doc

Para cada componente do design, mapear:

| Componente | Testes Unitarios | Testes Integracao | Testes E2E |
|---|---|---|---|
| Logica de precificacao | Regras de calculo, descontos, limites | N/A | Fluxo de compra com preco correto |
| API de pedidos | Validacao de input, mapeamentos | Contract tests com consumers, repo tests | Criar pedido completo |
| Consumer de eventos | Parsing, logica de processamento | Consumer + broker real (testcontainers) | Evento -> notificacao recebida |

### Criterios de Readiness para Testes
- Estrategia de testes definida por componente.
- Proporcao da piramide justificada (desvios explicados).
- Ferramentas de teste identificadas.
- Dados de teste planejados (fixtures, factories, seeds).
- Ambiente de testes de integracao definido.

## Anti-Piramide: O Cone de Sorvete

O anti-padrao mais comum e inverter a piramide: muitos testes E2E, poucos unitarios.

**Sintomas:**
- Suite de testes leva horas para executar.
- Testes sao frageis e falham por razoes nao relacionadas ao codigo.
- Ninguem confia nos testes.
- Equipe desiste de rodar testes localmente.

**Causas na Pre-Programacao:**
- Design altamente acoplado que dificulta testes unitarios.
- Ausencia de interfaces/abstracoes para injecao de dependencias.
- Logica de negocio misturada com framework.

**Prevencao na Pre-Programacao:**
- Avaliar testabilidade como criterio de design.
- Exigir separacao de logica de negocio e infraestrutura.
- Planejar interfaces para injecao de dependencias.

## Honeycomb: Alternativa para Microsservicos

Para microsservicos, o Spotify propoe o modelo honeycomb: mais testes de integracao no centro, menos unitarios e E2E nas pontas.

**Justificativa:** Em microsservicos, o valor esta na integracao entre componentes, nao na logica interna (que tende a ser simples). Testes de integracao com testcontainers oferecem melhor custo-beneficio.

**Quando usar honeycomb vs. piramide:**
- Piramide: servicos com logica de negocio complexa.
- Honeycomb: servicos com logica simples mas integracao complexa (API gateways, orchestrators).

## Metricas de Saude da Suite de Testes

| Metrica | Target | Alerta |
|---|---|---|
| Tempo total de execucao (CI) | < 10 minutos | > 20 minutos |
| Taxa de flaky tests | < 1% | > 5% |
| Cobertura de logica de negocio | > 90% | < 70% |
| Ratio unitario:integracao:E2E | ~70:20:10 | Invertida |
| Tempo medio para corrigir teste quebrado | < 1 dia | > 3 dias |
