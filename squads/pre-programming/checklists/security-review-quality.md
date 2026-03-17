# Checklist: Qualidade da Revisão de Segurança

## Propósito
Garantir que aspectos de segurança foram avaliados antes da implementação, incluindo autenticação, autorização, dados sensíveis e cenários de abuso.

## Quando Usar
- Após definição de arquitetura e contratos
- Antes de iniciar implementação de qualquer funcionalidade que lide com dados ou acesso
- Em revisões de segurança pré-implementação

---

## Checklist

### Autenticação (AuthN)
- [ ] Mecanismo de autenticação está definido (OAuth2, JWT, API Key, etc.)
- [ ] Fluxo de login/logout está mapeado
- [ ] Política de senhas/credenciais está definida
- [ ] Mecanismo de refresh de tokens está especificado
- [ ] Autenticação multi-fator foi avaliada (necessária ou não)

### Autorização (AuthZ)
- [ ] Modelo de permissões está definido (RBAC, ABAC, etc.)
- [ ] Roles e permissões por funcionalidade estão mapeados
- [ ] Princípio de menor privilégio está aplicado
- [ ] Elevação de privilégio está protegida
- [ ] Autorização é verificada no backend (não apenas no frontend)

### Dados Sensíveis
- [ ] Dados pessoais (PII) estão identificados e classificados
- [ ] Dados sensíveis são criptografados em repouso e em trânsito
- [ ] Política de retenção de dados está definida
- [ ] Mascaramento de dados em logs está planejado
- [ ] Conformidade com LGPD/GDPR foi avaliada

### Misuse Cases / Cenários de Abuso
- [ ] Cenários de abuso por usuário mal-intencionado foram mapeados
- [ ] Injection attacks (SQL, XSS, CSRF) foram considerados
- [ ] Rate limiting e throttling estão planejados
- [ ] Proteção contra automação maliciosa (bots, scraping) foi avaliada
- [ ] Cenários de escalonamento de privilégio foram analisados

### Infraestrutura de Segurança
- [ ] Secrets management está definido (vault, env vars seguras)
- [ ] Certificados e chaves têm processo de rotação
- [ ] Dependências de terceiros foram avaliadas por vulnerabilidades
- [ ] Política de atualização de dependências está definida
- [ ] Scanning de vulnerabilidades está planejado no pipeline

---

## Critérios de Aprovação
- **Mínimo**: AuthN, AuthZ e Dados Sensíveis completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Dados sensíveis não classificados ou autenticação indefinida

## Sinais de Alerta (Red Flags)
- "Segurança a gente vê depois" (dívida técnica de alto risco)
- Credenciais hardcoded em código ou configuração
- Autorização apenas no frontend
- Nenhum cenário de abuso considerado
- Dados pessoais sem criptografia ou sem política de retenção

## Agente Responsável
**Agente de Risk & Failure Analysis** — em colaboração com time de Cyber Security quando disponível.
