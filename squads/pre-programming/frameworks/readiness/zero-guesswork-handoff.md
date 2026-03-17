# Zero-Guesswork Handoff

## Título e Propósito

O **Zero-Guesswork Handoff** é um framework para criar pacotes de entrega entre fases (pré-programação → implementação) tão completos que o implementador não precise adivinhar nada. O propósito é eliminar o "gap de adivinhação" — aquele momento onde o dev para, pensa "o que eles queriam dizer com isso?" e toma uma decisão que pode estar errada.

## Quando Usar

- Na transição de pré-programação para implementação (uso primário)
- Quando devs frequentemente interrompem POs ou designers com perguntas durante implementação
- Quando entregas são rejeitadas por "não era isso que eu queria"
- Em equipes distribuídas onde comunicação assíncrona exige documentação mais precisa
- Quando há rotatividade na equipe e o contexto precisa ser transmissível

## Conceitos-Chave

1. **Guesswork**: Qualquer decisão que o implementador precisa tomar porque a especificação é ambígua, incompleta ou ausente.
2. **Completude Explícita**: Toda decisão relevante está documentada. Não há "todo mundo sabe" ou "é óbvio".
3. **Zero não é Literal**: O objetivo é minimizar, não eliminar 100% (impossível). O alvo é que nenhuma adivinhação produza risco de retrabalho.
4. **Decisão Documentada vs. Decisão Delegada**: Decisões importantes estão documentadas. Decisões de implementação são explicitamente delegadas ao dev.
5. **Pacote de Handoff**: O conjunto completo de artefatos entregues ao implementador.

## Processo / Passos

### Passo 1 — Compilar o Pacote de Handoff
Reúna todos os artefatos produzidos na pré-programação:
- Requisitos com critérios de aceite
- Design/arquitetura com decisões e justificativas
- Edge cases mapeados com decisões para cada um
- Plano de testes (testes antes das tarefas)
- Lista de dependências com status
- Riscos e mitigações
- Perguntas respondidas e perguntas abertas

### Passo 2 — Revisar Cada Seção com "Olhos de Dev"
Para cada seção, pergunte: "Se eu fosse implementar isso agora, o que me faria parar e perguntar?" Identifique gaps.

### Passo 3 — Preencher Gaps
Para cada gap identificado, forneça a resposta ou marque explicitamente como "decisão delegada ao implementador".

### Passo 4 — Marcar Decisões Delegadas
Liste explicitamente o que o dev pode decidir: "Escolha de biblioteca de validação: a critério do dev. Estrutura interna do módulo: a critério do dev."

### Passo 5 — Incluir Exemplos Concretos
Para comportamentos ambíguos, inclua exemplos: "Input: X → Output esperado: Y." Exemplos eliminam ambiguidade melhor que prosa.

### Passo 6 — Sessão de Walkthrough
Apresente o pacote ao implementador em sessão síncrona. Colete perguntas e preencha gaps em tempo real.

### Passo 7 — Definir Canal para Dúvidas Residuais
Estabeleça como o dev escala dúvidas que surgem durante implementação. Não deveria precisar, mas na prática precisa.

## Perguntas de Ativação

- "Se eu entregasse isso para um dev que não participou de nenhuma reunião, ele conseguiria implementar?"
- "Há comportamento esperado que 'todo mundo sabe' mas não está escrito em lugar nenhum?"
- "Para cada edge case, o dev sabe o que fazer sem perguntar?"
- "Os critérios de aceite são testáveis ou precisam de interpretação?"
- "O que estou delegando ao dev e o que estou decidindo por ele?"
- "Incluí exemplos concretos de input → output para os casos mais complexos?"

## Output Esperado

```
PACOTE DE HANDOFF — [Feature]
Preparado por: [nome] | Data: [data]

1. REQUISITOS E CRITÉRIOS DE ACEITE
   [link para documento detalhado]
   Status: Completo e validado com PO

2. DECISÕES DE DESIGN
   - Arquitetura: [resumo + link para ADR]
   - Modelo de dados: [link para diagrama]
   - Integrações: [contratos definidos]

3. EDGE CASES E DECISÕES
   | Cenário | Decisão | Justificativa |
   |---|---|---|
   | Usuário com email inválido já cadastrado no legado | Aceitar e marcar para limpeza | PO decidiu — migração gradual |
   | Timeout na API de endereço | Permitir input manual | Fallback para não bloquear cadastro |

4. EXEMPLOS CONCRETOS
   - Input: CPF "123.456.789-09" → Output: Válido, salvar como "12345678909"
   - Input: CPF "000.000.000-00" → Output: Inválido, erro "CPF inválido"

5. DECISÕES DELEGADAS AO IMPLEMENTADOR
   - Estrutura interna de pastas e módulos
   - Escolha de biblioteca de validação de CPF
   - Naming conventions (seguir padrão do projeto)

6. PLANO DE TESTES [link]

7. RISCOS E MITIGAÇÕES [link]

8. PERGUNTAS ABERTAS
   - [NENHUMA — todas respondidas]

9. CANAL PARA DÚVIDAS: #squad-channel ou DM para [nome]
```

## Armadilhas Comuns

1. **"É auto-explicativo"**: Nada é auto-explicativo quando o contexto está na sua cabeça e não no documento.
2. **Prosa demais, exemplos de menos**: Parágrafos longos explicando comportamento que um exemplo de input/output esclareceria melhor.
3. **Decisões implícitas**: "Ninguém mencionou timezone então assumo que é UTC" — se ninguém mencionou, não é decisão, é omissão.
4. **Pacote incompleto**: Requisitos completos mas sem edge cases, ou edge cases sem decisões.
5. **Sem walkthrough**: Enviar o pacote por email e achar que foi comunicado. Sessão síncrona captura dúvidas que leitura não revela.
6. **Excesso de especificação**: Especificar implementação interna em vez de comportamento. O dev precisa saber o quê, não o como.
