# Technical Debt Assessment Framework

## Propósito
Framework para identificar, classificar e priorizar dívida técnica antes da implementação, evitando que novo código herde problemas existentes.

## Quando Usar
- Durante a fase de pré-programação quando o contexto exige este tipo de análise
- Quando há complexidade ou incerteza no aspecto coberto por este framework
- Como parte do pipeline padrão para projetos de média/alta complexidade

## Processo / Passos

### Passo 1
Mapear áreas do código/sistema que serão tocadas

### Passo 2
Identificar dívida técnica existente nessas áreas

### Passo 3
Classificar dívida por tipo (design, código, teste, infra, doc)

### Passo 4
Avaliar impacto da dívida no novo trabalho

### Passo 5
Decidir: pagar agora, pagar depois, ou aceitar

### Passo 6
Registrar decisões no decision log com justificativa

## Armadilhas Comuns

- **Ignorar dívida existente e construir em cima**
- **Querer pagar toda a dívida antes de qualquer implementação**
- **Não quantificar o custo de manter vs pagar a dívida**
- **Confundir dívida deliberada (trade-off) com dívida acidental (descuido)**

## Output Esperado
Documento estruturado com análise, decisões e justificativas seguindo os passos acima.

## Frameworks Relacionados
Consultar `config.yaml` para ver quais outros frameworks são acionados junto com este no pipeline de cada tipo de projeto.
