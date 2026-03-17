# Template: Revisão de Segurança

## Título
Security Review — Revisão de Segurança Pré-Implementação

## Propósito
Avaliar a postura de segurança do projeto antes da implementação, identificando vulnerabilidades potenciais, requisitos de compliance e controles necessários.

## Quando Usar
- Antes de iniciar a implementação de funcionalidades que lidam com dados sensíveis.
- Em projetos que envolvem autenticação, pagamentos ou dados pessoais.
- Como parte do checklist de readiness pré-desenvolvimento.

## Seções

### 1. Informações Gerais
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| Responsável | `[nome]` |
| Data | `[YYYY-MM-DD]` |
| Classificação de Dados | `[Público/Interno/Confidencial/Restrito]` |

### 2. Superfície de Ataque
| Componente | Exposição | Dados Acessíveis | Nível de Risco |
|------------|-----------|------------------|---------------|
| `[API pública]` | `[Internet]` | `[dados pessoais]` | `[Alto/Médio/Baixo]` |

### 3. OWASP Top 10 — Checklist
| Vulnerabilidade | Aplicável? | Mitigação Planejada | Status |
|----------------|-----------|---------------------|--------|
| A01 - Broken Access Control | `[Sim/Não]` | `[controle planejado]` | `[status]` |
| A02 - Cryptographic Failures | `[Sim/Não]` | `[controle planejado]` | `[status]` |
| A03 - Injection | `[Sim/Não]` | `[controle planejado]` | `[status]` |
| A04 - Insecure Design | `[Sim/Não]` | `[controle planejado]` | `[status]` |
| A05 - Security Misconfiguration | `[Sim/Não]` | `[controle planejado]` | `[status]` |
| A06 - Vulnerable Components | `[Sim/Não]` | `[controle planejado]` | `[status]` |
| A07 - Auth Failures | `[Sim/Não]` | `[controle planejado]` | `[status]` |
| A08 - Software/Data Integrity | `[Sim/Não]` | `[controle planejado]` | `[status]` |
| A09 - Logging/Monitoring Failures | `[Sim/Não]` | `[controle planejado]` | `[status]` |
| A10 - SSRF | `[Sim/Não]` | `[controle planejado]` | `[status]` |

### 4. Autenticação e Autorização
| Aspecto | Design | Implementação |
|---------|--------|--------------|
| Método de autenticação | `[OAuth2/JWT/SAML/etc.]` | `[biblioteca/serviço]` |
| Gestão de sessão | `[stateless/stateful]` | `[detalhes]` |
| Controle de acesso | `[RBAC/ABAC/ACL]` | `[detalhes]` |
| MFA | `[Sim/Não]` | `[detalhes]` |

### 5. Proteção de Dados
| Dado | Classificação | Em Trânsito | Em Repouso | Retenção | Acesso |
|------|---------------|-------------|-----------|----------|--------|
| `[tipo de dado]` | `[PII/Financeiro/Saúde]` | `[TLS 1.3]` | `[AES-256]` | `[prazo]` | `[quem]` |

### 6. Compliance e Regulações
| Regulação | Requisitos Aplicáveis | Status de Conformidade |
|-----------|----------------------|-----------------------|
| `[LGPD/PCI-DSS/SOC2]` | `[requisitos específicos]` | `[Conforme/Parcial/Pendente]` |

### 7. Dependências e Supply Chain
| Dependência | Versão | Vulnerabilidades Conhecidas | Alternativa |
|-------------|--------|---------------------------|------------|
| `[biblioteca/serviço]` | `[versão]` | `[CVEs conhecidos]` | `[se houver]` |

### 8. Plano de Ação
| Ação | Prioridade | Responsável | Prazo | Status |
|------|-----------|-------------|-------|--------|
| `[ação de segurança]` | `[Crítica/Alta/Média/Baixa]` | `[nome]` | `[data]` | `[status]` |

## Exemplo de Preenchimento

### 5. Proteção de Dados
| Dado | Classificação | Em Trânsito | Em Repouso | Retenção | Acesso |
|------|---------------|-------------|-----------|----------|--------|
| CPF do cliente | PII | TLS 1.3 | AES-256 (campo) | 5 anos | Equipe de suporte (mascarado) |
| Número do cartão | PCI | TLS 1.3 | Tokenizado (Stripe) | Não armazenado | Ninguém (token only) |
| Email | PII | TLS 1.3 | Sem criptografia adicional | Enquanto ativo | Equipe de marketing |

## Dicas de Qualidade
- **Security by design:** Segurança é requisito, não feature opcional.
- **Princípio do menor privilégio:** Conceda apenas os acessos estritamente necessários.
- **Não reinvente criptografia:** Use bibliotecas e padrões estabelecidos.
- **Scan automatizado:** Integre ferramentas de scan de vulnerabilidades no CI/CD.
- **Pense em dados sensíveis em logs:** Nunca registre senhas, tokens ou dados pessoais em logs.
