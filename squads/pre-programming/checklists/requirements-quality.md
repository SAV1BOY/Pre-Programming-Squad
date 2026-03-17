# Checklist: Qualidade dos Requisitos

## Propósito
Garantir que os requisitos estão claros, completos, não-ambíguos e verificáveis antes de avançar para design de solução ou implementação.

## Quando Usar
- Após a fase de discovery, ao formalizar requisitos
- Antes de iniciar o design de solução ou arquitetura
- Em revisões periódicas de requisitos durante o pré-programming

---

## Checklist

### Clareza e Completude
- [ ] Cada requisito está escrito em linguagem clara e sem jargão desnecessário
- [ ] Cada requisito é independente (pode ser entendido sem ler outros)
- [ ] Cada requisito é verificável (existe forma de testar se foi atendido)
- [ ] Requisitos funcionais estão separados dos não-funcionais
- [ ] Não há requisitos duplicados ou contraditórios

### Requisitos Explícitos
- [ ] Comportamentos esperados do sistema estão descritos com inputs e outputs
- [ ] Regras de negócio estão formalizadas com exemplos concretos
- [ ] Fluxos principais (happy path) estão documentados passo a passo
- [ ] Requisitos não-funcionais têm valores mensuráveis (latência < 200ms, uptime 99.9%)
- [ ] Requisitos de dados estão especificados (formatos, validações, limites)

### Requisitos Implícitos
- [ ] Requisitos de segurança foram considerados mesmo sem pedido explícito
- [ ] Requisitos de acessibilidade foram avaliados
- [ ] Requisitos de auditoria e compliance foram verificados
- [ ] Expectativas de performance foram tornadas explícitas
- [ ] Requisitos de observabilidade e monitoramento foram incluídos

### Ambiguidades
- [ ] Termos ambíguos foram identificados e definidos em glossário
- [ ] Palavras como "rápido", "seguro", "fácil" foram quantificadas
- [ ] Casos onde "depende" aparecem foram resolvidos com regras claras
- [ ] Pronomes vagos ("isso", "aquilo") foram substituídos por termos específicos
- [ ] Cada "ou" e "e" nos requisitos tem semântica clara

### Rastreabilidade
- [ ] Cada requisito tem identificador único
- [ ] Cada requisito tem origem rastreável (stakeholder, discovery, regulação)
- [ ] Requisitos estão priorizados (MoSCoW ou similar)
- [ ] Dependências entre requisitos estão mapeadas
- [ ] Requisitos estão versionados com histórico de mudanças

---

## Critérios de Aprovação
- **Mínimo**: Clareza/Completude e Ambiguidades completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Requisitos ambíguos não resolvidos ou sem verificabilidade

## Sinais de Alerta (Red Flags)
- Requisitos escritos como solução ("usar Redis para cache") em vez de necessidade
- Ausência total de requisitos não-funcionais
- Todos os requisitos com mesma prioridade (sem priorização real)
- Requisitos que ninguém consegue explicar a origem
- Lista com mais de 50 requisitos sem agrupamento ou hierarquia

## Agente Responsável
**Agente de Requirements & Scope** — responsável por refinar e validar a qualidade dos requisitos.
