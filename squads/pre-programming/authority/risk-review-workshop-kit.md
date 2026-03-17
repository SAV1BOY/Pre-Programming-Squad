# Workshop Kit — Revisão de Riscos

## Objetivo

Desenvolver a habilidade do squad e dos times adjacentes em identificar, avaliar e planejar respostas a riscos técnicos e de projeto durante a fase de pré-programação. O workshop ensina técnicas estruturadas de identificação de riscos, análise qualitativa/quantitativa e criação de planos de resposta acionáveis. O foco é sair do genérico ("pode dar problema") para o específico e acionável.

---

## Duração

**3.5 horas**, divididas em:
- 30min — Fundamentos de gestão de riscos
- 30min — Técnicas de identificação
- 15min — Intervalo
- 60min — Exercício prático: identificação e avaliação
- 45min — Plano de resposta e contingência
- 30min — Retrospectiva e integração com processos do squad

---

## Participantes

- **Mínimo**: 4 pessoas | **Máximo**: 12 pessoas
- **Perfil ideal**: Engenheiros, tech leads, SREs, product managers, membros do squad
- **Pré-requisito**: Envolvimento em pelo menos um projeto de software
- **Facilitador**: Membro do squad com experiência em gestão de riscos ou arquiteto sênior

---

## Agenda Detalhada

### Bloco 1 — Fundamentos (30 min)

1. **O que é risco em software** (10 min)
   - Evento incerto com impacto potencial no projeto
   - Risco vs problema: risco é futuro, problema é presente
   - Risco vs premissa: premissa é algo assumido como verdade; se falsa, vira risco materializado
   - Apetite de risco: quanto risco a organização aceita

2. **Anatomia de um risco bem documentado** (10 min)
   - Título específico (não "risco técnico")
   - Causa raiz identificável
   - Probabilidade estimada com justificativa
   - Impacto quantificado
   - Gatilhos mensuráveis
   - Plano de resposta com ações concretas

3. **Estratégias de resposta** (10 min)
   - **Evitar**: Eliminar a causa raiz (mudar o design, remover dependência)
   - **Mitigar**: Reduzir probabilidade ou impacto (redundância, testes, monitoring)
   - **Transferir**: Mover responsabilidade (seguro, SLA contratual, fornecedor)
   - **Aceitar**: Reconhecer e monitorar (quando custo de mitigação > impacto esperado)

### Bloco 2 — Técnicas de Identificação (30 min)

1. **Pre-mortem** (10 min)
   - "O projeto falhou. O que aconteceu?"
   - Cada pessoa escreve individualmente 3-5 razões de falha
   - Consolida e agrupa por categoria
   - Técnica mais eficaz para identificação de riscos em grupo

2. **Checklist de Categorias** (10 min)
   - Técnicos: performance, segurança, escala, integração, dados
   - Organizacionais: pessoas, conhecimento, dependência de time
   - Externos: fornecedores, regulação, mercado
   - De projeto: escopo, prazo, orçamento, qualidade

3. **Análise de Dependências** (10 min)
   - Para cada dependência no mapa: "O que acontece se falhar?"
   - Para cada premissa no log: "O que acontece se for falsa?"
   - Para cada decisão no ADR: "O que acontece se estiver errada?"

### Intervalo (15 min)

### Bloco 3 — Exercício Prático: Identificação e Avaliação (60 min)

**Setup**: Facilitador apresenta um cenário de projeto (fictício ou real descaracterizado) com:
- Design doc resumido
- 5 dependências externas
- 8 premissas
- 3 ADRs
- Cronograma de 4 meses

**Dinâmica**:

1. (15 min) **Pre-mortem individual**: Cada pessoa escreve 5 riscos em post-its
2. (10 min) **Consolidação**: Agrupar riscos similares, eliminar duplicatas
3. (15 min) **Avaliação**: Para cada risco, estimar probabilidade (1-5) e impacto (1-5)
4. (10 min) **Matriz de risco**: Plotar riscos na matriz probabilidade x impacto
5. (10 min) **Priorização**: Selecionar top 5 riscos para plano de resposta

### Bloco 4 — Plano de Resposta (45 min)

Dividir em grupos. Cada grupo recebe 2-3 riscos do top 5.

Para cada risco, desenvolver:
- Estratégia de resposta (evitar/mitigar/transferir/aceitar)
- Ações específicas com responsável e prazo
- Gatilhos de monitoramento
- Plano de contingência (se o risco se materializar apesar da mitigação)
- Custo estimado da mitigação vs custo do impacto

Apresentar e receber feedback dos outros grupos.

### Bloco 5 — Retrospectiva (30 min)

- Quais técnicas de identificação foram mais eficazes?
- A avaliação de probabilidade/impacto foi consistente entre participantes?
- Como integrar essas práticas no fluxo regular do squad?
- Com que frequência revisar o registro de riscos?

---

## Exercícios

1. **Pre-mortem Rápido**: Em 5 minutos, listar 10 formas de o projeto falhar. Velocidade força pensamento divergente.

2. **Risco Reverso**: Para cada "risco" genérico (ex: "problema de performance"), transformar em risco específico com causa, gatilho e impacto quantificado.

3. **Debate de Probabilidade**: Dois participantes recebem o mesmo risco mas devem defender probabilidades opostas (alta vs baixa). O grupo decide quem é mais convincente.

4. **Custo da Mitigação**: Dado um risco com impacto estimado de R$500K, o grupo tem R$50K para investir em mitigação. Como alocar?

---

## Outputs Esperados

- Registro de riscos populado com riscos realistas e bem documentados
- Matriz de risco visual mostrando distribuição de riscos por probabilidade/impacto
- Planos de resposta para os top 5 riscos
- Processo de revisão de riscos integrado ao fluxo do squad
- Participantes capacitados a identificar e documentar riscos em projetos futuros
