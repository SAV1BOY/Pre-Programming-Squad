# Domain Modeler Checklist

## Propósito
Garantir que o modelo de domínio captura corretamente entidades, relações, regras de negócio e invariantes.

## Quando Usar
- Durante a fase correspondente do pipeline de pré-programação
- Em revisões de qualidade antes de avançar para a próxima fase
- Quando o Readiness Gatekeeper solicita verificação

---

## Checklist

### Modelo de Domínio
- [ ] Entidades principais estão identificadas e nomeadas
- [ ] Relações entre entidades estão mapeadas
- [ ] Invariantes de domínio estão documentados
- [ ] Estados e transições de cada entidade estão definidos
- [ ] Ciclo de vida das entidades está mapeado

### Regras de Negócio
- [ ] Regras de negócio estão explícitas e testáveis
- [ ] Exceções às regras estão documentadas
- [ ] Bounded contexts estão definidos
- [ ] Linguagem ubíqua está documentada
- [ ] Aggregates e seus limites estão claros

---

## Critérios de Aprovação
- **Mínimo:** 80% dos itens marcados
- **Recomendado:** 100% dos itens marcados
- **Bloqueador:** Qualquer item crítico não atendido deve ser escalado

## Red Flags
- Mais de 3 itens não marcados sem justificativa
- Itens marcados sem evidência de verificação real
- Checklist preenchido em menos de 5 minutos (superficialidade)
