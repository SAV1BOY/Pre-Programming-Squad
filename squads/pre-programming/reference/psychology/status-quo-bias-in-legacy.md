# Vies de Status Quo em Legado

## Vies/Efeito

**Vies de Status Quo (Status Quo Bias):** A preferencia desproporcional por manter o estado atual das coisas, mesmo quando alternativas seriam objetivamente melhores. Combinacao de aversao a perda, custo afundado e medo do desconhecido.

## Descricao

Samuelson e Zeckhauser (1988) demonstraram que pessoas tem forte tendencia a manter a opcao default, mesmo quando mudar e vantajoso. Em software, isso se manifesta como resistencia a mudancas em sistemas legados, processos estabelecidos e tecnologias familiares — nao porque sao melhores, mas porque sao conhecidas.

## Como se Manifesta em Pre-Programacao

### Na Avaliacao de Sistemas Legados
- **"O sistema funciona, por que mudar?"** Ignorar custo de manutencao crescente, risco de seguranca, perda de velocidade de desenvolvimento.
- **"Ninguem entende esse sistema, nao podemos mexer."** Usar a falta de conhecimento como razao para nao mudar, quando e exatamente a razao para mudar.
- **"E arriscado demais migrar."** Superestimar o risco de mudar e subestimar o risco de nao mudar.

### Na Escolha de Tecnologias
- **"Sempre usamos Java, vamos continuar com Java."** Sem avaliar se Java e a melhor opcao para o problema atual.
- **"Temos expertise em X, nao vale a pena aprender Y."** O custo de aprender Y pode ser menor que o custo de usar X onde nao e adequado.
- **"Mudamos a stack, e se der errado?"** Pensar assimetricamente: o custo de mudar e salientado, o custo de nao mudar e invisivel.

### Na Definicao de Processos
- **"Sempre fizemos deploy assim."** Processos manuais persistem por inércia, mesmo quando automacao e claramente superior.
- **"O processo de review funciona."** Processos que funcionam "mais ou menos" persistem porque o custo de melhorar parece maior que o custo de tolerar ineficiencia.

## Como Mitigar

### 1. Quantificar o Custo do Status Quo
Tornar visivel o custo de nao mudar: "Quanto gastamos em manutencao do sistema legado por mes? Quantos incidentes causou? Quanto tempo de desenvolvimento perdemos?"

### 2. Analise Assimetrica Explicita
Forcar avaliacao simetrica: listar custos e riscos de mudar E custos e riscos de nao mudar. O status quo nao e gratuito.

| | Mudar | Nao Mudar |
|---|---|---|
| Custos | [esforco de migracao] | [custo de manutencao crescente] |
| Riscos | [falha na migracao] | [incidentes, vulnerabilidades] |
| Beneficios | [velocidade, seguranca] | [previsibilidade] |

### 3. Sunset Policy
Definir politica de obsolescencia: "Toda tecnologia sera reavaliada a cada 2 anos. Se nao seria escolhida novamente, planejar transicao."

### 4. Innovation Time / Spikes
Alocar tempo para experimentar alternativas. Sem experiencia pratica com o novo, o vies de status quo domina.

### 5. Reverse Burden of Proof
Inverter o onus da prova: em vez de exigir justificativa para mudar, exigir justificativa para manter. "Por que devemos continuar usando X?" em vez de "Por que devemos mudar de X?"

## Exemplo Real

**Contexto:** Sistema de faturamento em COBOL roda ha 20 anos em mainframe. Funciona, mas: 2 desenvolvedores COBOL restantes se aposentam em 18 meses, custo de mainframe e $50k/mes, novas features levam 6 meses para implementar, e nao integra com APIs modernas.

**Manifestacao do status quo:**
- "O sistema nunca falhou em 20 anos." (Verdade, mas o risco e futuro, nao passado.)
- "Migracao e arriscada, podemos perder dados." (Risco real, mas mitigavel.)
- "Custa muito migrar." (Sim, mas custa mais nao migrar: $600k/ano de mainframe + impossibilidade de novas features.)
- "Vamos manter e contratar mais um desenvolvedor COBOL." (O mercado de COBOL esta secando.)

**O que deveria ter acontecido na pre-programacao:**
- Quantificar custo do status quo: $600k/ano mainframe, $0 em novas features, risco critico de key-person dependency.
- Quantificar custo da migracao: estimativa de 12 meses, $400k, risco controlado com Strangler Fig Pattern.
- Analise assimetrica: migrar custa $400k uma vez; manter custa $600k/ano indefinidamente + risco crescente.
- Decisao baseada em dados, nao em conforto com o familiar.
