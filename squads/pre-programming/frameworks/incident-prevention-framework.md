# Incident Prevention Framework

## Propósito
Framework para antecipar e prevenir incidentes em produção durante a fase de pré-programação.

## Quando Usar
- Durante a fase de pré-programação quando o contexto exige este tipo de análise
- Quando há complexidade ou incerteza no aspecto coberto por este framework
- Como parte do pipeline padrão para projetos de média/alta complexidade

## Processo / Passos

### Passo 1
Revisar incidentes históricos de sistemas similares

### Passo 2
Identificar pontos de falha no design proposto

### Passo 3
Definir circuit breakers e fallbacks

### Passo 4
Planejar graceful degradation

### Passo 5
Definir alertas proativos

### Passo 6
Documentar runbooks de resposta

## Armadilhas Comuns

- **Confiar apenas em monitoramento reativo**
- **Não estudar incidentes históricos**
- **Design sem fallback para dependências externas**
- **Não testar cenários de falha antes de produção**

## Output Esperado
Documento estruturado com análise, decisões e justificativas seguindo os passos acima.

## Frameworks Relacionados
Consultar `config.yaml` para ver quais outros frameworks são acionados junto com este no pipeline de cada tipo de projeto.
