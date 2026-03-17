# Symptom-Cause Separation

## Título e Propósito

O **Symptom-Cause Separation** é um framework para disciplinar a equipe a distinguir rigorosamente entre o que se observa (sintoma) e o que produz o que se observa (causa). O propósito é evitar o erro mais caro em engenharia: construir uma solução perfeita para o sintoma enquanto a causa raiz continua ativa, gerando novos sintomas.

## Quando Usar

- Quando tickets de bug descrevem comportamentos sem investigar origens
- Quando a mesma classe de problema reaparece após "correções"
- Em triagem de incidentes para priorizar investigação vs. mitigação
- Quando stakeholders apresentam pedidos que parecem soluções para sintomas
- Antes de estimar qualquer trabalho corretivo

## Conceitos-Chave

1. **Sintoma**: Efeito observável — algo que alguém vê, sente ou mede. Exemplos: lentidão, erro na tela, dados incorretos.
2. **Causa Proximal**: O mecanismo técnico imediato que produz o sintoma. Exemplo: query sem índice.
3. **Causa Raiz**: A razão estrutural pela qual a causa proximal existe. Exemplo: ausência de revisão de queries no processo de deploy.
4. **Cadeia Causal**: A sequência completa de causa raiz → causa proximal → sintoma. Pode ter múltiplos níveis.
5. **Mitigação vs. Correção**: Mitigação trata o sintoma (apaga o incêndio). Correção elimina a causa (remove o combustível).

## Processo / Passos

### Passo 1 — Listar Observações Brutas
Colete todas as observações sem interpretá-las. "O que exatamente está acontecendo?" Use linguagem descritiva, não explicativa.

### Passo 2 — Classificar como Sintoma ou Causa
Para cada observação, pergunte: "Isso é algo que alguém vê/experimenta ou é uma explicação de por que algo acontece?" Classifique cada item.

### Passo 3 — Construir Cadeias Causais
Para cada sintoma, pergunte: "O que produz isso?" Conecte sintomas a causas proximais e causas proximais a causas raiz.

### Passo 4 — Verificar Direção da Causalidade
Para cada conexão na cadeia, pergunte: "Se eu eliminasse essa causa, o sintoma desapareceria?" Se não, a conexão está errada ou incompleta.

### Passo 5 — Identificar Causas Compartilhadas
Verifique se múltiplos sintomas compartilham a mesma causa raiz. Isso indica alto alavancagem — resolver uma causa elimina vários sintomas.

### Passo 6 — Decidir: Mitigar ou Corrigir
Para cada cadeia, decida se a ação imediata é mitigação (tratar sintoma) ou correção (eliminar causa). Em incidentes, geralmente faz-se mitigação primeiro e correção depois.

### Passo 7 — Documentar a Separação
Registre o mapa completo de sintomas, causas e decisões para referência futura e aprendizado da equipe.

## Perguntas de Ativação

- "Se eu colocasse um band-aid nisso, o problema voltaria em outra forma?"
- "Estou descrevendo o que vejo ou o que acho que está causando o que vejo?"
- "Quantos outros sintomas desapareceriam se eu resolvesse essa causa?"
- "Essa 'solução' proposta trata o sintoma ou a causa?"
- "Temos dados que comprovam a relação entre essa causa e esse sintoma?"
- "Esse problema já foi 'corrigido' antes? Se sim, por que voltou?"

## Output Esperado

| Sintoma Observado | Causa Proximal | Causa Raiz | Evidência | Ação: Mitigar ou Corrigir |
|---|---|---|---|---|
| Página de checkout lenta (>5s) | Query N+1 no carregamento de itens | Ausência de eager loading no ORM | APM mostra 200+ queries por request | Corrigir: adicionar eager loading |
| Usuários reportam dados desatualizados | Cache não invalida após update | Evento de invalidação não implementado | Logs mostram cache hit com dados stale | Corrigir: implementar invalidação |
| Timeout em integrações | Retry sem backoff exponencial | Padrão de retry copiado sem revisão | Métricas de timeout concentradas em picos | Corrigir: implementar backoff |

## Armadilhas Comuns

1. **Tratar sintoma como causa**: "O sistema está lento" não é causa — é sintoma. A causa é o que produz a lentidão.
2. **Parar na causa proximal**: Corrigir a query lenta sem perguntar por que queries lentas passam pelo processo de review.
3. **Causalidade reversa**: Assumir que A causa B quando na verdade B causa A, ou ambos são causados por C.
4. **Correlação como causalidade**: "O problema começou quando fizemos deploy" não prova que o deploy causou o problema.
5. **Mitigação permanente**: Aplicar uma mitigação de emergência e nunca voltar para fazer a correção real.
6. **Causa raiz única forçada**: Insistir que há apenas uma causa raiz quando o problema é multifatorial.
