# Checklist: Qualidade do Sketch de Arquitetura

## Propósito
Verificar se o esboço arquitetural define módulos, fluxos, fronteiras e responsabilidades de forma clara o suficiente para guiar a implementação sem ambiguidade.

## Quando Usar
- Após a escolha da solução, ao desenhar a arquitetura
- Antes de detalhar contratos de API ou modelo de domínio
- Em revisões de arquitetura com o time

---

## Checklist

### Módulos e Componentes
- [ ] Todos os módulos/serviços/componentes principais estão identificados
- [ ] Cada módulo tem nome descritivo e propósito definido em uma frase
- [ ] A granularidade dos módulos é adequada (nem monolito nem nano-serviços)
- [ ] Módulos compartilhados ou transversais estão explícitos (auth, logging, etc.)
- [ ] Tecnologias/stacks por módulo estão indicadas quando relevante

### Fluxo de Dados
- [ ] Fluxos principais estão representados visualmente (diagrama)
- [ ] Direção do fluxo de dados está clara (quem chama quem)
- [ ] Fluxos síncronos vs assíncronos estão diferenciados
- [ ] Pontos de persistência de dados estão identificados
- [ ] Fluxos de erro/fallback estão representados

### Fronteiras (Boundaries)
- [ ] Fronteiras entre módulos estão claramente definidas
- [ ] Interfaces/contratos entre módulos estão indicados (mesmo que alto nível)
- [ ] Fronteiras com sistemas externos estão marcadas
- [ ] Fronteiras de segurança (trust boundaries) estão identificadas
- [ ] Fronteiras de deploy estão definidas (o que é deployado junto vs separado)

### Responsabilidades
- [ ] Cada módulo tem responsabilidade única e clara (SRP)
- [ ] Não há sobreposição de responsabilidades entre módulos
- [ ] Responsabilidades de orquestração vs execução estão claras
- [ ] Responsabilidade de dados está definida (quem é dono de cada dado)
- [ ] Responsabilidade de tratamento de erros está atribuída

### Comunicação e Formato
- [ ] Existe diagrama de arquitetura legível e atualizado
- [ ] O diagrama usa notação consistente (C4, UML ou outro padrão)
- [ ] Decisões arquiteturais estão acompanhadas de justificativa
- [ ] O sketch é compreensível por devs que não participaram da discussão
- [ ] Pontos de incerteza ou decisões em aberto estão sinalizados

---

## Critérios de Aprovação
- **Mínimo**: Módulos, Fronteiras e Responsabilidades completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Módulos sem responsabilidade definida ou fronteiras ausentes

## Sinais de Alerta (Red Flags)
- Diagrama que é apenas "caixas e setas" sem explicação
- Um módulo que faz "tudo" (God Module)
- Fronteiras entre módulos indefinidas ("depois a gente define")
- Arquitetura que requer tecnologia que o time não domina sem plano de capacitação
- Sketch que não pode ser explicado em 5 minutos

## Agente Responsável
**Agente de Solution Architecture** — responsável pelo design e validação do sketch arquitetural.
