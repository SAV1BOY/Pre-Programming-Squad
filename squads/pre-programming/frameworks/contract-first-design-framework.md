# Contract-First Design Framework

## Propósito
Framework para definir contratos de API e interface antes de iniciar implementação, garantindo alinhamento entre consumer e provider.

## Quando Usar
- Durante a fase de pré-programação quando o contexto exige este tipo de análise
- Quando há complexidade ou incerteza no aspecto coberto por este framework
- Como parte do pipeline padrão para projetos de média/alta complexidade

## Processo / Passos

### Passo 1
Identificar todos os pontos de integração do sistema

### Passo 2
Para cada integração, definir consumer e provider

### Passo 3
Documentar contrato: endpoint, payload, erros, SLA

### Passo 4
Validar contrato com ambos os lados (consumer e provider)

### Passo 5
Definir estratégia de versionamento

### Passo 6
Planejar contract tests

## Armadilhas Comuns

- **Definir contrato apenas do lado do provider**
- **Não versionar contratos desde o início**
- **Ignorar cenários de erro e timeout no contrato**
- **Não testar contratos automaticamente**

## Output Esperado
Documento estruturado com análise, decisões e justificativas seguindo os passos acima.

## Frameworks Relacionados
Consultar `config.yaml` para ver quais outros frameworks são acionados junto com este no pipeline de cada tipo de projeto.
