# Cognitive Load Assessment Framework

## Propósito
Framework para avaliar e reduzir a carga cognitiva de decisões arquiteturais e de design, baseado em Team Topologies e Ousterhout.

## Quando Usar
- Durante a fase de pré-programação quando o contexto exige este tipo de análise
- Quando há complexidade ou incerteza no aspecto coberto por este framework
- Como parte do pipeline padrão para projetos de média/alta complexidade

## Processo / Passos

### Passo 1
Identificar decisões que o time precisa tomar

### Passo 2
Classificar cada decisão por complexidade cognitiva (baixa/média/alta)

### Passo 3
Mapear dependências entre decisões

### Passo 4
Sequenciar decisões para minimizar carga simultânea

### Passo 5
Simplificar decisões complexas quebrando em sub-decisões

### Passo 6
Documentar decisões tomadas para reduzir carga futura

## Armadilhas Comuns

- **Subestimar o impacto de context-switching**
- **Não considerar experiência do time ao avaliar carga**
- **Tratar todas as decisões como igualmente importantes**
- **Não documentar decisões, forçando re-decisão futura**

## Output Esperado
Documento estruturado com análise, decisões e justificativas seguindo os passos acima.

## Frameworks Relacionados
Consultar `config.yaml` para ver quais outros frameworks são acionados junto com este no pipeline de cada tipo de projeto.
