# Standard para Revisão de Riscos

## Propósito

Estabelecer o processo de identificação, classificação e planejamento de mitigação de riscos técnicos e de negócio em projetos durante a fase de pré-programação. A revisão de riscos é preventiva — identifica problemas potenciais antes que se materializem em produção.

## Escopo

Todo projeto na pipeline do Pre-Programming Squad. Projetos P recebem revisão simplificada; projetos M/G/XG recebem revisão completa.

## Definições

| Termo | Definição |
|---|---|
| Risco | Evento incerto que, se ocorrer, terá impacto negativo no projeto ou sistema |
| Probabilidade | Estimativa da chance de o risco se materializar (Alta/Média/Baixa) |
| Impacto | Severidade da consequência se o risco se materializar (Crítico/Alto/Médio/Baixo) |
| Mitigação | Ação que reduz probabilidade ou impacto do risco |
| Contingência | Plano de ação para o caso de o risco se materializar apesar da mitigação |
| Risco residual | Risco remanescente após aplicação da mitigação |

## Processo

### 1. Identificação de Riscos

Examinar o projeto sob as seguintes categorias:

**Riscos Técnicos:**
- Complexidade da solução (tecnologia nova, padrão desconhecido)
- Dependências externas (APIs terceiras, serviços de outros times)
- Escalabilidade (volume previsto vs. capacidade do design)
- Integridade de dados (migração, consistência, backup)
- Performance (latência, throughput, uso de recursos)
- Segurança (autenticação, autorização, exposição de dados)

**Riscos de Projeto:**
- Escopo (scope creep, requisitos ambíguos, premissas frágeis)
- Prazo (dependências de entrega, janelas regulatórias)
- Capacidade do time (skill gap, disponibilidade, rotatividade)
- Comunicação (stakeholders muitos, prioridades conflitantes)

**Riscos de Negócio:**
- Impacto financeiro (receita em risco, custos não previstos)
- Regulatório (compliance, LGPD, PCI-DSS)
- Reputacional (experiência do usuário, disponibilidade)

### 2. Classificação

Para cada risco identificado, atribuir:

**Matriz de Probabilidade x Impacto:**

| | Impacto Baixo | Impacto Médio | Impacto Alto | Impacto Crítico |
|---|---|---|---|---|
| **Prob. Alta** | Médio | Alto | Crítico | Crítico |
| **Prob. Média** | Baixo | Médio | Alto | Crítico |
| **Prob. Baixa** | Baixo | Baixo | Médio | Alto |

**Justificativa obrigatória:** Cada classificação de probabilidade e impacto deve ser justificada com evidência ou raciocínio explícito.

### 3. Planejamento de Resposta

Para cada risco classificado como Médio ou superior:

| Estratégia | Quando Usar | Exemplo |
|---|---|---|
| **Mitigar** | É possível reduzir probabilidade ou impacto | Adicionar testes de carga antes do deploy |
| **Transferir** | Outro time/fornecedor pode gerenciar melhor | Delegar operação de infra para SRE |
| **Aceitar** | Custo de mitigação excede impacto esperado | Aceitar risco de 0.1% de conflito |
| **Evitar** | Eliminar a causa raiz | Mudar design para remover dependência |

### 4. Documentação

Formato obrigatório por risco:

```
### Risco [N] — [Título descritivo]
- **Categoria:** [Técnico / Projeto / Negócio]
- **Descrição:** [O que pode acontecer]
- **Probabilidade:** [Alta/Média/Baixa] — [Justificativa]
- **Impacto:** [Crítico/Alto/Médio/Baixo] — [Justificativa]
- **Classificação:** [Resultado da matriz]
- **Estratégia:** [Mitigar/Transferir/Aceitar/Evitar]
- **Ação:** [O que será feito, por quem, até quando]
- **Indicador antecedente:** [Métrica/sinal que indica materialização]
- **Contingência:** [O que fazer se acontecer mesmo assim]
```

### 5. Revisão e Monitoramento

- Riscos revisados a cada Pipeline Review (2x/semana)
- Riscos críticos comunicados imediatamente ao Tech Lead e stakeholders
- Revisão formal de todos os riscos no gate de go/no-go

## Critérios de Qualidade

- Todas as 3 categorias de risco avaliadas (técnico, projeto, negócio)
- Classificação com justificativa (não apenas "alta" ou "baixa")
- Plano de mitigação para todo risco Médio ou superior
- Owner e prazo definidos para cada ação de mitigação
- Riscos aceitos têm justificativa documentada e aprovação do Tech Lead

## Responsáveis

| Papel | Responsabilidade |
|---|---|
| Membro do squad | Identificar e documentar riscos, propor mitigações |
| Tech Lead | Validar classificação, aprovar riscos aceitos, escalar riscos críticos |
| Stakeholders | Fornecer contexto de negócio, validar impacto estimado |
| EM | Remover bloqueios de mitigação, alocar recursos quando necessário |

## Referências

- Standard de Arquitetura: `docs/architecture-review-standard.md`
- Standard de Segurança: `docs/security-precheck-standard.md`
- Standard de Go/No-Go: `docs/go-no-go-standard.md`
- Linguagem de Risco: `voice/language/risk-language.md`
