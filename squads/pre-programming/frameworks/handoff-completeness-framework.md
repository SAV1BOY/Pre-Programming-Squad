# Handoff Completeness Framework

## Título e Propósito

O **Handoff Completeness Framework** é um sistema para garantir que a transição entre fases (pré-programação → implementação, implementação → operações, equipe A → equipe B) transfira todo o conhecimento e contexto necessários. O propósito é eliminar a perda de informação nos handoffs — o momento onde mais conhecimento se perde em projetos de software.

## Quando Usar

- Na transição de pré-programação/design para implementação
- Quando um projeto muda de equipe ou de responsável
- Na entrega de projeto para operações/sustentação
- Quando alguém sai da equipe e precisa transferir conhecimento
- Em qualquer transição onde o próximo precisa continuar de onde o anterior parou

## Conceitos-Chave

1. **Conhecimento Explícito**: O que está documentado — specs, diagramas, ADRs, tickets. Transferível por leitura.
2. **Conhecimento Tácito**: O que está na cabeça das pessoas — decisões não documentadas, contexto, nuances. Transferível apenas por conversa.
3. **Completude do Handoff**: Percentual do conhecimento necessário que foi efetivamente transferido. 100% é impossível, mas 90%+ é o alvo.
4. **Perguntas sem Resposta**: Lista explícita de questões que o próximo time precisa saber que existem, mesmo que não tenham resposta ainda.
5. **Contexto de Decisão**: Não apenas qual decisão foi tomada, mas por quê, quais alternativas foram rejeitadas e sob que condições revisitar.

## Processo / Passos

### Passo 1 — Mapear o que Precisa Ser Transferido
Liste todas as categorias de conhecimento relevantes: requisitos, arquitetura, decisões, riscos, dependências, contatos, dívidas técnicas, perguntas abertas.

### Passo 2 — Avaliar Estado de Cada Categoria
Para cada categoria, avalie: **Completo e documentado**, **Parcial**, **Apenas tácito (na cabeça de alguém)**, **Não existe**.

### Passo 3 — Documentar o Conhecimento Tácito
Antes do handoff, reserve tempo para documentar o que está apenas na cabeça das pessoas. Foque em: decisões não documentadas, contexto político, armadilhas conhecidas.

### Passo 4 — Criar o Pacote de Handoff
Compile em um lugar centralizado: specs, diagramas, ADRs, lista de riscos, contatos, credenciais, runbooks, perguntas abertas.

### Passo 5 — Sessão de Transferência
Agende sessão presencial ou síncrona para walkthrough do pacote. O receptor faz perguntas. O objetivo é transferir conhecimento tácito.

### Passo 6 — Período de Sobreposição
Defina período onde ambas as partes estão disponíveis para perguntas. Handoff não é evento pontual — é processo.

### Passo 7 — Verificar Completude
Após o handoff, o receptor avalia: "Consigo continuar o trabalho sem depender do anterior?" Se não, identifique as lacunas.

## Perguntas de Ativação

- "Se a equipe anterior desaparecesse amanhã, o que nos faltaria para continuar?"
- "Quais decisões foram tomadas que não estão documentadas em lugar nenhum?"
- "Quais são as armadilhas que alguém novo neste projeto precisa saber?"
- "Quem são os contatos-chave e quais são suas expectativas?"
- "Há perguntas abertas que ninguém respondeu ainda?"
- "O que deu errado em handoffs anteriores que devemos evitar?"

## Output Esperado

| Categoria | Estado | Documentação | Conhecimento Tácito | Ação Necessária |
|---|---|---|---|---|
| Requisitos | Completo | Spec doc v3.2 | Nuances discutidas com PO | Documentar notas da conversa |
| Arquitetura | Completo | ADR-001 a ADR-007, diagrama C4 | Razão de rejeitar serverless | Incluir em ADR |
| Riscos | Parcial | Lista de riscos no Jira | Preocupação do CTO com performance | Documentar e comunicar |
| Dependências | Completo | Matriz de dependências | Contato do time de infra é o João | Adicionar à doc |
| Dívida técnica | Apenas tácito | Nenhuma doc | "O módulo de relatórios é frágil" | Criar lista de dívidas |
| Perguntas abertas | Não existe | — | Várias decisões pendentes | Criar lista explícita |

**Score de Completude**: 65% — precisa subir para 90%+ antes do handoff formal.

## Armadilhas Comuns

1. **Handoff como evento**: Tratar como reunião de 1 hora em vez de processo com sobreposição. Conhecimento tácito não se transfere em uma reunião.
2. **Documentação como substituto de conversa**: Docs são necessários mas insuficientes. O conhecimento tácito precisa de conversa.
3. **"Está tudo no Jira"**: Tickets capturam o quê, não o porquê. Contexto de decisão raramente está em tickets.
4. **Não documentar perguntas abertas**: O que o receptor não sabe que não sabe é o mais perigoso.
5. **Pressão de prazo**: "Não temos tempo para handoff adequado" resulta em semanas de descoberta que custariam horas de transferência.
6. **Handoff de uma via**: Apenas a equipe anterior fala. O receptor precisa fazer perguntas e validar entendimento.
