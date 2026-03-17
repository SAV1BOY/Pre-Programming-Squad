# Workshop Kit — Design de Testes

## Objetivo

Capacitar o squad e times de desenvolvimento a projetar estratégias de teste antes da codificação. O workshop ensina como mapear cenários sistematicamente, definir a pirâmide de testes, identificar edge cases, planejar dados de teste e criar critérios de aceitação verificáveis. O resultado é que os testes deixam de ser uma fase posterior e passam a ser parte integrante do design.

---

## Duração

**3.5 horas**, divididas em:
- 30min — Por que planejar testes antes de codificar
- 30min — Pirâmide de testes e estratégia por nível
- 15min — Intervalo
- 45min — Técnicas de mapeamento de cenários
- 45min — Exercício prático: design de testes para uma feature
- 15min — Dados de teste e ambientes
- 30min — Retrospectiva

---

## Participantes

- **Mínimo**: 4 pessoas | **Máximo**: 12 pessoas
- **Perfil ideal**: Engenheiros, QAs, membros do Pre-Programming Squad
- **Pré-requisito**: Experiência básica com testes automatizados
- **Facilitador**: QA lead ou engenheiro sênior com forte cultura de testes

---

## Agenda Detalhada

### Bloco 1 — Por que Planejar Testes Antes (30 min)

1. **O custo de bugs por fase** (10 min)
   - Pré-programação: 1x | Codificação: 5x | QA: 10x | Produção: 50-100x
   - Exemplos reais de bugs que custaram milhões
   - O teste mais barato é o que previne o bug no design

2. **Testes como especificação** (10 min)
   - Cenários de teste são a especificação mais precisa que existe
   - Se não consegue descrever o teste, não entendeu o requisito
   - TDD começa no planejamento, não no código

3. **Anti-padrões de teste** (10 min)
   - "Testamos depois": garante que edge cases são ignorados
   - "100% de cobertura": métrica vaidosa sem valor real
   - "Só testes unitários": false confidence — sistema pode falhar na integração
   - "Só testes e2e": lentos, frágeis, impossíveis de debugar

### Bloco 2 — Pirâmide de Testes (30 min)

1. **Unitários (70% dos testes)** (10 min)
   - Rápidos (< 100ms), isolados, determinísticos
   - Testam lógica de negócio, cálculos, validações
   - Não acessam banco, rede ou sistema de arquivos
   - Quando usar: regras de negócio, transformações de dados, validações

2. **Integração (20% dos testes)** (10 min)
   - Testam interação entre componentes reais
   - Banco de dados real (não mock), APIs reais (sandbox)
   - Velocidade: segundos a minutos
   - Quando usar: repositories, API endpoints, integrações com serviços

3. **E2E / Aceitação (10% dos testes)** (10 min)
   - Testam fluxo completo do usuário
   - Mais lentos e frágeis — usar com parcimônia
   - Cobrir apenas caminhos críticos de negócio
   - Quando usar: checkout, login, fluxos de conversão

### Intervalo (15 min)

### Bloco 3 — Técnicas de Mapeamento de Cenários (45 min)

1. **Partição de Equivalência** (10 min)
   - Dividir inputs em classes que devem ter o mesmo comportamento
   - Testar um representante de cada classe
   - Exemplo: campo idade — negativo, zero, 1-17, 18-120, >120

2. **Análise de Valor Limite** (10 min)
   - Testar nos limites de cada partição
   - Bugs se concentram nos limites (off-by-one errors)
   - Exemplo: se limite é 100 itens, testar 99, 100, 101

3. **Tabela de Decisão** (10 min)
   - Para regras com múltiplas condições, criar tabela de todas as combinações
   - Identificar quais combinações são possíveis e qual o resultado esperado
   - Reduz chance de esquecer combinações

4. **State Transition** (10 min)
   - Para entidades com ciclo de vida (pedido: criado -> pago -> enviado -> entregue)
   - Testar todas as transições válidas E as inválidas
   - O que acontece ao tentar entregar um pedido cancelado?

5. **Error Guessing** (5 min)
   - Experiência do testador: "O que costuma dar errado?"
   - Null/undefined, string vazia, unicode, caracteres especiais
   - Concorrência, timeout, disco cheio, conexão perdida

### Bloco 4 — Exercício Prático (45 min)

**Cenário**: Projetar os testes para um sistema de cupons de desconto.

Regras do negócio:
- Cupons podem ser percentuais (5%-50%) ou valor fixo (R$10-R$500)
- Cupom tem data de validade, limite de usos e valor mínimo de compra
- Máximo 1 cupom por pedido
- Cupons não acumulam com promoções
- Alguns cupons são exclusivos para primeira compra

**Tarefas do grupo**:
1. (10 min) Listar todos os cenários de teste (caminho feliz, edge cases, erros)
2. (10 min) Classificar na pirâmide (unitário, integração, e2e)
3. (10 min) Priorizar por risco (P1, P2, P3)
4. (10 min) Definir dados de teste necessários
5. (5 min) Apresentar para o grupo

### Bloco 5 — Dados de Teste e Ambientes (15 min)

- Fixtures vs factories vs seeds
- Dados determinísticos vs aleatórios (property-based testing)
- Isolamento entre testes: cada teste limpa o que criou
- Ambientes: local, CI, staging — o que roda em cada um

### Bloco 6 — Retrospectiva (30 min)

- Que técnica de mapeamento foi mais útil?
- O exercício revelou cenários que não teriam sido pensados sem o processo?
- Como integrar design de testes no fluxo de pré-programação?
- Quem deveria participar do design de testes? (só QA? devs também?)

---

## Exercícios

1. **Bug Hunting**: Apresentar uma especificação com bugs intencionais. Quem encontrar mais ganha.

2. **Edge Case Tournament**: Cada pessoa tem 3 minutos para listar o máximo de edge cases para uma funcionalidade. Comparar e discutir.

3. **Pirâmide Invertida**: Apresentar um projeto com pirâmide invertida (muitos e2e, poucos unitários). Grupo propõe refatoração da estratégia de testes.

4. **Test Case Review**: Apresentar um plano de testes e pedir ao grupo que identifique cenários faltantes.

---

## Outputs Esperados

- Participantes capacitados a mapear cenários de teste sistematicamente
- Template de plano de testes adaptado ao contexto do squad
- Diretrizes de pirâmide de testes acordadas pelo grupo
- Catálogo de edge cases comuns por tipo de funcionalidade
- Processo de design de testes integrado ao fluxo de pré-programação
