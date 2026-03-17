# Rollback Safety Ladder

## Título e Propósito

O **Rollback Safety Ladder** é um framework que define níveis progressivos de capacidade de rollback, do mais seguro ao mais arriscado. O propósito é garantir que cada mudança tenha uma estratégia de rollback proporcional ao seu risco — e que a equipe saiba exatamente em que "degrau" está antes de fazer deploy.

## Quando Usar

- Ao planejar qualquer deploy ou mudança em produção
- Na avaliação de risco de migrações e mudanças de schema
- Quando a equipe precisa decidir entre estratégias de deploy
- Em revisões de arquitetura para avaliar reversibilidade de decisões
- Após incidentes onde rollback falhou ou não existia

## Conceitos-Chave

1. **Nível de Segurança de Rollback**: Quão fácil, rápido e seguro é reverter uma mudança. Quanto mais alto o nível, mais seguro.
2. **Escada de Segurança**: Níveis de 5 (mais seguro) a 0 (sem rollback), cada um com capacidades e riscos diferentes.
3. **Tempo de Rollback**: Tempo entre decidir reverter e ter o sistema no estado anterior. De segundos a dias.
4. **Completude do Rollback**: O rollback reverte tudo (código, dados, configuração, estado) ou apenas parte?
5. **Ponto de Não-Retorno (PNR)**: O momento após o qual rollback se torna impossível ou proibitivamente caro.

## Processo / Passos

### Passo 1 — Identificar a Mudança
Descreva: o que muda (código, dados, config, infra)? O que é afetado?

### Passo 2 — Classificar na Escada
Identifique em qual nível a mudança se encontra:

**Nível 5 — Instant Toggle**: Feature flag. Rollback em segundos, sem redeploy.
**Nível 4 — Quick Redeploy**: Rollback via deploy da versão anterior. Minutos.
**Nível 3 — Reversible Migration**: Mudança de dados com script de reversão testado. Horas.
**Nível 2 — Manual Recovery**: Requer intervenção manual para restaurar estado. Horas a dias.
**Nível 1 — Backup Restore**: Rollback via restauração de backup. Perda de dados recentes.
**Nível 0 — No Rollback**: Mudança irreversível. Erro significa conviver ou reescrever.

### Passo 3 — Avaliar Adequação
O nível de rollback é adequado para o risco da mudança? Mudanças de alto risco devem estar em Nível 4+.

### Passo 4 — Subir na Escada se Necessário
Se o nível é insuficiente para o risco, projete mecanismos para subir: adicionar feature flag, criar script de reversão, implementar blue-green deploy.

### Passo 5 — Testar o Rollback
Execute o rollback em ambiente de staging. Rollback não testado é teoria, não capacidade.

### Passo 6 — Documentar o Plano
Registre: nível de rollback, como executar, quem executa, tempo esperado, PNR se houver.

### Passo 7 — Comunicar o PNR
Se houver ponto de não-retorno, todos devem saber quando ele é e o que significa.

## Perguntas de Ativação

- "Em que nível da escada está nosso rollback para essa mudança?"
- "Esse nível é adequado para o risco?"
- "Testamos o rollback ou estamos confiando que funciona?"
- "Há um ponto de não-retorno? Quando ele é e todos sabem?"
- "Se precisarmos reverter às 3h da manhã, quem faz e como?"
- "O rollback é completo (código + dados + config) ou apenas parcial?"

## Output Esperado

| Mudança | Nível Atual | Nível Necessário | Gap | Ação para Subir | Tempo de Rollback | PNR |
|---|---|---|---|---|---|---|
| Nova feature de busca | 5 (feature flag) | 4+ | OK | Nenhuma | ~5 segundos | Não há |
| Migração de schema de pedidos | 2 (manual) | 3+ | GAP | Criar script de reversão + testar | ~2 horas | Após rodar script de limpeza (dia 3) |
| Troca de provider de email | 4 (redeploy) | 4+ | OK | Nenhuma | ~5 minutos | Não há |
| Migração de banco para nova instância | 1 (backup) | 3+ | GAP | Implementar replicação bidirecional + cutover | ~4 horas para backup restore | Após desligar instância antiga |
| Mudança de formato de dados em fila | 0 (sem rollback) | 3+ | GAP CRÍTICO | Versionar formato + consumer suportar ambos | — | Imediato |

## Armadilhas Comuns

1. **Rollback não testado**: "Temos feature flag" — mas ninguém testou se desligar a flag realmente reverte o comportamento sem efeitos colaterais.
2. **Rollback parcial**: Reverter código mas não dados, ou reverter config mas não código. O sistema fica em estado inconsistente.
3. **Ignorar o PNR**: Não saber que existe um ponto de não-retorno e descobrir tarde demais.
4. **Nível 0 normalizado**: Tratar mudanças irreversíveis como normais em vez de exceções que exigem validação extra.
5. **Tempo de rollback subestimado**: "Alguns minutos" que na prática levam 2 horas porque dependem de aprovação, acesso e coordenação.
6. **Dependência de pessoa**: Apenas uma pessoa sabe como fazer rollback. Se estiver indisponível, o sistema fica no estado quebrado.
