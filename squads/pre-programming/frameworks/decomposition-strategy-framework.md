# Decomposition Strategy Framework

## Propósito
Framework para quebrar problemas complexos em partes implementáveis, ordenáveis e com dependências claras.

## Quando Usar
- Durante a fase de pré-programação quando o contexto exige este tipo de análise
- Quando há complexidade ou incerteza no aspecto coberto por este framework
- Como parte do pipeline padrão para projetos de média/alta complexidade

## Processo / Passos

### Passo 1
Identificar o problema ou feature de alto nível

### Passo 2
Decompor em módulos funcionais independentes

### Passo 3
Mapear dependências entre módulos

### Passo 4
Ordenar por: dependência técnica > valor > risco

### Passo 5
Definir interfaces e contratos entre módulos

### Passo 6
Validar que cada módulo é implementável e testável isoladamente

## Armadilhas Comuns

- **Decompor demais — partes tão pequenas que perdem contexto**
- **Decompor de menos — partes ainda muito complexas**
- **Ignorar dependências cíclicas**
- **Não definir contratos entre partes**

## Output Esperado
Documento estruturado com análise, decisões e justificativas seguindo os passos acima.

## Frameworks Relacionados
Consultar `config.yaml` para ver quais outros frameworks são acionados junto com este no pipeline de cada tipo de projeto.
