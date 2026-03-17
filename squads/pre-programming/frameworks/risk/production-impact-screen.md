# Production Impact Screen

## Título e Propósito

O **Production Impact Screen** é um framework para avaliar o impacto potencial de uma mudança em produção antes de implementá-la. O propósito é criar um filtro rápido mas rigoroso que classifica mudanças por nível de risco em produção — permitindo calibrar o nível de cuidado (testes, reviews, rollout gradual) proporcional ao risco real.

## Quando Usar

- Antes de qualquer deploy em produção
- Na priorização de reviews — mudanças de alto impacto primeiro
- Ao decidir entre deploy imediato e canary release
- Quando a equipe precisa decidir se uma hotfix precisa de ciclo completo de QA
- Em planejamento de releases para sequenciar mudanças por risco

## Conceitos-Chave

1. **Impacto em Produção**: O efeito que uma falha na mudança teria sobre usuários, dados, receita e reputação.
2. **Superfície de Impacto**: Quantos usuários, funcionalidades ou dados são afetados se a mudança falhar.
3. **Velocidade de Detecção**: Quão rápido uma falha seria detectada — minutos (monitoramento) vs. semanas (reclamação de cliente).
4. **Velocidade de Recuperação**: Quão rápido podemos reverter ou corrigir se der errado.
5. **Classificação de Mudança**: Categorização que determina o processo: Low-risk (auto-deploy), Medium-risk (review + monitoring), High-risk (canary + manual approval).

## Processo / Passos

### Passo 1 — Descrever a Mudança
O que exatamente está sendo mudado? Código, configuração, schema, infraestrutura, dados?

### Passo 2 — Avaliar Superfície de Impacto
Quantos usuários são afetados? Quais funcionalidades? Há dados sendo modificados? Há impacto financeiro direto?

### Passo 3 — Avaliar Detectabilidade
Se der errado, como saberemos? Em quanto tempo? Temos alertas, métricas, logs?

### Passo 4 — Avaliar Reversibilidade
Podemos reverter rapidamente? Há ponto de não-retorno (migração de dados destrutiva)?

### Passo 5 — Classificar a Mudança
Use a matriz:

| | Alta Reversibilidade | Baixa Reversibilidade |
|---|---|---|
| **Baixo Impacto** | Low-risk | Medium-risk |
| **Alto Impacto** | Medium-risk | High-risk |

### Passo 6 — Definir Processo Adequado
- **Low-risk**: Deploy automático, monitoramento padrão
- **Medium-risk**: Code review, testes de integração, monitoramento ativo por 2h
- **High-risk**: Review múltipla, canary 1-5%, observação 24h, aprovação manual para expansão

### Passo 7 — Documentar e Comunicar
Registre a classificação e comunique à equipe. Quem monitora? Quem decide rollback?

## Perguntas de Ativação

- "Se essa mudança causar um bug, quantos usuários são afetados?"
- "Temos como detectar um problema em menos de 5 minutos?"
- "Se precisarmos reverter, é possível em menos de 10 minutos?"
- "Essa mudança afeta dados de forma irreversível?"
- "Qual é o pior cenário se isso der errado no pico de tráfego?"
- "Alguém vai estar monitorando após o deploy?"

## Output Esperado

```
MUDANÇA: Migração do motor de busca de Elasticsearch 7 para 8

AVALIAÇÃO DE IMPACTO:
- Superfície: 100% dos usuários (busca é funcionalidade core)
- Funcionalidades afetadas: Busca, filtros, autocomplete, recomendações
- Impacto financeiro: Direto — busca quebrada = vendas perdidas
- Impacto reputacional: Alto — busca é a primeira interação do usuário

DETECTABILIDADE:
- Alertas configurados: Sim — latência de busca, taxa de erro, throughput
- Tempo estimado de detecção: < 2 minutos
- Métrica principal: Taxa de resultados vazios

REVERSIBILIDADE:
- Método: Feature flag para redirecionar para ES7 (mantido em paralelo por 2 semanas)
- Tempo de reversão: < 1 minuto (toggle de feature flag)
- Ponto de não-retorno: Quando ES7 for desligado (planejado para semana 3)

CLASSIFICAÇÃO: HIGH-RISK (alto impacto, mas alta reversibilidade → Medium+ elevado para High por criticidade)

PROCESSO DEFINIDO:
- [✓] Code review por 2 seniors
- [✓] Testes de integração com dados de produção anonimizados
- [✓] Canary 1% por 2h → 5% por 4h → 25% por 24h → 100%
- [✓] Monitoramento ativo pelo dev responsável em cada estágio
- [✓] ES7 mantido como fallback por 2 semanas
- [✓] Responsável por rollback: [nome]
```

## Armadilhas Comuns

1. **Todas as mudanças como low-risk**: Otimismo que leva a deploys descuidados de mudanças impactantes.
2. **Todas as mudanças como high-risk**: Burocracia que impede velocidade de entrega mesmo para mudanças triviais.
3. **Deploy sem monitoramento**: Classificar corretamente mas não ter ninguém observando após o deploy.
4. **Reversibilidade assumida**: "Podemos reverter" sem ter testado se o rollback realmente funciona.
5. **Deploy na sexta à tarde**: Mudanças de médio/alto risco sem ninguém para monitorar no fim de semana.
6. **Impacto subestimado**: "Só afeta um endpoint" — mas esse endpoint é usado por 90% dos clientes.
