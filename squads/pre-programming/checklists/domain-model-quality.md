# Checklist: Qualidade do Modelo de Domínio

## Propósito
Garantir que o modelo de domínio captura corretamente entidades, invariantes, estados e ciclos de vida, refletindo as regras de negócio de forma precisa.

## Quando Usar
- Ao modelar o domínio do problema
- Antes de definir schemas de banco de dados ou contratos de API
- Quando regras de negócio parecem confusas ou contraditórias

---

## Checklist

### Entidades e Agregados
- [ ] Entidades principais do domínio estão identificadas e nomeadas
- [ ] Cada entidade tem identidade clara (como é distinguida de outra)
- [ ] Value Objects estão diferenciados de Entidades
- [ ] Agregados estão definidos com raiz clara (aggregate root)
- [ ] Relacionamentos entre entidades estão mapeados (1:1, 1:N, N:M)

### Invariantes e Regras de Negócio
- [ ] Invariantes de cada entidade/agregado estão documentados
- [ ] Regras de validação estão explícitas (o que torna um dado válido/inválido)
- [ ] Regras de negócio estão expressas em linguagem ubíqua do domínio
- [ ] Regras condicionais estão mapeadas (se X então Y)
- [ ] Conflitos entre regras foram identificados e resolvidos

### Estados e Transições
- [ ] Estados possíveis de cada entidade principal estão enumerados
- [ ] Transições válidas entre estados estão definidas (máquina de estados)
- [ ] Transições inválidas estão explicitamente proibidas
- [ ] Eventos que disparam transições estão identificados
- [ ] Estados terminais estão identificados (não há saída)

### Ciclos de Vida
- [ ] Ciclo de vida completo de cada entidade está mapeado (criação → término)
- [ ] Condições de criação estão definidas (o que precisa existir para criar)
- [ ] Condições de exclusão/arquivamento estão definidas
- [ ] Impacto da exclusão em entidades relacionadas está documentado
- [ ] Temporalidade está considerada (expiração, TTL, vigência)

### Linguagem Ubíqua
- [ ] Existe glossário de termos do domínio
- [ ] Termos são consistentes entre documentação, código e comunicação
- [ ] Sinônimos e homônimos foram resolvidos
- [ ] Bounded contexts estão identificados quando termos mudam de significado
- [ ] Linguagem do domínio foi validada com especialistas do negócio

---

## Critérios de Aprovação
- **Mínimo**: Entidades, Invariantes e Estados completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Entidades sem invariantes ou estados indefinidos

## Sinais de Alerta (Red Flags)
- Modelo com entidades que são apenas "tabelas do banco" sem comportamento
- Ausência de invariantes (todo estado é válido = modelo anêmico)
- Entidade com 30+ atributos (provavelmente precisa ser decomposta)
- Estados que não têm transições definidas
- Linguagem técnica no modelo de domínio em vez de linguagem de negócio

## Agente Responsável
**Agente de Solution Architecture** — responsável pela modelagem e validação do domínio.
