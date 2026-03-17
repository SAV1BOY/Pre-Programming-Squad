# Checklist: Qualidade do Pacote de Handoff

## Propósito
Garantir que o pacote entregue ao time de desenvolvimento contém toda a documentação, contratos, testes e riscos necessários para implementação sem adivinhação.

## Quando Usar
- Ao preparar a entrega para o time de implementação
- Como verificação final antes do handoff formal
- Quando o time de dev reporta que "falta informação"

---

## Checklist

### Documentação
- [ ] Documento de visão/contexto do projeto está incluído
- [ ] Requisitos funcionais e não-funcionais estão documentados
- [ ] Glossário de termos do domínio está disponível
- [ ] Decisões tomadas durante pré-programação estão registradas (ADRs)
- [ ] Diagrama de arquitetura atualizado está incluído

### Contratos
- [ ] Contratos de API estão completos com schemas e exemplos
- [ ] Modelo de domínio está documentado com entidades e regras
- [ ] Contratos com sistemas externos estão especificados
- [ ] Formatos de dados de entrada e saída estão definidos
- [ ] Versionamento de contratos está especificado

### Estratégia de Testes
- [ ] Plano de testes por nível está incluído
- [ ] Casos de teste críticos estão descritos
- [ ] Dados de teste estão identificados ou disponíveis
- [ ] Critérios de aceite por funcionalidade estão definidos
- [ ] Definition of Done está clara e acordada

### Riscos e Mitigações
- [ ] Lista de riscos identificados está incluída com severidade
- [ ] Mitigações para cada risco estão documentadas
- [ ] Modos de falha e estratégias de fallback estão descritos
- [ ] Plano de rollback está documentado
- [ ] Premissas e suposições estão explícitas com status de validação

### Operacional
- [ ] Requisitos de observabilidade estão documentados
- [ ] Requisitos de segurança estão especificados
- [ ] Estimativa de esforço está incluída com breakdown
- [ ] Dependências de outros times/sistemas estão mapeadas com contatos
- [ ] Cronograma sugerido com gates está incluído

---

## Critérios de Aprovação
- **Mínimo**: Documentação, Contratos e Riscos completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Pacote sem contratos ou sem riscos documentados

## Sinais de Alerta (Red Flags)
- Pacote que é apenas "o Jira com as tasks"
- Documentação desatualizada em relação às decisões mais recentes
- Riscos listados sem mitigações
- Nenhum caso de teste incluído ("o dev escreve os testes")
- Time de dev recebe o pacote sem sessão de walkthrough

## Agente Responsável
**Agente de Final Review & Handoff** — responsável por montar e validar o pacote completo.
