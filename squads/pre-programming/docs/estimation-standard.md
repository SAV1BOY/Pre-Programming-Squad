# Standard para Estimativa de Esforço

## Propósito

Definir o processo para produzir estimativas de esforço confiáveis, transparentes e com incerteza explícita. Estimativas bem feitas permitem planejamento realista, alocação adequada de recursos e expectativas calibradas com stakeholders.

## Escopo

Todo projeto que passa pela pipeline do Pre-Programming Squad produz uma estimativa de esforço antes do handoff.

## Definições

| Termo | Definição |
|---|---|
| Estimativa | Previsão informada de esforço, não compromisso contratual |
| Cone de incerteza | Faixa de variação que diminui conforme o projeto avança e a informação aumenta |
| Story points / Dias ideais | Unidades de esforço — o squad usa dias ideais (dia de trabalho focado sem interrupções) |
| Fator de ajuste | Multiplicador que converte dias ideais em dias calendário (reuniões, interrupções, contexto switching) |
| Contingência | Margem adicionada para riscos identificados |

## Processo

### 1. Decomposição do Trabalho

Quebrar o projeto em unidades estimáveis:

**Regra:** Nenhuma unidade deve ter mais de 5 dias ideais. Se tiver, decompor mais.

**Categorias de trabalho a incluir:**
- Desenvolvimento de funcionalidades (código novo)
- Integração com sistemas existentes
- Migração de dados (se aplicável)
- Testes (unitários, integração, e2e, carga)
- Configuração de infraestrutura
- Observabilidade (métricas, alertas, dashboards)
- Documentação (runbook, API docs, ADRs)
- Code review e ajustes

### 2. Estimar Cada Unidade

Para cada unidade de trabalho, produzir 3 estimativas:

| Cenário | Definição | Quando Acontece |
|---|---|---|
| **Melhor caso** | Tudo corre bem, sem surpresas, sem impedimentos | ~10% das vezes |
| **Caso esperado** | Algumas dificuldades normais, impedimentos menores | ~60% das vezes |
| **Pior caso** | Dificuldades significativas, impedimentos, retrabalho | ~30% das vezes |

**Estimativa ponderada:** (Melhor + 4x Esperado + Pior) / 6

### 3. Aplicar Fatores de Ajuste

**Fator de produtividade:** Converter dias ideais para dias calendário:
- Time experiente no domínio e stack: fator 1.3x
- Time com experiência parcial: fator 1.5x
- Time novo no domínio ou stack: fator 2.0x

**Fator de incerteza:** Adicionar margem conforme nível de informação:
- Escopo bem definido, tecnologia conhecida: +10-20%
- Escopo definido, alguma incerteza técnica: +20-40%
- Escopo parcialmente definido, incerteza alta: +40-70%
- Escopo exploratório, muita incerteza: +70-100%

### 4. Identificar Riscos à Estimativa

Para cada risco que pode afetar a estimativa:

| Risco | Impacto na estimativa | Probabilidade | Contingência |
|---|---|---|---|
| [Integração com API terceira falha] | +5 dias (implementar fallback) | Média | Incluir na margem |
| [DBA não disponível na semana 2] | +3 dias (espera) | Alta | Agendar agora |

### 5. Documentar a Estimativa

```
## Estimativa — [Nome do Projeto]

### Resumo
- Esforço total estimado: [X] dias ideais ([Y]-[Z] dias calendário)
- Fator de ajuste aplicado: [valor]x — [justificativa]
- Margem de incerteza: +[N]% — [justificativa]
- Premissas: [lista]

### Decomposição

| Componente | Melhor | Esperado | Pior | Ponderado |
|---|---|---|---|---|
| [Modelo de dados + migrations] | 1d | 2d | 4d | 2.2d |
| [API endpoints] | 3d | 5d | 8d | 5.2d |
| [Integração com serviço X] | 2d | 3d | 7d | 3.5d |
| [Testes] | 2d | 3d | 5d | 3.2d |
| [Observabilidade] | 1d | 1d | 2d | 1.2d |
| [Documentação] | 0.5d | 1d | 1d | 0.9d |
| **Subtotal** | | | | **16.2d** |
| Fator de ajuste (1.5x) | | | | **24.3d** |
| Margem de incerteza (+30%) | | | | **31.6d** |
| **Total** | | | | **~32 dias calendário (6.4 semanas)** |

### Premissas
1. Time de 2 engenheiros dedicados full-time
2. Ambiente de staging disponível desde o dia 1
3. API do parceiro X com documentação atualizada e sandbox funcional
4. DBA disponível para revisão de schema na semana 1

### Se as premissas mudarem
- Se o time tiver apenas 1 engenheiro: prazo dobra (~13 semanas)
- Se API do parceiro não tiver sandbox: +2 semanas para mock
- Se DBA não estiver disponível: bloqueio de 3-5 dias
```

### 6. Validar a Estimativa

- Comparar com projetos similares passados (quando houver dados)
- Revisar com pelo menos 1 par do squad
- Apresentar faixa (não número único) ao solicitante
- Destacar premissas e dependências

## Critérios de Qualidade

- Estimativa decomposta (não um número único sem detalhamento)
- Três cenários (melhor, esperado, pior) para cada componente
- Premissas documentadas com impacto se falharem
- Fator de ajuste justificado
- Margem de incerteza proporcional ao nível de informação
- Comparação com projetos anteriores (quando disponível)
- Revisão por par antes de comunicar ao solicitante

## Responsáveis

| Papel | Responsabilidade |
|---|---|
| Membro do squad | Produzir estimativa com decomposição e premissas |
| Tech Lead | Calibrar estimativa, validar fatores de ajuste |
| Par revisor | Verificar completude e razoabilidade |
| Time de implementação (quando disponível) | Validar estimativa antes do handoff |

## Referências

- Standard de Scoping: `docs/scoping-standard.md`
- Standard de Handoff: `docs/handoff-standard.md`
- Linguagem de Incerteza: `voice/language/uncertainty-language.md`
