# Modo Profundo (Deep Dive)

## Nível de Detalhe

Máximo. Análise exaustiva com múltiplos cenários, evidências detalhadas, modelagem de impacto, riscos com probabilidades, planos de mitigação e referências completas. Inclui raciocínio intermediário, alternativas descartadas com justificativa e análise de sensibilidade. O documento deve ser autossuficiente — um leitor deve conseguir formar opinião independente sem informações externas.

**Proporção alvo:** 20% contexto, 50% análise detalhada, 20% recomendação fundamentada, 10% referências e apêndices.

## Quando Usar

- **Decisões de alto impacto** — mudanças arquiteturais que afetam múltiplos sistemas
- **Análises de migração** — quando o custo de reverter é muito alto
- **Investigações pós-incidente** profundas (não o relatório inicial, mas a análise completa)
- **Avaliação de build vs. buy** — quando o investimento é significativo
- **RFCs para mudanças cross-organization** — quando múltiplos stakeholders precisam avaliar
- **Due diligence técnica** — avaliação de sistemas legados ou aquisições
- **Decisões irreversíveis ou de alto custo de reversão**

**Não usar quando:**
- A decisão é local e facilmente reversível (use standard ou conciso)
- O prazo não permite análise exaustiva (use standard com flag de "análise parcial")
- A audiência não tem capacidade de absorver esse nível de detalhe

## Extensão Esperada

- **Análise de migração:** 3-8 páginas com diagramas, tabelas comparativas e timeline
- **RFC cross-org:** 4-10 páginas com seções para cada stakeholder
- **Build vs. buy:** 3-6 páginas com modelagem financeira e matriz de decisão
- **Post-mortem profundo:** 4-8 páginas com timeline detalhada, análise de causa raiz e plano de ação
- **Total:** Tipicamente 1.500-4.000 palavras + diagramas e tabelas

## Exemplo

```
## RFC-012: Migração da Camada de Autenticação para OAuth 2.0 + OIDC

### Metadata
- **Autor:** Ana Costa (Staff Engineer, Platform)
- **Revisores:** Carlos Lima (Security), Pedro Santos (Architect), Julia Mendes (Mobile)
- **Status:** Em revisão (deadline: 20/mar)
- **Impacto:** Todos os 23 serviços com autenticação + 3 apps mobile + 2 SPAs

### 1. Contexto e Motivação

#### 1.1 Estado Atual
O sistema de autenticação atual foi construído em 2019 como solução
interna baseada em JWT com sessões no Redis. Desde então:

- O número de serviços que consomem autenticação cresceu de 5 para 23
- Três aplicações mobile foram adicionadas sem padrão unificado
- O serviço de auth é single point of failure (99.1% uptime, abaixo do SLA de 99.9%)
- Não suportamos SSO, MFA hardware, ni federação com IdPs externos
- A LGPD exige controle de consentimento que o sistema atual não suporta nativamente

#### 1.2 Gatilho Imediato
Contrato com cliente Enterprise exige SAML/OIDC para federação com
Azure AD. Prazo: 90 dias. Sem essa capacidade, perdemos contrato
de R$ 2.4M ARR.

#### 1.3 Problemas Documentados

| Problema | Frequência | Impacto |
|---|---|---|
| Token não revogável (JWT stateless) | Constante | Segurança — tokens roubados válidos por 24h |
| Redis de sessão como SPOF | 3 incidentes/trimestre | Todos os usuários deslogados simultaneamente |
| Lógica de auth duplicada em 23 serviços | Cada deploy | Bug em um serviço não se propaga (inconsistência) |
| Sem audit trail de autenticação | Constante | Compliance — não rastreamos tentativas de login |
| Rotação de secrets manual | A cada 90 dias | Operacional — 2h de downtime parcial por rotação |

### 2. Análise de Alternativas

#### 2.1 Opção A — Evoluir Sistema Atual
Adicionar SAML/OIDC como camada sobre o sistema existente.

**Prós:**
- Menor disrupção imediata
- Equipe já conhece o código

**Contras:**
- Mantém todos os problemas estruturais
- SAML sobre JWT customizado = complexidade alta
- Estimativa: 6 semanas para SAML, mas sem resolver SPOF, MFA, audit trail
- Custo de manutenção crescente (~40h/mês atualmente)

**Veredicto:** Resolve o gatilho imediato mas não endereça os problemas
estruturais. Custo total em 12 meses supera migração completa.

#### 2.2 Opção B — Auth0 (SaaS)
Migrar completamente para Auth0 como provedor de identidade.

**Prós:**
- Implementação mais rápida (~4 semanas para básico)
- SAML, OIDC, MFA, SSO nativos
- SLA de 99.99%
- Compliance certifications (SOC 2, ISO 27001)

**Contras:**
- Custo: ~$18k/mês para 500k MAU (atual) escalando para $35k/mês em 12 meses
- Vendor lock-in: migração futura custosa
- Latência adicional: 50-150ms por request de auth (servidores mais próximos: us-east)
- Customização limitada para fluxos específicos do domínio
- Dados de usuários fora da nossa infraestrutura (implicação LGPD)

**Veredicto:** Resolve todos os problemas técnicos, mas custo e
dependência de vendor são riscos significativos.

#### 2.3 Opção C — Keycloak Self-Hosted
Deployment de Keycloak na nossa infraestrutura Kubernetes.

**Prós:**
- SAML, OIDC, MFA, SSO nativos
- Open source, sem custo de licença
- Dados permanecem na nossa infra
- Altamente customizável
- Comunidade ativa, bem documentado

**Contras:**
- Esforço de setup e operação: ~8 semanas para produção
- Requer expertise em Keycloak (curva de aprendizado: 2-3 semanas)
- Operação: precisamos garantir HA, backup, monitoramento
- Upgrade de versões requer planejamento

**Veredicto:** Melhor equilíbrio entre controle, custo e capacidade.
Custo operacional gerenciável com nossa infra Kubernetes existente.

### 3. Matriz de Decisão

| Critério (peso) | Atual evoluído | Auth0 | Keycloak |
|---|---|---|---|
| Atende requisito Enterprise (30%) | 6/10 | 10/10 | 9/10 |
| Custo total 12 meses (20%) | 7/10 | 4/10 | 8/10 |
| Tempo para produção (15%) | 7/10 | 9/10 | 6/10 |
| Segurança e compliance (15%) | 4/10 | 9/10 | 8/10 |
| Controle e customização (10%) | 8/10 | 5/10 | 9/10 |
| Operação e manutenção (10%) | 5/10 | 9/10 | 6/10 |
| **Score ponderado** | **6.1** | **7.6** | **7.9** |

### 4. Recomendação

**Keycloak self-hosted** com plano de migração em 3 fases.

### 5. Plano de Migração

**Fase 1 — Fundação (semanas 1-4)**
- Deploy de Keycloak em cluster Kubernetes com HA
- Configuração de realm, clients e identity providers
- Integração SAML com Azure AD para cliente Enterprise
- Resultado: contrato Enterprise desbloqueado

**Fase 2 — Migração Gradual (semanas 5-10)**
- Migrar serviços para OIDC, começando pelos menos críticos
- Dual-auth: aceitar token antigo E OIDC durante migração
- Migrar dados de usuários com zero downtime (sync bidirecional)
- Resultado: 100% dos serviços usando Keycloak

**Fase 3 — Decomissionamento (semanas 11-14)**
- Remover sistema de auth antigo
- Implementar audit trail completo
- Ativar MFA para todos os perfis administrativos
- Resultado: sistema legado desligado, nova plataforma estável

### 6. Riscos e Mitigações

| Risco | Prob. | Impacto | Mitigação |
|---|---|---|---|
| Keycloak não atende edge case | Baixa | Alto | Spike de 1 semana antes de iniciar Fase 1 |
| Migração de dados com perda | Média | Alto | Sync bidirecional + validação automatizada |
| Downtime durante migração | Média | Alto | Dual-auth elimina big bang |
| Equipe sem experiência Keycloak | Alta | Médio | Treinamento 1 semana + consultoria pontual |
| Performance sob carga | Média | Médio | Load test com 2x tráfego atual antes de go-live |

### 7. Referências
- Benchmark de auth providers: /docs/research/auth-benchmark-2025.pdf
- Análise de custo Auth0: /docs/finance/auth0-projection.xlsx
- Requisitos do cliente Enterprise: JIRA-5210
- Incidentes de auth últimos 6 meses: PagerDuty dashboard "auth-incidents"
- Keycloak documentation: https://www.keycloak.org/documentation
```
