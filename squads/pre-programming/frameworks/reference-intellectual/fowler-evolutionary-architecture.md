# Fowler: Arquitetura Evolutiva

## Título e Propósito

Framework baseado no trabalho de **Martin Fowler** (e Neal Ford/Rebecca Parsons em *Building Evolutionary Architectures*). A tese central: **arquitetura não deve ser definida de uma vez e congelada — deve evoluir incrementalmente** guiada por fitness functions que protegem qualidades importantes. O propósito é projetar sistemas que podem mudar sem colapsar.

## Quando Usar

- Em decisões arquiteturais onde há incerteza sobre requisitos futuros
- Ao definir como a arquitetura vai evoluir de v1 para vN
- Quando a equipe debate entre "projetar para o futuro" e "fazer o mínimo agora"
- Na definição de guardrails arquiteturais automatizados
- Em revisões de arquitetura para avaliar capacidade de evolução

## Conceitos-Chave

1. **Arquitetura Evolutiva**: Arquitetura que suporta mudança incremental como princípio, com múltiplas dimensões protegidas por fitness functions.
2. **Fitness Function**: Teste automatizado que verifica se uma qualidade arquitetural está sendo mantida. Exemplo: "nenhuma dependência cíclica entre módulos".
3. **Decisões Reversíveis**: Preferir decisões que podem ser mudadas depois (Tipo 2) para preservar opções.
4. **Last Responsible Moment**: Adiar decisões irreversíveis até ter informação suficiente, mas não depois disso.
5. **Sacrificial Architecture**: Projetar a v1 sabendo que será substituída, mas capturando aprendizados que informam a v2.

## Processo / Passos

### Passo 1 — Identificar Qualidades Arquiteturais Importantes
O que precisa ser preservado ao longo do tempo? Performance, modularidade, segurança, testabilidade?

### Passo 2 — Definir Fitness Functions
Para cada qualidade, crie um teste automatizado: "Latência p95 < 200ms", "Nenhum módulo com mais de 5 dependências diretas", "Cobertura de testes > 80%".

### Passo 3 — Projetar para Incrementalidade
A arquitetura deve permitir mudanças graduais: adicionar features, trocar componentes, escalar partes do sistema — tudo sem redesign total.

### Passo 4 — Identificar e Adiar Decisões
Quais decisões podem esperar? Quais devem ser tomadas agora? Para as adiáveis, defina o momento certo (last responsible moment).

### Passo 5 — Automatizar Fitness Functions no CI
Fitness functions rodam no pipeline. Violações bloqueiam merge/deploy. Isso protege a arquitetura de degradação gradual.

## Perguntas de Ativação

- "Se precisarmos mudar essa parte da arquitetura em 6 meses, quanto vai custar?"
- "Quais qualidades arquiteturais são mais importantes e como as protegemos automaticamente?"
- "Estamos tomando uma decisão irreversível agora que poderíamos adiar?"
- "Temos fitness functions que detectam degradação arquitetural?"
- "A arquitetura permite evolução incremental ou exige big bang para mudar?"

## Output Esperado

Lista de qualidades arquiteturais com fitness functions definidas, decisões classificadas como reversíveis/irreversíveis, estratégia de evolução documentada.

## Armadilhas Comuns

1. **Arquitetura congelada**: Definir na fase de design e nunca revisitar. O contexto muda, a arquitetura deve acompanhar.
2. **Fitness functions ausentes**: Sem testes automatizados, degradação arquitetural é invisível até ser catastrófica.
3. **Over-planning para o futuro**: Projetar para cenários que talvez nunca aconteçam. Evolução incremental supera planejamento central.
4. **Decisões irreversíveis prematuras**: Tomar decisões de lock-in sem necessidade urgente.
5. **Sacrificial architecture sem aprendizado**: Construir v1 descartável sem capturar os aprendizados que justificam descartá-la.
