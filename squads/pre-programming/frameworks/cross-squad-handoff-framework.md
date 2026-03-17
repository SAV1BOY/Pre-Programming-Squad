# Cross-Squad Handoff Framework

## Propósito
Framework para estruturar handoffs bidirecionais entre squads do MMOS, garantindo que artefatos, contratos e expectativas estejam alinhados.

## Quando Usar
- Durante a fase de pré-programação quando o contexto exige este tipo de análise
- Quando há complexidade ou incerteza no aspecto coberto por este framework
- Como parte do pipeline padrão para projetos de média/alta complexidade

## Processo / Passos

### Passo 1
Identificar squads envolvidos e tipo de handoff (entrada ou saída)

### Passo 2
Definir artefatos obrigatórios para cada direção

### Passo 3
Estabelecer contratos de interface (dados, formato, SLA)

### Passo 4
Validar completude com checklist de handoff cross-squad

### Passo 5
Confirmar recebimento e compreensão pelo squad receptor

### Passo 6
Registrar no handoff registry com data e responsáveis

## Armadilhas Comuns

- **Assumir que o outro squad já sabe o contexto**
- **Enviar artefatos incompletos e esperar que o receptor complete**
- **Não definir SLAs de resposta entre squads**
- **Ignorar dependências cíclicas entre squads**

## Output Esperado
Documento estruturado com análise, decisões e justificativas seguindo os passos acima.

## Frameworks Relacionados
Consultar `config.yaml` para ver quais outros frameworks são acionados junto com este no pipeline de cada tipo de projeto.
