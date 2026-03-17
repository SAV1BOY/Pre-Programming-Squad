# Task: Mapear Edge Cases

## Objetivo
Identificar sistematicamente cenários extremos, exceções e condições de contorno que o sistema deve tratar, prevenindo bugs e comportamentos inesperados em produção.

## Input Necessário
- Requisitos funcionais detalhados.
- Regras de negócio documentadas.
- Modelo de domínio.
- Contratos de API definidos.

## Agentes Envolvidos
- **Agente de Qualidade:** Conduz o mapeamento de edge cases.
- **Agente de Domínio:** Identifica exceções de negócio.
- **Agente de Arquitetura:** Identifica edge cases técnicos.
- **Equipe de Suporte:** Compartilha problemas recorrentes de sistemas similares.

## Passos

### 1. Revisar Cada Funcionalidade
- Para cada requisito funcional, perguntar:
  - O que acontece com input vazio, nulo ou inválido?
  - O que acontece com valores nos limites (zero, máximo, negativo)?
  - O que acontece com volumes extremos?
  - O que acontece com caracteres especiais ou encodings diferentes?

### 2. Mapear Cenários de Concorrência
- O que acontece se dois usuários fazem a mesma ação simultaneamente?
- Race conditions em operações de escrita.
- Deadlocks potenciais em acessos ao banco.

### 3. Mapear Cenários de Falha
- O que acontece se uma integração externa está fora do ar?
- O que acontece se o banco está lento ou indisponível?
- O que acontece em timeout de uma operação longa?
- O que acontece se o disco fica cheio?

### 4. Mapear Cenários de Negócio
- O que acontece com pedido sem itens?
- O que acontece com desconto maior que o valor?
- O que acontece se o produto é descontinuado durante uma compra?
- Consultar equipe de suporte sobre os problemas mais comuns.

### 5. Classificar e Priorizar
- Para cada edge case, definir:
  - Probabilidade de ocorrência.
  - Severidade do impacto.
  - Estratégia: prevenir, tratar, monitorar ou aceitar.

### 6. Documentar
- Adicionar edge cases ao template `test-design-template.md`.
- Vincular ao requisito funcional correspondente.

## Output Esperado
- Lista de edge cases identificados e classificados.
- Estratégia de tratamento para cada edge case.
- Cenários de teste para os edge cases críticos.

## Checklist de Validação
- [ ] Edge cases de input (vazio, nulo, limite, inválido) foram mapeados.
- [ ] Cenários de concorrência foram considerados.
- [ ] Cenários de falha de dependências foram mapeados.
- [ ] Edge cases de negócio foram identificados com ajuda de especialistas.
- [ ] Cada edge case tem probabilidade e severidade avaliadas.
- [ ] Estratégia de tratamento está definida para cada um.
- [ ] Cenários de teste foram criados para os mais críticos.
