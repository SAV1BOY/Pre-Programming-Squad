# Notas de Contexto do Projeto

## Propósito

Centralizar todas as informações contextuais relevantes sobre o projeto antes do início da codificação. Este documento serve como fonte única de verdade para que todos os membros do squad compreendam o cenário de negócio, as restrições técnicas, os stakeholders envolvidos e o histórico de decisões que moldaram o projeto até o momento atual.

A captura rigorosa do contexto evita retrabalho, reduz ambiguidades e garante que decisões de arquitetura e design sejam tomadas com base em informações completas.

---

## Estrutura de Registro

Cada nota de contexto deve ser registrada como um bloco independente contendo:

- **ID do Contexto**: Identificador único (ex.: `CTX-001`)
- **Data de Registro**: Data em que a informação foi capturada
- **Autor**: Pessoa responsável pela captura
- **Categoria**: Classificação do tipo de contexto (Negócio, Técnico, Organizacional, Regulatório)
- **Fonte**: De onde a informação foi obtida (reunião, documento, entrevista, etc.)
- **Descrição**: Texto detalhado da informação contextual
- **Impacto no Projeto**: Como essa informação afeta decisões de pré-programação
- **Ações Derivadas**: Próximos passos ou investigações necessárias
- **Status**: Ativo, Superado, Em Validação

---

## Campos Detalhados

### ID do Contexto
Formato: `CTX-NNN` onde NNN é sequencial. Permite rastreabilidade cruzada com decisões de arquitetura e registros de risco.

### Categoria
- **Negócio**: Requisitos de mercado, objetivos comerciais, métricas de sucesso do produto, prazos de lançamento, restrições orçamentárias.
- **Técnico**: Infraestrutura existente, limitações de plataforma, integrações obrigatórias, dívida técnica conhecida, SLAs vigentes.
- **Organizacional**: Estrutura de times, capacidade disponível, dependências entre squads, processos de aprovação, calendário de releases.
- **Regulatório**: LGPD, compliance setorial, requisitos de auditoria, políticas de segurança da informação, retenção de dados.

### Fonte
Indicar com precisão: nome da reunião, data, participantes, link para documento ou gravação. Fontes vagas como "alguém mencionou" são inaceitáveis.

### Impacto no Projeto
Classificar em: Alto (bloqueia decisões de arquitetura), Médio (influencia escolhas de design), Baixo (informação de background útil).

---

## Template de Entrada

```markdown
### CTX-[NNN] — [Título Descritivo]

- **Data de Registro**: AAAA-MM-DD
- **Autor**: [Nome do responsável]
- **Categoria**: [Negócio | Técnico | Organizacional | Regulatório]
- **Fonte**: [Descrição precisa da origem]
- **Status**: [Ativo | Superado | Em Validação]
- **Impacto**: [Alto | Médio | Baixo]

#### Descrição

[Texto detalhado descrevendo a informação contextual capturada. Incluir dados quantitativos quando disponíveis. Evitar linguagem ambígua.]

#### Impacto no Projeto

[Explicação de como essa informação afeta decisões de pré-programação, escolhas de arquitetura ou planejamento de entregas.]

#### Ações Derivadas

- [ ] [Ação 1 — Responsável — Prazo]
- [ ] [Ação 2 — Responsável — Prazo]

#### Notas Adicionais

[Observações relevantes, links para documentos relacionados, referências cruzadas com outros CTX.]
```

---

## Diretrizes de Uso

1. **Capturar cedo**: Registre informações contextuais assim que forem descobertas, mesmo que incompletas. Marque como "Em Validação" e complete depois.
2. **Revisar semanalmente**: O squad deve revisar notas de contexto ativas nas cerimônias de planejamento para verificar se ainda são válidas.
3. **Cruzar referências**: Vincule notas de contexto a decisões de arquitetura (ADRs), riscos identificados e premissas registradas.
4. **Evitar duplicação**: Antes de criar uma nova nota, verifique se o contexto já foi capturado anteriormente.
5. **Atualizar status**: Quando uma informação contextual for superada por novos fatos, marque como "Superado" com explicação.
