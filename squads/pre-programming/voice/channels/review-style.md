# Estilo Revisão Técnica

## Formato

Documento de revisão estruturado por áreas de análise, com severidade classificada para cada achado. Cada achado segue o padrão: observação, evidência, impacto, recomendação. Inclui sumário executivo no início e plano de ação consolidado no final.

## Estrutura

```
# Revisão Técnica — [Nome do Sistema/Projeto/Proposta]

## Metadata
- Revisor(es): [nomes e papéis]
- Data da revisão: [data]
- Artefatos revisados: [lista de documentos, código, diagramas]
- Tipo: [Arquitetura / Código / Segurança / Performance / Design]

## Sumário Executivo
[3-5 linhas: veredicto geral, achados críticos, recomendação principal]

## Achados

### [Área 1]
#### Achado 1.1 — [Título descritivo] [SEVERIDADE]
- **Observação:** [O que foi identificado]
- **Evidência:** [Dados, código, métricas que sustentam]
- **Impacto:** [Consequência se não endereçado]
- **Recomendação:** [Ação específica]

### [Área 2]
#### Achado 2.1 — ...

## Pontos Positivos
[O que está bem feito — reconhecimento explícito]

## Plano de Ação Consolidado
[Tabela com todos os achados, owner e prazo]

## Veredicto
[Aprovado / Aprovado com condições / Não aprovado — com justificativa]
```

## Tom

- Construtivo — o objetivo é melhorar, não criticar
- Objetivo — achados baseados em evidência, não opinião pessoal
- Classificado — severidade clara para priorização
- Acionável — toda observação tem recomendação concreta
- Balanceado — reconhece pontos positivos e negativos

## Audiência

- Time responsável pelo sistema/projeto revisado
- Tech leads e arquitetos que supervisionam a qualidade
- Engineering managers que precisam priorizar correções
- Registro institucional para futuras revisões

## Exemplo

```
# Revisão Técnica — Proposta de Arquitetura do Serviço de Relatórios

## Metadata
- Revisor: Pedro Santos (Architect), Julia Mendes (Staff Engineer)
- Data: 12/mar/2025
- Artefatos: RFC-019, diagrama C4 do serviço, protótipo de API
- Tipo: Revisão de Arquitetura

## Sumário Executivo

A proposta endereça bem o problema de geração de relatórios sob
demanda, mas apresenta 2 achados críticos (processamento síncrono
de relatórios pesados e ausência de estratégia de cache) e 3
moderados. Recomendamos aprovação condicionada à resolução dos
achados críticos antes da implementação.

## Achados

### Processamento

#### Achado 1.1 — Geração síncrona de relatórios pesados [CRÍTICO]
- **Observação:** A proposta processa todos os relatórios de forma
  síncrona no request HTTP, incluindo relatórios que agregam até
  6 meses de dados (~50M registros).
- **Evidência:** Benchmark do protótipo mostra timeout em relatórios
  com mais de 30 dias de dados (>45s de processamento).
- **Impacto:** Timeouts frequentes em produção; frustração do
  usuário; risco de saturar o serviço com requests pesados.
- **Recomendação:** Implementar processamento assíncrono para
  relatórios com período >7 dias. Padrão: request retorna 202
  com job ID, webhook/polling para resultado. Relatórios curtos
  (≤7 dias) podem permanecer síncronos.

#### Achado 1.2 — Ausência de limites no período do relatório [MODERADO]
- **Observação:** API aceita qualquer período sem limite máximo.
- **Evidência:** Teste com período de 5 anos gerou query que
  consumiu 100% CPU do banco por 12 minutos.
- **Impacto:** Um único request pode degradar o banco para
  todos os serviços.
- **Recomendação:** Limitar período máximo a 12 meses. Para
  períodos maiores, exigir aprovação ou gerar em batch offline.

### Cache e Performance

#### Achado 2.1 — Sem estratégia de cache para relatórios recorrentes [CRÍTICO]
- **Observação:** Análise de uso mostra que 60% dos relatórios
  são gerados com os mesmos parâmetros diariamente (dashboard
  reports). Cada execução reprocessa do zero.
- **Evidência:** Dados de uso do sistema atual: 200 relatórios/dia,
  120 com parâmetros repetidos.
- **Impacto:** Carga desnecessária no banco, custo de computação
  3x maior que o necessário, latência evitável.
- **Recomendação:** Cache de resultado com TTL de 1h para
  relatórios com mesma assinatura (hash dos parâmetros). Invalidação
  por evento quando dados subjacentes mudam.

### Segurança

#### Achado 3.1 — Autorização no nível do endpoint apenas [MODERADO]
- **Observação:** O controle de acesso verifica se o usuário pode
  acessar o endpoint /reports, mas não filtra dados por tenant/organização.
- **Evidência:** Na proposta de API, nenhum filtro por org_id nos
  queries ao banco.
- **Impacto:** Vazamento de dados entre organizações (violação LGPD).
- **Recomendação:** Implementar filtro obrigatório por org_id em
  todas as queries. Adicionar teste automatizado que verifica
  isolamento de dados.

#### Achado 3.2 — Export de relatório sem auditoria [BAIXO]
- **Observação:** Download de CSV/PDF não registra log de auditoria.
- **Evidência:** Ausência de logging no diagrama de sequência do export.
- **Impacto:** Impossibilidade de rastrear quem acessou dados
  sensíveis via relatório.
- **Recomendação:** Adicionar audit log em toda operação de export
  com: user_id, org_id, relatório, parâmetros, timestamp.

## Pontos Positivos

- Modelagem de dados bem normalizada com índices adequados
- Separação clara entre camada de API e camada de processamento
- Testes de integração incluídos na proposta desde o início
- Documentação de API com OpenAPI spec completa

## Plano de Ação Consolidado

| # | Achado | Severidade | Owner | Prazo |
|---|---|---|---|---|
| 1.1 | Processamento assíncrono | Crítico | @autor | Antes de implementar |
| 2.1 | Estratégia de cache | Crítico | @autor | Antes de implementar |
| 1.2 | Limite de período | Moderado | @autor | Sprint 1 |
| 3.1 | Filtro por org_id | Moderado | @autor | Sprint 1 |
| 3.2 | Audit log de export | Baixo | @autor | Sprint 2 |

## Veredicto

**Aprovado com condições.** Achados 1.1 e 2.1 (críticos) devem ser
endereçados na proposta antes de iniciar implementação. Achados
moderados podem ser endereçados durante a implementação. Segunda
revisão necessária após ajustes nos itens críticos.
```
