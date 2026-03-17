# Decomposition Strategy Framework

## Propósito
Quebrar problemas complexos em partes implementáveis, ordenáveis e independentes, garantindo que cada parte é testável isoladamente e que dependências entre partes estão claras.

## Problema que Resolve
Times recebem um problema grande ("precisamos de um sistema de pagamentos") e não sabem por onde começar. Sem decomposição, o trabalho vira monolito de escopo com dependências ocultas e paralelismo impossível.

## Quando Usar
- Após architecture sketch, antes de estimation
- Quando o escopo tem mais de 1 sprint de trabalho
- Quando múltiplos devs/times trabalharão em paralelo
- Obrigatório para projetos porte G/XG

## Princípios de Decomposição

### 1. Cada parte deve ser implementável e testável isoladamente
Se uma parte depende de 5 outras para funcionar, não é uma boa decomposição.

### 2. Dependências devem ser explícitas e mínimas
Grafo de dependências deve ser DAG (Directed Acyclic Graph), não um emaranhado.

### 3. Interfaces entre partes devem ser definidas antes
O contrato entre módulo A e módulo B é definido no pré-programming, não durante o coding.

### 4. Ordenação por: dependência técnica > valor > risco
Primeiro o que desbloqueia outras partes, depois o que entrega mais valor, depois o que reduz mais risco.

## Processo

### Passo 1 — Identificar Módulos Funcionais
Do architecture sketch, listar módulos/serviços/componentes:
```
1. Auth Module (autenticação + autorização)
2. Payment Processing (processamento de pagamento)
3. Order Management (gestão de pedidos)
4. Notification Service (notificações)
5. Admin Dashboard (painel administrativo)
```

### Passo 2 — Mapear Dependências
```
Auth ← Payment (precisa de auth para processar)
Auth ← Order (precisa de auth para criar pedido)
Order → Payment (pedido dispara pagamento)
Payment → Notification (pagamento aprovado notifica)
Admin ← All (dashboard consulta todos)
```

### Passo 3 — Definir Interfaces
Para cada seta de dependência, definir contrato:
```
Order → Payment:
  POST /payments
  Input: { order_id, amount, method }
  Output: { payment_id, status }
  Errors: 400 (invalid), 402 (insufficient), 500 (provider error)
```

### Passo 4 — Ordenar por Critério
| Módulo | Bloqueia | Valor | Risco | Ordem |
|--------|----------|-------|-------|-------|
| Auth | Payment, Order, Admin | Alto | Médio | 1º |
| Order | Payment, Admin | Alto | Baixo | 2º |
| Payment | Notification, Admin | Crítico | Alto | 3º |
| Notification | - | Médio | Baixo | 4º |
| Admin | - | Médio | Baixo | 5º |

### Passo 5 — Validar Paralelismo
Quais módulos podem ser desenvolvidos em paralelo?
- **Paralelo:** Auth + Order (se interface Auth estiver definida como mock)
- **Sequencial:** Payment precisa de Auth pronto
- **Independente:** Notification e Admin podem ser feitos por último

## Heurísticas
1. **Se não consegue explicar um módulo em 2 frases, ele é grande demais** → Decomponha mais
2. **Se um módulo tem mais de 3 dependências, ele pode ser muito central** → Considere quebrar em sub-módulos
3. **Se dois módulos sempre mudam juntos, eles podem ser um só** → Coesão > separação artificial
4. **Se a interface entre dois módulos é mais complexa que os módulos, a fronteira está errada**

## Armadilhas
- **Decompor demais** → Partes tão pequenas que o overhead de coordenação é maior que o benefício
- **Decompor de menos** → Partes ainda muito complexas para estimar ou implementar
- **Ignorar dependências cíclicas** → A depende de B que depende de A = problema de design
- **Não definir contratos entre partes** → Módulos prontos que não encaixam entre si
