# Auxiliares de Detecção de Ambiguidade (Ambiguity Detection Helpers)

## Propósito
Fornecer técnicas, heurísticas e checklists para identificar e classificar ambiguidades em requisitos, documentos de arquitetura e especificações durante a fase de pré-programação, antes que se tornem defeitos no desenvolvimento.

## Fórmulas e Modelos

### Score de Ambiguidade de Requisito

```
SAR = (PA * 0.3) + (PL * 0.25) + (PI * 0.25) + (PC * 0.2)

Onde:
  PA = Presença de palavras ambíguas (0-100)
  PL = Lacunas lógicas identificadas (0-100)
  PI = Incompletude de informação (0-100)
  PC = Inconsistência com outros requisitos (0-100)

Classificação:
  SAR 0-20:   Claro (sem ação)
  SAR 21-40:  Levemente ambíguo (revisar)
  SAR 41-60:  Moderadamente ambíguo (clarificar)
  SAR 61-80:  Altamente ambíguo (reescrever)
  SAR 81-100: Criticamente ambíguo (descartar e recomeçar)
```

### Detector de Palavras Ambíguas

```
Palavras que indicam ambiguidade em requisitos:

Grupo 1 - Termos vagos (peso: 3):
  "adequado", "apropriado", "razoável", "suficiente"
  "bom", "rápido", "eficiente", "amigável"
  "intuitivo", "fácil", "simples", "normal"
  "moderno", "robusto", "escalável" (sem métrica)

Grupo 2 - Quantificadores indefinidos (peso: 2):
  "vários", "alguns", "muitos", "poucos"
  "frequentemente", "ocasionalmente", "geralmente"
  "a maioria", "grande parte", "significativo"

Grupo 3 - Condicionais incompletos (peso: 3):
  "se possível", "quando necessário", "se aplicável"
  "opcionalmente", "preferencialmente"
  "em alguns casos", "dependendo de"

Grupo 4 - Referências vagas (peso: 2):
  "etc.", "e assim por diante", "entre outros"
  "similar a", "como mencionado", "conforme necessário"

PA = (sum(ocorrencias * peso) / total_palavras) * 100
```

### Checklist de Completude de Requisito

```
Item                                        Pontos
----------------------------------------------  ------
Tem sujeito claro (quem/o quê)                   10
Tem ação específica (verbo mensurável)            10
Tem objeto definido (sobre o quê)                 10
Tem critério de aceite                            15
Tem condições de contorno (limites)               10
Tem tratamento de erro definido                   10
Tem prioridade definida                            5
Tem rastreabilidade (link com objetivo)            5
Não contém palavras ambíguas                      10
Não contém dependências implícitas                10
Usa terminologia do glossário                      5
                                            ----------
Total possível:                                  100

PI (Incompletude) = 100 - Score_Completude
```

### Matriz de Inconsistência

```
Para N requisitos, verificar cada par (Ri, Rj):

Inconsistência = {
  "contradição":    Ri afirma X, Rj afirma NOT X
  "sobreposição":   Ri e Rj definem o mesmo comportamento diferentemente
  "lacuna":         Ri pressupõe algo que Rj contradiz
  "duplicação":     Ri e Rj dizem a mesma coisa com palavras diferentes
}

PC = (Pares_Inconsistentes / Total_Pares) * 100
Total_Pares = N * (N - 1) / 2
```

### Índice de Ambiguidade do Projeto

```
IAP = (sum(SAR_i) / N) * (1 + Fator_Criticidade)

Fator_Criticidade:
  0.0 se nenhum requisito crítico é ambíguo
  0.1 por cada requisito crítico com SAR > 40
  0.2 por cada requisito crítico com SAR > 60
```

## Como Usar

1. **Coletar** todos os requisitos e especificações do projeto
2. **Executar scanner** de palavras ambíguas em cada documento
3. **Aplicar checklist** de completude em cada requisito
4. **Verificar inconsistências** entre pares de requisitos
5. **Calcular SAR** para cada requisito e IAP para o projeto
6. **Priorizar resolução** por criticidade do requisito e score de ambiguidade
7. **Iterar** até IAP atingir limiar aceitável (< 25)

## Inputs e Outputs

### Inputs
- Lista de requisitos com texto completo
- Glossário de termos do projeto
- Classificação de criticidade por requisito
- Histórico de ambiguidades resolvidas (para calibração)

### Outputs
- Score de Ambiguidade por requisito (SAR)
- Índice de Ambiguidade do Projeto (IAP)
- Lista de palavras ambíguas encontradas com localização
- Lista de lacunas e inconsistências detectadas
- Sugestões de reformulação para requisitos ambíguos
- Burndown de ambiguidades ao longo do tempo

## Exemplos

### Exemplo: Análise de Requisito Ambíguo
```
ANTES (ambíguo):
  "O sistema deve responder rapidamente às consultas do usuário
   e exibir resultados de forma adequada."

Análise:
  Palavras ambíguas: "rapidamente" (G1), "adequada" (G1)
  Lacunas: Sem critério de aceite, sem limites definidos
  PA = 40, PI = 60, PL = 50, PC = 0
  SAR = (40*0.3) + (50*0.25) + (60*0.25) + (0*0.2) = 39.5

DEPOIS (claro):
  "O endpoint GET /api/busca deve retornar resultados em menos de
   200ms (p95) para consultas de até 100 caracteres, exibindo no
   máximo 20 resultados por página no formato JSON com campos:
   id, titulo, descricao, relevancia. Em caso de timeout (> 5s),
   retornar HTTP 504 com mensagem de erro padronizada."

Análise:
  PA = 0, PI = 5, PL = 0, PC = 0
  SAR = 1.25 (Claro)
```

### Exemplo: Burndown de Ambiguidades
```
Semana 1: IAP = 62 (45 requisitos, 28 ambíguos)
  Ações: Workshop de clarificação com PO

Semana 2: IAP = 41 (45 requisitos, 18 ambíguos)
  Ações: Revisão por pares, atualização de glossário

Semana 3: IAP = 23 (45 requisitos, 8 ambíguos)
  Ações: Sessão de detalhamento dos 8 restantes

Semana 4: IAP = 12 (45 requisitos, 3 ambíguos)
  Status: Dentro do limiar (< 25). 3 restantes aceitos como risco.
```
