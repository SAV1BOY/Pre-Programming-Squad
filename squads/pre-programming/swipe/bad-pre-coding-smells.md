# Maus Cheiros de Pré-Codificação — Exemplos Anotados

## Introdução

Assim como code smells indicam problemas no código, "pré-coding smells" indicam problemas no planejamento que vão se manifestar como bugs, atrasos e retrabalho durante o desenvolvimento. Identificar esses sinais durante a pré-programação é muito mais barato do que descobri-los depois. Este documento cataloga os maus cheiros mais comuns e como corrigi-los antes que causem dano.

---

## Smell 1 — "Todo mundo entendeu, né?"

### O Sintoma

Requisitos discutidos verbalmente em reunião. Ninguém anotou. Ninguém fez perguntas. "Todo mundo entendeu." Duas semanas depois, cada dev implementou algo diferente.

### Por que é perigoso

- Consenso silencioso não é consenso — é ambiguidade não confrontada
- Memória humana é seletiva — cada pessoa lembra de partes diferentes da reunião
- Sem registro escrito, não há como resolver conflitos de interpretação

### Correção

- Toda decisão deve ser documentada por escrito em até 24h
- "Se não está escrito, não foi decidido"
- Usar técnica de "repita o que entendeu" — cada dev explica o que vai implementar antes de começar

---

## Smell 2 — "A gente decide na hora"

### O Sintoma

Decisões técnicas importantes sendo adiadas para "quando chegarmos lá". "Qual banco de dados usar?" — "Decidimos quando for implementar." "Como tratar autenticação?" — "Vamos ver."

### Por que é perigoso

- Decisões adiadas acumulam e criam dependências não resolvidas
- Decisões tomadas sob pressão de prazo são piores que decisões tomadas com calma
- Código construído sem decisão de arquitetura terá que ser refatorado quando a decisão for tomada

### Correção

- Listar todas as decisões técnicas pendentes e priorizá-las
- Decisões de arquitetura (banco, comunicação, autenticação) devem ser tomadas na pré-programação
- Decisões de implementação podem ser adiadas, decisões estruturais não

---

## Smell 3 — "É só um CRUD"

### O Sintoma

Feature descrita como "simples CRUD" que na verdade envolve: validações complexas, regras de negócio condicionais, permissões granulares, auditoria, soft delete, histórico de alterações, busca full-text e integração com 3 serviços externos.

### Por que é perigoso

- Subestimação sistemática — "CRUD simples" é o eufemismo mais caro da engenharia de software
- Cada "detalhe" adicionado multiplica a complexidade
- O dev descobre a complexidade real durante a implementação, quando o prazo já está comprometido

### Correção

- Proibir a expressão "simples CRUD" no squad
- Para cada "CRUD", listar: validações, permissões, auditoria, soft delete, histórico, busca, integrações, cache, concorrência
- Se a lista tem mais de 3 itens além do CRUD básico, não é "simples"

---

## Smell 4 — "O Fulano sabe como funciona"

### O Sintoma

Conhecimento crítico concentrado em uma pessoa. "O João sabe como o sistema de billing funciona." "A Maria sabe por que aquele campo está naquele formato."

### Por que é perigoso

- Bus factor = 1. Se a pessoa estiver de férias, doente ou sair da empresa, o conhecimento vai embora
- Gargalo de decisão — time fica bloqueado esperando a pessoa estar disponível
- Conhecimento não documentado é conhecimento volátil

### Correção

- Identificar todos os "pontos de conhecimento único" no mapa de dependências
- Agendar sessões de knowledge transfer antes da codificação começar
- Documentar conhecimento tácito em notas de pesquisa de domínio

---

## Smell 5 — "Não precisa de design doc, é simples"

### O Sintoma

Feature classificada como "não precisa de documentação" que depois gera 15 threads no Slack com dúvidas, 3 reuniões para alinhar e 2 reescritas de código.

### Por que é perigoso

- O custo de escrever um design doc é horas. O custo de não escrever é semanas de retrabalho
- "Simples" é avaliação subjetiva que ignora complexidade de integração, edge cases e requisitos não-funcionais
- Sem design doc, não há revisão de arquitetura antes do código

### Correção

- Regra: se a feature leva mais de 3 dias para implementar, precisa de design doc
- Design doc pode ser curto (1-2 páginas) para features menores
- O ato de escrever força a pensar em cenários não óbvios

---

## Smell 6 — "Depois a gente testa"

### O Sintoma

Plano de testes inexistente ou tratado como fase separada "após o desenvolvimento". QA descobre bugs fundamentais que exigem refatoração significativa.

### Por que é perigoso

- Bugs descobertos em QA custam 10x mais que bugs prevenidos no design
- Sem plano de testes, desenvolvedores não consideram edge cases durante a implementação
- QA vira "encontrador de bugs" em vez de "validador de qualidade"

### Correção

- Plano de testes escrito antes do código, como parte do handoff
- Cenários de teste revisados pelo dev antes de implementar
- TDD ou test-first para cenários críticos

---

## Smell 7 — "Funciona no meu computador"

### O Sintoma

Nenhuma definição de ambiente de desenvolvimento padronizado. Cada dev com versão diferente de runtime, dependências e configurações. "Na minha máquina funciona" como resposta a bugs.

### Por que é perigoso

- Bugs de ambiente desperdiçam horas de debugging
- CI/CD que funciona diferente do local gera desconfiança nos testes
- Onboarding de novos membros leva dias em vez de horas

### Correção

- Definir ambiente com Docker, devcontainers ou Nix
- Documentar setup em 5 passos ou menos
- Validar que CI usa exatamente o mesmo ambiente que o dev local

---

## Resumo de Maus Cheiros

| Smell | Sinal de Alerta | Consequência |
|-------|-----------------|-------------|
| Consenso silencioso | Ninguém faz perguntas | Interpretações divergentes |
| Decisão adiada | "Vemos depois" | Refatoração obrigatória |
| "Só um CRUD" | Subestimação | Atraso e scope creep |
| Conhecimento concentrado | Bus factor = 1 | Bloqueios e perda de conhecimento |
| Sem design doc | "É simples" | Retrabalho e desalinhamento |
| Testes depois | QA como fase separada | Bugs caros e tardios |
| Ambiente inconsistente | "Funciona na minha máquina" | Bugs fantasmas e debugging desnecessário |
