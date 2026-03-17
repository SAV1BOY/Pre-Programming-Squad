# Ótimos Project Briefs — Exemplos Anotados

## Introdução

Um project brief excepcional comunica a essência de um projeto em poucas páginas. Ele responde com clareza: qual problema estamos resolvendo, para quem, por que agora, como mediremos sucesso e quais são as restrições. Os melhores briefs são aqueles que qualquer pessoa na organização consegue ler e entender, não apenas os envolvidos diretamente.

Este documento apresenta exemplos anotados de project briefs que se destacaram pela clareza, completude e capacidade de alinhar stakeholders.

---

## Exemplo 1 — Brief de Migração de Sistema de Pagamentos

### O Brief

> **Problema**: Nosso gateway de pagamento atual (Legado Pay) tem 99.2% de uptime, abaixo do SLA de 99.9% que prometemos aos sellers. Nos últimos 6 meses, 3 incidentes causaram R$2.4M em vendas perdidas. O contrato com o fornecedor vence em 8 meses.
>
> **Solução Proposta**: Migrar para arquitetura multi-gateway com failover automático, usando Stripe como primário e Adyen como backup, com camada de abstração própria.
>
> **Métricas de Sucesso**: Uptime >= 99.95%, tempo de failover < 30s, zero vendas perdidas por indisponibilidade de pagamento.
>
> **Escopo**: Cartão de crédito e PIX. Boleto fica para fase 2. Marketplace internacional fora de escopo.
>
> **Restrições**: Migração deve ser transparente para sellers. Zero downtime. Budget de R$800K para 6 meses.

### Por que funciona

- **Problema quantificado**: R$2.4M em perdas dá urgência real, não abstrata
- **Solução com arquitetura clara**: Multi-gateway com failover, não apenas "melhorar pagamentos"
- **Métricas específicas e mensuráveis**: 99.95%, 30 segundos, zero perdas
- **Escopo com exclusões explícitas**: Saber o que NÃO está incluído é tão importante quanto o incluído
- **Restrições realistas**: Budget, prazo e requisitos não-funcionais claros

---

## Exemplo 2 — Brief de Plataforma de Onboarding de Sellers

### O Brief

> **Problema**: O onboarding de novos sellers leva em média 14 dias e envolve 23 etapas manuais distribuídas entre 4 departamentos. 35% dos leads desistem no processo. Nosso principal concorrente faz em 48 horas.
>
> **Solução Proposta**: Plataforma de auto-onboarding digital com verificação automatizada de documentos (OCR + validação em bases públicas), contrato eletrônico e provisionamento automático de loja.
>
> **Métricas de Sucesso**: Tempo médio de onboarding <= 72h. Taxa de desistência <= 10%. NPS do processo >= 70. Redução de 80% em trabalho manual operacional.
>
> **Fora de Escopo**: Sellers internacionais. Categorias reguladas (farmácia, armas). Migração de sellers existentes.
>
> **Premissas Críticas**: API da Receita Federal permanecerá disponível. Jurídico aprovará contrato eletrônico via DocuSign. Time de compliance validará regras de KYC em até 2 semanas.

### Por que funciona

- **Benchmarking competitivo**: Comparação com concorrente cria senso de urgência estratégica
- **Dados do funil**: 35% de desistência quantifica a dor
- **Solução tecnicamente específica**: OCR, validação em bases públicas, contrato eletrônico
- **Premissas críticas explícitas**: Declara o que precisa ser verdade para o projeto funcionar

---

## Exemplo 3 — Brief de Sistema de Recomendação

### O Brief

> **Problema**: Nossa taxa de conversão no catálogo é de 2.1%, enquanto a média do setor é 3.8%. Análise de comportamento mostra que 68% dos usuários saem após visualizar apenas 3 produtos. Não temos personalização — todos veem o mesmo catálogo.
>
> **Solução Proposta**: Motor de recomendação baseado em collaborative filtering com fallback para popularity-based, integrado na home, páginas de produto e carrinho. Fase 1 com modelo batch (atualização diária), Fase 2 com modelo real-time.
>
> **Métricas de Sucesso**: Aumentar taxa de conversão em 0.5pp (de 2.1% para 2.6%) em 3 meses. Aumentar produtos visualizados por sessão de 3 para 5. CTR das recomendações >= 8%.
>
> **Restrições**: LGPD — todo processamento deve ser consentido e rastreável. Latência de renderização das recomendações < 200ms. Não pode degradar performance do catálogo existente.

### Por que funciona

- **Gap mensurável**: 2.1% vs 3.8% do setor — oportunidade clara
- **Abordagem em fases**: Batch primeiro, real-time depois — pragmatismo
- **Metas incrementais**: 0.5pp de aumento, não "dobrar a conversão"
- **Restrições regulatórias**: LGPD mencionada desde o brief, não como surpresa tardia

---

## Lições Extraídas

1. **Quantifique o problema**: Briefs sem números são opiniões disfarçadas de projetos
2. **Seja específico no escopo**: "Fora de escopo" é tão importante quanto "dentro do escopo"
3. **Declare premissas**: Premissas ocultas matam projetos — exponha-as no brief
4. **Defina métricas antes de começar**: Se não sabe como medir sucesso, não está pronto para começar
5. **Use comparações**: Benchmarks de concorrentes ou da indústria contextualizam o problema
6. **Mantenha curto**: Se o brief tem mais de 3 páginas, provavelmente não está claro o suficiente
7. **Escreva para não-técnicos**: O brief deve ser compreensível por qualquer stakeholder
8. **Inclua restrições reais**: Budget, prazo, regulação, dependências — tudo no brief
