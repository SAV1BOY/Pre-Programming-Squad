# Riscos de Sistemas Agenticos - Primer

## O que sao Sistemas Agenticos

Sistemas agenticos sao sistemas de IA que operam com autonomia: recebem um objetivo, planejam acoes, executam ferramentas, observam resultados e iteram ate alcançar o objetivo. Diferente de chamadas simples a LLMs (pergunta-resposta), agentes tomam multiplas decisoes encadeadas, usam ferramentas (APIs, bancos de dados, code execution) e podem modificar o estado do mundo.

## Por que Sistemas Agenticos tem Riscos Amplificados

### 1. Autonomia Multiplicada
Cada decisao autonoma do agente e um ponto onde pode dar errado. Um agente que faz 10 chamadas de API em sequencia tem 10 oportunidades de erro, e erros em passos anteriores propagam para passos posteriores.

### 2. Acesso a Ferramentas (Tool Use)
Agentes interagem com o mundo real: enviam emails, modificam bancos de dados, criam recursos em cloud, fazem transacoes financeiras. Um erro nao e apenas uma resposta errada — pode ser uma acao irreversivel.

### 3. Loops de Feedback
Agentes que observam os resultados de suas acoes e ajustam comportamento podem entrar em loops: tentar repetidamente uma acao que falha, consumir recursos indefinidamente, ou escalar privilegios para alcançar um objetivo.

### 4. Composicao de Incerteza
Em um pipeline multi-step, a incerteza se compoe. Se cada passo tem 95% de acuracia, 10 passos tem ~60% de acuracia total (0.95^10 = 0.60).

## Taxonomia de Riscos

### Riscos de Planejamento
| Risco | Descricao | Exemplo |
|---|---|---|
| Goal misalignment | Agente interpreta objetivo diferente do pretendido | "Otimizar vendas" → agente cria descontos absurdos |
| Overplanning | Agente planeja acoes desnecessarias | Agente consulta 50 APIs quando 3 bastam |
| Underplanning | Agente pula etapas criticas | Agente faz deploy sem rodar testes |
| Infinite planning | Agente fica em loop de planejamento sem executar | Agente replaneja infinitamente buscando plano perfeito |

### Riscos de Execucao de Ferramentas
| Risco | Descricao | Exemplo |
|---|---|---|
| Wrong tool selection | Agente escolhe ferramenta errada | Usar DELETE quando deveria usar GET |
| Incorrect parameters | Agente passa parametros errados | Transferir R$10.000 em vez de R$100 |
| Side effects | Acao tem consequencias nao previstas | Deletar dados de producao |
| Resource exhaustion | Agente consome recursos excessivos | Loop de chamadas a API paga |
| Privilege escalation | Agente usa permissoes alem do necessario | Acessar dados de outros usuarios |

### Riscos de Observacao/Feedback
| Risco | Descricao | Exemplo |
|---|---|---|
| Misinterpretation | Agente interpreta resultado incorretamente | Erro HTTP 429 interpretado como sucesso |
| Retry storms | Agente retenta obsessivamente | 1000 retries em API indisponivel |
| Confirmation bias | Agente ignora evidencia contraria ao plano | Ignorar erros e declarar sucesso |

### Riscos de Seguranca
| Risco | Descricao | Exemplo |
|---|---|---|
| Prompt injection via tool output | Dados retornados por ferramenta manipulam o agente | Website malicioso injeta instrucoes via conteudo |
| Data exfiltration | Agente vaza dados via ferramentas | Enviar dados internos por email |
| Indirect prompt injection | Atacante planta instrucoes em dados que o agente vai processar | Documento com instrucoes ocultas |

## Mitigacoes na Pre-Programacao

### 1. Principio de Menor Privilegio (Least Privilege)
O agente deve ter acesso apenas as ferramentas e dados estritamente necessarios para sua funcao.

```markdown
## Definicao de Ferramentas do Agente

### Permitidas
- Buscar pedidos por ID do usuario autenticado.
- Consultar status de entrega.
- Criar ticket de suporte.

### Proibidas
- Acessar pedidos de outros usuarios.
- Modificar dados de pedido diretamente.
- Executar SQL arbitrario.
- Enviar emails para enderecos nao-cadastrados.
```

### 2. Limites de Execucao (Execution Boundaries)
Definir limites rigidos para prevenir runaway agents.

```markdown
## Limites de Execucao

- Max steps por execucao: 20
- Max tool calls por execucao: 15
- Max tokens consumidos: 100k
- Max tempo de execucao: 120 segundos
- Max custo por execucao: $1.00
- Max retries por tool call: 3
```

### 3. Human-in-the-Loop para Acoes Criticas
Definir quais acoes requerem aprovacao humana antes de execucao.

```markdown
## Classificacao de Acoes

### Auto-aprovadas (sem intervencao humana)
- Consultar dados (read-only).
- Gerar relatorios.
- Responder perguntas informativas.

### Requerem confirmacao do usuario
- Modificar dados pessoais.
- Cancelar pedidos.
- Agendar servicos.

### Requerem aprovacao de operador
- Emitir reembolsos > R$500.
- Alterar permissoes de acesso.
- Executar acoes que afetam multiplos usuarios.
```

### 4. Sandboxing de Ferramentas
Ferramentas devem ser executadas em ambiente isolado com permissoes restritas.

### 5. Validacao de Output de Ferramentas
Antes de usar o resultado de uma ferramenta, validar formato, tipo e razoabilidade.

### 6. Circuit Breakers para Agentes
Se o agente excede limites de custo, tempo ou tentativas, parar e escalar para humano.

## Design Doc para Sistemas Agenticos: Secoes Adicionais

```markdown
## Secao: Analise de Riscos Agenticos

### Ferramentas Disponiveis
[Lista de cada ferramenta, suas permissoes, e o dano potencial de uso incorreto.]

### Cenarios de Falha
[Para cada ferramenta, o que acontece se o agente usa incorretamente.]

### Limites de Execucao
[Max steps, max cost, max time, max retries.]

### Classificacao de Acoes
[Auto-aprovadas, requerem confirmacao, requerem aprovacao.]

### Estrategia de Rollback
[Como desfazer acoes do agente que foram executadas incorretamente.]

### Monitoramento
[Metricas de sucesso, taxa de escalonamento, custo medio por execucao,
 taxa de loop detection.]
```

## Criterios de Readiness para Sistemas Agenticos

- "Ferramentas do agente estao definidas com principio de menor privilegio?"
- "Limites de execucao estao definidos e implementados?"
- "Acoes criticas tem human-in-the-loop?"
- "Cenarios de prompt injection via tool output foram avaliados?"
- "Estrategia de rollback existe para acoes com side effects?"
- "Monitoramento de custo e execucao esta planejado?"
- "Circuit breakers estao definidos para runaway scenarios?"
- "Eval dataset inclui cenarios adversariais para o agente?"
