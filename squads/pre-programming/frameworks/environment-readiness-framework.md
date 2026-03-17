# Environment Readiness Framework

## Propósito
Garantir que ambientes de desenvolvimento, teste e staging estão prontos antes do kick-off de implementação. Ambiente não pronto = time parado = desperdício.

## Problema que Resolve
Times começam a implementar e descobrem que: não têm acesso ao repo, CI/CD não está configurado, ambiente de teste não existe, mocks não estão prontos. Dias perdidos que poderiam ser evitados com preparação.

## Quando Usar
- Na fase de Readiness, antes do handoff para Coding Squad
- Quando o projeto requer infraestrutura nova
- Quando há integrações com serviços externos que precisam de mocks/sandboxes
- Em projetos com requisitos de dados de teste específicos

## Checklist de Readiness por Ambiente

### Desenvolvimento
- [ ] Repositório criado com branch strategy definida
- [ ] Acessos configurados para todos os devs
- [ ] Dependências documentadas e instaláveis
- [ ] Variáveis de ambiente documentadas (.env.example)
- [ ] Docker/dev containers configurados (se aplicável)
- [ ] Linter e formatador configurados

### Teste
- [ ] Ambiente de teste isolado disponível
- [ ] Dados de teste preparados (fixtures, seeds, factories)
- [ ] Mocks/stubs para serviços externos configurados
- [ ] CI pipeline executando testes automaticamente
- [ ] Cobertura de testes configurada e reportando

### Staging/Preview
- [ ] Ambiente de staging acessível
- [ ] Deploy automatizado para staging
- [ ] Dados representativos carregados
- [ ] Feature flags configurados (se aplicável)
- [ ] Monitoramento básico ativo

### Observabilidade
- [ ] Logging configurado e acessível
- [ ] Métricas básicas sendo coletadas
- [ ] Alertas críticos configurados
- [ ] Dashboard de saúde disponível

## Processo

### Passo 1 — Inventariar Necessidades
Baseado no architecture sketch, listar:
- Serviços a serem criados/modificados
- Dependências externas (APIs, databases, queues)
- Ferramentas necessárias (CI/CD, monitoramento)

### Passo 2 — Atribuir Responsáveis
| Necessidade | Responsável | Prazo |
|-------------|-------------|-------|
| Repo + CI/CD | DevOps / Platform | D-3 antes do kick-off |
| Mocks de APIs externas | Backend dev + Pre-Prog | D-2 |
| Dados de teste | QA + Domain expert | D-2 |
| Acessos e permissões | Tech Lead | D-3 |

### Passo 3 — Validar Antes do Handoff
O Handoff Orchestrator verifica todos os itens do checklist antes de declarar readiness.

## Armadilhas
- **"O ambiente já existe"** → Verificar se está atualizado e funcional, não apenas se existe
- **Dados de teste genéricos** → Dados devem representar cenários reais do projeto
- **Mocks que não refletem comportamento real** → Mock deve simular latência, erros e edge cases
- **Deixar CI/CD para depois** → Sem CI, bugs são descobertos manualmente = lento
