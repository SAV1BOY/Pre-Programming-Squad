# Ótimos Planos de Teste — Exemplos Anotados

## Introdução

Um plano de teste excepcional é escrito antes do código e guia tanto a implementação quanto a validação. Ele mapeia cenários sistematicamente, define a pirâmide de testes, identifica dados necessários e estabelece critérios claros de aprovação. O melhor plano de teste é aquele que faz o desenvolvedor pensar "ah, eu não tinha considerado esse caso" antes de escrever a primeira linha.

---

## Exemplo 1 — Plano de Teste para Checkout de E-commerce

### O Plano

> **Pirâmide de Testes**:
> - Unitários (70%): Cálculo de preço, aplicação de cupom, validação de estoque, cálculo de frete
> - Integração (20%): Fluxo completo de checkout com banco real, integração com gateway de pagamento (sandbox)
> - E2E (10%): Fluxo completo do usuário do carrinho ao pedido confirmado
>
> **Cenários Críticos (caminho feliz)**:
> 1. Checkout com cartão de crédito — parcela única
> 2. Checkout com PIX — geração de QR code e confirmação
> 3. Checkout com cupom de desconto percentual
> 4. Checkout com frete calculado por CEP
>
> **Edge Cases Mapeados**:
> 1. Produto fica sem estoque entre adicionar ao carrinho e finalizar compra
> 2. Cupom expira durante o checkout
> 3. Timeout do gateway de pagamento (> 30s)
> 4. Usuário faz double-click no botão de pagamento
> 5. Preço do produto muda entre visualização e compra
> 6. CEP inválido ou de área não atendida
> 7. Carrinho com 100+ itens (limite de payload)
> 8. Moeda diferente para compra internacional (se aplicável)
>
> **Cenários de Erro**:
> 1. Cartão recusado por saldo insuficiente
> 2. Cartão recusado por fraude
> 3. Falha de rede durante processamento
> 4. Serviço de frete indisponível
>
> **Dados de Teste**:
> - Fixtures: 10 produtos com variações de estoque, 5 cupons com regras diferentes, 3 endereços (capital, interior, área remota)
> - Cartões de teste do gateway (aprovado, recusado, timeout)

### Por que funciona

- **Pirâmide quantificada**: 70/20/10 — time sabe exatamente a distribuição
- **Edge cases que revelam bugs reais**: Double-click, mudança de preço, timeout — esses são os bugs de produção
- **Dados de teste planejados**: Fixtures definidas antes da codificação

---

## Exemplo 2 — Plano de Teste para API de Autenticação

### O Plano

> **Cenários de Segurança (obrigatórios)**:
> 1. Brute force: bloqueio após 5 tentativas em 5 minutos
> 2. Token JWT expirado retorna 401, não 500
> 3. Token JWT com assinatura inválida retorna 401
> 4. Refresh token: funciona uma vez, invalidado após uso
> 5. SQL injection em campo de login: sanitizado
> 6. XSS em campo de nome de usuário: escapado
> 7. CSRF protection: requests sem token CSRF são rejeitados
> 8. Rate limiting: 429 após exceder limite
>
> **Testes de Concorrência**:
> 1. Dois logins simultâneos do mesmo usuário — ambos devem funcionar
> 2. Refresh token usado simultaneamente em dois devices — apenas um deve funcionar
> 3. Logout em um device não invalida sessão de outro device (a menos que "logout all")
>
> **Testes de Contrato**:
> - Todos os endpoints retornam JSON com structure consistente
> - Erros seguem formato padrão: `{error: {code, message, details}}`
> - Headers de segurança presentes: X-Content-Type-Options, X-Frame-Options, Strict-Transport-Security

### Por que funciona

- **Segurança como primeira classe**: Não é "testar depois" — é o primeiro bloco do plano
- **Concorrência explícita**: Race conditions em auth são bugs de segurança
- **Testes de contrato**: Garantem consistência na interface

---

## Lições Extraídas

1. **Escreva edge cases antes do código**: Se o dev conhece os edge cases, a implementação os trata
2. **Quantifique a pirâmide**: Percentuais concretos, não "muitos unitários"
3. **Planeje dados de teste cedo**: Fixtures mal pensadas desperdiçam dias
4. **Priorize cenários**: Nem todo teste tem a mesma importância — classifique por risco
5. **Inclua cenários de concorrência**: Race conditions são os bugs mais difíceis de debugar
6. **Segurança não é opcional**: Todo plano de teste deve ter uma seção de segurança
7. **Defina critérios de aprovação**: "Todos os testes passando" não é suficiente — cobertura, performance, segurança
