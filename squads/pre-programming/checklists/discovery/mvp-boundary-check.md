# Checklist: Verificação de Fronteira do MVP

## Propósito
Garantir que o MVP representa o menor escopo que entrega valor real, sem ser tão pequeno que não resolve nada nem tão grande que não pode ser entregue nas restrições.

## Quando Usar
- Ao definir o escopo da primeira versão
- Quando há pressão para "incluir só mais uma coisa"
- Quando o MVP parece grande demais para as restrições

---

## Checklist

### Menor Escopo Valioso
- [ ] O MVP resolve o problema central identificado na discovery
- [ ] Cada feature do MVP contribui diretamente para o critério de sucesso
- [ ] Features que são "nice-to-have" foram removidas do MVP
- [ ] O MVP pode ser usado por um usuário real e gerar valor
- [ ] É possível coletar feedback real com o MVP

### Viabilidade
- [ ] O MVP pode ser implementado dentro das restrições de prazo
- [ ] O MVP pode ser implementado com os recursos disponíveis
- [ ] Complexidade técnica do MVP está no nível adequado para a v1
- [ ] Dívida técnica aceita no MVP está documentada e é consciente
- [ ] O MVP não cria problemas que inviabilizam iterações futuras

### Completude Funcional
- [ ] Fluxo principal (happy path) funciona de ponta a ponta
- [ ] Erros críticos são tratados (não precisa ser elegante, mas não pode quebrar)
- [ ] Segurança mínima está garantida (auth, dados sensíveis)
- [ ] Performance mínima aceitável é atingida
- [ ] Observabilidade mínima para operar está incluída

### Fronteiras Claras
- [ ] O que está dentro do MVP está listado explicitamente
- [ ] O que está fora do MVP está listado com justificativa
- [ ] Não há "áreas cinza" (tudo é in ou out)
- [ ] Features cortadas têm destino definido (v2, backlog, descartado)
- [ ] Stakeholders aprovaram as fronteiras do MVP

### Evolução
- [ ] O MVP é extensível (não é um dead-end técnico)
- [ ] Caminho de evolução do MVP para a versão completa está esboçado
- [ ] Critérios para avançar do MVP para a próxima iteração estão definidos
- [ ] Aprendizados esperados do MVP estão listados (o que queremos validar)
- [ ] O MVP não compromete a experiência a ponto de invalidar o feedback

---

## Critérios de Aprovação
- **Mínimo**: Menor Escopo Valioso e Fronteiras Claras completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: MVP que não resolve o problema central ou fronteiras indefinidas

## Sinais de Alerta (Red Flags)
- MVP com 30+ features (não é mínimo)
- MVP que não pode ser demonstrado a um usuário real
- MVP que requer 6 meses de implementação
- "MVP" que é na verdade o produto completo com menos polish
- MVP que cria dívida técnica impossível de pagar depois

## Agente Responsável
**Agente de Requirements & Scope** — em colaboração com o **Agente de Discovery & Framing**.
