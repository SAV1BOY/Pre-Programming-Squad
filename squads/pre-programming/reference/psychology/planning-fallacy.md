# Falacia do Planejamento

## Vies/Efeito

**Falacia do Planejamento (Planning Fallacy):** A tendencia de subestimar o tempo, custo e risco de acoes futuras e, simultaneamente, superestimar seus beneficios. Identificada por Kahneman e Tversky (1979), ocorre mesmo quando a pessoa tem experiencia com tarefas similares que demoraram mais do que o previsto.

## Descricao

A falacia do planejamento e distinta do otimismo generico. E especifica para planejamento: ao prever nossos proprios projetos, adotamos uma "visao interna" (focada no caso especifico) em vez de uma "visao externa" (baseada em taxas base de projetos similares). O resultado e que 80-90% dos projetos de software excedem o prazo e/ou o orcamento original.

## Como se Manifesta em Pre-Programacao

### No Planejamento de Projetos
- **Focar no cenario ideal:** Planejar assumindo que tudo correra sem problemas — sem bugs inesperados, sem mudancas de requisitos, sem ausencias, sem dependencias bloqueadas.
- **Ignorar taxas base:** Saber que projetos similares atrasaram e acreditar que "desta vez sera diferente."
- **Decompor sem margem:** Quebrar o projeto em tarefas, estimar cada uma otimisticamente e somar — sem margem para o inesperado.

### Na Estimativa de Migrações
- **Subestimar integracao:** Cada componente funciona isoladamente, mas a integracao adiciona complexidade nao prevista.
- **Ignorar a cauda longa:** Os ultimos 10-20% do trabalho (edge cases, observabilidade, documentacao, rollback) frequentemente consomem 40-50% do tempo.

### Na Definicao de Escopo
- **Escopo otimista:** Incluir tudo no MVP porque "nao e tao dificil."
- **Subestimar dependencias externas:** Assumir que outras equipes, APIs externas e infraestrutura estarao disponiveis quando necessario.

## Como Mitigar

### 1. Reference Class Forecasting (Kahneman)
Ignor a visao interna. Busque a taxa base: "Quanto tempo projetos similares levaram?" Use dados historicos, nao intuicao.

**Implementacao pratica:**
- Manter banco de dados de projetos anteriores: escopo, estimativa, duracao real.
- Para cada novo projeto, buscar 3-5 projetos similares e usar a media como base.

### 2. Adicionar Buffer Sistematico
Regra pratica baseada em dados empiricos:
- Tarefa bem conhecida: +30%
- Tarefa com alguma incerteza: +50-100%
- Tarefa com alta incerteza: +100-200% (ou fazer spike antes)

### 3. Planejar para o Cenario Provavel, nao o Ideal
Em vez de perguntar "Quanto tempo leva se tudo der certo?", perguntar "Quanto tempo leva considerando os problemas que tipicamente surgem?"

### 4. Outside View (Visao Externa)
Pedir para alguem de fora do projeto estimar. Pessoas nao envolvidas emocionalmente tendem a ser mais realistas.

### 5. Decomposicao + Margem por Camada
Decompor em tarefas. Estimar cada uma. Adicionar margem em cada tarefa (nao so no total). Adicionar margem adicional para integracao entre tarefas.

### 6. Trackear Historico de Estimativas
Comparar estimativas passadas com duracao real. Calcular o "fator de correcao" medio da equipe e aplicar automaticamente.

## Exemplo Real

**Contexto:** Equipe planeja migrar sistema de autenticacao de sessoes server-side para JWT. Estimativa: 4 semanas.

**Decomposicao original:**
- Semana 1: Implementar emissao e validacao de JWT.
- Semana 2: Migrar endpoints para usar JWT.
- Semana 3: Testes e correcoes.
- Semana 4: Deploy e monitoramento.

**O que realmente aconteceu (12 semanas):**
- Semanas 1-2: Implementacao basica (conforme estimado).
- Semana 3: Descoberta de que apps mobile cacheiam tokens de forma diferente.
- Semana 4: Redesign da estrategia de refresh token para mobile.
- Semana 5-6: Migracao gradual com dual-auth (sessao + JWT simultaneos).
- Semana 7: Descoberta de que servico interno de relatorios depende de sessoes.
- Semana 8-9: Adaptacao do servico de relatorios.
- Semana 10: Testes de performance revelam que JWT payload e grande demais.
- Semana 11: Otimizacao de claims no JWT.
- Semana 12: Deploy final com rollback pronto.

**O que deveria ter acontecido na pre-programacao:**
- Mapear todos os consumers de sessao (servicos internos, mobile, web).
- Planejar periodo de dual-auth como fase explicita.
- Incluir margem para descobertas de dependencias nao mapeadas.
- Estimar 4 semanas (ideal) + 4 semanas (buffer de integracao) + 2 semanas (buffer de incerteza) = 10 semanas.
- Comunicar range: "8-12 semanas" em vez de "4 semanas."
