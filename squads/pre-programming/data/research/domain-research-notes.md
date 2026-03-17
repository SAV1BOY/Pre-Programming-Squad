# Notas de Pesquisa de Domínio

## Propósito

Documentar toda a pesquisa realizada sobre o domínio de negócio do projeto. Compreender profundamente o domínio antes de codificar é o diferencial entre software que resolve problemas reais e software que precisa ser reescrito. Este documento captura conceitos do domínio, regras de negócio, fluxos operacionais, terminologia específica e modelos mentais dos stakeholders.

A pesquisa de domínio alimenta diretamente o design de entidades, a modelagem de dados, a definição de bounded contexts e a validação de requisitos.

---

## Estrutura de Registro

Cada nota de pesquisa de domínio deve conter:

- **ID da Pesquisa**: Identificador único (ex.: `DOM-001`)
- **Data**: Data da pesquisa ou entrevista
- **Pesquisador**: Membro do squad responsável
- **Subdomínio**: Área específica do domínio investigada
- **Método**: Como a informação foi obtida (entrevista, análise documental, observação, workshop)
- **Descobertas**: Informações obtidas
- **Termos do Domínio**: Glossário de termos específicos encontrados
- **Regras de Negócio**: Regras explícitas ou implícitas identificadas
- **Contradições**: Informações conflitantes entre fontes
- **Lacunas**: Perguntas ainda sem resposta
- **Impacto na Modelagem**: Como as descobertas afetam o design do software

---

## Campos Detalhados

### Subdomínio
Segmentar o domínio em áreas gerenciáveis. Exemplos: Faturamento, Logística, Atendimento ao Cliente, Compliance, Gestão de Estoque. Cada subdomínio pode se tornar um bounded context no design.

### Método de Pesquisa
- **Entrevista com Especialista**: Conversa estruturada com profissional do domínio. Registrar nome, cargo, data e duração.
- **Análise Documental**: Estudo de manuais, regulamentos, processos documentados. Registrar título e localização do documento.
- **Observação em Campo**: Acompanhamento do processo real em operação. Registrar local, data e duração.
- **Workshop de Descoberta**: Sessão colaborativa com múltiplos stakeholders. Registrar participantes e artefatos gerados.
- **Análise de Sistema Legado**: Engenharia reversa de regras em sistemas existentes. Registrar sistema e módulos analisados.

### Termos do Domínio
Manter um glossário vivo. Para cada termo registrar:
- Nome do termo (como os especialistas do domínio o utilizam)
- Definição precisa
- Sinônimos ou variações regionais
- Contexto de uso
- Termos relacionados

### Regras de Negócio
Classificar cada regra em:
- **Invariante**: Sempre verdadeira, sem exceção (ex.: "Toda nota fiscal deve ter CNPJ válido")
- **Condicional**: Depende de contexto (ex.: "Frete grátis se valor acima de R$200")
- **Temporal**: Varia com o tempo (ex.: "Promoção válida até 31/12")
- **Derivada**: Calculada a partir de outras regras

### Contradições
Registrar fielmente quando duas fontes dão informações conflitantes. Não tentar resolver sozinho — escalar para o Product Owner ou especialista do domínio.

---

## Template de Entrada

```markdown
### DOM-[NNN] — [Título da Pesquisa]

- **Data**: AAAA-MM-DD
- **Pesquisador**: [Nome]
- **Subdomínio**: [Área do domínio]
- **Método**: [Entrevista | Análise Documental | Observação | Workshop | Análise de Legado]
- **Fonte/Participantes**: [Detalhamento da fonte]

#### Descobertas Principais

1. [Descoberta 1 — detalhar com dados e exemplos]
2. [Descoberta 2 — detalhar com dados e exemplos]
3. [Descoberta 3 — detalhar com dados e exemplos]

#### Glossário de Termos

| Termo | Definição | Contexto de Uso |
|-------|-----------|-----------------|
| [Termo 1] | [Definição precisa] | [Quando e como é usado] |
| [Termo 2] | [Definição precisa] | [Quando e como é usado] |

#### Regras de Negócio Identificadas

- **RN-[NNN]** ([Invariante | Condicional | Temporal | Derivada]): [Descrição da regra]
  - Fonte: [Quem/o que confirmou esta regra]
  - Exceções conhecidas: [Se houver]

#### Contradições Encontradas

- [Fonte A] afirma [X], enquanto [Fonte B] afirma [Y]. Resolução pendente com [responsável].

#### Lacunas de Conhecimento

- [ ] [Pergunta 1 — quem pode responder — prazo desejado]
- [ ] [Pergunta 2 — quem pode responder — prazo desejado]

#### Impacto na Modelagem

[Como essas descobertas influenciam a modelagem de entidades, os bounded contexts, as validações necessárias ou os fluxos de dados.]
```

---

## Diretrizes de Uso

1. **Linguagem ubíqua**: Sempre use os termos do domínio, não invente sinônimos técnicos. Se o negócio chama de "pedido", o código deve chamar de "pedido" (ou "order" se o codebase for em inglês, mas documente o mapeamento).
2. **Nunca assumir**: Se um especialista do domínio não confirmou uma regra de negócio, ela é uma premissa, não um fato. Registre no log de premissas.
3. **Mapear exceções**: As exceções às regras de negócio são onde os bugs mais caros moram. Documente cada exceção explicitamente.
4. **Atualizar continuamente**: O domínio evolui. Revise estas notas quando novas informações surgirem.
5. **Compartilhar com o time**: Pesquisa de domínio não documentada é pesquisa perdida. Socialize as descobertas nas dailies ou em sessões dedicadas.
