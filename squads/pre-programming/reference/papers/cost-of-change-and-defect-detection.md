# Custo de Mudanca e Deteccao de Defeitos

## Titulo

The Cost of Change Curve and Early Defect Detection in Software Development

## Resumo

Pesquisas de Barry Boehm (1981, atualizado em 2001) e do NIST (2002) demonstram que o custo de corrigir um defeito cresce exponencialmente ao longo das fases do ciclo de desenvolvimento. Um defeito identificado na fase de requisitos custa 1x para corrigir; na fase de design, 3-6x; na implementacao, 10x; em testes, 15-40x; e em producao, 30-100x. Estudos da IBM Systems Sciences Institute e do Capers Jones confirmam esses multiplicadores em projetos de diversas escalas.

## Insight Principal

A pre-programacao e o ponto de maior alavancagem economica de todo o ciclo de desenvolvimento. Cada hora investida na identificacao de defeitos em requisitos e design economiza 10-100 horas de trabalho futuro. O squad de pre-programacao nao e um custo adicional — e o investimento de maior retorno de toda a engenharia.

## Dados de Referencia

| Fase de Deteccao | Custo Relativo | Exemplo Concreto |
|---|---|---|
| Requisitos | 1x | Corrigir uma ambiguidade no documento |
| Design/Arquitetura | 3-6x | Refazer um design doc |
| Implementacao | 10x | Reescrever codigo |
| Testes | 15-40x | Investigar, corrigir, re-testar |
| Producao | 30-100x | Hotfix + rollback + postmortem + dano reputacional |

## Tipos de Defeitos Detectaveis na Pre-Programacao

### 1. Defeitos de Requisitos
- Requisitos ambiguos ou contraditorios.
- Requisitos ausentes (funcionalidades implicitas nao documentadas).
- Requisitos impossiveis ou economicamente inviaveis.
- Requisitos sem criterios de aceitacao verificaveis.

### 2. Defeitos de Design
- Decisoes arquiteturais que nao suportam requisitos nao-funcionais.
- Acoplamento excessivo entre componentes.
- Ausencia de tratamento de falhas.
- Escolhas tecnologicas inadequadas para o contexto.

### 3. Defeitos de Integracao
- Contratos de API inconsistentes.
- Expectativas divergentes entre equipes.
- Dependencias circulares.
- Incompatibilidade de modelos de dados.

## Aplicacao ao Squad

### Como Argumento para Investimento em Pre-Programacao
- Usar os multiplicadores de custo para justificar tempo investido em reviews.
- Quantificar economia: "Se este design doc preveniu 3 defeitos de producao, economizamos ~300 horas de trabalho."
- Rastrear defeitos escapados para demonstrar valor da pre-programacao.

### Como Guia de Priorizacao
- Focar revisoes nos pontos de maior impacto: contratos entre sistemas, decisoes arquiteturais, requisitos ambiguos.
- Investir mais tempo em revisoes de areas de alto risco (seguranca, dados financeiros, integracao com terceiros).

### Como Metrica de Eficacia
- Medir a taxa de defeitos encontrados em pre-programacao vs. fases posteriores.
- Rastrear o custo evitado por trimestre.
- Comparar taxa de falha em mudancas (DORA) antes e depois de adotar praticas de pre-programacao rigorosas.

## Referencias

- Boehm, B. (1981). "Software Engineering Economics." Prentice Hall.
- Boehm, B. & Basili, V. (2001). "Software Defect Reduction Top 10 List." IEEE Computer, 34(1).
- NIST (2002). "The Economic Impacts of Inadequate Infrastructure for Software Testing."
- Jones, C. (2008). "Applied Software Measurement." McGraw-Hill.
