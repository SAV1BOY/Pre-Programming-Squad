# Template: Prontidão de Ambiente

## Título
Environment Readiness — Checklist de Prontidão de Ambientes

## Propósito
Garantir que todos os ambientes necessários para desenvolvimento, teste e deploy estejam configurados e funcionais antes do início da implementação.

## Quando Usar
- Antes do início da fase de desenvolvimento.
- Ao provisionar novos ambientes para o projeto.
- Em revisões de readiness antes de sprints ou releases.

## Seções

### 1. Informações Gerais
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| Responsável | `[nome]` |
| Data | `[YYYY-MM-DD]` |

### 2. Ambientes Necessários
| Ambiente | Propósito | Status | Responsável | Data Prevista |
|----------|-----------|--------|-------------|--------------|
| Local Dev | Desenvolvimento individual | `[Pronto/Em progresso/Pendente]` | `[nome]` | `[data]` |
| CI/CD | Build e testes automatizados | `[status]` | `[nome]` | `[data]` |
| Staging | Testes integrados e demo | `[status]` | `[nome]` | `[data]` |
| Produção | Ambiente final | `[status]` | `[nome]` | `[data]` |

### 3. Checklist por Ambiente

#### Desenvolvimento Local
- [ ] Repositório criado e acessível
- [ ] README com instruções de setup
- [ ] Docker Compose / devcontainer configurado
- [ ] Variáveis de ambiente documentadas
- [ ] Seeds/fixtures de dados disponíveis
- [ ] Testes rodando localmente

#### CI/CD
- [ ] Pipeline configurado (`[GitHub Actions / GitLab CI / Jenkins]`)
- [ ] Build automatizado
- [ ] Testes automatizados no pipeline
- [ ] Análise estática de código (linting)
- [ ] Scan de segurança configurado
- [ ] Deploy automatizado para staging

#### Staging
- [ ] Infraestrutura provisionada
- [ ] Banco de dados configurado com dados de teste
- [ ] Integrações externas apontando para sandbox
- [ ] SSL/TLS configurado
- [ ] Monitoramento básico ativo
- [ ] Acesso concedido à equipe

#### Produção
- [ ] Infraestrutura provisionada e revisada
- [ ] Banco de dados configurado com backup automático
- [ ] Integrações externas configuradas
- [ ] SSL/TLS com certificado válido
- [ ] Monitoramento e alertas configurados
- [ ] Logs centralizados
- [ ] Plano de disaster recovery documentado

### 4. Dependências de Infraestrutura
| Dependência | Tipo | Responsável | Status | Bloqueante? |
|-------------|------|-------------|--------|------------|
| `[serviço/recurso]` | `[Cloud/On-prem/SaaS]` | `[equipe]` | `[status]` | `[Sim/Não]` |

### 5. Acessos Necessários
| Sistema/Serviço | Perfil | Solicitado Para | Status |
|----------------|--------|----------------|--------|
| `[sistema]` | `[admin/dev/read-only]` | `[nomes]` | `[Concedido/Pendente]` |

### 6. Configurações de Segurança
| Item | Configuração | Status |
|------|-------------|--------|
| Secrets Management | `[Vault/AWS Secrets Manager/etc.]` | `[status]` |
| Network Policies | `[VPC/Firewall/etc.]` | `[status]` |
| IAM/Permissions | `[least privilege configurado]` | `[status]` |

## Exemplo de Preenchimento

### 2. Ambientes Necessários
| Ambiente | Propósito | Status | Responsável | Data Prevista |
|----------|-----------|--------|-------------|--------------|
| Local Dev | Desenvolvimento individual | Pronto | DevOps Team | 2026-03-10 |
| CI/CD | Build e testes automatizados | Pronto | DevOps Team | 2026-03-12 |
| Staging | Testes integrados e demo | Em progresso | DevOps Team | 2026-03-20 |
| Produção | Ambiente final | Pendente | DevOps Team | 2026-04-01 |

## Dicas de Qualidade
- **Ambiente antes do código:** Desenvolvedores não devem esperar por ambientes.
- **Paridade de ambientes:** Quanto mais parecidos dev/staging/prod, menos surpresas.
- **Automatize o provisioning:** Ambientes manuais são ambientes inconsistentes.
- **Documente variáveis de ambiente:** Toda config deve estar documentada e versionada.
- **Teste o ambiente:** Um ambiente "pronto" significa que uma aplicação roda nele, não apenas que foi provisionado.
