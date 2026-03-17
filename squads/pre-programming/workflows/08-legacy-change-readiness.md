# Workflow 08: Prontidão para Mudanças em Legado

## Objetivo
Garantir que mudanças em sistemas legados sejam planejadas com análise de impacto, compatibilidade e migração adequadas, reduzindo o risco de quebras em sistemas existentes.

## Trigger
- Projeto classificado como "Evolução de sistema existente" ou "Migração/Modernização".

## Agentes Envolvidos
- Agente de Legado
- Agente de Arquitetura
- DBA
- Equipe do sistema legado

## Passos

### 1. Analisar Sistema Existente
- Executar task `analyze-existing-system.md`.
- Preencher template `legacy-impact-template.md`.
- **Output:** Documentação atualizada do legado.

### 2. Avaliar Compatibilidade
- Executar task `assess-compatibility.md`.
- Comparar modelos de dados, interfaces e processos.
- **Output:** Matriz de compatibilidade.

### 3. Planejar Migração
- Executar task `plan-migration.md`.
- Definir estratégia, fases e rollback.
- **Output:** Plano de migração detalhado.

### 4. Revisar Riscos de Legado
- Atualizar template `risk-register-template.md` com riscos específicos de legado.
- Definir planos de mitigação.
- **Output:** Riscos de legado documentados.

### 5. Definir Período de Coexistência
- Determinar quanto tempo ambos os sistemas coexistem.
- Definir como dados são sincronizados.
- Definir como usuários são roteados.
- **Output:** Estratégia de coexistência.

### 6. Aprovar Plano de Legado
- Apresentar para stakeholders e equipe do legado.
- Obter aceite formal.
- **Output:** Plano aprovado.

## Gates de Qualidade
- [ ] O sistema legado foi analisado e documentado.
- [ ] Compatibilidade foi avaliada campo a campo.
- [ ] Breaking changes estão identificadas com plano de resolução.
- [ ] Plano de migração tem rollback para cada fase.
- [ ] Riscos de legado têm mitigação.
- [ ] Período de coexistência está definido.
- [ ] Equipe do legado aprovou o plano.

## Output
- Legacy impact analysis completa.
- Plano de migração aprovado.
- Estratégia de coexistência definida.

## Próximo Workflow
→ Retorna ao workflow principal (03 ou 06, conforme o caso).
