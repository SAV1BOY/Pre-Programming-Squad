# Enterprise SaaS - Readiness Primer

## Contexto da Industria

Enterprise SaaS (Software as a Service) serve empresas de medio e grande porte com solucoes como CRM, ERP, HCM, project management, comunicacao e colaboracao. Caracteriza-se por contratos longos, ciclos de venda complexos, requisitos de customização, multi-tenancy, integracao com sistemas corporativos e exigencias rigorosas de segurança, compliance e SLAs.

## Desafios Especificos de Pre-Programacao

### Multi-Tenancy
Multiplos clientes compartilham infraestrutura. Isolamento de dados e mandatorio. Opcoes: banco compartilhado com discriminador de tenant, schema por tenant, banco por tenant. Cada opcao tem trade-offs de custo, isolamento, complexidade operacional e performance. Na pre-programacao, a decisao de multi-tenancy e arquitetural e de alto impacto.

### Customizacao e Configurabilidade
Clientes enterprise exigem customizacao: campos personalizados, workflows configuraveis, regras de negocio especificas, branding. Na pre-programacao, projetar para configurabilidade sem explodir a complexidade do codigo-base.

### Integracao Enterprise
Clientes exigem integracao com seus sistemas: SSO (SAML, OIDC), LDAP/AD, ERP (SAP, Oracle), APIs de terceiros. Na pre-programacao, definir estrategia de integracao e APIs abertas.

### SLAs Contratuais
Clientes enterprise negociam SLAs com penalidades financeiras. 99.9% de uptime e frequentemente o minimo. Na pre-programacao, SLOs devem ser definidos para serem atingiveis e sustentaveis.

### Compliance e Certificacoes
SOC 2, ISO 27001, LGPD, GDPR (se clientes europeus). Clientes enterprise exigem evidencias de compliance. Na pre-programacao, requisitos de compliance informam decisoes de arquitetura.

## Regulacoes Relevantes

| Regulacao/Certificacao | Escopo | Impacto no Design |
|---|---|---|
| SOC 2 Type II | Controles de seguranca | Logging, access control, change management |
| ISO 27001 | Gestao de seguranca | Politicas, processos, controles |
| LGPD | Dados pessoais | Consentimento, DPO, data residency |
| GDPR | Dados pessoais (EU) | Similiar LGPD, portabilidade, erasure |
| HIPAA | Dados de saude (EUA) | Se atender healthcare, requisitos adicionais |

## Padroes de Readiness

### Checklist de Pre-Programacao para Enterprise SaaS

**Multi-Tenancy:**
- [ ] Modelo de multi-tenancy definido e justificado.
- [ ] Isolamento de dados entre tenants garantido por design.
- [ ] Noisy neighbor prevention: um tenant nao degrada performance de outros.
- [ ] Estrategia de onboarding/offboarding de tenants definida.
- [ ] Data residency requirements atendidos (dados em regiao especifica).

**Customizacao:**
- [ ] Estrategia de campos customizaveis definida.
- [ ] Engine de workflow/regras de negocio planejada.
- [ ] Limites de customização documentados (o que e e nao e customizavel).

**Integracao:**
- [ ] SSO (SAML 2.0, OIDC) planejado.
- [ ] API publica com documentacao e versionamento definidos.
- [ ] Webhooks para eventos importantes.
- [ ] Rate limiting e quotas por tenant.

**Seguranca e Compliance:**
- [ ] SOC 2 controls mapeados.
- [ ] Audit logging para todas as operacoes administrativas.
- [ ] Encriptacao at-rest e in-transit.
- [ ] Role-based access control (RBAC) com granularidade por tenant.
- [ ] Data retention e deletion policies definidas.

**SLAs e Operacao:**
- [ ] SLOs definidos e atingiveis com a arquitetura proposta.
- [ ] Estrategia de zero-downtime deployment definida.
- [ ] Monitoramento por tenant (per-tenant dashboards).
- [ ] Plano de disaster recovery documentado.
- [ ] Runbooks para cenarios de falha comuns.

## Riscos Tipicos

1. **Vazamento de dados entre tenants:** Catastrofico — pode encerrar o negocio.
2. **Violacao de SLA:** Penalidades financeiras, perda de cliente.
3. **Noisy neighbor:** Um tenant degrada performance para todos.
4. **Migracao de tenant:** Dificuldade de offboarding ou portabilidade de dados.
5. **Compliance failure:** Perda de certificacao, inelegibilidade para contratos.
6. **Customizacao descontrolada:** Codigo-base se torna ingerenciavel com configs por tenant.
