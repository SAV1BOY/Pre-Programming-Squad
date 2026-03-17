# Template: Design de Testes

## Título
Test Design — Estratégia e Design de Testes

## Propósito
Definir a estratégia de testes do projeto antes da implementação, incluindo níveis de teste, cobertura esperada, cenários críticos e ferramentas a serem utilizadas.

## Quando Usar
- Após definição de requisitos e arquitetura.
- Antes de iniciar a implementação (test-first approach).
- Quando é necessário alinhar a equipe sobre a abordagem de qualidade.

## Seções

### 1. Informações Gerais
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| Responsável | `[nome]` |
| Data | `[YYYY-MM-DD]` |
| Cobertura Alvo | `[percentual mínimo]` |

### 2. Pirâmide de Testes
```
        /  E2E  \          ← Poucos, lentos, caros
       /----------\
      / Integração \       ← Moderados
     /----------------\
    /    Unitários      \  ← Muitos, rápidos, baratos
   /----------------------\
```

| Nível | Quantidade Estimada | Ferramentas | Responsável |
|-------|-------------------|------------|-------------|
| Unitário | `[estimativa]` | `[Jest/pytest/etc.]` | `[equipe]` |
| Integração | `[estimativa]` | `[Supertest/TestContainers/etc.]` | `[equipe]` |
| E2E | `[estimativa]` | `[Cypress/Playwright/etc.]` | `[equipe]` |

### 3. Cenários de Teste Críticos
| ID | Cenário | Tipo | Pré-condição | Passos | Resultado Esperado | Prioridade |
|----|---------|------|-------------|--------|-------------------|-----------|
| TC-01 | `[nome do cenário]` | `[Unitário/Integração/E2E]` | `[estado inicial]` | `[passos]` | `[resultado]` | `[Alta/Média/Baixa]` |

### 4. Cenários de Borda (Edge Cases)
| ID | Cenário | Input | Comportamento Esperado |
|----|---------|-------|----------------------|
| EC-01 | `[cenário extremo]` | `[dados de entrada]` | `[como o sistema deve reagir]` |

### 5. Testes Não-Funcionais
| Tipo | Ferramenta | Métrica | Valor Alvo | Critério de Falha |
|------|-----------|---------|-----------|-------------------|
| Performance | `[k6/JMeter/etc.]` | `[latência/throughput]` | `[valor]` | `[quando falha]` |
| Segurança | `[OWASP ZAP/etc.]` | `[vulnerabilidades]` | `[zero críticas]` | `[quando falha]` |
| Carga | `[ferramenta]` | `[usuários simultâneos]` | `[valor]` | `[quando falha]` |

### 6. Dados de Teste
| Cenário | Dados Necessários | Fonte | Anonimização |
|---------|------------------|-------|-------------|
| `[cenário]` | `[tipo de dados]` | `[Fixtures/Factory/Produção anonimizada]` | `[Sim/Não/N/A]` |

### 7. Ambientes de Teste
| Ambiente | Propósito | Dados | Integrações |
|----------|-----------|-------|-------------|
| `[Local/CI/Staging]` | `[para que serve]` | `[mock/real/subconjunto]` | `[mock/sandbox/real]` |

### 8. Critérios de Aceite de Qualidade
- [ ] Cobertura de testes unitários ≥ `[X]`%
- [ ] Todos os cenários críticos passando
- [ ] Zero vulnerabilidades de segurança críticas
- [ ] Performance dentro dos limites definidos
- [ ] `[critério adicional]`

## Exemplo de Preenchimento

### 3. Cenários de Teste Críticos
| ID | Cenário | Tipo | Pré-condição | Passos | Resultado Esperado | Prioridade |
|----|---------|------|-------------|--------|-------------------|-----------|
| TC-01 | Criar pedido com sucesso | Integração | Usuário autenticado, produto em estoque | 1. POST /orders com payload válido | 201 Created, pedido no banco, evento emitido | Alta |
| TC-02 | Criar pedido sem estoque | Integração | Produto com estoque = 0 | 1. POST /orders com produto sem estoque | 422, mensagem de erro clara, nenhum pedido criado | Alta |
| TC-03 | Fluxo completo de compra | E2E | Usuário logado, carrinho com itens | 1. Checkout → 2. Pagamento → 3. Confirmação | Pedido confirmado, email enviado, estoque atualizado | Alta |

## Dicas de Qualidade
- **Test-first mindset:** Pense nos testes antes de implementar. Isso melhora o design.
- **Foque em cenários, não em cobertura:** 80% de cobertura com cenários ruins é pior que 60% com cenários certos.
- **Automatize o que importa:** Nem todo teste precisa ser automatizado, mas os críticos sim.
- **Dados de teste realistas:** Fixtures com "foo" e "bar" não pegam os bugs que dados reais pegam.
- **Revise edge cases com o time:** A equipe de QA e de negócio conhece casos extremos que devs não imaginam.
