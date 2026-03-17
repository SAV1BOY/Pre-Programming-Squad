# Standard para Definição de Escopo

## Propósito

Definir o processo para transformar os achados do discovery em um escopo de projeto claro, delimitado e acordado entre todos os stakeholders. O scoping é onde se define o que será feito, o que não será feito, e quais as fronteiras do trabalho.

## Escopo

Todo projeto que passou pela fase de discovery (ou que foi classificado como P e recebeu escopo direto no intake).

## Definições

| Termo | Definição |
|---|---|
| Escopo | Conjunto explícito e delimitado de funcionalidades, requisitos e entregas que compõem o projeto |
| In scope | Funcionalidades e requisitos que fazem parte do projeto |
| Out of scope | Funcionalidades e requisitos que explicitamente NÃO fazem parte do projeto |
| Scope creep | Expansão não controlada do escopo durante o ciclo de preparação ou implementação |
| MVP | Versão mínima viável que entrega o valor central do projeto |

## Processo

### 1. Derivar Escopo do Discovery

A partir do documento de discovery:
- Listar todos os requisitos funcionais identificados
- Listar requisitos não-funcionais com valores quantitativos
- Mapear dependências e pré-requisitos
- Identificar itens que podem ser faseados (MVP vs. v2)

### 2. Definir Fronteiras

Para cada item, classificar explicitamente:

| Classificação | Critério | Exemplo |
|---|---|---|
| **MVP (obrigatório)** | Sem isso, o projeto não entrega valor | CRUD de pedidos, validação de pagamento |
| **v1 (importante)** | Agrega valor significativo, viável no mesmo ciclo | Notificação por email, relatório básico |
| **v2 (futuro)** | Valioso, mas não cabe neste ciclo ou depende de outra entrega | Recomendação por ML, dashboard avançado |
| **Out of scope** | Não faz parte deste projeto, independentemente da versão | Migração de dados históricos, app mobile |

### 3. Documentar Escopo

O documento de escopo deve conter:

- **Objetivo do projeto** (1-2 frases)
- **In scope — MVP:** Lista numerada com critério de aceitação por item
- **In scope — v1:** Lista numerada com critério de aceitação por item
- **Out of scope:** Lista com justificativa para cada exclusão
- **Futuro (v2):** Lista para registro e referência
- **Dependências:** Tabela com dependência, status, owner, prazo
- **Premissas:** Lista de suposições assumidas como verdadeiras
- **Requisitos não-funcionais:** Tabela com atributo, meta, justificativa
- **Critérios de sucesso:** Métricas que definem se o projeto atingiu seu objetivo

### 4. Validar com Stakeholders

- Apresentar escopo ao solicitante e patrocinador
- Confirmar que MVP entrega o valor esperado
- Obter aceite formal por escrito (mensagem, email ou assinatura no doc)
- Registrar quaisquer divergências e como foram resolvidas

### 5. Congelar Escopo

Após aceite, o escopo está congelado. Mudanças só via processo formal:
- Pedido de change request com justificativa
- Análise de impacto (prazo, esforço, risco)
- Aprovação do patrocinador
- Registro da mudança no documento de escopo

## Critérios de Qualidade

- Todo item de escopo tem critério de aceitação verificável
- Lista de "out of scope" é tão detalhada quanto "in scope"
- Premissas documentadas com impacto se forem falsas
- Aceite do escopo registrado formalmente
- Zero change requests no primeiro sprint de implementação (indicador de scoping bem feito)

## Responsáveis

| Papel | Responsabilidade |
|---|---|
| Membro do squad | Derivar escopo do discovery, documentar, facilitar validação |
| Tech Lead | Revisar completude e qualidade do escopo |
| Solicitante/PM | Validar que escopo atende necessidade de negócio |
| Patrocinador | Aprovar escopo e assumir compromisso de não mudar sem change request |

## Referências

- Standard de Discovery: `docs/discovery-standard.md`
- Standard de Estimativa: `docs/estimation-standard.md`
- Definição de Readiness: `docs/readiness-definition.md`
