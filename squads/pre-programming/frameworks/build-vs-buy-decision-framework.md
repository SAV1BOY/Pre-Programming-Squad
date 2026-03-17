# Build vs. Buy Decision Framework

## Título e Propósito

O **Build vs. Buy Decision Framework** é um sistema estruturado para decidir quando construir internamente e quando adotar soluções prontas (SaaS, bibliotecas, serviços gerenciados). O propósito é evitar dois erros caros: reinventar a roda (síndrome do "Not Invented Here") e adotar soluções externas para competências que deveriam ser core.

## Quando Usar

- Quando surge necessidade de uma nova capacidade (autenticação, pagamentos, busca, monitoramento, etc.)
- Quando uma solução interna existente está custando caro para manter
- Quando um fornecedor propõe substituir algo que a equipe construiu
- Em revisões arquiteturais para avaliar componentes do sistema
- Quando a equipe debate se deve usar biblioteca X ou implementar do zero

## Conceitos-Chave

1. **Competência Core vs. Contexto**: Core é o que diferencia seu produto no mercado. Contexto é tudo que é necessário mas não diferencia. Build para core, buy para contexto.
2. **Custo Total de Propriedade (TCO)**: Não compare preço de licença com custo de desenvolvimento. Compare licença + integração + manutenção + risco de lock-in com desenvolvimento + manutenção + evolução + recrutamento.
3. **Lock-in**: Dependência de um fornecedor que torna caro mudar. Avalie: quão padrão é a interface? Há alternativas? O custo de migração é aceitável?
4. **Debt de Integração**: Toda solução externa exige integração. Quanto mais customização, mais o "buy" se parece com "build".
5. **Velocidade vs. Controle**: Buy é mais rápido para começar. Build dá mais controle a longo prazo.

## Processo / Passos

### Passo 1 — Definir a Capacidade Necessária
Descreva o que precisa ser feito, não como. Foque na necessidade, não na solução.

### Passo 2 — Classificar: Core ou Contexto
Pergunte: "Se essa capacidade fosse 10x melhor que a concorrência, nosso produto seria significativamente melhor?" Se sim, é core.

### Passo 3 — Avaliar Opções de Buy
Liste soluções disponíveis no mercado. Para cada uma, avalie: funcionalidades, preço, SLA, integração, lock-in, maturidade, comunidade.

### Passo 4 — Estimar Custo de Build
Estime: desenvolvimento inicial, manutenção contínua, evolução, operação, documentação e risco de falha.

### Passo 5 — Calcular TCO de Ambos
Compare custo total em horizonte de 2-3 anos, incluindo custos ocultos: integração, customização, migração de dados, treinamento.

### Passo 6 — Avaliar Riscos
Para cada opção, mapeie riscos: lock-in, descontinuação do fornecedor, perda de conhecimento interno, segurança, compliance.

### Passo 7 — Decidir com Critérios Explícitos
Use uma scorecard com pesos para cada critério. Documente a decisão e os fatores decisivos.

## Perguntas de Ativação

- "Isso é o que nos diferencia no mercado ou é infraestrutura?"
- "Em 2 anos, vamos querer ter controle total sobre isso?"
- "Quanto custa manter essa solução interna por ano, incluindo pessoas?"
- "Se o fornecedor triplicar o preço ou fechar, qual é nosso plano B?"
- "Temos (e teremos) as skills internas para manter isso?"
- "Estamos querendo construir porque é divertido ou porque é estratégico?"

## Output Esperado

| Critério | Build | Buy (Solução X) | Peso |
|---|---|---|---|
| Alinhamento com core business | Alto — é diferencial | N/A — genérico | 5 |
| Tempo para produção | 3 meses | 2 semanas | 4 |
| TCO em 2 anos | R$ 400k (dev + manutenção) | R$ 250k (licença + integração) | 4 |
| Controle e customização | Total | Limitado por API | 3 |
| Risco de lock-in | Nenhum | Alto — formato proprietário | 3 |
| Manutenção contínua | Equipe interna necessária | Fornecedor mantém | 2 |

**Decisão**: [Build/Buy] porque [justificativa baseada nos pesos].

## Armadilhas Comuns

1. **"Not Invented Here"**: Recusar soluções externas por orgulho de engenharia, reconstruindo o que o mercado já faz bem.
2. **Subestimar custo de manutenção do Build**: O custo de construir é uma fração do custo de manter, evoluir e operar ao longo dos anos.
3. **Subestimar custo de integração do Buy**: A solução "pronta" pode levar meses para integrar e customizar.
4. **Ignorar lock-in**: Adotar solução proprietária sem plano de saída é apostar que o fornecedor será bom para sempre.
5. **Comparação injusta**: Comparar o custo de build sem manutenção com o custo de buy com licença anual.
6. **Decisão emocional**: "A equipe quer construir" ou "o diretor viu uma demo legal" não são critérios de decisão.
