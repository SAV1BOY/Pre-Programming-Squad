# Standard para Intake de Projetos

## Propósito

Definir o processo padronizado pelo qual novos projetos entram na pipeline do Pre-Programming Squad. O intake garante que todo projeto recebido tenha informação mínima para triagem e priorização, evitando trabalho em projetos mal definidos ou sem patrocinador.

## Escopo

Todo projeto que solicita preparação do Pre-Programming Squad, independentemente de origem (produto, engenharia, liderança, compliance).

## Definições

| Termo | Definição |
|---|---|
| Intake | Processo de recebimento e registro inicial de um novo projeto na pipeline |
| Solicitante | Pessoa ou squad que submete o pedido de preparação |
| Triagem | Avaliação inicial que classifica o projeto por tamanho, prioridade e viabilidade |
| Patrocinador | Pessoa com autoridade para priorizar o projeto e alocar recursos para implementação |

## Processo

### 1. Submissão

O solicitante preenche o formulário de intake com as seguintes informações obrigatórias:

**Informações Obrigatórias:**
- Nome do projeto (descritivo, não genérico)
- Solicitante (nome, papel, squad)
- Patrocinador (pessoa com poder de decisão sobre prioridade)
- Problema de negócio (o que dói e para quem)
- Resultado esperado (o que muda quando o projeto for concluído)
- Urgência (data limite e justificativa, se houver)
- Restrições conhecidas (tecnologia, orçamento, regulatório, dependências)

**Informações Opcionais (mas valorizadas):**
- Dados quantitativos sobre o problema (volume, custo, frequência)
- Soluções já tentadas e por que falharam
- Stakeholders adicionais que devem ser consultados
- Documentos existentes (PRD, RFC, pesquisas)

### 2. Triagem (SLA: 24h úteis)

O membro de plantão do squad avalia o intake e classifica:

**Prioridade:**
- P0 — Bloqueio de receita, segurança ou compliance com deadline
- P1 — Alto impacto em negócio ou usuários, prazo definido
- P2 — Melhoria importante, sem urgência imediata
- P3 — Nice-to-have, fazer quando houver capacidade

**Tamanho:** P, M, G, XG (conforme modelo operacional)

**Resultado da triagem:**
- **Aceito** — entra na pipeline com prioridade e tamanho definidos
- **Devolvido** — informações insuficientes; lista de gaps enviada ao solicitante
- **Redirecionado** — não é escopo do squad; encaminhado para squad/área correta
- **Recusado** — justificativa documentada (ex: escopo muito pequeno para o squad, já resolvido, inviável)

### 3. Comunicação

- Solicitante recebe confirmação de recebimento em até 4h úteis
- Resultado da triagem comunicado em até 24h úteis
- Se aceito: previsão de início e membro responsável informados em até 48h úteis

### 4. Registro

Todo intake é registrado no tracker do squad com:
- Data de submissão
- Data de triagem
- Resultado da triagem
- Prioridade e tamanho
- Membro responsável (se aceito)
- Data prevista de início

## Critérios de Qualidade

- 100% dos intakes recebem resposta em até 24h úteis
- < 15% dos intakes devolvidos por informação insuficiente (indica formulário eficaz)
- Todos os intakes recusados têm justificativa documentada
- Tempo médio de triagem a início < 3 dias úteis para P0/P1

## Responsáveis

| Papel | Responsabilidade |
|---|---|
| Membro de plantão | Receber intake, executar triagem, comunicar resultado |
| Tech Lead | Priorizar entre intakes concorrentes, resolver conflitos de prioridade |
| Solicitante | Preencher formulário com completude, fornecer informações adicionais quando solicitado |
| Patrocinador | Confirmar prioridade e garantir disponibilidade de stakeholders |

## Referências

- Modelo Operacional: `docs/operating-model.md`
- Standard de Discovery: `docs/discovery-standard.md`
- Formulário de Intake: [link do formulário no sistema de tracking]
