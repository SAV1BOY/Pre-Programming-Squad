# Checklist: Lista de Eliminação de Ambiguidades

## Propósito
Registrar e resolver todas as perguntas em aberto, termos vagos e decisões pendentes que podem gerar retrabalho ou entendimento errado durante a implementação.

## Quando Usar
- Continuamente durante toda a fase de discovery e pré-programming
- Antes de cada gate/revisão de qualidade
- Quando alguém diz "isso depende" ou "a gente vê depois"

---

## Checklist

### Perguntas em Aberto
- [ ] Todas as perguntas levantadas durante análises estão registradas
- [ ] Cada pergunta tem owner responsável por respondê-la
- [ ] Cada pergunta tem prazo para resposta
- [ ] Perguntas estão classificadas por criticidade (bloqueante, importante, nice-to-have)
- [ ] Perguntas respondidas foram fechadas com a resposta documentada

### Termos Vagos
- [ ] Palavras ambíguas nos requisitos foram identificadas ("rápido", "muitos", "fácil")
- [ ] Cada termo vago foi substituído por definição precisa com número ou critério
- [ ] Glossário de termos do projeto está criado e compartilhado
- [ ] Termos técnicos que o negócio usa diferente foram alinhados
- [ ] Acrônimos e siglas estão definidos

### Decisões Pendentes
- [ ] Decisões que precisam ser tomadas estão listadas
- [ ] Cada decisão pendente tem owner e prazo
- [ ] Impacto de adiar cada decisão está avaliado
- [ ] Decisões que bloqueiam outras atividades estão priorizadas
- [ ] Premissas temporárias para decisões pendentes estão explícitas

### Cenários Indefinidos
- [ ] Cenários onde "depende" foi a resposta estão listados com as condições
- [ ] Comportamento para cada cenário está definido ou tem plano de definição
- [ ] Edge cases sem tratamento definido estão registrados
- [ ] Cenários de erro sem resposta clara estão identificados
- [ ] Regras de negócio que "todo mundo sabe" mas ninguém documentou estão registradas

### Resolução
- [ ] Processo de escalação para perguntas sem resposta está definido
- [ ] SLA de resposta para perguntas bloqueantes está acordado
- [ ] Perguntas que ninguém consegue responder foram escaladas
- [ ] Ambiguidades resolvidas foram comunicadas a todos os envolvidos
- [ ] Status geral de ambiguidades é revisado regularmente

---

## Critérios de Aprovação
- **Mínimo**: Perguntas em Aberto e Decisões Pendentes completos
- **Recomendado**: Todos os itens marcados, zero ambiguidades bloqueantes abertas
- **Bloqueante**: Perguntas bloqueantes sem owner ou sem prazo

## Sinais de Alerta (Red Flags)
- Lista de ambiguidades vazia (não é sinal de clareza, é sinal de falta de análise)
- Perguntas abertas há semanas sem progresso
- "A gente resolve durante a implementação" para questões estruturais
- Termos vagos aceitos sem questionamento
- Ninguém sabe quem pode responder uma pergunta crítica

## Agente Responsável
**Agente de Discovery & Framing** — responsável por identificar e perseguir a resolução de ambiguidades.
