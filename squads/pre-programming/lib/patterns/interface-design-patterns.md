# Padrões de Design de Interfaces

## Nome do Padrão
Padrões para Design de Interfaces entre Componentes e Serviços

## Problema que Resolve
Interfaces mal projetadas entre componentes causam: acoplamento forte, quebras em cascata durante mudanças, dificuldade de teste isolado, versionamento problemático e comunicação ineficiente entre equipes. Definir padrões de interface na pré-programação previne retrabalho significativo.

## Solução

### 1. Interface Segregada (Interface Segregation)
Criar interfaces pequenas e específicas ao invés de interfaces grandes e genéricas. Cada consumidor deve depender apenas dos métodos que utiliza.

**Aplicação prática:**
- Mapear consumidores de cada interface
- Identificar quais métodos cada consumidor realmente usa
- Dividir interfaces grandes em contratos menores e coesos
- Documentar a razão de cada divisão

### 2. Contrato Tolerante (Tolerant Reader)
Projetar consumidores que ignoram campos desconhecidos e não falham com adições ao contrato, permitindo evolução independente.

**Aplicação prática:**
- Consumidores extraem apenas campos necessários
- Validação não rejeita campos extras
- Campos opcionais têm valores padrão documentados
- Testes verificam tolerância a campos novos

### 3. Versionamento Semântico de API
Aplicar versionamento semântico nas interfaces, com regras claras sobre o que constitui breaking change.

**Aplicação prática:**
- Major: breaking changes (remoção de campo, mudança de tipo)
- Minor: adições retrocompatíveis (novos campos opcionais)
- Patch: correções sem mudança de contrato
- Manter suporte a N-1 por período definido

### 4. Documentação por Exemplo (Example-Driven)
Documentar interfaces primariamente através de exemplos concretos de requisição e resposta, não apenas com descrições abstratas.

**Aplicação prática:**
- Cada endpoint com pelo menos 2 exemplos (sucesso e erro)
- Exemplos executáveis como testes de contrato
- Gerar documentação a partir dos exemplos
- Manter exemplos atualizados via CI

## Quando Usar

- Ao definir APIs REST, GraphQL ou gRPC
- Na comunicação entre microsserviços
- Em integrações com equipes externas
- Ao projetar SDKs ou bibliotecas públicas
- Em sistemas com múltiplos consumidores de uma mesma API

## Quando NÃO Usar

- Em interfaces internas de módulos de um monolito coeso
- Em protótipos rápidos com um único consumidor
- Quando o provedor e consumidor são mantidos pela mesma pessoa
- Em comunicação ponto-a-ponto dentro de um único processo

## Exemplos

### Exemplo 1: Interface Segregada para Serviço de Usuário
```
ANTES (interface grande):
  UserService:
    - getUser(id)
    - updateUser(id, data)
    - deleteUser(id)
    - getUserPermissions(id)
    - getUserPreferences(id)
    - getUserPaymentMethods(id)
    - getUserOrderHistory(id)

DEPOIS (interfaces segregadas):
  UserProfileService:     getUser, updateUser, deleteUser
  UserPermissionService:  getUserPermissions, updatePermissions
  UserPreferenceService:  getUserPreferences, updatePreferences
  UserPaymentService:     getUserPaymentMethods, addPaymentMethod
  UserOrderService:       getUserOrderHistory
```

### Exemplo 2: Contrato Tolerante
```
Resposta da API v1.0:
{
  "id": "usr_123",
  "nome": "Maria",
  "email": "maria@exemplo.com"
}

Resposta da API v1.1 (campo adicionado):
{
  "id": "usr_123",
  "nome": "Maria",
  "email": "maria@exemplo.com",
  "telefone": "+55-11-99999-0000"    // campo novo
}

Consumidor tolerante:
  - Funciona com v1.0 e v1.1 sem mudança de código
  - Extrai apenas: id, nome, email
  - Ignora campo "telefone" até precisar dele
```

### Exemplo 3: Versionamento com Período de Suporte
```
Timeline de versionamento:
  v1 lançada em Jan/2025 - suporte até Jul/2025
  v2 lançada em Abr/2025 - suporte até Out/2025

Comunicação:
  - 3 meses antes do sunset: header "Deprecation" nas respostas
  - 1 mês antes: e-mail para consumidores registrados
  - No sunset: retorno 410 Gone com link para migração

Compatibilidade:
  v1 -> v2: Guia de migração publicado
  Mudanças breaking: campo "endereco" (string -> objeto)
  Adaptador temporário disponível: /v1/compat/*
```
