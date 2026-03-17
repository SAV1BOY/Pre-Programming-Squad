# Requirement Proof Chain

## Título e Propósito

O **Requirement Proof Chain** é um framework para criar uma cadeia de prova que conecta cada requisito de negócio a uma evidência verificável de que foi implementado corretamente. O propósito é garantir rastreabilidade completa: do pedido do stakeholder ao código que o implementa e ao teste que o prova — eliminando o "achismo" de que as coisas funcionam.

## Quando Usar

- Em projetos com requisitos regulatórios ou de compliance onde rastreabilidade é obrigatória
- Quando stakeholders questionam se requisitos foram realmente implementados
- Em projetos complexos com dezenas de requisitos interdependentes
- Quando a equipe precisa provar que o sistema faz o que deveria fazer
- Em auditorias internas ou externas de qualidade de software

## Conceitos-Chave

1. **Cadeia de Prova**: Requisito de negócio → critério de aceite → caso de teste → código → resultado de teste. Cada elo é rastreável.
2. **Evidência Executável**: Testes automatizados que provam continuamente que o requisito é atendido, não apenas documentação estática.
3. **Gap na Cadeia**: Qualquer ponto onde a conexão entre elos está quebrada: requisito sem teste, teste sem resultado, código sem requisito.
4. **Prova Contínua**: A cadeia é verificada em cada build/deploy, não apenas uma vez. Regressões são detectadas automaticamente.
5. **Cobertura de Requisitos**: Diferente de cobertura de código — mede quantos requisitos têm prova completa na cadeia.

## Processo / Passos

### Passo 1 — Numerar Requisitos
Cada requisito recebe um identificador único (REQ-001, REQ-002...). Sem numeração, rastreabilidade é impossível.

### Passo 2 — Derivar Critérios de Aceite
Para cada requisito, derive 1-N critérios de aceite verificáveis. Cada critério recebe um ID (AC-001-01, AC-001-02...).

### Passo 3 — Criar Casos de Teste
Para cada critério de aceite, crie pelo menos um caso de teste (TC-001-01-a). O caso de teste é a prova de que o critério é atendido.

### Passo 4 — Implementar Testes
Transforme casos de teste em testes automatizados sempre que possível. Para testes que não podem ser automatizados, crie checklist de verificação manual.

### Passo 5 — Mapear Código
Para cada teste, identifique qual código (módulo, função, endpoint) implementa o comportamento testado.

### Passo 6 — Construir a Matriz de Rastreabilidade
Crie a matriz completa: Requisito → Critérios → Testes → Código → Status.

### Passo 7 — Verificar Continuamente
Integre testes no CI/CD. A cadeia de prova é verificada em cada build. Falha no teste = requisito não atendido.

## Perguntas de Ativação

- "Para cada requisito, temos um teste que prova que funciona?"
- "Se esse teste falhar, qual requisito de negócio está comprometido?"
- "Há requisitos que 'todo mundo sabe que funcionam' mas ninguém nunca testou?"
- "Se um auditor perguntar 'como vocês garantem que X funciona?', temos uma resposta concreta?"
- "Quando um requisito muda, sabemos quais testes precisam ser atualizados?"
- "Nosso CI verifica todos os requisitos ou apenas o que os devs cobriram?"

## Output Esperado

| Requisito | Critério de Aceite | Caso de Teste | Tipo | Código | Status |
|---|---|---|---|---|---|
| REQ-001: Usuário cria conta com email | AC-001-01: Email válido aceito | TC-001-01-a: Criar com email@valid.com | Automatizado | UserService.create() | Passando |
| | AC-001-02: Email inválido rejeitado | TC-001-02-a: Criar com "invalido" | Automatizado | UserValidator.email() | Passando |
| | AC-001-03: Email duplicado rejeitado | TC-001-03-a: Criar com email existente | Automatizado | UserService.create() | Passando |
| REQ-002: Dados criptografados em repouso | AC-002-01: Coluna de CPF criptografada | TC-002-01-a: Verificar coluna no DB | Automatizado | encryption.middleware | Passando |
| | AC-002-02: Chave gerenciada por KMS | TC-002-02-a: Verificar config de KMS | Manual | infra/kms.tf | Pendente |
| REQ-003: Tempo de resposta < 200ms | AC-003-01: p95 abaixo de 200ms | TC-003-01-a: Load test com 1000 req/s | Periódico | — | Último: Passando |

**Cobertura**: 15 de 18 requisitos com cadeia completa (83%). 3 gaps identificados e priorizados.

## Armadilhas Comuns

1. **Cadeia incompleta**: Ter requisitos e ter testes, mas sem conexão entre eles. Se um teste falha, ninguém sabe qual requisito foi afetado.
2. **Documentação estática**: Cadeia de prova em documento que ninguém atualiza. Testes automatizados são a prova viva.
3. **Apenas happy path**: A cadeia prova que funciona quando tudo dá certo mas não quando as coisas dão errado.
4. **Cobertura como meta**: 100% de cobertura com testes superficiais dá falsa segurança. Qualidade dos testes importa.
5. **Não atualizar a cadeia**: Requisito mudou, código mudou, mas a matriz de rastreabilidade ficou a mesma.
6. **Testes que sempre passam**: Testes mal escritos que nunca falham não provam nada. Um bom teste deve ser capaz de falhar.
