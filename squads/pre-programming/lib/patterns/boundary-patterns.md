# Padrões de Limites (Boundary Patterns)

## Nome do Padrão
Padrões de Definição de Limites do Sistema

## Problema que Resolve
Projetos frequentemente falham por não definir claramente onde o sistema começa e termina. Sem limites bem estabelecidos, ocorrem: escopo crescente descontrolado (scope creep), integrações mal planejadas, responsabilidades ambíguas entre equipes e componentes que tentam fazer mais do que deveriam.

## Solução

### 1. Contexto Delimitado (Bounded Context)
Dividir o domínio em contextos claramente delimitados, cada um com seu próprio modelo de dados e linguagem ubíqua. A comunicação entre contextos ocorre exclusivamente através de interfaces bem definidas.

**Aplicação prática:**
- Mapear os subdomínios do problema
- Definir a linguagem específica de cada contexto
- Estabelecer contratos de comunicação entre contextos
- Documentar traduções de termos entre contextos

### 2. Camada Anticorrupção (Anti-Corruption Layer)
Criar uma camada intermediária que protege o modelo interno do sistema contra influências de sistemas externos ou legados.

**Aplicação prática:**
- Identificar sistemas externos com modelos incompatíveis
- Projetar adaptadores que traduzem entre modelos
- Isolar a lógica de tradução em componentes dedicados

### 3. Portão de Entrada (Gateway Pattern)
Centralizar o acesso a sistemas externos em um único ponto de entrada, abstraindo detalhes de protocolo e localização.

**Aplicação prática:**
- Listar todos os sistemas externos consumidos
- Criar interfaces abstratas para cada integração
- Implementar resiliência (retry, circuit breaker) no gateway

### 4. Contrato do Consumidor (Consumer-Driven Contract)
Definir contratos de API a partir das necessidades reais dos consumidores, não apenas da perspectiva do provedor.

**Aplicação prática:**
- Coletar requisitos de cada consumidor da API
- Gerar contratos a partir das expectativas dos consumidores
- Validar contratos automaticamente na CI/CD

## Quando Usar

- No início do projeto, ao definir a arquitetura de alto nível
- Ao integrar com sistemas legados ou de terceiros
- Quando múltiplas equipes trabalham em partes diferentes do sistema
- Ao migrar de um monolito para microsserviços
- Quando o domínio é complexo e tem múltiplos subdomínios

## Quando NÃO Usar

- Em projetos pequenos com um único domínio simples
- Quando todo o sistema será mantido por uma única equipe pequena
- Em protótipos ou MVPs onde a velocidade é prioridade absoluta
- Quando não há integrações externas significativas
- Em sistemas CRUD simples sem lógica de negócio complexa

## Exemplos

### Exemplo 1: E-commerce com Contextos Delimitados
```
Contextos identificados:
- Catálogo: Produto, Categoria, Atributo
- Pedidos: Pedido, ItemPedido, StatusPedido
- Pagamentos: Transação, Método, Estorno
- Logística: Envio, Rastreamento, Endereço

Comunicação entre contextos:
- Catálogo -> Pedidos: evento "ProdutoAtualizado"
- Pedidos -> Pagamentos: comando "ProcessarPagamento"
- Pagamentos -> Pedidos: evento "PagamentoConfirmado"
- Pedidos -> Logística: comando "IniciarEnvio"
```

### Exemplo 2: Camada Anticorrupção para Sistema Legado
```
Sistema legado (ERP):
- Usa códigos numéricos para status (1, 2, 3...)
- Datas no formato DD/MM/YYYY como string
- Nomes de campos em inglês abreviado (cst_nm, ord_dt)

Camada anticorrupção:
- Traduz códigos para enums tipados (ATIVO, INATIVO)
- Converte datas para ISO 8601
- Mapeia campos para nomes legíveis no domínio
```

### Exemplo 3: Gateway para APIs Externas
```
Integrações externas:
- API de Pagamento (Stripe): Gateway de Pagamento
- API de CEP (ViaCEP): Gateway de Endereço
- API de Notificação (SendGrid): Gateway de Comunicação

Cada gateway:
- Interface abstrata no domínio
- Implementação concreta com retry e timeout
- Fallback definido para indisponibilidade
- Métricas de latência e erro
```
