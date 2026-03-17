# Ferramenta Interna — Fase 06: Testes

## Objetivo da Fase

Definir testes pragmáticos proporcionais à criticidade da ferramenta. Ferramentas internas de baixo risco não precisam de coverage de 90%. Ferramentas com acesso a dados de produção precisam de testes rigorosos de proteção.

## Agentes Envolvidos

- **Agente de Testes** (líder da fase) — Calibra nível de testes
- **Agente de Riscos** — Prioriza cenários de risco para cobertura

## Inputs

- MVP da ferramenta (Fase 03)
- Matriz de riscos (Fase 05)
- Proteções para ações destrutivas
- Modelo de acesso a dados

## Atividades

1. **Calibrar nível de testes** — Ferramenta read-only: testes de integração com dados. Ferramenta read-write: testes de proteção e validação obrigatórios. Ferramenta temporária: smoke tests são suficientes.
2. **Testar proteções de ações destrutivas** — Cada proteção (confirmação, dry-run, undo) deve ser testada. Simular operação destrutiva e confirmar que proteção funciona.
3. **Testar autenticação e autorização** — Usuário sem acesso é barrado? Usuário com acesso parcial vê apenas o que deve? Sessão expira?
4. **Testar com dados realistas** — Usar amostra de dados de produção (anonimizados se necessário). Verificar que a ferramenta funciona com volume e formato real.
5. **Testar cenários de erro** — O que acontece quando o sistema fonte está indisponível? Quando dados estão em formato inesperado? Quando o usuário faz input inválido?
6. **User acceptance test** — Pelo menos 2 usuários-alvo testam a ferramenta antes do lançamento e dão feedback.

## Outputs

- Suite de testes proporcional à criticidade
- Testes de proteção para ações destrutivas
- Testes de autenticação e autorização
- Resultado de testes com dados realistas
- Feedback de user acceptance test

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Proteções testadas | Cada proteção destrutiva foi validada | Sim (se aplicável) |
| Auth testada | Autenticação e autorização verificadas | Sim |
| Dados realistas | Testada com amostra de produção | Sim |
| UAT realizado | Pelo menos 2 usuários testaram | Sim |

## Próxima Fase

→ [07-readiness.md](./07-readiness.md) — Avaliação de prontidão para lançamento interno
