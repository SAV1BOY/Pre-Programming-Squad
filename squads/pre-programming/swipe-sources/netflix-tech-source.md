# Netflix Tech — Fonte de Referência

## Fonte

**Organização**: Netflix
**Prática**: Chaos Engineering, resiliência, cultura de liberdade e responsabilidade
**Referências Principais**:
- Netflix Tech Blog (netflixtechblog.com)
- "Chaos Engineering" (Livro, O'Reilly, Casey Rosenthal & Nora Jones)
- Simian Army, Chaos Monkey e ferramentas de resiliência open source

## URL de Referência

- https://netflixtechblog.com/
- https://netflix.github.io/
- https://www.gremlin.com/community/tutorials/chaos-engineering-the-history-principles-and-practice/

---

## O que Aprender

### Chaos Engineering

A Netflix popularizou a prática de injetar falhas intencionalmente em sistemas de produção para descobrir fraquezas antes que causem incidentes reais. Princípios:

- **Construir uma hipótese sobre o comportamento steady-state**: "Se o serviço X falhar, o sistema degrada gracefully"
- **Variar eventos do mundo real**: Derrubar instâncias, injetar latência, simular particionamento de rede
- **Rodar em produção**: Testes em staging são insuficientes — produção tem complexidade que staging não reproduz
- **Automatizar e executar continuamente**: Não é exercício pontual, é prática contínua

### Cultura de Liberdade e Responsabilidade

A Netflix dá extrema liberdade técnica aos times, mas espera responsabilidade proporcional:
- Times escolhem suas próprias ferramentas e arquiteturas
- Cada time é responsável por operar o que constrói (you build it, you run it)
- Revisões pós-incidente sem culpa (blameless post-mortems)

### Full Cycle Developers

Na Netflix, engenheiros são responsáveis por todo o ciclo: design, implementação, deploy, operação e suporte. Isso gera:
- Design com operabilidade em mente
- Código escrito pensando em debugging e monitoring
- Ownership real do produto técnico

---

## Práticas Relevantes para Pré-Programação

1. **Plano de resiliência no design**: Todo design doc deve incluir "failure mode analysis" — para cada componente e dependência, documentar o que acontece quando falha e como o sistema responde.

2. **Testes de caos no plano de testes**: Incluir cenários de chaos engineering no plano de testes pré-codificação. Mesmo que a execução seja pós-deploy, o planejamento é pré-codificação.

3. **Operabilidade como requisito**: Incluir nos critérios de readiness review: logs estruturados, métricas de negócio, health checks, alertas definidos, runbooks de operação.

4. **Blameless culture no squad**: Quando premissas se provam erradas ou riscos se materializam, a análise foca em melhorar o processo, não em encontrar culpados.

5. **"You build it, you run it" no planejamento**: Se o time de desenvolvimento vai operar o sistema, incluir requisitos operacionais (monitoring, alerting, runbooks) nos artefatos de pré-programação.

6. **Steady-state hypothesis**: Para cada funcionalidade, definir o que é "comportamento normal" em termos mensuráveis. Isso se torna a base para alerts e para testes de caos.

7. **Degradação graceful como padrão**: Em vez de "funciona ou não funciona", planejar modos intermediários de operação para cada cenário de falha.
