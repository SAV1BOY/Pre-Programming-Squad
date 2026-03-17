# Taxonomia de Riscos

## Categorias

### 1. Riscos Técnicos (RT)
Riscos relacionados à tecnologia, implementação e infraestrutura.

#### Subcategorias
- **RT-CMPL:** Complexidade técnica subestimada
- **RT-INTG:** Falhas de integração entre sistemas
- **RT-PERF:** Problemas de performance e escalabilidade
- **RT-SECU:** Vulnerabilidades de segurança
- **RT-INFR:** Falhas de infraestrutura
- **RT-DATA:** Problemas com dados (integridade, migração, volume)
- **RT-TECH:** Risco de tecnologia imatura ou desconhecida
- **RT-DEBT:** Débito técnico acumulado

#### Definições
| Subcategoria | Definição | Indicadores |
|---|---|---|
| RT-CMPL | Complexidade real excede a estimada | Tarefas que excedem estimativa em > 50% |
| RT-INTG | Falha na comunicação entre componentes | APIs instáveis, timeouts frequentes |
| RT-PERF | Sistema não atende requisitos de performance | Latência acima do SLO, timeout |
| RT-SECU | Vulnerabilidade explorável | Achado em pentest, CVE em dependência |
| RT-INFR | Falha de hardware, rede ou cloud | Indisponibilidade, perda de dados |
| RT-DATA | Inconsistência ou perda de dados | Migração falha, corrupção, duplicação |
| RT-TECH | Tecnologia não funciona como esperado | Bug em framework, limitação descoberta |
| RT-DEBT | Custo crescente de manutenção | Tempo de fix aumentando, cobertura caindo |

### 2. Riscos de Requisitos (RR)
Riscos relacionados à especificação e compreensão dos requisitos.

#### Subcategorias
- **RR-AMBG:** Ambiguidade nos requisitos
- **RR-INCM:** Requisitos incompletos
- **RR-INST:** Requisitos instáveis (mudanças frequentes)
- **RR-CONF:** Conflito entre requisitos
- **RR-SCOP:** Expansão descontrolada de escopo

#### Definições
| Subcategoria | Definição | Indicadores |
|---|---|---|
| RR-AMBG | Requisito pode ser interpretado de formas diferentes | Score de ambiguidade > 40 |
| RR-INCM | Informação insuficiente para implementar | Critério de aceite ausente |
| RR-INST | Requisito muda frequentemente | > 2 mudanças por sprint |
| RR-CONF | Dois requisitos se contradizem | Matriz de inconsistência detecta conflito |
| RR-SCOP | Escopo cresce sem controle formal | Itens adicionados sem aprovação |

### 3. Riscos Organizacionais (RO)
Riscos relacionados a pessoas, processos e organização.

#### Subcategorias
- **RO-EQUI:** Riscos de equipe (turnover, disponibilidade, skill gap)
- **RO-COMU:** Falhas de comunicação entre equipes
- **RO-PROC:** Processos inadequados ou ausentes
- **RO-STAK:** Indisponibilidade ou desalinhamento de stakeholders
- **RO-DEPE:** Dependência de pessoa-chave (bus factor)

#### Definições
| Subcategoria | Definição | Indicadores |
|---|---|---|
| RO-EQUI | Equipe insuficiente ou sem skills | Posições não preenchidas, skills ausentes |
| RO-COMU | Informação não flui entre equipes | Decisões desconhecidas, retrabalho |
| RO-PROC | Processo não suporta o projeto | Burocracia excessiva ou ausência de processo |
| RO-STAK | Stakeholder não participa | Decisões atrasadas, falta de feedback |
| RO-DEPE | Conhecimento concentrado em 1 pessoa | Bus factor = 1 |

### 4. Riscos Externos (RE)
Riscos fora do controle direto da equipe.

#### Subcategorias
- **RE-FORN:** Dependência de fornecedores e terceiros
- **RE-MERC:** Mudanças de mercado ou regulatórias
- **RE-CONC:** Ações de concorrentes
- **RE-FORC:** Força maior (eventos imprevisíveis)

### 5. Riscos de Gerenciamento (RG)
Riscos relacionados ao planejamento e gestão do projeto.

#### Subcategorias
- **RG-PRAZ:** Estimativas de prazo irrealistas
- **RG-ORCA:** Orçamento insuficiente
- **RG-PRIO:** Priorização inadequada
- **RG-PLAN:** Planejamento insuficiente

## Exemplos por Categoria

### RT-INTG: Risco de Integração
```
ID: RSK-001
Categoria: RT-INTG
Título: Instabilidade da API de pagamento do fornecedor
Descrição: A API do gateway de pagamento (Fornecedor X) apresentou
  3 incidentes de indisponibilidade no último trimestre, com duração
  média de 45 minutos cada.
Probabilidade: Alta (4/5)
Impacto: Alto (4/5)
Severidade: 16 (crítico)
Mitigação:
  Estratégia: Mitigar
  Ações:
    - Implementar circuit breaker com fallback
    - Configurar fila de retry com backoff exponencial
    - Avaliar gateway de pagamento secundário
  Responsável: Tech Lead
  Prazo: Sprint 3
Gatilho: Timeout > 5s em 3 requisições consecutivas
```

### RR-AMBG: Risco de Ambiguidade
```
ID: RSK-005
Categoria: RR-AMBG
Título: Requisitos de relatórios gerenciais mal definidos
Descrição: Os requisitos RF-RPRT-003 a RF-RPRT-008 usam termos
  vagos como "relatório adequado" e "métricas relevantes" sem
  definir quais dados, filtros e formato são esperados.
Probabilidade: Muito Alta (5/5)
Impacto: Médio (3/5)
Severidade: 15 (alto)
Mitigação:
  Estratégia: Evitar
  Ações:
    - Agendar workshop de 2h com área de negócio
    - Criar protótipos de relatórios para validação
    - Definir critérios de aceite mensuráveis
  Responsável: Product Owner
  Prazo: Semana 2
```

### RO-DEPE: Risco de Dependência de Pessoa-Chave
```
ID: RSK-012
Categoria: RO-DEPE
Título: Conhecimento do sistema legado concentrado em 1 desenvolvedor
Descrição: Apenas o desenvolvedor Sr. João conhece a arquitetura
  e regras de negócio do sistema ERP legado que será integrado.
  Sua ausência (férias, doença) bloquearia o projeto.
Probabilidade: Média (3/5)
Impacto: Muito Alto (5/5)
Severidade: 15 (alto)
Mitigação:
  Estratégia: Mitigar
  Ações:
    - Sessões de knowledge transfer (2x por semana)
    - Documentação do sistema legado
    - Pair programming em tarefas de integração
  Responsável: Engineering Manager
  Prazo: Contínuo durante o projeto
```
