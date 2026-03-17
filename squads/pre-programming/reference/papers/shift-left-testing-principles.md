# Principios de Shift-Left Testing

## Titulo

Shift-Left Testing: Principles, Practices, and Impact on Software Quality

## Resumo

Shift-left testing e a pratica de mover atividades de verificacao e validacao para o inicio do ciclo de desenvolvimento, em vez de concentra-las no final. Originado do trabalho de Larry Smith (2001) e expandido por pesquisas do Google, Microsoft e Thoughtworks, o conceito demonstra que testes realizados mais cedo sao mais baratos, mais rapidos e mais eficazes. A pre-programacao representa o shift-left maximo: verificar antes de escrever qualquer codigo.

## Insight Principal

Shift-left nao e apenas "testar mais cedo" — e repensar fundamentalmente o que significa verificacao. Na fase de pre-programacao, as "verificacoes" sao design reviews, especificacoes executaveis, spikes tecnicos e analise de riscos. Essas atividades previnem defeitos em vez de detecta-los, tornando-as ordens de magnitude mais eficientes que testes tradicionais.

## Niveis de Shift-Left

### Nivel 1: Testes Unitarios Automatizados (TDD)
Escrever testes antes do codigo. Verifica comportamento de componentes isolados. Feedback em segundos. Custo de correcao minimo.

### Nivel 2: Testes de Integracao Automatizados
Verificar interacoes entre componentes cedo no pipeline. Contract testing para validar interfaces. Feedback em minutos.

### Nivel 3: Especificacoes Executaveis (BDD/SbE)
Definir comportamento esperado em formato executavel antes da implementacao. Validar entendimento com stakeholders. Feedback sobre requisitos.

### Nivel 4: Design Reviews e Analise Estatica
Revisar design antes da implementacao. Analise estatica de modelos, contratos e interfaces. Detectar defeitos estruturais sem executar codigo.

### Nivel 5: Pre-Programacao (Shift-Left Maximo)
Validar requisitos, design, viabilidade e riscos antes de qualquer implementacao. Prevenir defeitos na fonte. O custo mais baixo possivel.

## Praticas de Shift-Left na Pre-Programacao

### 1. Design Review como Teste
A revisao de um design doc e, efetivamente, um teste do design. Verificamos se o design atende requisitos, se e viavel, se lida com falhas, se e testavel.

### 2. Contract-First Design
Definir contratos de API antes da implementacao. Validar contratos com consumers antes de implementar providers. Detectar incompatibilidades antes de escrever codigo.

### 3. Threat Modeling
Analise sistematica de ameacas de seguranca no design. Identificar vulnerabilidades antes da implementacao.

### 4. Failure Mode Analysis
Mapear modos de falha de cada componente e integracao. Definir mitigacoes antes de implementar.

### 5. Prototype/Spike Validation
Construir provas de conceito para validar viabilidade tecnica de decisoes de alto risco. Falhar rapido e barato.

### 6. Specification Workshops
Sessoes colaborativas (Three Amigos) para derivar exemplos concretos de requisitos. Detectar ambiguidade e incompletude antes da implementacao.

## Metricas de Eficacia do Shift-Left

| Metrica | Descricao | Como Medir |
|---|---|---|
| Defect Detection Rate por Fase | % de defeitos encontrados em cada fase | Rastrear origem e deteccao de cada defeito |
| Cost of Quality | Custo total de prevencao + deteccao + correcao | Somar horas por categoria |
| Escaped Defect Rate | % de defeitos que chegam a producao | Defeitos producao / defeitos totais |
| Pre-programming Effectiveness | Defeitos prevenidos na pre-programacao | Comparar projetos com e sem pre-programacao |

## Aplicacao ao Squad

### Como Framework de Atividades
- Organizar as atividades de pre-programacao como niveis de shift-left.
- Priorizar atividades pelo custo-beneficio: design reviews, contract validation, specification workshops.
- Medir eficacia de cada atividade pela taxa de defeitos prevenidos.

### Como Justificativa para o Squad
- Usar dados de shift-left para demonstrar ROI da pre-programacao.
- Comparar custo de atividades de pre-programacao vs. custo de defeitos escapados.
- Demonstrar reducao progressiva de defeitos em producao.

### Como Evolucao Continua
- Comecar com atividades de shift-left de maior impacto (design reviews).
- Expandir gradualmente para praticas mais sofisticadas (contract testing, threat modeling).
- Medir e ajustar continuamente a eficacia de cada pratica.

## Referencias

- Smith, L. (2001). "Shift-Left Testing." Dr. Dobb's Journal.
- Google Testing Blog. "Testing at Google" series.
- Humble, J. & Farley, D. (2010). "Continuous Delivery." Addison-Wesley.
- Forsgren, N. et al. (2018). "Accelerate." IT Revolution Press.
