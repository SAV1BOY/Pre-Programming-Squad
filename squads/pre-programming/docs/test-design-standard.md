# Standard para Design de Testes

## Propósito

Definir a estratégia de testes durante a fase de pré-programação, antes que uma única linha de código de teste seja escrita. O design de testes garante que o time de implementação saiba exatamente o que testar, como testar e qual o critério de sucesso — antes de começar a codar.

## Escopo

Todo projeto que passa pela pipeline do Pre-Programming Squad. A profundidade varia conforme tamanho: projetos P recebem cenários básicos; projetos G/XG recebem estratégia completa.

## Definições

| Termo | Definição |
|---|---|
| Cenário de teste | Descrição de uma condição a ser verificada, com input, ação e resultado esperado |
| Pirâmide de testes | Distribuição de testes por tipo: muitos unitários, moderados de integração, poucos e2e |
| Cobertura funcional | Percentual de requisitos com pelo menos 1 cenário de teste associado |
| Dados de teste | Conjunto de dados pré-definidos ou critérios de geração para execução de testes |

## Processo

### 1. Derivar Cenários dos Requisitos

Para cada requisito funcional e critério de aceitação do escopo:
- Identificar o happy path (fluxo principal de sucesso)
- Identificar edge cases (fronteiras, limites, valores extremos)
- Identificar cenários de erro (input inválido, falha de dependência, timeout)
- Identificar cenários de concorrência (quando aplicável)
- Identificar cenários de segurança (acesso não autorizado, injection, overflow)

**Formato de cenário:**

```
Cenário: [Nome descritivo]
Dado: [Pré-condição / estado inicial]
Quando: [Ação executada]
Então: [Resultado esperado]
Prioridade: [Crítico / Alto / Médio / Baixo]
Tipo: [Unitário / Integração / E2E / Carga / Segurança]
```

### 2. Definir Estratégia por Tipo de Teste

**Testes Unitários:**
- O que cobrir: lógica de negócio, validações, cálculos, transformações
- Meta de cobertura: ≥ 85% em módulos de lógica core
- Responsável: time de implementação

**Testes de Integração:**
- O que cobrir: comunicação entre componentes, acesso a banco, chamadas de API
- Cenários foco: contrato de API, tratamento de erros de dependência, transações
- Responsável: time de implementação

**Testes End-to-End:**
- O que cobrir: fluxos completos do ponto de vista do usuário
- Cenários foco: happy paths dos fluxos principais (máximo 10-15 cenários e2e)
- Responsável: time de implementação com suporte de QA (se houver)

**Testes de Carga (quando aplicável):**
- O que cobrir: performance sob volume esperado e pico
- Cenários: volume normal, 2x pico, degradação gradual
- Meta: SLA de latência e throughput definidos nos requisitos não-funcionais
- Ferramenta recomendada: k6, Locust ou similar
- Responsável: time de implementação com suporte de SRE

**Testes de Segurança (quando aplicável):**
- O que cobrir: autenticação, autorização, injection, exposição de dados
- Cenários: acesso sem token, token de outro usuário, SQL injection, XSS
- Responsável: time de implementação com revisão de Security

### 3. Definir Dados de Teste

- Listar datasets necessários para cada tipo de teste
- Definir se dados são fixtures estáticas ou gerados dinamicamente
- Mapear dados sensíveis que precisam de anonimização
- Definir estratégia de seed de banco para testes de integração

### 4. Documentar Matriz de Rastreabilidade

| Requisito | Cenário(s) de Teste | Tipo | Prioridade |
|---|---|---|---|
| REQ-001: Criar pedido | CT-001: Happy path, CT-002: Produto sem estoque, CT-003: Usuário não autenticado | Integração, Unitário, E2E | Crítico |
| ... | ... | ... | ... |

### 5. Definir Critérios de Qualidade dos Testes

- Cobertura funcional: 100% dos requisitos com pelo menos 1 cenário
- Cobertura de código: meta por módulo
- Tempo de execução: suite completa < X minutos
- Flakiness: < 1% de testes instáveis

## Critérios de Qualidade

- Todo requisito funcional tem pelo menos 1 cenário de teste associado
- Edge cases e cenários de erro cobrem pelo menos os casos mais prováveis
- Dados de teste definidos ou com critérios claros de geração
- Estratégia de teste proporcional ao risco do projeto
- Documento de test design revisado por par antes do handoff

## Responsáveis

| Papel | Responsabilidade |
|---|---|
| Membro do squad | Derivar cenários, documentar estratégia, definir dados |
| Tech Lead | Revisar completude da estratégia, calibrar profundidade |
| Time de implementação | Implementar testes conforme estratégia, reportar gaps |
| QA (se houver) | Complementar cenários de e2e, validar cobertura funcional |

## Referências

- Standard de Scoping: `docs/scoping-standard.md`
- What Good Looks Like: `docs/what-good-looks-like.md`
- Standard de Performance: `docs/performance-precheck-standard.md`
