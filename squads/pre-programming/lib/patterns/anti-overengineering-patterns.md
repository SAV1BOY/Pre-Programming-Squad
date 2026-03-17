# Padrões Anti-Overengineering

## Nome do Padrão
Padrões para Evitar Engenharia Excessiva

## Problema que Resolve
Equipes técnicas frequentemente projetam soluções mais complexas do que o necessário, adicionando abstrações, camadas e funcionalidades que não são requisitadas. Isso resulta em: aumento de prazo e custo, código difícil de manter, onboarding lento de novos membros e fragilidade do sistema.

## Solução

### 1. Regra dos Três Usos (Rule of Three)
Não abstrair ou generalizar até que o mesmo padrão apareça em pelo menos três contextos diferentes. Até lá, manter a implementação concreta e específica.

**Aplicação prática:**
- Na primeira ocorrência: implementar direto
- Na segunda ocorrência: anotar a duplicação, mas não abstrair
- Na terceira ocorrência: refatorar para uma abstração comum
- Documentar a decisão de esperar no ADR

### 2. YAGNI Estruturado (You Aren't Gonna Need It)
Não implementar funcionalidades, extensões ou abstrações que não são necessárias agora. Complementar com documentação de decisões adiadas.

**Aplicação prática:**
- Para cada decisão de design, perguntar: "Precisamos disso AGORA?"
- Manter um backlog de "itens adiados por YAGNI"
- Revisitar o backlog a cada sprint/iteração
- Documentar o custo estimado de adicionar depois

### 3. Protótipo Descartável (Spike)
Antes de investir em uma solução complexa, criar um protótipo rápido e descartável para validar premissas técnicas.

**Aplicação prática:**
- Limitar spikes a 1-2 dias de trabalho
- Definir perguntas específicas que o spike deve responder
- Descartar o código do spike (não reutilizar em produção)
- Documentar aprendizados na nota de arquitetura

### 4. Arquitetura Evolutiva
Projetar para evolução, não para todas as possibilidades futuras. Criar pontos de extensão apenas onde a mudança é provável e evidenciada.

**Aplicação prática:**
- Identificar os 2-3 eixos de mudança mais prováveis
- Criar flexibilidade apenas nesses eixos
- Usar interfaces simples nos pontos de extensão
- Aceitar que refatoração futura é mais barata que abstração prematura

### 5. Complexidade Justificada
Cada camada de abstração ou padrão de design deve ter uma justificativa documentada e mensurável.

**Aplicação prática:**
- Para cada padrão aplicado, responder: "Qual problema concreto resolve?"
- Se a justificativa for "pode ser útil no futuro", não aplicar
- Medir o custo cognitivo da complexidade adicionada
- Preferir composição sobre herança, funções sobre classes

## Quando Usar

- Em todo início de projeto, como princípio orientador
- Quando a equipe tem tendência a criar abstrações prematuras
- Em projetos com prazo restrito
- Quando o domínio ainda não é bem compreendido
- Em MVPs e primeiras versões de produtos

## Quando NÃO Usar

- Em sistemas com requisitos regulatórios rígidos que exigem estruturas formais
- Quando há evidência concreta de que a extensibilidade será necessária em breve
- Em plataformas/frameworks onde abstração é parte fundamental do produto
- Quando a equipe já tem um padrão maduro e bem compreendido

## Exemplos

### Exemplo 1: API Simples vs. Over-engineered
```
Over-engineered (evitar no início):
  Controller -> Service -> Repository -> DAO -> Entity -> DTO -> Mapper
  + Factory + Strategy + Observer + AbstractFactory
  Total: 10+ classes para um CRUD simples

Abordagem anti-overengineering:
  Controller -> Service -> Repository
  Total: 3 classes, lógica clara e direta
  Adicionar camadas QUANDO a complexidade justificar
```

### Exemplo 2: YAGNI em Configuração
```
Tentação: "Vamos criar um sistema de configuração dinâmica
com hot-reload, versionamento e interface admin"

Realidade: O sistema tem 5 configurações que mudam 1x por trimestre

Decisão YAGNI: Arquivo de configuração simples (YAML/ENV)
Custo de migrar depois: 2-3 dias (se necessário)
Economia agora: 2-3 semanas de desenvolvimento
```

### Exemplo 3: Regra dos Três
```
Sprint 1: Notificação por e-mail
  -> Implementar envio direto de e-mail (concreto)

Sprint 3: Notificação por SMS
  -> Duplicação notada, mas NÃO abstrair ainda

Sprint 5: Notificação por push
  -> Terceira ocorrência: criar abstração NotificationService
  -> Interface com implementações: EmailNotifier, SmsNotifier, PushNotifier
```
