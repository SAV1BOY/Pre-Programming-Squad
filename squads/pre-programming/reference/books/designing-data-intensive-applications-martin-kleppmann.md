# Designing Data-Intensive Applications

## Informações Gerais

- **Titulo:** Designing Data-Intensive Applications
- **Autor:** Martin Kleppmann
- **Ano:** 2017

## Tese Central

A maioria das aplicacoes modernas sao data-intensive, nao compute-intensive. O desafio principal nao e a capacidade de processamento, mas a quantidade, complexidade e velocidade de mudanca dos dados. Escolhas de modelagem de dados, armazenamento, replicacao, particionamento e processamento determinam fundamentalmente a confiabilidade, escalabilidade e manutenibilidade de um sistema.

## Conceitos-Chave para Pre-Programacao

### 1. Os Tres Pilares: Confiabilidade, Escalabilidade, Manutenibilidade
Toda decisao de pre-programacao deve ser avaliada sob essas tres dimensoes. Confiabilidade significa funcionar corretamente mesmo diante de falhas. Escalabilidade e a capacidade de lidar com carga crescente. Manutenibilidade e a facilidade de operar, entender e evoluir o sistema.

### 2. Modelos de Dados e Linguagens de Consulta
A escolha entre relacional, documento, grafo ou outros modelos tem implicacoes profundas. O modelo relacional favorece joins e normalizacao. O modelo de documento favorece localidade de dados e esquemas flexiveis. Na pre-programacao, essa decisao deve ser explicitada e justificada.

### 3. Armazenamento e Recuperacao
Indices B-tree vs. LSM-tree, OLTP vs. OLAP, row-oriented vs. column-oriented. Cada escolha de engine de armazenamento afeta performance, custo e padroes de acesso. O squad deve entender o perfil de leitura/escrita antes de decidir.

### 4. Replicacao e Particionamento
Replicacao single-leader, multi-leader e leaderless. Particionamento por chave, por hash, por range. Cada estrategia traz trade-offs em consistencia, disponibilidade e performance. Decisoes de pre-programacao devem antecipar padroes de acesso e requisitos de disponibilidade.

### 5. Transacoes e Consistencia
Niveis de isolamento (read committed, snapshot isolation, serializability), problemas de concorrencia (dirty reads, lost updates, write skew). A pre-programacao deve definir claramente quais garantias transacionais sao necessarias.

### 6. Sistemas Distribuidos e Consenso
Problemas fundamentais: falhas parciais, relogios nao confiaveis, atrasos de rede imprevisíveis. Algoritmos de consenso (Raft, Paxos). Na pre-programacao, nao subestimar a complexidade inerente a distribuicao.

### 7. Processamento em Batch e Stream
MapReduce, dataflows, processamento de eventos, CDC (Change Data Capture), event sourcing. A escolha entre processamento sincrono e assincrono afeta toda a arquitetura.

## Como Aplicar no Squad

### Na Fase de Analise de Requisitos
- Mapear perfis de leitura vs. escrita antes de escolher tecnologias.
- Definir requisitos de consistencia explicitamente (eventual, forte, causal).
- Identificar padroes de acesso a dados predominantes.
- Quantificar volumes de dados esperados (atuais e projetados).

### Na Avaliacao de Design Docs
- Verificar se a escolha de banco de dados e justificada pelo modelo de dados e padroes de acesso.
- Avaliar se estrategias de replicacao e particionamento estao alinhadas com requisitos de disponibilidade.
- Confirmar que garantias transacionais foram definidas e sao atingiveis com a arquitetura proposta.
- Verificar se cenarios de falha distribuida foram considerados.

### Na Definicao de Contratos
- Definir SLAs de latencia e throughput com base nos padroes de acesso documentados.
- Especificar comportamento esperado em cenarios de particionamento de rede.
- Documentar garantias de ordering e delivery em fluxos assincronos.

### Nos Criterios de Readiness
- Checklist de decisoes de dados: modelo, armazenamento, replicacao, particionamento.
- Validacao de que requisitos nao-funcionais de dados estao quantificados.
- Confirmacao de que cenarios de crescimento foram modelados.

## Citacoes Importantes

> "An application has to meet various requirements in order to be useful. There are functional requirements and nonfunctional requirements. Reliability, scalability, and maintainability are the nonfunctional requirements that are most important."

> "Data outlives code. Your data model will affect not only how the software is written, but also how you think about the problem."

> "Transactions are not the antithesis of distributed systems. They are a mechanism for simplifying the programming model."

> "In a distributed system, you can satisfy at most two of these three properties: Consistency, Availability, and Partition tolerance."

> "The limits of my language mean the limits of my world. — The same applies to data models."

## Relacao com Outros Livros de Referencia

- **System Design Interview (Xu):** Kleppmann fornece a base teorica profunda que fundamenta as decisoes praticas de system design.
- **Release It! (Nygard):** Complementa com padroes de estabilidade para sistemas distribuidos em producao.
- **SRE (Google):** Os principios de confiabilidade de Kleppmann alinham-se com as praticas de SRE.
