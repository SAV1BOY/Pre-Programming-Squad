# Standard para Pré-check de Segurança

## Propósito

Garantir que aspectos de segurança sejam avaliados antes da implementação, identificando vulnerabilidades de design, requisitos de compliance e práticas de segurança necessárias. Não substitui auditorias de segurança profundas, mas captura os riscos mais comuns e críticos preventivamente.

## Escopo

Todo projeto que envolva: dados de usuários, autenticação/autorização, integração externa, processamento de pagamentos, armazenamento de dados sensíveis ou exposição de APIs públicas.

## Definições

| Termo | Definição |
|---|---|
| PII | Personally Identifiable Information — dados que identificam uma pessoa |
| Dados sensíveis | PII, dados financeiros, credenciais, tokens, dados de saúde |
| Security by design | Princípio de considerar segurança como requisito desde o design, não como adição posterior |
| Threat model | Identificação sistemática de ameaças, vetores de ataque e controles necessários |

## Processo

### 1. Classificação de Sensibilidade

Classificar o projeto em nível de sensibilidade:

| Nível | Critério | Profundidade do Pre-check |
|---|---|---|
| **Alto** | Processa pagamentos, dados de saúde, credenciais, ou é exposto publicamente | Completo + threat modeling |
| **Médio** | Processa PII, integra com sistemas externos, ou altera autenticação/autorização | Completo |
| **Baixo** | Serviço interno, sem dados sensíveis, sem exposição externa | Simplificado |

### 2. Checklist de Segurança

#### Autenticação e Autorização
- [ ] Todos os endpoints requerem autenticação (exceto os explicitamente públicos, listados)
- [ ] Autorização granular implementada (RBAC/ABAC conforme necessidade)
- [ ] Tokens têm expiração adequada e mecanismo de revogação
- [ ] Não há escalação de privilégio possível no design
- [ ] Multi-tenancy: isolamento de dados entre organizações garantido no design

#### Dados
- [ ] PII identificada e mapeada (quais campos, onde armazenados, por quanto tempo)
- [ ] Encriptação at-rest para dados sensíveis (algoritmo e gerenciamento de chaves definidos)
- [ ] Encriptação in-transit (TLS 1.2+ para todas as comunicações)
- [ ] Política de retenção definida (quanto tempo guardar, como purgar)
- [ ] Mascaramento/anonimização em ambientes não-produtivos
- [ ] Logs não contêm dados sensíveis (PII, tokens, senhas)

#### Input e Validação
- [ ] Validação de input em todos os endpoints (tipo, tamanho, formato)
- [ ] Proteção contra injection (SQL, NoSQL, LDAP, OS command)
- [ ] Proteção contra XSS (output encoding, Content-Security-Policy)
- [ ] Rate limiting configurado em endpoints públicos e de autenticação
- [ ] Upload de arquivos (se houver) com validação de tipo, tamanho e scanning

#### Infraestrutura e Configuração
- [ ] Secrets armazenados em vault (não em código, variáveis de ambiente ou config files)
- [ ] Rotação de secrets automatizada ou com procedimento documentado
- [ ] Princípio de menor privilégio em IAM roles e permissões de banco
- [ ] Network segmentation: serviço acessível apenas por quem precisa
- [ ] Dependências escaneadas por vulnerabilidades conhecidas (Snyk, Dependabot)

#### Auditoria e Observabilidade
- [ ] Audit trail para operações sensíveis (quem, o quê, quando)
- [ ] Alertas para padrões suspeitos (multiple failed logins, unusual access patterns)
- [ ] Logs estruturados com correlation ID para investigação

#### Compliance
- [ ] LGPD: base legal para tratamento de dados identificada
- [ ] LGPD: mecanismo de consentimento (se aplicável)
- [ ] LGPD: capacidade de atender direitos do titular (acesso, correção, exclusão)
- [ ] PCI-DSS (se aplicável): escopo de compliance mapeado
- [ ] Regulação setorial (se aplicável): requisitos identificados

### 3. Threat Modeling (para projetos de sensibilidade Alta)

Identificar:
- **Ativos:** O que precisa ser protegido (dados, funcionalidades, infraestrutura)
- **Ameaças:** Quem pode atacar e como (STRIDE: Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege)
- **Controles:** O que previne ou detecta cada ameaça
- **Gaps:** Onde os controles são insuficientes

### 4. Documentação e Veredicto

- Checklist preenchido com status e evidência para cada item
- Achados classificados por severidade
- Veredicto: Aprovado / Aprovado com condições / Não aprovado
- Itens condicionais com owner e prazo

## Critérios de Qualidade

- Checklist completo para o nível de sensibilidade do projeto
- Achados com recomendação acionável
- Threat model para projetos de alta sensibilidade
- Revisão validada pelo time de segurança (quando disponível)
- Nenhum item de severidade Crítica sem plano de mitigação

## Responsáveis

| Papel | Responsabilidade |
|---|---|
| Membro do squad | Executar pre-check, documentar achados |
| Tech Lead | Validar completude, priorizar achados |
| Time de Segurança | Revisar achados de sensibilidade Alta, validar threat model |
| Autor da proposta | Endereçar achados no design antes da implementação |

## Referências

- Standard de Revisão de Riscos: `docs/risk-review-standard.md`
- Standard de Arquitetura: `docs/architecture-review-standard.md`
- OWASP Top 10: referência para vulnerabilidades comuns
- LGPD: referência para tratamento de dados pessoais
