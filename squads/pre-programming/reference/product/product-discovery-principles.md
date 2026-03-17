# Principios de Product Discovery

## O que e Product Discovery

Product discovery e o processo de decidir o que construir. Envolve identificar problemas reais de usuarios, gerar hipoteses de solucao, validar essas hipoteses com o menor investimento possivel e reduzir riscos antes de comprometer recursos de engenharia. A pre-programacao e a etapa final de discovery antes do inicio da construcao.

## Os Quatro Riscos do Produto (Marty Cagan)

### 1. Risco de Valor
**Pergunta:** Os usuarios realmente querem isso?
**Tecnicas de validacao:** Entrevistas de usuario, testes de proposta de valor, fake door tests, landing page tests, surveys.
**Relevancia para pre-programacao:** Se o risco de valor nao foi mitigado, nao deveriamos iniciar o design tecnico.

### 2. Risco de Usabilidade
**Pergunta:** Os usuarios conseguem usar?
**Tecnicas de validacao:** Prototipos de alta fidelidade, testes de usabilidade, wizard of oz.
**Relevancia para pre-programacao:** Requisitos de UX influenciam decisoes tecnicas (latencia, responsividade, offline support).

### 3. Risco de Viabilidade (Feasibility)
**Pergunta:** Conseguimos construir com a tecnologia, equipe e prazo disponiveis?
**Tecnicas de validacao:** Spikes tecnicos, prototipos de viabilidade, consulta com especialistas.
**Relevancia para pre-programacao:** Este e o risco que o squad de pre-programacao mais diretamente aborda.

### 4. Risco de Negocio (Business Viability)
**Pergunta:** Funciona para o negocio? E regulatoriamente possivel? E financeiramente viavel?
**Tecnicas de validacao:** Analise de business case, consulta juridica/compliance, analise financeira.
**Relevancia para pre-programacao:** Restricoes regulatorias e de compliance afetam design tecnico diretamente.

## Principios Fundamentais

### 1. Comece pelo Problema, nao pela Solucao
Nunca comece o design tecnico sem entender claramente o problema que esta resolvendo. Questione: "Por que estamos fazendo isso?" ate chegar ao problema raiz.

### 2. Valide antes de Construir
O custo de validar uma hipotese com um prototipo e ordens de magnitude menor do que construir a solucao errada. Na pre-programacao, spikes tecnicos cumprem essa funcao.

### 3. Busque Evidencias, nao Opinioes
Decisoes devem ser baseadas em dados, nao em opinioes do HiPPO (Highest Paid Person's Opinion). Na pre-programacao, isso significa benchmarks, provas de conceito e metricas, nao achismo.

### 4. Abrace a Incerteza
Nem tudo pode ser previsto. O objetivo nao e eliminar toda incerteza, mas reduzi-la a niveis aceitaveis e projetar o sistema para tolerar o desconhecido.

### 5. Entregue Valor Incrementalmente
Prefira entregar 20% da solucao que resolve 80% do problema a 100% da solucao depois de 6 meses. Na pre-programacao, projetar para MVP tecnico.

### 6. Meça Resultados, nao Output
O sucesso e medido por mudanca nas metricas de negocio, nao por linhas de codigo escritas ou stories entregues. Na pre-programacao, definir as metricas que importam.

## Tecnicas de Discovery Relevantes para Pre-Programacao

### 1. Opportunity Solution Tree (Teresa Torres)
Conectar outcomes desejados a oportunidades a solucoes a experimentos. Visualiza como cada solucao proposta se conecta ao objetivo de negocio.

**Na pre-programacao:** Usar para validar que o design tecnico esta conectado ao outcome de negocio.

### 2. Assumption Mapping
Listar todas as suposicoes do projeto, classificar por risco (probabilidade de estar errado x impacto), e testar as mais arriscadas primeiro.

**Na pre-programacao:**
```markdown
## Suposicoes de Alto Risco

| Suposicao | Risco | Como Validar | Status |
|---|---|---|---|
| PostgreSQL suporta 10k writes/segundo | Alto | Benchmark com dados reais | Validado |
| API do parceiro suporta nosso volume | Alto | Contato com equipe do parceiro | Pendente |
| Usuarios aceitam latencia de 2s na busca | Medio | Teste A/B | Pendente |
| Equipe consegue implementar em 8 semanas | Medio | Decomposicao detalhada | Em validacao |
```

### 3. Spike Tecnico (Prova de Conceito)
Experimento tecnico time-boxed para validar viabilidade de uma abordagem.

**Boas praticas:**
- Time-box rigoroso (1-3 dias).
- Definir criterio de sucesso/falha antes de comecar.
- Documentar resultado independente do outcome.
- Spike nao e produção — jogue fora e reimplemente direito.

### 4. Design Sprint (Jake Knapp)
Processo de 5 dias para ir do problema ao prototipo testado com usuarios.
- Dia 1: Mapear o problema.
- Dia 2: Esbocar solucoes.
- Dia 3: Decidir.
- Dia 4: Prototipar.
- Dia 5: Testar com usuarios.

### 5. Continuous Discovery Habits (Teresa Torres)
Entrevistas semanais com usuarios, oportunity solution trees atualizadas, experimentos constantes. Discovery nao e uma fase — e um habito continuo.

## Interacao entre Discovery e Pre-Programacao

### O que Discovery Deve Entregar para Pre-Programacao
- Problema claramente articulado com evidencias.
- Riscos de valor e usabilidade mitigados (ou aceitos conscientemente).
- Metricas de sucesso definidas.
- Restricoes de negocio e compliance documentadas.
- Personas e cenarios de uso validados.

### O que Pre-Programacao Deve Entregar de Volta para Discovery
- Avaliacao de viabilidade tecnica.
- Estimativa de esforco e timeline.
- Trade-offs tecnicos que impactam decisoes de produto.
- Alternativas tecnicas que ampliam o espaco de solucoes.
- Riscos tecnicos identificados com mitigacoes propostas.

### Criterios de Readiness para Transicao Discovery -> Pre-Programacao
- [ ] Problema definido com evidencias (dados, pesquisa, feedback).
- [ ] Risco de valor mitigado (usuarios querem isso).
- [ ] Metricas de sucesso definidas e mensuráveis.
- [ ] Stakeholders alinhados no escopo.
- [ ] Restricoes conhecidas documentadas.
- [ ] MVP de produto definido.

### Criterios de Readiness para Transicao Pre-Programacao -> Implementacao
- [ ] Design doc revisado e aprovado.
- [ ] Viabilidade tecnica validada (spikes concluidos).
- [ ] Estrategia de testes definida.
- [ ] Contratos de API e eventos definidos.
- [ ] Estimativas refinadas e aceitas pela equipe.
- [ ] Plano de entrega incremental definido.
