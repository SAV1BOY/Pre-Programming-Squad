# Test Surface Mapping

## Título e Propósito

O **Test Surface Mapping** é um framework para mapear sistematicamente todas as superfícies testáveis de um sistema e decidir conscientemente o que testar, como testar e o que não testar (com justificativa). O propósito é substituir a cobertura de testes ad-hoc por uma estratégia deliberada que maximiza o valor dos testes com investimento proporcional ao risco.

## Quando Usar

- Ao definir estratégia de teste para um novo projeto ou componente
- Quando a suíte de testes cresceu sem estratégia e precisa ser racionalizada
- Para identificar áreas do sistema com cobertura insuficiente
- Em revisões de qualidade para avaliar maturidade de testes
- Quando a equipe debate sobre "quanto testar" e "que tipo de teste usar"

## Conceitos-Chave

1. **Superfície de Teste**: Um aspecto do sistema que pode ser verificado: endpoint de API, função de negócio, fluxo de UI, contrato de integração, requisito de performance.
2. **Pirâmide de Testes**: Muitos testes unitários (rápidos, baratos), menos de integração (médios), poucos E2E (lentos, caros).
3. **Valor do Teste**: Capacidade de detectar regressões reais. Teste que nunca falha ou que falha por motivos irrelevantes tem valor baixo.
4. **Custo do Teste**: Tempo para escrever + tempo para executar + tempo para manter. Testes que quebram com refactors internos são caros.
5. **Risco sem Teste**: O risco aceito ao decidir não testar uma superfície. Deve ser explícito.

## Processo / Passos

### Passo 1 — Mapear Superfícies
Liste todas as superfícies testáveis do sistema. Categorize por tipo: lógica de negócio, API/contrato, integração, UI, performance, segurança.

### Passo 2 — Avaliar Risco de Cada Superfície
Para cada superfície, avalie: "Se isso quebrar sem detectarmos, qual é o impacto?" Classifique: Crítico, Alto, Médio, Baixo.

### Passo 3 — Avaliar Volatilidade
Superfícies que mudam frequentemente precisam de testes mais robustos. Superfícies estáveis podem tolerar menos cobertura.

### Passo 4 — Escolher Tipo de Teste por Superfície
Para cada superfície, defina o tipo de teste mais eficiente:
- Lógica pura → unitário
- Contrato de API → contrato/integração
- Fluxo completo → E2E (seletivo)
- Performance → load test (periódico)
- Segurança → scan + teste manual

### Passo 5 — Definir Cobertura-Alvo por Superfície
Não persiga 100% em tudo. Defina cobertura proporcional ao risco:
- Crítico: 90%+ com múltiplos tipos de teste
- Alto: 80%+ com testes automatizados
- Médio: 60%+ com testes seletivos
- Baixo: Teste manual ou nenhum (risco aceito)

### Passo 6 — Identificar Gaps e Excessos
Gaps: superfícies de alto risco sem teste. Excessos: testes caros em superfícies de baixo risco.

### Passo 7 — Documentar Decisões
Registre o mapa, as decisões e as justificativas. "Decidimos não testar X porque [justificativa]" é melhor que "esquecemos de testar X".

## Perguntas de Ativação

- "Se todos os nossos testes passarem, temos confiança de fazer deploy?"
- "Quais áreas do sistema nos causam medo quando fazemos mudanças?"
- "Temos testes caros (lentos, frágeis) cobrindo áreas de baixo risco?"
- "Quais superfícies críticas não têm nenhum teste?"
- "Nossos testes testam comportamento (estável) ou implementação (frágil)?"
- "Quanto tempo nossa suíte de testes leva para rodar? É proporcional ao valor?"

## Output Esperado

| Superfície | Tipo | Risco | Volatilidade | Teste Recomendado | Cobertura Atual | Cobertura Alvo | Ação |
|---|---|---|---|---|---|---|---|
| Motor de preços | Lógica de negócio | Crítico | Alta | Unitário extensivo | 45% | 90% | Prioridade 1: adicionar testes |
| API de pedidos | Contrato | Alto | Média | Contrato + integração | 70% | 80% | Adicionar cenários de erro |
| Fluxo de checkout | E2E | Crítico | Média | E2E seletivo | 30% | 70% | Adicionar 3 cenários E2E |
| Página "Sobre" | UI | Baixo | Baixa | Nenhum (risco aceito) | 0% | 0% | Nenhuma |
| Autenticação | Segurança | Crítico | Baixa | Unitário + security scan | 60% | 90% | Adicionar testes de injection, brute force |
| Geração de relatórios | Performance | Alto | Média | Load test periódico | 0% | 1 teste/semana | Criar load test |

**Resumo**: 6 superfícies críticas, 3 abaixo da cobertura alvo. 2 testes caros em áreas de baixo risco — candidatos a remoção.

## Armadilhas Comuns

1. **Cobertura uniforme**: Tratar todas as superfícies com a mesma intensidade desperdiça esforço.
2. **Testes de implementação**: Testar como o código funciona internamente em vez de o que ele faz. Quebram com refactors legítimos.
3. **E2E como padrão**: Usar testes E2E para tudo porque "testam tudo". São lentos, frágeis e caros de manter.
4. **Cobertura de código como proxy**: 80% de cobertura de código pode significar 0% de cobertura de requisitos.
5. **Testes que nunca falham**: Se um teste nunca falhou em 2 anos, pode estar testando algo trivial ou estar mal escrito.
6. **Não testar integrações**: Unitários passam, integração falha. O espaço entre componentes é onde os bugs moram.
