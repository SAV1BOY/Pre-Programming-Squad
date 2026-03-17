# Environment Readiness Framework

## Propósito
Framework para garantir que ambientes de desenvolvimento, teste e staging estão prontos antes de iniciar implementação.

## Quando Usar
- Durante a fase de pré-programação quando o contexto exige este tipo de análise
- Quando há complexidade ou incerteza no aspecto coberto por este framework
- Como parte do pipeline padrão para projetos de média/alta complexidade

## Processo / Passos

### Passo 1
Mapear ambientes necessários (dev, test, staging, preview)

### Passo 2
Verificar acessos e permissões para o time

### Passo 3
Validar ferramentas e dependências instaladas

### Passo 4
Preparar mocks e stubs para serviços externos

### Passo 5
Configurar CI/CD pipeline básico

### Passo 6
Validar datasets de teste e fixtures

## Armadilhas Comuns

- **Assumir que ambientes existentes estão prontos**
- **Não testar acessos e permissões antes do kick-off**
- **Deixar configuração de CI/CD para depois**
- **Não preparar dados de teste realistas**

## Output Esperado
Documento estruturado com análise, decisões e justificativas seguindo os passos acima.

## Frameworks Relacionados
Consultar `config.yaml` para ver quais outros frameworks são acionados junto com este no pipeline de cada tipo de projeto.
