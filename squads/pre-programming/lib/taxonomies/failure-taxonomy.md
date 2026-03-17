# Taxonomia de Falhas

## Categorias

### 1. Falhas de Planejamento (FP)
Falhas originadas na fase de pré-programação e planejamento.

#### Subcategorias
- **FP-REQT:** Falha por requisitos mal definidos
- **FP-ARQT:** Falha por decisão arquitetural inadequada
- **FP-ESTM:** Falha por estimativa incorreta
- **FP-ESCP:** Falha por escopo mal delimitado
- **FP-RISK:** Falha por risco não identificado
- **FP-DPND:** Falha por dependência não mapeada
- **FP-CMUN:** Falha por comunicação deficiente no planejamento

#### Definições
| Subcategoria | Definição | Como Detectar |
|---|---|---|
| FP-REQT | Implementação não atende necessidade real | Divergência entre entregue e esperado pelo PO |
| FP-ARQT | Arquitetura não suporta requisito real | Refatoração estrutural necessária durante dev |
| FP-ESTM | Prazo ou esforço subestimado | Desvio > 30% da estimativa original |
| FP-ESCP | Funcionalidades necessárias fora do escopo | Descoberta tardia de requisitos essenciais |
| FP-RISK | Problema que poderia ter sido previsto | Risco materializado sem plano de mitigação |
| FP-DPND | Dependência bloqueante não identificada | Bloqueio por sistema externo não previsto |
| FP-CMUN | Informação não chegou a quem precisava | Decisão tomada sem input necessário |

### 2. Falhas de Implementação (FI)
Falhas introduzidas durante o desenvolvimento do código.

#### Subcategorias
- **FI-LOGC:** Erro de lógica de programação
- **FI-BORD:** Falha em caso de borda não tratado
- **FI-CONC:** Problema de concorrência (race condition, deadlock)
- **FI-MEMO:** Vazamento de memória ou recursos
- **FI-TIPO:** Erro de tipo ou conversão de dados
- **FI-EXCP:** Tratamento inadequado de exceções
- **FI-CONF:** Erro de configuração

#### Definições
| Subcategoria | Definição | Exemplo |
|---|---|---|
| FI-LOGC | Algoritmo produz resultado incorreto | Cálculo de desconto com fórmula errada |
| FI-BORD | Comportamento inesperado em valores extremos | Lista vazia causa NullPointerException |
| FI-CONC | Problema por acesso simultâneo | Dois pedidos compram último item do estoque |
| FI-MEMO | Recurso não liberado adequadamente | Conexão de banco não devolvida ao pool |
| FI-TIPO | Incompatibilidade de tipos | String onde esperava Integer |
| FI-EXCP | Exceção não tratada ou silenciada | Erro engolido com catch vazio |
| FI-CONF | Parâmetro mal configurado | URL de produção apontando para staging |

### 3. Falhas de Integração (FG)
Falhas na comunicação entre componentes e sistemas.

#### Subcategorias
- **FG-CONT:** Quebra de contrato entre serviços
- **FG-TIME:** Timeout e latência em chamadas
- **FG-VERS:** Incompatibilidade de versão
- **FG-FORM:** Formato de dados incompatível
- **FG-AUTH:** Falha de autenticação/autorização entre serviços
- **FG-REDE:** Falha de rede ou conectividade

#### Definições
| Subcategoria | Definição | Exemplo |
|---|---|---|
| FG-CONT | Resposta diferente do esperado | Campo renomeado sem aviso ao consumidor |
| FG-TIME | Chamada excede tempo limite | API externa lenta causa cascata de timeouts |
| FG-VERS | Versões incompatíveis em produção | Serviço A espera v2, serviço B responde v1 |
| FG-FORM | Serialização/deserialização falha | Data em DD/MM/YYYY onde esperava ISO 8601 |
| FG-AUTH | Credencial inválida ou expirada | Token JWT expirado não renovado |
| FG-REDE | Comunicação interrompida | DNS não resolve, firewall bloqueia |

### 4. Falhas Operacionais (FO)
Falhas em produção e operação do sistema.

#### Subcategorias
- **FO-INFR:** Falha de infraestrutura (servidor, disco, rede)
- **FO-DEPL:** Falha durante deploy ou rollback
- **FO-CAPA:** Esgotamento de capacidade (CPU, memória, disco)
- **FO-CERT:** Certificado expirado ou inválido
- **FO-MIGR:** Falha em migração de dados
- **FO-MONIT:** Falha não detectada por monitoramento

### 5. Falhas de Processo (FC)
Falhas nos processos de trabalho da equipe.

#### Subcategorias
- **FC-REVI:** Falha escapou do code review
- **FC-TEST:** Cobertura de teste insuficiente
- **FC-DOCM:** Documentação ausente ou desatualizada
- **FC-APRO:** Aprovação sem verificação adequada

## Exemplos por Categoria

### FP-ARQT: Falha Arquitetural
```
ID: FAIL-001
Categoria: FP-ARQT
Título: Banco relacional não suporta volume de eventos
Descrição: A decisão de usar PostgreSQL para armazenar eventos
  de telemetria (1M eventos/hora) causou degradação severa de
  performance. A escolha não considerou o padrão de escrita
  append-only em alto volume.
Fase de origem: Arquitetura (sprint 0)
Fase de detecção: Teste de carga (sprint 6)
Custo de correção: 3 sprints para migrar para TimescaleDB
Lição aprendida: Avaliar padrão de acesso a dados (read vs write
  heavy) ao escolher banco de dados. Incluir teste de carga
  no checklist de validação arquitetural.
```

### FG-CONT: Quebra de Contrato
```
ID: FAIL-015
Categoria: FG-CONT
Título: API de parceiro mudou formato de resposta sem aviso
Descrição: O parceiro de logística alterou o campo "status" de
  string para inteiro na API de rastreamento, quebrando a
  deserialização do nosso serviço.
Fase de origem: Integração (dependência externa)
Fase de detecção: Produção (alerta de erro)
Tempo de impacto: 2 horas até correção
Lição aprendida: Implementar testes de contrato automatizados
  para APIs de parceiros. Configurar alertas para mudanças
  de schema em respostas externas.
```

### FI-CONC: Race Condition
```
ID: FAIL-023
Categoria: FI-CONC
Título: Venda dupla de último item do estoque
Descrição: Dois usuários simultâneos conseguiram comprar o
  último item em estoque porque a verificação de disponibilidade
  e a reserva não eram atômicas.
Fase de origem: Implementação
Fase de detecção: Produção (reclamação de cliente)
Correção: Implementar lock otimista com versionamento na
  tabela de estoque.
Lição aprendida: Identificar operações que requerem atomicidade
  durante a fase de design. Incluir cenários de concorrência
  no plano de testes.
```
