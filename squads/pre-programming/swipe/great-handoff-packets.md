# Ótimos Pacotes de Handoff — Exemplos Anotados

## Introdução

Um pacote de handoff excepcional transfere não apenas documentos, mas contexto, raciocínio e sabedoria acumulada. O time receptor deve ser capaz de iniciar o desenvolvimento com confiança, sabendo o que construir, por que, quais armadilhas evitar e onde encontrar cada informação necessária. Um handoff ruim transforma semanas de pré-programação em desperdício.

---

## Exemplo 1 — Handoff de Projeto de Checkout

### O Pacote

> **Índice do Handoff**:
> 1. Project Brief (2 páginas) — Problema, solução, métricas, escopo
> 2. Design Doc (8 páginas) — Arquitetura, fluxos, modelo de dados, APIs
> 3. ADRs (5 decisões) — Stack, banco, mensageria, autenticação, cache
> 4. Contratos de API (3 contratos) — Pedidos, Pagamento, Frete
> 5. Plano de Testes (4 páginas) — Pirâmide, cenários, edge cases, dados
> 6. Registro de Riscos (8 riscos) — Com mitigações e contingências
> 7. Mapa de Dependências (12 dependências) — Status, contatos, alternativas
> 8. Glossário do Domínio (30 termos) — Linguagem ubíqua documentada
> 9. Premissas Abertas (3 itens) — Com responsável e prazo de validação
> 10. Perguntas Frequentes (15 Q&A) — Antecipando dúvidas comuns
>
> **Sessão de Walkthrough**: 2 horas, gravada, com todo o time de desenvolvimento presente. Estrutura: 30min contexto de negócio, 45min arquitetura e design, 30min riscos e dependências, 15min dúvidas.
>
> **Suporte Pós-Handoff**: Membro do squad disponível por 2 semanas para dúvidas. Canal Slack dedicado. Revisão de PR dos primeiros 3 dias.

### Por que funciona

- **Índice organizado**: O time sabe exatamente onde encontrar cada informação
- **Walkthrough estruturado e gravado**: Quem não pôde comparecer tem acesso
- **FAQ antecipando dúvidas**: Reduz drasticamente as perguntas de volta ao squad
- **Suporte pós-handoff**: Transição não é evento pontual, é processo
- **Glossário incluído**: Time de dev fala a mesma língua que o negócio

---

## Exemplo 2 — Handoff de Migração de Infraestrutura

### O Pacote

> **Checklist de Prontidão do Receptor**:
> - [ ] Acesso ao repositório configurado para todos os membros
> - [ ] Ambiente de desenvolvimento local funcionando
> - [ ] Acesso a staging e sandbox de APIs externas
> - [ ] Credenciais de serviços de terceiros provisionadas
> - [ ] CI/CD pipeline configurado e testado
> - [ ] Monitoring dashboards criados
>
> **Decisões com Contexto Perdido**:
> Para cada ADR, seção extra explicando "o que tentamos que não funcionou":
> - "Tentamos usar Redis Cluster, mas o driver Node tinha bug com redirects. Optamos por Redis Sentinel."
> - "Consideramos gRPC para comunicação interna, mas o API Gateway não suportava. Mantivemos REST com circuit breaker."
>
> **Mapa de "Onde Dói"**:
> - "O serviço de frete tem timeout de 10s. Se ultrapassar, precisamos retornar estimativa cached."
> - "A API de KYC rejeita silenciosamente requests com headers duplicados. Configurar proxy para deduplicar."
> - "O banco legado tem triggers que atualizam tabelas de audit. Cuidado com deadlocks em batch updates."

### Por que funciona

- **Checklist de prontidão**: Verifica se o receptor está realmente preparado
- **Contexto de tentativas falhas**: O que NÃO fazer é tão valioso quanto o que fazer
- **Mapa de dores**: Conhecimento tácito documentado — evita que o time repita descobertas dolorosas

---

## Lições Extraídas

1. **Organize com índice**: Time de dev não vai ler 50 páginas. Precisa saber onde está o quê
2. **Grave o walkthrough**: Pessoas mudam de time, novos membros entram — a gravação é eterna
3. **Inclua o que falhou**: Tentativas malsucedidas são conhecimento precioso
4. **Antecipe perguntas**: FAQ bem feito economiza horas de interrupção
5. **Defina suporte pós-handoff**: Handoff sem suporte é abandono
6. **Verifique prontidão do receptor**: Não adianta entregar se o time não tem acesso, ambiente ou contexto
7. **Documente o tácito**: "Onde dói" e "cuidados especiais" são o tipo de conhecimento que se perde
8. **Peça feedback**: Após 1 semana, pergunte ao receptor o que faltou — melhore para o próximo handoff
