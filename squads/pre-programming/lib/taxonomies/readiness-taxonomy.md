# Taxonomia de Prontidão (Readiness)

## Categorias

### 1. Prontidão de Requisitos (PR)
Avalia o grau de preparação dos requisitos para início do desenvolvimento.

#### Subcategorias
- **PR-CLAR:** Clareza - requisitos são compreensíveis sem ambiguidade
- **PR-COMP:** Completude - todos os cenários estão cobertos
- **PR-CONS:** Consistência - requisitos não se contradizem
- **PR-TEST:** Testabilidade - é possível verificar o atendimento
- **PR-RAST:** Rastreabilidade - ligação com objetivos de negócio
- **PR-PRIO:** Priorização - ordem de importância definida

#### Definições
| Subcategoria | Score Alto (> 80%) | Score Baixo (< 40%) | Como Medir |
|---|---|---|---|
| PR-CLAR | Sem palavras ambíguas, linguagem precisa | Termos vagos, múltiplas interpretações | Score de ambiguidade < 20 |
| PR-COMP | Cenários positivos, negativos e de borda | Apenas caminho feliz descrito | Checklist de completude > 80% |
| PR-CONS | Zero conflitos entre requisitos | Contradições detectadas | Matriz de inconsistência |
| PR-TEST | Todo requisito tem critério verificável | Critérios subjetivos ou ausentes | % com critério de aceite |
| PR-RAST | Cada requisito liga a um objetivo | Requisitos órfãos sem justificativa | % com rastreabilidade |
| PR-PRIO | MoSCoW definido para todos | Tudo é "prioridade alta" | Distribuição de prioridades |

### 2. Prontidão Técnica (PT)
Avalia a preparação técnica e arquitetural.

#### Subcategorias
- **PT-ARQT:** Decisões arquiteturais documentadas e validadas
- **PT-INFR:** Infraestrutura planejada e provisionável
- **PT-INTG:** Integrações mapeadas com contratos definidos
- **PT-SEGR:** Requisitos de segurança endereçados
- **PT-OBSV:** Estratégia de observabilidade definida
- **PT-TOOL:** Ferramentas e ambientes prontos

#### Definições
| Subcategoria | Score Alto (> 80%) | Score Baixo (< 40%) | Como Medir |
|---|---|---|---|
| PT-ARQT | ADRs completos, diagramas atualizados | Sem documentação arquitetural | Checklist de arquitetura |
| PT-INFR | IaC pronto, ambientes provisionados | Sem definição de infraestrutura | % de recursos definidos |
| PT-INTG | Contratos de API definidos e validados | Integrações não mapeadas | Contratos documentados |
| PT-SEGR | Threat model feito, requisitos OWASP | Segurança não considerada | Checklist de segurança |
| PT-OBSV | SLIs/SLOs definidos, alertas planejados | Sem plano de monitoramento | Checklist de observabilidade |
| PT-TOOL | CI/CD, repos, ambientes configurados | Nada configurado | Checklist de infraestrutura |

### 3. Prontidão de Qualidade (PQ)
Avalia a preparação para garantia de qualidade.

#### Subcategorias
- **PQ-ESTR:** Estratégia de testes definida
- **PQ-CENA:** Cenários de teste documentados
- **PQ-DADO:** Dados de teste preparados
- **PQ-AUTO:** Infraestrutura de automação pronta
- **PQ-CRIT:** Critérios de aceite verificáveis
- **PQ-REGR:** Estratégia de regressão definida

#### Definições
| Subcategoria | Score Alto (> 80%) | Score Baixo (< 40%) |
|---|---|---|
| PQ-ESTR | Pirâmide de testes definida, níveis claros | Sem estratégia documentada |
| PQ-CENA | Cenários positivos, negativos e de borda | Sem cenários de teste |
| PQ-DADO | Dados gerados/importados e anonimizados | Sem dados de teste |
| PQ-AUTO | Framework configurado, pipeline integrado | Sem automação |
| PQ-CRIT | Todos os requisitos com critérios testáveis | Critérios vagos ou ausentes |
| PQ-REGR | Suite de regressão existente e estável | Sem testes de regressão |

### 4. Prontidão de Riscos (PK)
Avalia a gestão de riscos.

#### Subcategorias
- **PK-IDEN:** Riscos identificados de forma abrangente
- **PK-AVAL:** Riscos avaliados (probabilidade e impacto)
- **PK-MITI:** Planos de mitigação definidos para riscos altos
- **PK-RESP:** Responsáveis atribuídos
- **PK-MONI:** Indicadores de monitoramento definidos
- **PK-CONT:** Planos de contingência para riscos críticos

### 5. Prontidão Operacional (PO)
Avalia a preparação para operação em produção.

#### Subcategorias
- **PO-DEPL:** Estratégia de deploy definida
- **PO-ROLL:** Plano de rollback testado
- **PO-MONIT:** Dashboards e alertas planejados
- **PO-RUNB:** Runbooks documentados
- **PO-SUPT:** Processo de suporte definido
- **PO-COMU:** Plano de comunicação para incidentes

### 6. Prontidão de Equipe (PE)
Avalia a preparação da equipe para executar.

#### Subcategorias
- **PE-SKIL:** Skills necessários presentes na equipe
- **PE-CAPA:** Capacidade (pessoas) disponível
- **PE-KNOW:** Conhecimento do domínio adequado
- **PE-PROC:** Processos de trabalho definidos (ceremonies, DoD)

## Exemplos por Categoria

### Avaliação Completa de Prontidão
```
Projeto: "Novo Portal do Cliente"
Data: 2025-03-15

PRONTIDÃO DE REQUISITOS (Peso: 20%)
  PR-CLAR: 85%  [################....]
  PR-COMP: 70%  [##############......]
  PR-CONS: 90%  [##################..]
  PR-TEST: 65%  [#############.......]
  PR-RAST: 80%  [################....]
  PR-PRIO: 95%  [###################.]
  Subtotal: 80.8%

PRONTIDÃO TÉCNICA (Peso: 25%)
  PT-ARQT: 90%  [##################..]
  PT-INFR: 75%  [###############.....]
  PT-INTG: 85%  [#################...]
  PT-SEGR: 60%  [############........]
  PT-OBSV: 70%  [##############......]
  PT-TOOL: 95%  [###################.]
  Subtotal: 79.2%

PRONTIDÃO DE QUALIDADE (Peso: 15%)
  PQ-ESTR: 80%  PQ-CENA: 60%
  PQ-DADO: 40%  PQ-AUTO: 85%
  PQ-CRIT: 65%  PQ-REGR: 70%
  Subtotal: 66.7%

PRONTIDÃO DE RISCOS (Peso: 15%)
  PK-IDEN: 85%  PK-AVAL: 90%
  PK-MITI: 75%  PK-RESP: 80%
  PK-MONI: 60%  PK-CONT: 70%
  Subtotal: 76.7%

PRONTIDÃO OPERACIONAL (Peso: 15%)
  PO-DEPL: 80%  PO-ROLL: 60%
  PO-MONIT: 65%  PO-RUNB: 30%
  PO-SUPT: 70%  PO-COMU: 75%
  Subtotal: 63.3%

PRONTIDÃO DE EQUIPE (Peso: 10%)
  PE-SKIL: 90%  PE-CAPA: 85%
  PE-KNOW: 75%  PE-PROC: 90%
  Subtotal: 85.0%

SCORE TOTAL: 75.3% -> Classificação: BOM

Áreas de atenção:
  - PQ-DADO (40%): Dados de teste não preparados
  - PO-RUNB (30%): Runbooks não documentados
  - PT-SEGR (60%): Requisitos de segurança incompletos

Decisão: GO CONDICIONAL
  Condições:
  1. Preparar dados de teste antes da sprint 2
  2. Completar threat model antes da sprint 3
  3. Documentar runbooks durante o desenvolvimento
```
