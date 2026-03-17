# Task: Executar Pré-check de Performance

## Objetivo
Avaliar se a arquitetura e o design propostos são capazes de atender os requisitos de performance, identificando potenciais gargalos antes da implementação.

## Input Necessário
- Requisitos não-funcionais de performance.
- Esboço de arquitetura.
- Volumetria esperada (usuários, transações, dados).
- Mapa de integrações com SLAs.

## Agentes Envolvidos
- **Agente de Qualidade:** Conduz a análise de performance.
- **Agente de Arquitetura:** Apresenta o design e explica decisões.
- **DBA/Especialista de Dados:** Avalia modelo de dados sob perspectiva de performance.

## Passos

### 1. Revisar Metas de Performance
- Confirmar que metas estão definidas e mensuráveis.
- Validar que metas são realistas dado o volume esperado.
- Definir cenários de carga (normal, pico, stress).

### 2. Analisar Gargalos Potenciais
- Banco de dados: queries sem índice, N+1, locks.
- Rede: latência de integrações, volume de dados trafegados.
- CPU/Memória: processos pesados, memory leaks potenciais.
- I/O: operações de disco, upload/download de arquivos.

### 3. Revisar Estratégias de Otimização
- Cache: onde é aplicável e qual estratégia (write-through, write-behind, TTL).
- Paginação: como dados grandes serão paginados.
- Async: quais operações podem ser assíncronas.
- CDN: para assets estáticos.

### 4. Avaliar Escalabilidade
- O design escala horizontalmente?
- Quais componentes são stateful e como afetam a escala?
- Há pontos de contenção (single point of failure/bottleneck)?

### 5. Planejar Testes de Performance
- Definir cenários de teste de carga.
- Selecionar ferramenta (k6, Gatling, JMeter).
- Definir quando os testes serão executados.

### 6. Documentar
- Preencher o template `performance-plan-template.md`.
- Registrar riscos e plano de ação.

## Output Esperado
- Análise de gargalos potenciais documentada.
- Estratégias de otimização planejadas.
- Plano de testes de performance.
- Performance plan preenchido.

## Checklist de Validação
- [ ] Metas de performance estão definidas e mensuráveis.
- [ ] Gargalos potenciais foram identificados por camada.
- [ ] Estratégias de otimização estão planejadas (cache, async, CDN).
- [ ] Escalabilidade foi avaliada.
- [ ] Plano de testes de performance está definido.
- [ ] Ferramenta de teste de carga foi selecionada.
- [ ] Cenários de carga (normal, pico, stress) estão definidos.
- [ ] Riscos de performance têm plano de ação.
