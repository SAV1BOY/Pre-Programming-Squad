# John Allspaw — Resumo de Autoridade

## Autor

**Nome**: John Allspaw
**Afiliação**: Ex-CTO Etsy, fundador da Adaptive Capacity Labs
**Obras Principais**: "The Art of Capacity Planning" (2008), "Web Operations" (2010), múltiplos papers sobre resiliência organizacional
**Área de Expertise**: Operações web, resposta a incidentes, fatores humanos em engenharia de software, resiliência organizacional

---

## Tese Central

Sistemas complexos falham de formas que não podem ser completamente previstas. A resiliência verdadeira não vem de tentar prevenir todas as falhas (impossível), mas de construir **capacidade adaptativa** — a habilidade da organização e de seus sistemas de se adaptar a situações imprevistas. O fator humano é central: são as pessoas que detectam anomalias, diagnosticam problemas e orquestram respostas. Investir em capacidade humana é tão importante quanto investir em redundância técnica.

---

## Conceitos-Chave

### 1. Blameless Post-Mortems
Análise de incidentes sem atribuição de culpa individual. O objetivo é aprender, não punir. Princípios:
- Pessoas agem racionalmente com base na informação disponível no momento
- Encontrar "o culpado" encerra a investigação prematuramente
- As condições que levaram ao incidente são mais importantes que o ato individual
- Counter-factuals ("se fulano tivesse feito X") não são úteis

### 2. Resiliência como Propriedade Emergente
Resiliência não é feature que se implementa — é propriedade que emerge de:
- Redundância (técnica e organizacional)
- Diversidade de respostas
- Capacidade de improvisação
- Aprendizado com incidentes anteriores

### 3. Capacity Planning
Planejamento de capacidade não é apenas "adicionar mais servidores":
- Entender padrões de uso (picos, sazonalidade, crescimento)
- Modelar carga futura com base em métricas históricas
- Definir limites operacionais (quando escalar, quando degradar)
- Testar limites antes que produção os encontre

### 4. Expertise em Operações como Ativo
O conhecimento tácito de operadores experientes (como diagnosticam, que sinais observam, que atalhos conhecem) é um dos ativos mais valiosos e menos documentados de uma organização.

### 5. MTTR sobre MTBF
Mean Time To Recovery é mais importante que Mean Time Between Failures. Sistemas vão falhar — o que importa é quão rápido você recupera. Investir em detecção rápida, diagnóstico eficiente e rollback automático.

---

## Aplicação ao Squad

- **Blameless culture como valor do squad**: Quando premissas se provam erradas, quando riscos não identificados se materializam — a resposta é análise, não culpa. Criar template de "learning review" para falhas de pré-programação.

- **Capacity planning no design doc**: Incluir seção obrigatória de capacity planning: carga esperada, projeção de crescimento, limites operacionais, plano de escala.

- **MTTR como métrica de design**: No design doc, o plano de rollback deve incluir tempo estimado de recuperação. Se MTTR > 30 minutos para um serviço crítico, o design precisa de ajuste.

- **Conhecimento tácito no handoff**: Durante o handoff, capturar não apenas documentos formais, mas o conhecimento tácito: "como você diagnosticaria um problema neste sistema?", "que sinais indicam que algo está errado?".

- **Diversidade de perspectivas na revisão**: Incluir pessoas com diferentes backgrounds (dev, ops, QA, produto) nas readiness reviews. Cada perspectiva identifica riscos diferentes.

---

## Citações Relevantes

> "Human error is not the cause of failure; it is the consequence of the system design."

> "The goal of a post-incident review is not to find who is responsible, but to find what is responsible."

> "We don't have a 'people problem.' We have a 'systems that make it easy for people to fail' problem."

> "Resilience is not a property of individual components but of the system as a whole, including its human operators."

> "The question is not 'how do we prevent failure?' but 'how do we build the capacity to respond to failure?'"
