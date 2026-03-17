# Checklist: Verificação de Arquitetura da Primeira Versão

## Propósito
Garantir que a arquitetura da v1 é adequada para entregar o MVP sem overengineering, mas sem criar dead-ends que impeçam evolução futura.

## Quando Usar
- Ao finalizar o design da primeira versão
- Quando há tensão entre "fazer direito" e "entregar rápido"
- Antes de aprovar a arquitetura para implementação

---

## Checklist

### Adequação para v1
- [ ] A arquitetura suporta todos os requisitos do MVP
- [ ] A complexidade é proporcional ao escopo da v1 (não do produto final)
- [ ] Decisões foram tomadas para o presente com informação real, não para futuro especulativo
- [ ] O time consegue implementar esta arquitetura com as skills atuais
- [ ] O prazo da v1 é viável com esta arquitetura

### Sem Overengineering
- [ ] Não há microsserviços onde um monolito modular bastaria
- [ ] Não há abstração prematura de componentes que podem não mudar
- [ ] Não há infra dimensionada para 100x a carga esperada na v1
- [ ] Patterns de design são usados onde resolvem problema real, não por dogma
- [ ] Features de "plataforma" são limitadas ao mínimo necessário

### Caminho de Evolução
- [ ] A arquitetura da v1 pode evoluir para v2 sem reescrever do zero
- [ ] Pontos de evolução mais prováveis estão identificados
- [ ] Fronteiras entre módulos permitem extrair serviços depois se necessário
- [ ] Schema de dados é extensível (pode adicionar campos, tabelas)
- [ ] Contratos de API suportam versionamento para evolução

### Decisões da v1
- [ ] Decisões simplificadoras da v1 estão documentadas como dívida consciente
- [ ] Cada simplificação tem estimativa de custo para "resolver depois"
- [ ] Nenhuma simplificação cria risco de segurança ou perda de dados
- [ ] Simplificações não afetam a experiência core do usuário
- [ ] Existe priorização de quais dívidas pagar primeiro na v2

### Validação
- [ ] A arquitetura foi revisada por pelo menos um desenvolvedor sênior
- [ ] Os fluxos críticos foram trace-ados na arquitetura (de ponta a ponta)
- [ ] Pontos de maior risco técnico têm spike/PoC planejado
- [ ] A arquitetura foi validada com cenários de falha (e se X cair?)
- [ ] O time de implementação entende e concorda com a arquitetura

---

## Critérios de Aprovação
- **Mínimo**: Adequação para v1 e Sem Overengineering completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Arquitetura que não suporta o MVP ou que cria dead-end para evolução

## Sinais de Alerta (Red Flags)
- Arquitetura da v1 idêntica à visão de 3 anos (prematura)
- v1 com 15 serviços para 3 fluxos de negócio
- "Vamos usar monorepo com 5 packages para 2 telas"
- Nenhuma dívida técnica aceita (perfeccionismo que impede entrega)
- Arquitetura que nenhum dev do time consegue implementar sem treinamento extenso

## Agente Responsável
**Agente de Solution Architecture** — responsável por garantir arquitetura pragmática para a primeira versão.
