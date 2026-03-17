# Standard para Readiness de Legado

## Propósito

Definir o processo de avaliação de sistemas legados que serão impactados ou substituídos por um novo projeto. Garante que a realidade do legado seja compreendida antes da implementação, evitando surpresas com comportamentos não documentados, dependências ocultas e dados inconsistentes.

## Escopo

Projetos que envolvam: migração de sistema legado, integração com sistema legado, substituição parcial ou total de funcionalidade existente, ou mudança de schema em banco compartilhado com sistema legado.

## Definições

| Termo | Definição |
|---|---|
| Sistema legado | Software em produção que será substituído, alterado ou integrado pelo novo projeto |
| Comportamento não documentado | Funcionalidade ou regra de negócio implementada no código mas não descrita em nenhuma documentação |
| Dependência oculta | Integração ou consumidor do sistema que não está documentado formalmente |
| Dados órfãos | Registros no banco de dados que não correspondem mais a regras de negócio ativas |

## Processo

### 1. Mapeamento do Sistema Legado

**Inventário funcional:**
- Quais funcionalidades o sistema executa?
- Quais delas serão substituídas pelo novo projeto?
- Quais permanecerão no legado (escopo parcial)?
- Existem funcionalidades que ninguém sabe se ainda são usadas?

**Inventário técnico:**
- Stack tecnológica (linguagem, framework, versões)
- Banco de dados (tipo, tamanho, schema)
- Integrações (APIs consumidas e expostas, filas, jobs, cron)
- Infraestrutura (onde roda, como faz deploy, como escala)
- Observabilidade (logs, métricas, alertas existentes)

**Inventário de conhecimento:**
- Quem no time conhece o sistema? Nível de profundidade?
- Existe documentação? Está atualizada?
- Último deploy significativo — quando, por quem?
- Histórico de incidentes (frequência, causas recorrentes)

### 2. Investigação de Comportamentos Não Documentados

**Técnicas:**
- Análise de código para regras de negócio implícitas
- Comparação entre documentação e implementação real
- Entrevistas com pessoas que operam o sistema
- Análise de logs para identificar padrões de uso real
- Revisão de tickets de suporte para entender edge cases reportados

**Documentar:**
- Lista de regras de negócio encontradas no código e não na documentação
- Comportamentos especiais para edge cases (ex: "se o valor é zero, faz X diferente")
- Jobs agendados e suas funções
- Flags de configuração e seus efeitos

### 3. Mapeamento de Dependências

**Consumidores:**
- Quais sistemas/serviços consomem dados ou APIs deste legado?
- Qual o volume e a frequência de acesso?
- Existem consumidores informais (queries diretas no banco, scripts manuais)?

**Dependências:**
- De quais sistemas este legado depende?
- Quais são críticas (falha nelas = falha aqui)?
- Existem dependências de versão específica?

**Dados:**
- Quais outros sistemas leem/escrevem no banco deste legado?
- Existem views, stored procedures ou triggers que outros sistemas usam?
- Existe replicação de dados para outros destinos (data warehouse, analytics)?

### 4. Avaliação de Dados

- Volume de dados e taxa de crescimento
- Qualidade dos dados (registros com nulls inesperados, dados inconsistentes, duplicatas)
- Dados órfãos ou obsoletos
- Necessidade de migração e estimativa de complexidade
- Mapeamento de schema: campos, tipos, constraints, diferenças com o novo modelo

### 5. Análise de Risco do Legado

| Categoria | Perguntas |
|---|---|
| **Estabilidade** | O sistema é estável? Qual a frequência de incidentes? |
| **Modificabilidade** | É seguro alterar este sistema? Existe suite de testes? |
| **Operabilidade** | Quem sabe operar? O que acontece se der problema durante a migração? |
| **Documentação** | A documentação é confiável? Onde há gaps? |
| **Dados** | Os dados são limpos o suficiente para migrar? Qual o esforço de limpeza? |

### 6. Plano de Coexistência

Se legado e novo sistema coexistirão durante um período:
- Qual a estratégia de coexistência (dual-write, feature flag, roteamento gradual)?
- Como garantir consistência de dados entre os dois?
- Qual o critério para desligar o legado?
- Qual o plano de rollback se o novo falhar?
- Quanto tempo dura o período de coexistência?

## Critérios de Qualidade

- Inventário funcional e técnico completos
- Comportamentos não documentados identificados e registrados
- Dependências mapeadas (consumidores e fornecedores)
- Qualidade dos dados avaliada com números concretos
- Riscos classificados com plano de mitigação
- Plano de coexistência definido (quando aplicável)
- Pelo menos 1 pessoa que conhece o legado revisou o documento

## Responsáveis

| Papel | Responsabilidade |
|---|---|
| Membro do squad | Conduzir investigação, documentar achados |
| Conhecedor do legado | Fornecer contexto, validar achados, identificar armadilhas |
| DBA | Avaliar dados, schema, dependências de banco |
| Tech Lead | Validar completude, avaliar riscos, aprovar plano de coexistência |

## Referências

- Standard de Discovery: `docs/discovery-standard.md`
- Standard de Revisão de Riscos: `docs/risk-review-standard.md`
- Standard de Arquitetura: `docs/architecture-review-standard.md`
