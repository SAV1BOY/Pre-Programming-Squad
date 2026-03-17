# Carta do Squad — Pre-Programming Squad

## Propósito

Definir a missão, visão, valores e escopo de atuação do Pre-Programming Squad, estabelecendo o contrato social e organizacional que guia todas as atividades do squad.

## Escopo

Este documento se aplica a todos os membros do Pre-Programming Squad e a todos os stakeholders que interagem com o squad. É o documento fundacional que orienta todas as demais políticas e standards.

## Definições

| Termo | Definição |
|---|---|
| Pre-Programming | Fase que antecede a implementação de software, incluindo discovery, scoping, design, revisão e preparação de handoff |
| Implementation Readiness | Estado no qual um projeto tem toda a informação, decisões e artefatos necessários para que um time de desenvolvimento inicie a implementação com confiança |
| Squad | Unidade organizacional autônoma com missão, escopo e responsabilidades definidas |

## Missão

Garantir que todo projeto de software chegue ao time de implementação com clareza, completude e confiança. Eliminamos ambiguidade, antecipamos riscos e transformamos requisitos de negócio em pacotes de trabalho acionáveis e bem fundamentados.

**Em uma frase:** Nenhum time de desenvolvimento deve começar a codar sem saber exatamente o que construir, por que construir e como validar que construiu certo.

## Visão

Ser a referência organizacional em qualidade de preparação técnica, onde:

- Zero projetos iniciam implementação sem readiness validada
- O retrabalho por requisitos incompletos é eliminado
- As decisões técnicas são documentadas, rastreáveis e contestáveis
- O tempo entre "ideia aprovada" e "primeiro commit" é mínimo e previsível
- Os times de implementação confiam nos pacotes de trabalho que recebem

## Valores

### 1. Clareza sobre Velocidade
Preferimos investir tempo em preparação completa a entregar artefatos rápidos e ambíguos. Cada dia investido em preparação economiza semanas de retrabalho.

### 2. Evidência sobre Opinião
Toda recomendação é fundamentada em dados, métricas, benchmarks ou experiência documentada. Opiniões são válidas como hipóteses, mas precisam de validação.

### 3. Honestidade sobre Conforto
Comunicamos riscos, incertezas e limitações com transparência, mesmo quando a mensagem é inconveniente. Problemas identificados cedo são baratos; problemas descobertos em produção são caros.

### 4. Colaboração sobre Território
Trabalhamos com todos os squads, não para eles. O sucesso do Pre-Programming Squad é medido pelo sucesso dos times que recebem nossos entregáveis.

### 5. Melhoria Contínua sobre Perfeição
Cada ciclo de trabalho gera aprendizados que refinam nossos processos. Preferimos processos bons que melhoram a processos perfeitos que não existem.

## Escopo de Atuação

### O que fazemos
- Intake e triagem de projetos novos
- Discovery técnica e de negócio
- Definição e validação de escopo
- Revisão de arquitetura
- Design de estratégia de testes
- Revisão de riscos técnicos e de negócio
- Pre-checks de segurança e performance
- Análise build vs. buy
- Avaliação de readiness de legado
- Estimativa de esforço
- Preparação de pacotes de handoff
- Decisão de go/no-go
- Retrospectivas de processo (RalphLoop)

### O que não fazemos
- Implementação de código de produção
- Operação de sistemas em produção
- Gestão de produto (priorizção de backlog, roadmap)
- Suporte a incidentes (exceto análise pré-incidente preventiva)
- Testes de aceitação em software implementado

### Fronteiras com Outros Squads

| Squad | Interface |
|---|---|
| Squads de implementação | Recebem nossos pacotes de handoff; fornecem feedback de qualidade |
| Produto | Fornecem requisitos de negócio; recebem análise de viabilidade |
| Arquitetura | Colaboração em decisões cross-system; revisão mútua de ADRs |
| Segurança | Recebem nossos pre-checks; validam e complementam |
| SRE/Infra | Fornecem constraints operacionais; recebem requisitos de infra |

## Critérios de Qualidade

- Toda entrega do squad segue os standards documentados em `/docs/`
- Entregáveis são auto-avaliados antes da entrega usando "What Good Looks Like"
- Feedback dos squads receptores é coletado sistematicamente
- Métricas de eficácia são revisadas mensalmente

## Responsáveis

| Papel | Responsabilidade |
|---|---|
| Tech Lead do Squad | Guardar a missão, qualidade dos entregáveis, desenvolvimento do time |
| Membros do Squad | Executar processos com rigor, propor melhorias, manter standards |
| Engineering Manager | Suporte organizacional, remoção de bloqueios, alocação de recursos |
| Stakeholders | Fornecer inputs completos, respeitar processos de intake, dar feedback |

## Referências

- Modelo Operacional: `docs/operating-model.md`
- Definição de Readiness: `docs/readiness-definition.md`
- What Good Looks Like: `docs/what-good-looks-like.md`
- Todos os standards operacionais: `docs/*.md`
