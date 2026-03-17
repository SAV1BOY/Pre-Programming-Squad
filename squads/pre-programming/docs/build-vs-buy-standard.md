# Standard para Decisão Build vs. Buy

## Propósito

Estabelecer um processo estruturado para decidir entre construir uma solução interna (build) ou adquirir/adotar uma solução externa (buy — SaaS, open source, licenciamento). Garante que a decisão seja baseada em análise multidimensional e não em preferência pessoal ou viés.

## Escopo

Todo projeto em que existe uma alternativa de mercado viável para a funcionalidade desejada. Inclui decisões de SaaS, open source auto-hospedado, bibliotecas e frameworks.

## Definições

| Termo | Definição |
|---|---|
| Build | Desenvolver solução internamente com o time de engenharia |
| Buy | Adquirir solução de mercado (SaaS, licença, consultoria) |
| Adopt | Adotar solução open source, operando internamente |
| TCO | Total Cost of Ownership — custo total incluindo implementação, operação e evolução |
| Vendor lock-in | Grau de dependência de um fornecedor que dificulta migração futura |

## Processo

### 1. Definir Requisitos de Avaliação

Antes de avaliar alternativas, documentar:
- Requisitos funcionais que a solução deve atender
- Requisitos não-funcionais (performance, segurança, compliance, escalabilidade)
- Restrições (orçamento, prazo, regulatório, integração com stack existente)
- Horizonte de avaliação (1 ano, 3 anos, 5 anos)
- Critérios de decisão priorizados (custo? velocidade? controle? customização?)

### 2. Identificar Alternativas

Levantar pelo menos 3 opções:
- 1 opção de build interno
- 1-2 opções de SaaS/licenciado
- 1 opção de open source (quando existir)

Para cada alternativa, coletar:
- Funcionalidades oferecidas vs. requisitos
- Modelo de pricing e projeção de custo
- Referências de empresas similares que usam
- Limitações conhecidas
- Modelo de suporte e SLA

### 3. Análise Comparativa

#### Matriz de Decisão

| Critério (peso) | Build | SaaS/Vendor | Open Source |
|---|---|---|---|
| Custo total 12 meses (X%) | | | |
| Custo total 36 meses (X%) | | | |
| Time-to-market (X%) | | | |
| Adequação funcional (X%) | | | |
| Customização/flexibilidade (X%) | | | |
| Segurança e compliance (X%) | | | |
| Dependência de vendor (X%) | | | |
| Operação e manutenção (X%) | | | |
| Escala e performance (X%) | | | |
| Qualidade/experiência do time (X%) | | | |
| **Score ponderado** | | | |

#### Análise de TCO

Para cada alternativa, calcular custo total em 12 e 36 meses:

**Build:**
- Desenvolvimento: horas x custo/hora
- Infraestrutura: servidores, banco, serviços cloud
- Operação: monitoramento, on-call, manutenção
- Evolução: novas features, bug fixes, upgrades
- Oportunidade: o que o time NÃO faz enquanto constrói isso

**Buy (SaaS):**
- Licença/assinatura: custo mensal x meses
- Integração: esforço de implementação
- Customização: ajustes necessários
- Migração: custo de mover dados/processos
- Exit cost: custo de sair do fornecedor se necessário

**Adopt (Open Source):**
- Implementação: setup, configuração, customização
- Infraestrutura: hospedagem, banco, backup
- Operação: updates, patches de segurança, monitoramento
- Suporte: comunidade vs. suporte pago
- Contribuição: custos de contribuir upstream (se necessário)

### 4. Análise de Riscos por Opção

| Risco | Build | Buy | Adopt |
|---|---|---|---|
| Time-to-market excessivo | | | |
| Vendor descontinua produto | N/A | | |
| Custo escala além do previsto | | | |
| Dependência de skills específicas | | | |
| Compliance/regulatório | | | |
| Integração com stack existente | | | |

### 5. Recomendação e Decisão

Documentar:
- Recomendação com justificativa baseada na análise
- Trade-offs aceitos na opção recomendada
- Condições que invalidariam a recomendação
- Plano de saída (exit strategy) se a opção escolhida não funcionar
- Data de revisão da decisão

## Critérios de Qualidade

- Pelo menos 3 alternativas avaliadas
- TCO calculado para 12 e 36 meses
- Matriz de decisão com pesos justificados
- Riscos por opção documentados
- Decisão registrada em ADR com justificativa
- Exit strategy definida para a opção escolhida

## Responsáveis

| Papel | Responsabilidade |
|---|---|
| Membro do squad | Conduzir análise, levantar alternativas, calcular TCO |
| Tech Lead | Validar análise técnica, calibrar pesos da matriz |
| PM/Solicitante | Fornecer contexto de negócio, validar prioridade de critérios |
| Finance (para decisões > R$ 50k) | Validar projeções financeiras, aprovar orçamento |
| Patrocinador | Aprovar decisão final |

## Referências

- Standard de Arquitetura: `docs/architecture-review-standard.md`
- Standard de Estimativa: `docs/estimation-standard.md`
- Linguagem de Trade-offs: `voice/language/tradeoff-language.md`
- Linguagem de Decisão: `voice/language/decision-language.md`
