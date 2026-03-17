# Red Flag Escalation Framework

## Título e Propósito

O **Red Flag Escalation Framework** é um sistema para identificar, classificar e escalar sinais de alerta (red flags) que indicam que um projeto está em risco. O propósito é criar uma cultura onde red flags são detectados cedo e escalados rapidamente — em vez de serem ignorados por otimismo, medo ou pressão hierárquica, até se tornarem crises.

## Quando Usar

- Continuamente durante qualquer projeto (não é pontual, é permanente)
- Quando a equipe sente que algo "não está certo" mas não sabe como comunicar
- Em check-ins regulares (standups, retrospectivas, 1:1s)
- Quando há pressão para reportar progresso positivo apesar de problemas
- Quando riscos identificados na pré-programação começam a se materializar

## Conceitos-Chave

1. **Red Flag**: Sinal observável que indica risco de falha, atraso ou degradação de qualidade. Pode ser técnico, organizacional ou processual.
2. **Escalação**: O ato de levar a informação para quem tem poder de ação. Não é falha — é responsabilidade.
3. **Nível de Escalação**: Para quem escalar depende da gravidade: equipe, tech lead, gerente, diretor.
4. **Janela de Ação**: O tempo disponível para agir antes que o red flag se torne crise. Diminui com cada dia sem escalação.
5. **Segurança Psicológica**: O ambiente onde levantar red flags é encorajado, não punido. Sem isso, o framework falha.

## Processo / Passos

### Passo 1 — Definir Red Flags Conhecidos
Liste sinais de alerta comuns para o contexto do projeto:
- Estimativas estourando consistentemente
- Requisitos mudando sem ajuste de prazo
- Dependências atrasando sem plano B
- Equipe trabalhando overtime para "compensar"
- Bugs em módulos que deveriam estar estáveis
- Stakeholders não disponíveis para decisões
- Escopo crescendo sem discussão formal

### Passo 2 — Classificar por Gravidade
- **Amarelo**: Risco observado mas controlável. Ação da equipe é suficiente.
- **Laranja**: Risco significativo que requer atenção do tech lead ou gerente.
- **Vermelho**: Risco que ameaça o sucesso do projeto. Requer ação de liderança.

### Passo 3 — Definir Para Quem Escalar
| Gravidade | Escalar para | Prazo |
|---|---|---|
| Amarelo | Tech Lead + equipe | Próximo standup |
| Laranja | Gerente + stakeholders | Dentro de 24h |
| Vermelho | Diretor/VP + todos os stakeholders | Imediatamente |

### Passo 4 — Criar Formato de Escalação
Padronize: "RED FLAG [cor]: [descrição factual do sinal]. IMPACTO POTENCIAL: [o que pode acontecer]. AÇÃO SUGERIDA: [o que recomendamos]. URGÊNCIA: [quando precisa de resposta]."

### Passo 5 — Escalar de Fato
Envie a escalação. Não espere "mais dados" ou "mais um sprint para ver se melhora." Red flags deterioram, não melhoram sozinhos.

### Passo 6 — Acompanhar
Red flag escalado precisa de resposta e ação. Se não houve resposta, re-escale para o nível acima.

### Passo 7 — Reconhecer e Recompensar
Agradeça quem levanta red flags. Punir o mensageiro garante que futuros red flags serão escondidos.

## Perguntas de Ativação

- "Há algo que estou evitando mencionar porque sei que vai gerar desconforto?"
- "Se um consultor externo olhasse para este projeto, o que ele sinalizaria?"
- "Estamos 'na meta' porque estamos bem ou porque estamos cortando qualidade?"
- "A equipe está trabalhando overtime para compensar algo? O quê?"
- "Há um elefante na sala que ninguém está mencionando?"
- "Se eu saísse de férias por 2 semanas, o projeto continuaria progredindo?"

## Output Esperado

```
RED FLAG REPORT — [Projeto] — [Data]

🟡 AMARELO: Estimativas do módulo de integração estouraram em 40%
   Impacto: Sprint pode não ser completada conforme planejado
   Ação sugerida: Reestimar módulo restante, negociar escopo do sprint
   Escalado para: Tech Lead
   Status: Em discussão

🟠 LARANJA: API do parceiro não tem sandbox funcional (descoberto ontem)
   Impacto: Integração pode atrasar 2-3 semanas. Caminho crítico afetado.
   Ação sugerida: Contatar parceiro para SLA de sandbox OU implementar mock + integração real na última semana
   Escalado para: PM + Gerente
   Status: Aguardando resposta do PM

🔴 VERMELHO: Requisito regulatório (LGPD consent) não considerado no design
   Impacto: Feature pode precisar de redesign significativo. Risco legal se lançar sem.
   Ação sugerida: Parar implementação do módulo de cadastro, envolver jurídico, redesenhar
   Escalado para: CTO + Jurídico + Diretor de Produto
   Status: Reunião marcada para amanhã 9h
```

## Armadilhas Comuns

1. **Matar o mensageiro**: Punir quem levanta red flags garante que futuros problemas serão escondidos até virarem crise.
2. **Otimismo como padrão**: "Vai melhorar no próximo sprint" sem nenhuma ação concreta para mudar a situação.
3. **Escalação tardia**: Esperar até ter "certeza" de que é um problema. Red flags são sinais, não certezas — escale o sinal.
4. **Escalação sem ação**: Escalar e ninguém faz nada. Se o nível atual não age, escale para o próximo.
5. **Red flags normalizados**: "Sempre atrasamos, isso é normal aqui." Normalizar problemas não os resolve.
6. **Confundir escalar com reclamar**: Escalação tem formato: fato + impacto + ação sugerida. Reclamação é só frustração sem proposta.
