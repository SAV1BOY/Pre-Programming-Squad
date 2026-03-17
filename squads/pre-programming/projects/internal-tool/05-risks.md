# Ferramenta Interna — Fase 05: Riscos

## Objetivo da Fase

Identificar riscos de ferramentas internas: acesso indevido a dados de produção, ações destrutivas acidentais, ferramenta temporária que vira permanente sem manutenção.

## Agentes Envolvidos

- **Agente de Riscos** (líder da fase) — Identifica riscos operacionais e de segurança
- **Agente de Arquitetura** — Valida proteções técnicas

## Inputs

- Arquitetura da ferramenta (Fase 04)
- Modelo de acesso a dados
- Perfil dos usuários-alvo (Fase 01)
- Classificação de dados acessados (sensíveis ou não)

## Atividades

1. **Avaliar risco de ação destrutiva** — A ferramenta pode excluir dados, modificar configurações ou afetar produção? Se sim, quais proteções existem (confirmação, dry-run, undo)?
2. **Avaliar risco de acesso indevido** — Quem tem acesso? Os acessos são revisados periodicamente? Há princípio de menor privilégio?
3. **Avaliar risco de "ferramenta zumbi"** — Ferramenta temporária que ninguém mantém mas todos usam. Sem atualizações de segurança, sem documentação, sem owner.
4. **Avaliar risco de dados sensíveis** — PII, dados financeiros, credenciais visíveis na ferramenta? Logs da ferramenta contêm dados sensíveis?
5. **Avaliar risco de single point of failure** — Se a ferramenta ficar indisponível, o processo manual pode ser retomado? Os usuários ainda sabem fazer manualmente?
6. **Definir plano de ownership** — Quem é o owner da ferramenta? Quem mantém? O que acontece quando o owner muda de time?

## Outputs

- Matriz de riscos operacionais
- Proteções para ações destrutivas (confirmação, dry-run, undo)
- Política de acesso (quem, como, revisão periódica)
- Plano de ownership e manutenção
- Avaliação de risco de ferramenta zumbi
- Procedimento de fallback manual documentado

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Ações destrutivas protegidas | Confirmação e/ou dry-run para operações de escrita | Sim |
| Acesso controlado | Autenticação e autorização configuradas | Sim |
| Owner definido | Pessoa/time responsável pela manutenção | Sim |
| Fallback manual | Processo manual documentado como backup | Sim |

## Próxima Fase

→ [06-tests.md](./06-tests.md) — Testes pragmáticos para ferramenta interna
