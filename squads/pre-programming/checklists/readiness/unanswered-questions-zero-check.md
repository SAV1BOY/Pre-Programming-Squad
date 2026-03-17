# Checklist: Verificação de Zero Perguntas sem Resposta

## Propósito
Garantir que não existem ambiguidades críticas abertas que forçariam o time de implementação a adivinhar ou tomar decisões que não são deles.

## Quando Usar
- Como verificação final antes do go da implementação
- Quando o ambiguity kill list ainda tem itens abertos
- Quando o time de dev reporta incertezas

---

## Checklist

### Inventário de Perguntas
- [ ] Lista consolidada de todas as perguntas levantadas durante pré-programming existe
- [ ] Cada pergunta tem status atualizado (respondida, pendente, irrelevante)
- [ ] Perguntas pendentes estão classificadas por criticidade
- [ ] Nenhuma pergunta bloqueante está sem resposta
- [ ] Perguntas não-bloqueantes pendentes têm plano e prazo para resolução

### Tipos de Ambiguidade Verificados
- [ ] Requisitos funcionais não têm ambiguidade crítica
- [ ] Requisitos não-funcionais estão quantificados (não vagos)
- [ ] Regras de negócio estão claras e sem contradição
- [ ] Escopo está definido sem áreas cinza bloqueantes
- [ ] Contratos de API estão completos sem lacunas

### Premissas Explícitas
- [ ] Premissas assumidas na ausência de respostas estão documentadas
- [ ] Cada premissa tem owner que pode validá-la
- [ ] Risco de cada premissa se provar falsa está avaliado
- [ ] Premissas com alto risco foram priorizadas para validação
- [ ] Time de dev sabe quais são premissas vs fatos confirmados

### Decisões Pendentes
- [ ] Nenhuma decisão arquitetural crítica está pendente
- [ ] Nenhuma decisão de negócio bloqueante está pendente
- [ ] Decisões adiadas conscientemente têm prazo e owner
- [ ] Impacto de decisões adiadas na implementação está avaliado
- [ ] Decisões que o time de dev pode tomar estão delegadas com autoridade

### Processo de Resolução
- [ ] Canal para resolver novas dúvidas durante implementação está definido
- [ ] SLA de resposta para dúvidas bloqueantes está acordado
- [ ] Escalação para dúvidas que não são respondidas no SLA está definida
- [ ] Pessoa de contato para cada área de conhecimento está identificada
- [ ] Processo não bloqueia o dev (pode continuar em outras tarefas enquanto aguarda)

---

## Critérios de Aprovação
- **Mínimo**: Zero perguntas bloqueantes abertas
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Qualquer pergunta bloqueante sem resposta

## Sinais de Alerta (Red Flags)
- "Depois a gente descobre" para questão estrutural
- Lista de perguntas que ninguém revisa há semanas
- Premissas de alto risco aceitas sem plano de validação
- Time de dev descobre ambiguidades no primeiro dia de implementação
- Nenhum canal definido para resolver dúvidas durante implementação

## Agente Responsável
**Agente de Final Review & Handoff** — responsável por garantir que ambiguidades críticas estão resolvidas antes do go.
