# Standard para Handoff

## Propósito

Definir o processo e os requisitos de qualidade para transferência de projetos preparados pelo Pre-Programming Squad para squads de implementação. O handoff é o momento mais crítico do processo — uma transferência bem feita acelera a implementação; uma mal feita causa retrabalho e frustração.

## Escopo

Todo projeto que completa a pipeline do Pre-Programming Squad e é entregue a um squad de implementação.

## Definições

| Termo | Definição |
|---|---|
| Handoff | Transferência formal de responsabilidade e contexto de um squad para outro |
| Pacote de handoff | Conjunto de todos os artefatos, decisões e informações necessárias para implementação |
| Período de suporte | Janela após o handoff em que o squad de origem permanece disponível para dúvidas |
| Aceite | Confirmação formal pelo squad receptor de que o pacote é suficiente para iniciar |

## Processo

### 1. Preparação do Pacote (Antes do Handoff)

O membro responsável pelo projeto compila:

**Artefatos obrigatórios:**
- Documento de escopo com critérios de aceitação
- Decisões técnicas registradas (ADRs)
- Contratos de API (OpenAPI spec ou equivalente)
- Modelo de dados (ERD ou DDL)
- Cenários de teste documentados
- Estimativa de esforço com decomposição
- Revisão de riscos com mitigações
- Sequência de implementação recomendada

**Artefatos condicionais (quando aplicável):**
- Diagrama de arquitetura (C4 ou equivalente)
- Pre-check de segurança
- Pre-check de performance
- Análise de legado
- Análise build vs. buy
- Protótipo ou resultado de spike

**Metadata:**
- Contato no Pre-Programming Squad para dúvidas
- Canal de comunicação preferido
- Período de disponibilidade para suporte

### 2. Auto-avaliação

Antes de agendar o handoff, verificar:

- [ ] Todos os artefatos obrigatórios estão completos e acessíveis
- [ ] Nenhum artefato contém "TBD" sem owner e prazo
- [ ] Links e referências estão funcionais
- [ ] Documento revisado por par dentro do Pre-Programming Squad
- [ ] Readiness assessment indica "Ready" ou "Conditionally Ready"

### 3. Sessão de Handoff

**Formato:** Reunião de 60-90 minutos (presencial ou videoconferência)

**Participantes obrigatórios:**
- Membro do Pre-Programming Squad responsável pelo projeto
- Tech Lead do squad receptor
- Pelo menos 1 engenheiro do squad receptor que vai implementar

**Agenda:**
1. Contexto e objetivo do projeto (10 min)
2. Walkthrough do escopo e decisões técnicas (20 min)
3. Riscos e armadilhas conhecidas (10 min)
4. Sequência de implementação recomendada (10 min)
5. Perguntas e esclarecimentos (20-30 min)
6. Alinhamento de próximos passos e suporte (10 min)

**Regras:**
- Não é apresentação unilateral — é sessão colaborativa
- Dúvidas são encorajadas e registradas
- Se surgir gap significativo, o handoff pode ser pausado para completar

### 4. Aceite Formal

O Tech Lead do squad receptor confirma por escrito (mensagem, email ou checkbox no doc):

- [ ] Pacote de handoff revisado e compreendido
- [ ] Artefatos acessíveis ao time
- [ ] Dúvidas iniciais esclarecidas
- [ ] Capacidade para iniciar identificada (quando e quem)
- [ ] Canal de comunicação com squad de origem estabelecido

**Se o aceite for recusado:**
- Lista de gaps documentada
- Prazo para endereçar gaps definido
- Nova sessão de handoff agendada

### 5. Período de Suporte Pós-Handoff

- **Duração:** 2 semanas a partir do aceite
- **Formato:** Assíncrono via canal dedicado + 1 slot semanal de 30min para dúvidas
- **Escopo do suporte:** Esclarecimentos sobre artefatos entregues, contexto de decisões, ajustes menores
- **Fora do escopo:** Implementação, debugging, decisões de implementação

### 6. Feedback

2 semanas após o início da implementação, coletar feedback estruturado:

| Pergunta | Escala |
|---|---|
| O pacote de handoff estava completo? | 1-10 |
| As decisões técnicas estavam bem fundamentadas? | 1-10 |
| Os riscos identificados eram relevantes? | 1-10 |
| A estimativa de esforço estava calibrada? | 1-10 |
| Quantas perguntas de esclarecimento foram necessárias? | Número |
| O que faltou no pacote? | Texto livre |
| O que estava a mais (desnecessário)? | Texto livre |

## Critérios de Qualidade

- 100% dos handoffs têm aceite formal registrado
- < 10% dos handoffs são recusados na primeira tentativa
- < 5 perguntas de esclarecimento por handoff (média)
- Satisfação do squad receptor ≥ 8/10 (média)
- Período de suporte respeitado (respostas em até 24h úteis)
- Feedback coletado em 100% dos handoffs

## Responsáveis

| Papel | Responsabilidade |
|---|---|
| Membro do squad | Preparar pacote, conduzir sessão, fornecer suporte pós-handoff |
| Par revisor | Revisar pacote antes do handoff |
| Tech Lead (Pre-Prog) | Garantir qualidade do pacote, mediar se houver rejeição |
| Tech Lead (receptor) | Participar da sessão, confirmar aceite, fornecer feedback |
| EM | Garantir que capacidade está alocada no squad receptor |

## Referências

- Definição de Readiness: `docs/readiness-definition.md`
- What Good Looks Like: `docs/what-good-looks-like.md`
- Estilo de Handoff: `voice/channels/handoff-style.md`
- Tom de Handoff: `voice/tone-profiles/implementation-handoff.md`
