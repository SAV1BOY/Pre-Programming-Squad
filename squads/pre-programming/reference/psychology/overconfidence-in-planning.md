# Overconfidence em Planejamento

## Vies/Efeito

**Overconfidence Bias (Vies de Excesso de Confianca):** A tendencia sistematica de superestimar nossa capacidade de prever resultados, subestimar riscos e acreditar que nosso julgamento e mais preciso do que realmente e.

## Descricao

Estudos de Fischhoff, Slovic e Lichtenstein (1977) demonstram que quando pessoas dizem ter "90% de certeza" sobre algo, estao corretas apenas 70-80% das vezes. No contexto de software, o overconfidence se manifesta em estimativas imprecisas, avaliacao de risco deficiente e decisoes tomadas sem dados suficientes.

## Como se Manifesta em Pre-Programacao

### Na Avaliacao de Complexidade
- **"Isso e simples, so precisa fazer X."** Subestimar a complexidade de edge cases, integracao, testes, deploy.
- **"Ja fiz algo parecido antes."** Ignorar diferencas criticas de contexto entre projetos.
- **"A documentacao da API e boa, a integracao deve ser rapida."** Documentacao raramente cobre todos os edge cases.

### Na Avaliacao de Risco
- **"A chance de isso dar errado e minima."** Sem dados para quantificar "minima."
- **"Nossa equipe e boa, vamos conseguir."** Competencia nao elimina complexidade inerente.
- **"O pior caso e [cenario moderado]."** O pior caso real e quase sempre pior do que imaginamos.

### Na Confianca em Tecnologias
- **"Essa tecnologia resolve nosso problema."** Baseado em blog posts e marketing, nao em avaliacao tecnica profunda.
- **"O managed service cuida disso."** Managed services tem limites, bugs e comportamentos inesperados.

### Na Comunicacao de Progresso
- **"Estamos 90% prontos."** Os ultimos 10% frequentemente levam mais tempo que os primeiros 90%.
- **"A parte dificil ja foi."** Muitas vezes, a integracao final e mais dificil que cada componente individualmente.

## Como Mitigar

### 1. Calibracao de Confianca
Treinar a equipe a calibrar niveis de confianca. Exercicio: para cada estimativa, pedir o intervalo de 90% de confianca. Historicamente, intervalos de "90% de confianca" contem o valor real apenas 50-60% das vezes.

### 2. Previsao por Classes de Referencia
Em vez de estimar baseado em intuicao, buscar dados historicos de projetos similares. Quanto tempo levaram projetos com escopo e complexidade comparaveis?

### 3. Red Team / Pre-Mortem
Ter uma pessoa ou grupo cuja funcao e encontrar falhas no plano. Nao como obstrucao, mas como servico de calibracao de confianca.

### 4. Margens de Seguranca Explicitas
Adicionar margem de seguranca proporcional a incerteza: pouca incerteza (+20%), incerteza moderada (+50%), alta incerteza (+100% ou spike antes de estimar).

### 5. Demonstrar com Dados
Manter registro historico de estimativas vs. realizacoes. Mostrar a discrepancia real forca humildade baseada em evidencias.

### 6. Linguagem de Incerteza
Substituir "vai funcionar" por "acreditamos que funciona, mas nao validamos X, Y, Z." Tornar incerteza explicita.

## Exemplo Real

**Contexto:** Tech lead estima integracao com gateway de pagamentos em 3 sprints. "Ja integrei com gateways antes, sei como funciona."

**Manifestacao do overconfidence:**
- Experiencia anterior era com gateway diferente, API completamente distinta.
- Documentacao do novo gateway omite comportamento em cenarios de timeout.
- Ambiente de sandbox do gateway tem bugs nao presentes em producao (e vice-versa).
- Requisitos de PCI-DSS nao foram contabilizados na estimativa.
- Reconciliacao financeira nao foi considerada no escopo.

**Resultado:** Integracao leva 7 sprints. 3 sprints para a integracao basica (como estimado), 2 sprints para edge cases de timeout e retry, 1 sprint para PCI-DSS compliance, 1 sprint para reconciliacao.

**O que deveria ter acontecido:**
- Spike de 3 dias para explorar a API real (nao so documentacao).
- Checklist de concerns de integracao com pagamentos (PCI-DSS, reconciliacao, disputas, reembolsos).
- Estimativa em tres pontos: 3 sprints (otimista), 5 sprints (provavel), 8 sprints (pessimista).
- Comunicar a incerteza: "Estimamos 5 sprints com margem de +/- 3 sprints ate validarmos o spike."
