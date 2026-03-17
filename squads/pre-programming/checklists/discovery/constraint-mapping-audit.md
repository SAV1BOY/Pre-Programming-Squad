# Checklist: Auditoria de Mapeamento de Restrições

## Propósito
Verificar se as restrições do projeto são reais e validadas, distinguindo restrições genuínas de suposições não questionadas, e garantindo que todas estão documentadas.

## Quando Usar
- No início da discovery ao mapear o espaço de solução
- Quando restrições parecem arbitrárias ou contraditórias
- Antes de descartar opções de solução por "restrição"

---

## Checklist

### Restrições Reais
- [ ] Restrições de prazo estão validadas com justificativa concreta (evento, contrato, regulação)
- [ ] Restrições orçamentárias têm valor definido e aprovado
- [ ] Restrições técnicas são verificáveis (limitação de plataforma, licença, infra)
- [ ] Restrições regulatórias estão confirmadas com fonte legal/compliance
- [ ] Restrições de equipe (tamanho, skills) estão validadas com gestão

### Restrições Assumidas
- [ ] Suposições que estão sendo tratadas como restrições foram identificadas
- [ ] Cada suposição-restrição foi questionada ("isso é realmente uma restrição?")
- [ ] Restrições históricas foram reavaliadas (podem não ser mais válidas)
- [ ] Restrições políticas foram diferenciadas de restrições técnicas
- [ ] Custo de remover cada restrição foi avaliado (algumas são negociáveis)

### Impacto das Restrições
- [ ] Impacto de cada restrição no espaço de solução está avaliado
- [ ] Restrições que eliminam opções viáveis estão destacadas
- [ ] Conflitos entre restrições foram identificados
- [ ] Restrições foram priorizadas (quais são inegociáveis vs flexíveis)
- [ ] Trade-offs impostos pelas restrições estão documentados

### Documentação
- [ ] Todas as restrições estão registradas em um único lugar
- [ ] Cada restrição tem fonte/responsável identificado
- [ ] Data de validação de cada restrição está registrada
- [ ] Restrições removidas ou alteradas estão versionadas
- [ ] Restrições foram comunicadas a todo o time

### Gestão de Restrições
- [ ] Processo para questionar restrições está definido (quem pode negociar)
- [ ] Restrições que podem mudar durante o projeto estão monitoradas
- [ ] Novas restrições descobertas durante o projeto são incorporadas
- [ ] Impacto de mudança de restrição é avaliado antes de aceitar
- [ ] Stakeholders são notificados quando restrições mudam

---

## Critérios de Aprovação
- **Mínimo**: Restrições Reais e Restrições Assumidas completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Restrições não validadas sendo tratadas como absolutas

## Sinais de Alerta (Red Flags)
- "Sempre fizemos assim" como justificativa de restrição
- Restrição de prazo sem justificativa ("precisa ser para Q2")
- Todas as restrições são inegociáveis (nenhuma flexibilidade)
- Restrição técnica que ninguém consegue explicar tecnicamente
- Nenhuma restrição identificada (análise incompleta)

## Agente Responsável
**Agente de Discovery & Framing** — responsável por mapear e validar restrições do projeto.
