# Task: Executar Pré-check de Segurança

## Objetivo
Realizar uma revisão de segurança antes da implementação, identificando vulnerabilidades potenciais na arquitetura, no design e nas dependências planejadas.

## Input Necessário
- Esboço de arquitetura.
- Contratos de API.
- Mapa de integrações.
- Classificação de dados do projeto.
- Requisitos regulatórios aplicáveis.

## Agentes Envolvidos
- **Agente de Qualidade:** Conduz a revisão de segurança.
- **Agente de Arquitetura:** Apresenta o design para revisão.
- **Especialista de Segurança (se disponível):** Valida a análise.

## Passos

### 1. Classificar Dados
- Identificar todos os tipos de dados que o sistema trata.
- Classificar: Público, Interno, Confidencial, Restrito.
- Mapear dados pessoais (PII) para conformidade LGPD.

### 2. Revisar OWASP Top 10
- Para cada item do OWASP Top 10, avaliar se o design é vulnerável.
- Documentar mitigações planejadas para cada vulnerabilidade aplicável.

### 3. Revisar Autenticação e Autorização
- Validar mecanismo de autenticação escolhido.
- Verificar modelo de autorização (RBAC/ABAC).
- Identificar endpoints que precisam de proteção.
- Validar gestão de sessões e tokens.

### 4. Revisar Dependências
- Listar bibliotecas e serviços de terceiros planejados.
- Verificar vulnerabilidades conhecidas (CVEs).
- Avaliar maturidade e manutenção dos projetos.

### 5. Revisar Proteção de Dados
- Criptografia em trânsito (TLS).
- Criptografia em repouso (campos sensíveis, backups).
- Política de retenção e exclusão de dados.
- Logs: garantir que dados sensíveis não serão logados.

### 6. Documentar
- Preencher o template `security-review-template.md`.
- Registrar plano de ação para vulnerabilidades encontradas.

## Output Esperado
- Revisão de segurança documentada.
- Lista de vulnerabilidades potenciais com mitigações.
- Plano de ação para itens pendentes.
- Confirmação de conformidade regulatória (ou gaps identificados).

## Checklist de Validação
- [ ] Classificação de dados está completa.
- [ ] OWASP Top 10 foi revisado contra o design.
- [ ] Autenticação e autorização estão validadas.
- [ ] Dependências foram verificadas quanto a CVEs.
- [ ] Proteção de dados em trânsito e repouso está planejada.
- [ ] Logs não exporão dados sensíveis.
- [ ] Requisitos regulatórios (LGPD, etc.) foram considerados.
- [ ] Plano de ação tem responsáveis e prazos.
