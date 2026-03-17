# Multi-Team Coordination Framework

## Propósito
Coordenar trabalho entre múltiplos times/squads quando um projeto afeta mais de um domínio, reduzindo atrito de comunicação e dependências não gerenciadas.

## Problema que Resolve
Projetos cross-team falham não por incompetência técnica, mas por falha de coordenação: times trabalham com premissas diferentes, entregas não sincronizam, dependências bloqueiam silenciosamente.

## Quando Usar
- Em projetos porte G/XG que envolvem múltiplos squads
- Quando dependency map revela dependências cross-team
- Quando config.yaml aciona `cross_squad_sync: required`

## Processo

### Passo 1 — Mapear Times e Responsabilidades
| Time | Responsabilidade | Entrega | Dependências |
|------|-----------------|---------|-------------|
| Pre-Programming | Arch, risks, handoff | Implementation package | Design (UX), Data (schema) |
| Design | UX flows, prototypes | Wireframes, specs | Pre-Prog (requirements) |
| Coding | Implementation | Working code | Pre-Prog (handoff) |
| Data | Analytics, metrics | Pipeline, dashboards | Pre-Prog (event taxonomy) |

### Passo 2 — Definir Pontos de Contato
Cada time designa um **liaison** que é o ponto único de contato para coordenação. Liaisons participam de syncs cross-team.

### Passo 3 — Estabelecer Cadência
| Cerimônia | Frequência | Participantes | Duração |
|-----------|-----------|--------------|---------|
| Cross-team standup | 2x/semana | Liaisons | 15 min |
| Dependency review | Semanal | Liaisons + chiefs | 30 min |
| Integration checkpoint | Por milestone | Todos os envolvidos | 60 min |

### Passo 4 — Rastrear Dependências
Manter dependency board atualizado:
```
[BLOQUEADO] Auth API spec → Coding squad aguarda Pre-Prog
[EM RISCO] Design system component → Design squad atrasado 2 dias
[OK] Database schema → Data squad entregou
[OK] Security review → Cyber squad aprovou
```

### Passo 5 — Resolução de Conflitos
1. Liaisons tentam resolver em 24h
2. Se não resolve → Chiefs dos squads envolvidos
3. Se não resolve → Escalação para C-Level com decision memo

## Armadilhas
- **Assumir contexto compartilhado** → Cada time tem seu próprio contexto; sincronizar explicitamente
- **Syncs demais** → Mais de 3 syncs/semana = overhead; manter cadência mínima efetiva
- **Dependência sem owner** → Toda dependência precisa de responsável e prazo
- **Não ter processo de desbloqueio** → Bloqueio sem escalação = atraso silencioso
