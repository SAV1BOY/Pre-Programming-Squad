# Accelerate

## Informações Gerais

- **Titulo:** Accelerate: The Science of Lean Software and DevOps
- **Autores:** Nicole Forsgren, Jez Humble, Gene Kim
- **Ano:** 2018

## Tese Central

Com base em quatro anos de pesquisa rigorosa do programa DORA (DevOps Research and Assessment), o livro demonstra que alta performance em entrega de software impulsiona diretamente resultados organizacionais. As quatro metricas-chave (DORA metrics) — lead time de mudancas, frequencia de deploy, taxa de falha em mudancas e tempo de recuperacao — sao preditores confiaveis de performance tanto tecnica quanto de negocio.

## Conceitos-Chave para Pre-Programacao

### 1. As Quatro Metricas DORA
- **Lead Time de Mudancas:** Tempo do commit ao deploy em producao.
- **Frequencia de Deploy:** Quantas vezes a equipe faz deploy em producao.
- **Taxa de Falha em Mudancas (Change Failure Rate):** Percentual de mudancas que causam falha em producao.
- **Tempo de Recuperacao (MTTR):** Tempo para restaurar o servico apos uma falha.

Na pre-programacao, o design deve viabilizar deploys frequentes, mudancas pequenas e recuperacao rapida.

### 2. Capacidades Tecnicas que Impulsionam Performance
- Integracao continua e entrega continua.
- Arquitetura fracamente acoplada (loosely coupled).
- Trunk-based development.
- Testes automatizados.
- Monitoramento e observabilidade.

O squad de pre-programacao deve garantir que decisoes de design nao comprometam essas capacidades.

### 3. Arquitetura Fracamente Acoplada
Equipes de alta performance podem fazer mudancas em seus servicos sem coordenacao com outras equipes. Isso requer limites de servico bem definidos, contratos claros e baixo acoplamento. A pre-programacao e o momento de garantir esses limites.

### 4. Cultura Generativa (Modelo Westrum)
Organizacoes com cultura generativa (alta cooperacao, mensageiros bem-vindos, falhas levam a investigacao) superam organizacoes burocraticas ou patologicas. A pre-programacao deve fomentar um ambiente onde levantar riscos e questionamentos e valorizado.

### 5. Trabalho em Pequenos Lotes
Mudancas menores sao mais seguras, mais rapidas de revisar e mais faceis de reverter. Na pre-programacao, o design deve permitir entrega incremental, nao big-bang.

### 6. Lean Product Management
Trabalhar em pequenos lotes, tornar o fluxo de trabalho visivel, coletar feedback do cliente, experimentar ativamente. A pre-programacao deve considerar como viabilizar experimentacao rapida.

## Como Aplicar no Squad

### Na Avaliacao de Arquitetura
- Verificar se o design proposto permite deploys independentes por equipe.
- Avaliar o grau de acoplamento entre componentes e servicos.
- Confirmar que o design suporta trunk-based development com feature flags.
- Validar que a estrategia de rollback esta definida.

### Na Definicao de Metricas
- Estabelecer targets para as quatro metricas DORA como parte dos criterios de readiness.
- Incluir nos design docs como o design proposto afeta cada metrica.
- Monitorar a correlacao entre decisoes de pre-programacao e performance de entrega.

### Na Cultura do Squad
- Praticar cultura generativa: todo questionamento e bem-vindo durante design reviews.
- Tratar a identificacao de riscos como contribuicao positiva, nao como obstrucao.
- Usar retrospectivas para correlacionar decisoes de pre-programacao com resultados em producao.

### No Planejamento de Entrega
- Exigir que design docs demonstrem como o trabalho pode ser entregue em incrementos pequenos.
- Rejeitar designs que requerem entregas monoliticas (big-bang releases).
- Definir MVP tecnico como parte do design.

## Citacoes Importantes

> "Our research has found that the factors that predict high performance are the same for all types of organizations."

> "Architecture is the biggest predictor of whether teams can deploy independently — and independently deployable teams are the biggest predictor of continuous delivery performance."

> "High performers have shorter lead times, deploy more frequently, have lower change failure rates, and recover from incidents faster."

> "Lean management and continuous delivery practices create the conditions for delivering value faster, more reliably, and more efficiently."

> "Improvements in software delivery performance lead to improvements in organizational performance."

## Relacao com Outros Livros de Referencia

- **Continuous Delivery (Humble/Farley):** Accelerate fornece a evidencia empirica para as praticas propostas em Continuous Delivery.
- **The DevOps Handbook:** Ambos compartilham autores e se complementam — DevOps Handbook e prescritivo, Accelerate e descritivo/evidencial.
- **Team Topologies:** Expande a dimensao organizacional que Accelerate identifica como critica.
