# Padroes de Falha em Engenharia de Requisitos

## Titulo

Requirements Engineering Failure Patterns and Their Impact on Project Outcomes

## Resumo

Pesquisas do Standish Group (CHAOS Reports, 1994-2023), IEEE e estudos de Capers Jones demonstram consistentemente que problemas de requisitos sao a causa raiz mais frequente de fracasso em projetos de software. Aproximadamente 50-70% dos defeitos em sistemas podem ser rastreados ate problemas originados na fase de requisitos. Os padroes de falha sao recorrentes e previsíveis: ambiguidade, incompletude, inconsistencia, scope creep, e falta de validacao com stakeholders.

## Insight Principal

Falhas de requisitos nao sao aleatorias — seguem padroes previsíveis e detectaveis. Um squad de pre-programacao treinado para reconhecer esses padroes pode preveni-los sistematicamente. A chave nao e criar requisitos perfeitos (impossivel), mas criar processos que detectem e corrijam problemas rapidamente.

## Padroes de Falha Recorrentes

### 1. Ambiguidade Nao Detectada
**Descricao:** Requisitos que podem ser interpretados de multiplas formas.
**Exemplo:** "O sistema deve ser rapido" — rapido para quem? Em que operacao? Qual metrica?
**Deteccao:** Procurar por adjetivos subjetivos, termos relativos, pronomes ambiguos.
**Mitigacao:** Exigir metricas quantificaveis e exemplos concretos (Specification by Example).

### 2. Requisitos Implicitos
**Descricao:** Comportamentos esperados que ninguem documentou porque "sao obvios."
**Exemplo:** Ninguem mencionou que o sistema precisa funcionar em dispositivos moveis.
**Deteccao:** Checklists de requisitos nao-funcionais, personas de usuario, cenarios de uso.
**Mitigacao:** Usar checklists de completude e conduzir sessoes de "Three Amigos".

### 3. Requisitos Contraditorios
**Descricao:** Dois requisitos que nao podem ser satisfeitos simultaneamente.
**Exemplo:** "O sistema deve ser altamente seguro" + "O login deve ser sem fricção."
**Deteccao:** Matriz de conflito entre requisitos nao-funcionais.
**Mitigacao:** Priorizacao explicita de trade-offs com stakeholders.

### 4. Gold Plating
**Descricao:** Requisitos adicionados pela equipe tecnica sem validacao de valor com o negocio.
**Exemplo:** Implementar cache distribuido quando um cache local bastaria.
**Deteccao:** Perguntar "qual problema de negocio isso resolve?" para cada requisito tecnico.
**Mitigacao:** Vincular todo requisito a um objetivo de negocio mensuravel.

### 5. Scope Creep
**Descricao:** Expansao gradual e nao controlada do escopo do projeto.
**Exemplo:** "Ja que estamos aqui, vamos adicionar tambem..."
**Deteccao:** Monitorar mudancas de escopo apos design doc aprovado.
**Mitigacao:** Non-goals explicitos, change control process, MVP rigido.

### 6. Stakeholder Ausente
**Descricao:** Decisoes tomadas sem input de stakeholders criticos.
**Exemplo:** Design aprovado sem consultar equipe de seguranca ou compliance.
**Deteccao:** Mapeamento de stakeholders no inicio do projeto.
**Mitigacao:** Stakeholder map obrigatorio em design docs, RACI matrix.

### 7. Solucao Disfarçada de Requisito
**Descricao:** Stakeholder prescreve a solucao em vez de descrever o problema.
**Exemplo:** "Precisamos de um microservico em Go" em vez de "Precisamos processar 10k transacoes/segundo."
**Deteccao:** Perguntar "por que?" repetidamente ate chegar ao problema real.
**Mitigacao:** Separar descricao do problema de proposta de solucao nos templates.

## Aplicacao ao Squad

### Como Checklist de Deteccao
- Incorporar os 7 padroes como checklist obrigatoria em revisoes de requisitos.
- Treinar o squad para reconhecer cada padrao instintivamente.
- Registrar ocorrencias para medir frequencia e direcionar melhorias.

### Como Criterio de Readiness
- Nenhum requisito ambiguo passa sem quantificacao.
- Requisitos implicitos sao buscados ativamente via checklists.
- Contradições sao resolvidas com priorizacao explicita.
- Non-goals estao documentados para prevenir scope creep.

### Como Metrica de Eficacia
- Rastrear quantos defeitos de requisitos sao detectados na pre-programacao vs. fases posteriores.
- Medir reducao de retrabalho apos adocao de deteccao sistematica.

## Referencias

- Standish Group. CHAOS Reports (1994-2023).
- Boehm, B. & Basili, V. (2001). "Software Defect Reduction Top 10 List."
- Jones, C. (2008). "Applied Software Measurement."
- IEEE 830-1998. "IEEE Recommended Practice for Software Requirements Specifications."
