# Data Migration Readiness Framework

## Propósito
Framework para planejar migrações de dados com segurança, validação e rollback.

## Quando Usar
- Durante a fase de pré-programação quando o contexto exige este tipo de análise
- Quando há complexidade ou incerteza no aspecto coberto por este framework
- Como parte do pipeline padrão para projetos de média/alta complexidade

## Processo / Passos

### Passo 1
Mapear dados de origem e destino (schema, volume, qualidade)

### Passo 2
Definir regras de transformação e mapeamento

### Passo 3
Estabelecer critérios de validação pós-migração

### Passo 4
Planejar migração incremental vs big-bang

### Passo 5
Preparar rollback plan com verificação de integridade

### Passo 6
Definir janela de migração e comunicação

## Armadilhas Comuns

- **Não validar qualidade dos dados de origem**
- **Migrar sem rollback plan testado**
- **Subestimar o tempo de migração para volumes grandes**
- **Não comunicar downtime ou impacto para usuários**

## Output Esperado
Documento estruturado com análise, decisões e justificativas seguindo os passos acima.

## Frameworks Relacionados
Consultar `config.yaml` para ver quais outros frameworks são acionados junto com este no pipeline de cada tipo de projeto.
