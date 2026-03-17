# Checklist: Auditoria de Definição de Fronteiras

## Propósito
Verificar se as responsabilidades e fronteiras entre módulos, serviços e sistemas estão claramente definidas, evitando sobreposições e lacunas.

## Quando Usar
- Ao definir ou revisar a arquitetura da solução
- Quando há dúvida sobre "quem é responsável pelo quê"
- Antes de definir contratos entre componentes

---

## Checklist

### Fronteiras de Responsabilidade
- [ ] Cada módulo/serviço tem uma responsabilidade principal claramente definida
- [ ] Não há sobreposição de responsabilidade entre módulos
- [ ] Não há lacuna de responsabilidade (algo que ninguém faz)
- [ ] Responsabilidades estão documentadas em linguagem que devs entendem
- [ ] A regra "se X muda, apenas módulo Y precisa mudar" é verdadeira

### Fronteiras de Dados
- [ ] Cada entidade de dados tem um único dono (source of truth)
- [ ] Dados compartilhados entre módulos têm protocolo de acesso definido
- [ ] Não há acesso direto ao banco de outro módulo
- [ ] Formato e contrato de dados na fronteira estão especificados
- [ ] Estratégia de consistência eventual vs forte está definida por fronteira

### Fronteiras de Deploy
- [ ] O que é deployado junto vs separado está definido
- [ ] Dependências de deploy entre módulos estão mapeadas
- [ ] Cada unidade de deploy pode ser atualizada independentemente (se possível)
- [ ] Versionamento de cada componente deployável está definido
- [ ] Processo de deploy está documentado por componente

### Fronteiras de Segurança
- [ ] Trust boundaries estão identificadas (onde dados mudam de nível de confiança)
- [ ] Autenticação e autorização estão definidas em cada fronteira
- [ ] Dados que cruzam fronteiras de segurança são validados
- [ ] Fronteiras de rede (DMZ, VPC, subnet) estão mapeadas
- [ ] Princípio de menor privilégio está aplicado entre módulos

### Fronteiras de Time
- [ ] Cada módulo tem um time responsável definido
- [ ] Dependências entre times estão mapeadas com base nas fronteiras
- [ ] Fronteiras foram desenhadas para minimizar comunicação entre times (Lei de Conway)
- [ ] Processo de mudança em fronteiras compartilhadas está definido
- [ ] Times concordam com as fronteiras definidas

---

## Critérios de Aprovação
- **Mínimo**: Fronteiras de Responsabilidade e Dados completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Responsabilidades sobrepostas ou lacunas não resolvidas

## Sinais de Alerta (Red Flags)
- Módulo que "faz de tudo" (God Module/Service)
- Múltiplos módulos acessando o mesmo banco diretamente
- Fronteiras definidas por tecnologia em vez de domínio
- Nenhuma fronteira de segurança definida
- Times discordando sobre quem é responsável por uma funcionalidade

## Agente Responsável
**Agente de Solution Architecture** — responsável por definir e validar fronteiras arquiteturais.
