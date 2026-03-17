# Security by Design Primer

## Título e Propósito

O **Security by Design Primer** é um framework para incorporar segurança como critério de design desde a fase de pré-programação, não como checklist de última hora antes do deploy. O propósito é garantir que decisões arquiteturais considerem superfície de ataque, proteção de dados e princípios de segurança desde o início — porque vulnerabilidades nascidas no design são as mais caras de corrigir.

## Quando Usar

- Durante design de qualquer sistema que processa dados sensíveis
- Na definição de arquitetura de APIs, autenticação e autorização
- Ao projetar integrações com sistemas externos
- Quando há requisitos regulatórios (LGPD, PCI-DSS, SOC2)
- Na avaliação de soluções de terceiros

## Conceitos-Chave

1. **Princípio do Menor Privilégio**: Cada componente, usuário ou serviço tem apenas as permissões mínimas necessárias para sua função.
2. **Defesa em Profundidade**: Múltiplas camadas de proteção. Se uma falha, as outras contêm o impacto.
3. **Superfície de Ataque**: Todos os pontos onde um atacante pode interagir com o sistema. Quanto menor, mais seguro.
4. **Dados em Trânsito vs. em Repouso**: Proteções diferentes para dados que estão sendo transmitidos vs. armazenados.
5. **Fail Secure**: Quando o sistema falha, ele deve falhar em estado seguro (negar acesso), não em estado aberto.
6. **Segregação de Responsabilidades**: Nenhuma entidade deve ter controle total sobre uma operação crítica.

## Processo / Passos

### Passo 1 — Classificar Dados
Identifique todos os dados que o sistema processa. Classifique: público, interno, confidencial, regulado (PII, financeiro, saúde).

### Passo 2 — Mapear Superfície de Ataque
Liste todos os pontos de entrada: APIs, formulários, uploads, webhooks, console de admin, APIs internas.

### Passo 3 — Definir Modelo de Autenticação e Autorização
Quem pode acessar o quê? Como identidades são verificadas? Como permissões são gerenciadas e auditadas?

### Passo 4 — Projetar Proteção de Dados
Para cada classe de dados, defina: criptografia em trânsito (TLS), criptografia em repouso, mascaramento em logs, política de retenção.

### Passo 5 — Aplicar Princípio do Menor Privilégio
Para cada componente, defina permissões mínimas: acesso ao banco, APIs que pode chamar, recursos que pode acessar.

### Passo 6 — Projetar Auditoria
Defina: quais ações são logadas para auditoria, quem acessa os logs, retenção, imutabilidade.

### Passo 7 — Planejar Resposta a Incidentes
Defina: como detectar breach, quem notificar, como conter, como comunicar, obrigações legais (LGPD: 72h para notificar ANPD).

## Perguntas de Ativação

- "Se um atacante conseguisse acesso a esse componente, o que poderia fazer?"
- "Estamos armazenando dados sensíveis que não precisamos armazenar?"
- "Esse serviço tem mais permissões do que precisa?"
- "Se esse token/credencial vazar, qual é o blast radius?"
- "Os logs contêm dados pessoais ou sensíveis?"
- "Quanto tempo levamos para detectar um breach? Horas ou semanas?"

## Output Esperado

| Aspecto | Design de Segurança | Implementação | Verificação |
|---|---|---|---|
| Autenticação | OAuth2 + MFA para admin | Biblioteca validada (não custom) | Teste de penetração |
| Autorização | RBAC com menor privilégio | Middleware de autorização centralizado | Revisão de permissões trimestralmente |
| Dados PII | Criptografia AES-256 em repouso, TLS 1.3 em trânsito | KMS para gestão de chaves | Scan de dados sensíveis em logs |
| API Security | Rate limiting, input validation, CORS restrito | WAF + validação no código | OWASP Top 10 checklist |
| Secrets | Vault externo, rotação automática | Nenhum secret em código ou config | Scan de repositório |
| Auditoria | Log de todas as ações administrativas | Append-only log, retenção 1 ano | Revisão mensal |

## Armadilhas Comuns

1. **Segurança como afterthought**: "Depois a gente adiciona segurança" é como construir uma casa e depois tentar adicionar fundação.
2. **Criptografia como bala de prata**: Criptografar tudo sem gerenciar chaves adequadamente é teatro de segurança.
3. **Autenticação sem autorização**: Verificar quem é o usuário mas não verificar o que ele pode fazer.
4. **Secrets no código**: Credenciais hard-coded em repositórios, variáveis de ambiente sem proteção, configs em plain text.
5. **Logs com PII**: Logar dados pessoais para "debug" e depois esquecê-los lá, violando LGPD.
6. **Segurança por obscuridade**: Confiar que "ninguém vai descobrir essa URL/API" em vez de proteger adequadamente.
