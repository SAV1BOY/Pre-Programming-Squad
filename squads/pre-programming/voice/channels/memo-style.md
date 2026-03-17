# Estilo Memo / Documento Formal

## Formato

Documento estruturado com seções numeradas, cabeçalho com metadata e distribuição clara. Segue formato de memorando técnico: autossuficiente, formal e arquivável. Cada memo tem número de referência único para rastreabilidade.

## Estrutura

```
MEMO-[SQUAD]-[NÚMERO]
Data: [dd/mmm/aaaa]
De: [autor, papel]
Para: [destinatários primários]
CC: [destinatários informativos]
Assunto: [título descritivo e específico]
Classificação: [Interna / Restrita / Confidencial]

---

1. OBJETIVO
   [Por que este memo existe — 1-2 frases]

2. CONTEXTO
   [Situação atual relevante — máximo 1 parágrafo]

3. ANÁLISE / CONTEÚDO PRINCIPAL
   [Corpo do memo — seções conforme necessário]
   3.1 [Subtópico]
   3.2 [Subtópico]

4. RECOMENDAÇÃO
   [Ação recomendada — clara e acionável]

5. DECISÃO NECESSÁRIA
   [O que precisa ser decidido, por quem, até quando]

6. PRÓXIMOS PASSOS
   [Lista numerada com owner e prazo]

7. REFERÊNCIAS
   [Documentos, dados, links relevantes]
```

## Tom

- Formal e impessoal — foco no conteúdo, não no autor
- Estruturado — cada seção tem propósito claro
- Completo — leitor não precisa buscar informação fora do memo
- Objetivo — apresenta fatos e análise separados de opinião
- Rastreável — toda afirmação tem fonte ou referência

## Audiência

- Liderança técnica e de produto que precisa de registro formal
- Stakeholders cross-team que precisam de contexto completo
- Registro institucional para decisões que afetam múltiplos squads
- Documentação de compliance ou auditoria

## Exemplo

```
MEMO-PPS-2025-017
Data: 10/mar/2025
De: Ana Costa, Tech Lead — Pre-Programming Squad
Para: Comitê de Arquitetura
CC: VP de Engenharia, Head de Produto
Assunto: Proposta de Adoção de Feature Flags como Padrão Organizacional
Classificação: Interna

---

1. OBJETIVO

Propor a adoção de feature flags como prática padrão para todos
os squads de engenharia, com ferramenta centralizada e governança
definida.

2. CONTEXTO

Atualmente, 4 de 8 squads usam feature flags de forma independente:
2 com LaunchDarkly, 1 com Unleash e 1 com solução customizada.
Essa fragmentação gera custo duplicado (R$ 8.5k/mês total),
impossibilita visibilidade cross-squad e impede práticas como
kill-switches globais.

No último trimestre, 2 incidentes P1 poderiam ter sido resolvidos
em minutos com kill-switch, mas levaram 45min+ por exigirem rollback
de deploy.

3. ANÁLISE

3.1 Estado Atual
- 4 squads com feature flags: resultados positivos em deploy safety
- 4 squads sem feature flags: rollback médio de 35 minutos
- Ferramentas fragmentadas: sem visão consolidada de flags ativas
- Custo atual: R$ 8.5k/mês dividido entre 3 fornecedores

3.2 Proposta
Consolidar em LaunchDarkly (plano Enterprise) para todos os 8 squads.
Custo: R$ 12k/mês (+R$ 3.5k vs. atual, mas cobrindo 100% dos squads).
Governança: flag naming convention, lifecycle policy (flags > 30 dias
sem alteração geram alerta), auditoria mensal.

3.3 Alternativa Avaliada
Unleash self-hosted: custo de licença zero, mas custo operacional
estimado em 2 dias/mês de SRE + risco de disponibilidade.
Descartado: overhead operacional não justifica economia.

4. RECOMENDAÇÃO

Aprovar consolidação em LaunchDarkly Enterprise com rollout em 3 fases
(squads críticos primeiro, depois demais, depois governança completa).

5. DECISÃO NECESSÁRIA

Aprovação do Comitê de Arquitetura para:
- Budget adicional de R$ 3.5k/mês (R$ 42k/ano)
- Mandato organizacional de adoção por todos os squads
Prazo: reunião do comitê de 20/mar

6. PRÓXIMOS PASSOS

6.1 Aprovação do comitê — 20/mar — @comitê
6.2 Setup da conta Enterprise — 25/mar — @ana.costa
6.3 Migração squad Pagamentos (piloto) — 01/abr — @pedro.santos
6.4 Documentação de padrões e governança — 05/abr — @ana.costa
6.5 Rollout para demais squads — abr/mai — @tech.leads

7. REFERÊNCIAS

- Análise de custo detalhada: /docs/finance/feature-flags-cost-2025.xlsx
- Post-mortem incidentes P1: INC-2025-003, INC-2025-007
- Benchmark LaunchDarkly vs Unleash: /docs/research/ff-benchmark.md
```
