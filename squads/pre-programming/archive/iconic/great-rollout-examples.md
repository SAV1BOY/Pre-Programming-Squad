# Exemplos Icônicos de Planos de Rollout

## Objetivo

Documentar exemplos anotados de planos de rollout excepcionais. Um bom plano de rollout é a diferença entre um deploy tranquilo e um incidente em produção. Estes exemplos mostram como planejar a entrega com segurança.

---

## Exemplo 1: Rollout da Migração do Gateway de Pagamentos

### Contexto
E-commerce processando R$2M/dia migrando de gateway legado para novo provedor. Zero tolerance para perda de transações. Migração precisava ser invisível para o usuário final.

### Trechos Anotados

**Fase de Shadow Traffic:**
> "Semana 1-2: Toda transação é processada no gateway atual E enviada (sem cobrar) ao novo gateway em paralelo. Comparar: (1) taxa de aprovação simulada, (2) latência de resposta, (3) códigos de erro mapeados corretamente. Gate: taxa de discrepância < 0.1% para avançar."

*Anotação: Shadow traffic permite validar o novo sistema com dados reais sem risco. O gate quantitativo (< 0.1% discrepância) remove subjetividade da decisão de avançar.*

**Plano de Rollback:**
> "Rollback é automático se: (1) taxa de erro > 2% por 5 minutos, (2) latência p99 > 3 segundos, (3) qualquer transação duplicada detectada. Rollback manual disponível via feature flag — tempo de execução: <30 segundos. Pós-rollback: todas as transações em voo no novo gateway são reconciliadas manualmente em até 1 hora."

*Anotação: Rollback com critérios automáticos E manuais. O detalhe sobre "transações em voo" mostra que o time pensou em estados intermediários — o cenário mais perigoso em migrações.*

**Comunicação:**
> "Dia D-3: Email para time de suporte com FAQ sobre possíveis perguntas de clientes. Dia D: Canal dedicado no Slack (#migration-war-room) com on-call de pagamentos, infra e produto. Dia D+1: Relatório de reconciliação enviado ao financeiro até 10h."

*Anotação: Comunicação planejada para cada stakeholder. O time de suporte é preparado ANTES, não durante o incidente.*

### O Que Torna Este Rollout Excelente
- Shadow traffic antes de qualquer exposição real
- Gates quantitativos em cada fase
- Rollback automático com critérios explícitos
- Comunicação planejada para cada stakeholder
- Reconciliação de estados intermediários documentada
- War room com papéis definidos

---

## Exemplo 2: Rollout de Nova Versão da API Pública (v2)

### Contexto
API REST usada por 340+ parceiros. Versão 2 com breaking changes. Necessidade de período de convivência e migração assistida.

### Trechos Anotados

**Estratégia de Versionamento:**
> "v1 e v2 coexistem por 6 meses. Após 3 meses: v1 retorna header X-API-Deprecation com data de desativação. Após 5 meses: v1 retorna HTTP 299 (aviso) além do resultado normal. Mês 6: v1 retorna 410 Gone com link para guia de migração."

*Anotação: Degradação progressiva e comunicativa. Cada fase dá sinal mais forte ao consumidor. O uso de HTTP 299 como warning antes do 410 é uma prática avançada que reduz surpresas.*

**Plano de Migração de Parceiros:**
> "Tier 1 (top 20 parceiros, 85% do volume): Migração assistida com call individual e sandbox dedicado. Tier 2 (50 parceiros, 12% do volume): Guia de migração detalhado + office hours semanais. Tier 3 (270+ parceiros, 3% do volume): Documentação self-service + suporte via ticket."

*Anotação: Segmentação de parceiros por impacto de negócio. Investimento de suporte proporcional ao valor. Pragmático e eficiente.*

**Monitoramento de Adoção:**
> "Dashboard em tempo real: % de requests em v1 vs v2 por parceiro. Alerta se parceiro Tier 1 não fez nenhuma request v2 após 30 dias. Relatório semanal para Product com curva de adoção."

*Anotação: Monitoramento de adoção é tão importante quanto monitoramento técnico. O alerta proativo para Tier 1 previne surpresas no deadline.*

### O Que Torna Este Rollout Excelente
- Período de convivência generoso com sinais progressivos
- Segmentação de clientes por impacto
- Suporte proporcional ao valor do parceiro
- Monitoramento de adoção em tempo real
- Sandbox para validação antes da migração real
- Timeline clara com marcos comunicados antecipadamente

---

## Exemplo 3: Rollout de Feature com Experimentação (A/B Test)

### Contexto
Nova experiência de checkout em plataforma com 2M de transações/mês. Necessidade de validar impacto na conversão antes do rollout completo.

### Trechos Anotados

**Design do Experimento:**
> "Métrica primária: taxa de conversão do checkout (baseline: 68.3%). Métrica guardrail: tempo médio de checkout (não pode aumentar >10%). Poder estatístico mínimo: 80%. MDE (Minimum Detectable Effect): 1.5pp. Tamanho da amostra calculado: 47K sessões por variante. Duração estimada: 12 dias com tráfego atual."

*Anotação: Rigor estatístico no design do experimento. MDE e poder estatístico definidos antes — não "vamos rodar e ver o que acontece".*

**Critérios de Parada Antecipada:**
> "Parada por dano: se conversão cair >5pp em 48h (teste sequencial). Parada por vitória: se efeito >3pp com p-value <0.001 após mínimo de 5 dias. Parada manual: qualquer bug funcional reportado no novo checkout."

*Anotação: Critérios de parada protegem contra dano prolongado e permitem capturar vitórias claras mais cedo. O mínimo de 5 dias previne false positives por efeito novidade.*

**Rollout Pós-Experimento:**
> "Resultado positivo: rollout gradual 25% → 50% → 100% em 5 dias, monitorando métricas guardrail. Resultado neutro: manter A/B por mais 7 dias para confirmar, depois decisão de produto. Resultado negativo: desligar variante, post-mortem em 48h, iterar no design."

*Anotação: Plano para todos os cenários possíveis. Resultado neutro tem protocolo próprio — não fica no limbo.*

### O Que Torna Este Rollout Excelente
- Rigor estatístico no design do experimento
- Métricas guardrail protegem contra degradação
- Critérios de parada antecipada em ambas direções
- Plano para cada cenário de resultado
- Rollout gradual mesmo após resultado positivo
- Timeline realista baseada em cálculo de amostra

---

## Lições Aplicáveis

### Para o Pre-Programming Squad

1. **Todo rollout precisa de plano de rollback** — Se não tem rollback, não está pronto para deploy. O Agente de Riscos deve validar isso como gate obrigatório.

2. **Gates quantitativos, não subjetivos** — "Parece ok" não é critério de avanço. Defina números antes do rollout começar.

3. **Shadow traffic quando possível** — Para migrações de sistemas críticos, shadow traffic é a forma mais segura de validar. O Agente de Testes deve incluir isso no plano.

4. **Comunique antes, durante e depois** — Stakeholders surpresos são stakeholders que atrapalham. Planeje comunicação como parte do rollout.

5. **Segmente por impacto** — Nem todos os usuários/parceiros são iguais. Rollout faseado por segmento reduz blast radius.

6. **Monitore adoção, não só saúde** — Em migrações e mudanças de API, a métrica mais importante é adoção. Saúde técnica sem adoção é irrelevante.

7. **Defina critérios para todos os cenários** — Sucesso, falha e empate devem ter protocolo definido antes do rollout. Decisões sob pressão são piores.
