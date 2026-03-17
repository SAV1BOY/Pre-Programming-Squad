# Estilo Readout Executivo

## Formato

Apresentação concisa de resultados e status para liderança executiva. Formato otimizado para reuniões de 15-30 minutos ou leitura assíncrona em 5 minutos. Prioriza impacto de negócio sobre detalhes técnicos. Usa estrutura visual com indicadores de status por cores e métricas em destaque.

## Estrutura

```
# Readout Executivo — [Nome do Projeto/Iniciativa]
## [Período de referência]

### Status Geral: [🟢 No prazo | 🟡 Em risco | 🔴 Atrasado/Bloqueado]

### Destaques (Top 3)
1. [Conquista ou progresso mais importante]
2. [Segunda conquista ou marco atingido]
3. [Terceira conquista ou item de atenção]

### Métricas-chave
[Tabela com indicadores de progresso e saúde]

### Riscos e Bloqueios
[Apenas itens que precisam de atenção executiva]

### Decisões Necessárias
[O que precisa ser aprovado/decidido e por quem]

### Próximas Entregas
[O que vem a seguir com datas]
```

## Tom

- Ultra-conciso — respeitar o tempo do executivo
- Orientado a impacto — números de negócio, não detalhes técnicos
- Visual — status por cores, métricas em destaque, tabelas compactas
- Proativo — antecipar perguntas, não esperar serem feitas
- Honesto — status real, sem maquiagem; executivos preferem más notícias cedo

## Audiência

- VP/C-level de Engenharia e Produto
- Head de áreas impactadas pelo projeto
- Board members em contexto de report trimestral
- Stakeholders executivos que acompanham portfólio de projetos

## Exemplo

```
# Readout Executivo — Programa de Modernização da Plataforma
## Período: fev/2025

### Status Geral: 🟡 Em Risco

Programa 65% concluído (meta: 70%). Workstream de dados atrasado
por dependência de contratação. Workstreams de API e infra no prazo.

---

### Destaques

1. **API Gateway v2 em produção** — migração concluída sem incidentes.
   Latência média reduziu 40% (de 120ms para 72ms). Economia de
   R$ 23k/mês em infraestrutura já realizada.

2. **Contratação de Data Engineer travada** — posição aberta há 60
   dias, 0 candidatos finalistas. Workstream de dados bloqueado.
   Impacto: atraso de 4-6 semanas se não resolver em março.

3. **Migração de autenticação adiantada** — Keycloak em produção
   para 3 serviços (meta era 2). Time acelerou por conta de
   learnings do API Gateway.

---

### Métricas-chave

| Indicador | Meta | Atual | Tendência | Status |
|---|---|---|---|---|
| Progresso geral | 70% | 65% | ↘ | 🟡 |
| Serviços migrados | 12/23 | 11/23 | → | 🟡 |
| Incidentes P1 (plataforma) | ≤ 1/mês | 0 | ↘ | 🟢 |
| Economia mensal realizada | R$ 40k | R$ 38k | ↗ | 🟢 |
| NPS do desenvolvedor | 7.0 | 6.8 | ↗ | 🟡 |
| Headcount alocado | 8 | 7 | → | 🔴 |

---

### Riscos e Bloqueios

| # | Risco/Bloqueio | Impacto | Ação Necessária |
|---|---|---|---|
| 1 | Contratação de Data Engineer | Atraso de 4-6 semanas no workstream de dados | Aprovar contratação de consultor temporário (R$ 25k/mês por 3 meses) |
| 2 | Serviço legado de faturamento sem owner | Migração bloqueada; ninguém conhece o código | Alocar 1 engenheiro sênior por 2 semanas para discovery |

---

### Decisões Necessárias

1. **Aprovar consultor temporário para dados**
   Custo: R$ 75k (3 meses). Evita: atraso de 6 semanas que
   compromete deadline de Q2. Alternativa: aceitar atraso.
   **De quem:** VP de Engenharia. **Até:** 15/mar.

2. **Priorizar discovery do serviço de faturamento**
   Requer: realocar @engenheiro.senior do squad Y por 2 semanas.
   **De quem:** EM do squad Y + VP. **Até:** 20/mar.

---

### Próximas Entregas

| Entrega | Data | Confiança |
|---|---|---|
| Migração serviço de Notificações | 20/mar | 🟢 Alta |
| Migração serviço de Catálogo | 05/abr | 🟢 Alta |
| Pipeline de dados v2 (depende contratação) | 30/abr | 🔴 Baixa |
| Migração serviço de Faturamento | 15/mai | 🟡 Média |
| Go-live completo | 30/jun | 🟡 Em risco |

---

### Próximo Readout: 01/abr/2025

Contato para dúvidas: Ana Costa (@ana.costa) — Tech Lead do programa
```
