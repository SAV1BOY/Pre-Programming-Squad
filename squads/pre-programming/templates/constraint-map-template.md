# Template: Mapa de Restrições

## Título
Constraint Map — Mapeamento de Restrições do Projeto

## Propósito
Identificar e documentar todas as restrições que limitam as opções de design, arquitetura e implementação do projeto, permitindo decisões informadas dentro dos limites reais.

## Quando Usar
- Durante a fase de discovery, para mapear limites do projeto.
- Antes de decisões de arquitetura ou escolha de tecnologia.
- Quando surgem novas restrições ao longo do planejamento.

## Seções

### 1. Informações Gerais
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| Responsável | `[nome]` |
| Data | `[YYYY-MM-DD]` |
| Versão | `[número da versão]` |

### 2. Restrições de Tempo
| Restrição | Origem | Negociável? | Impacto no Escopo |
|-----------|--------|------------|-------------------|
| `[prazo ou deadline]` | `[quem impôs]` | `[Sim/Não]` | `[o que muda se não cumprir]` |

### 3. Restrições de Orçamento
| Restrição | Valor | Origem | Negociável? |
|-----------|-------|--------|------------|
| `[limite financeiro]` | `[R$ ou recurso]` | `[quem definiu]` | `[Sim/Não]` |

### 4. Restrições Tecnológicas
| Restrição | Descrição | Motivo | Alternativa |
|-----------|-----------|--------|------------|
| `[tecnologia obrigatória ou proibida]` | `[detalhe]` | `[por quê]` | `[se houver]` |

### 5. Restrições de Equipe
| Restrição | Descrição | Impacto |
|-----------|-----------|---------|
| `[limitação de equipe]` | `[detalhe]` | `[como afeta o projeto]` |

### 6. Restrições Regulatórias e de Compliance
| Regulação | Requisito | Impacto Técnico | Validação |
|-----------|-----------|----------------|-----------|
| `[LGPD, PCI-DSS, etc.]` | `[o que exige]` | `[como afeta a arquitetura]` | `[como provar conformidade]` |

### 7. Restrições de Infraestrutura
| Restrição | Ambiente | Impacto |
|-----------|----------|---------|
| `[limitação de infra]` | `[prod/staging/dev]` | `[como afeta decisões]` |

### 8. Restrições Organizacionais
| Restrição | Descrição | Impacto |
|-----------|-----------|---------|
| `[processos, aprovações, cultura]` | `[detalhe]` | `[como afeta o projeto]` |

### 9. Resumo de Impacto
| Categoria | Nível de Restrição | Principal Impacto |
|-----------|-------------------|-------------------|
| Tempo | `[Alto/Médio/Baixo]` | `[resumo]` |
| Orçamento | `[Alto/Médio/Baixo]` | `[resumo]` |
| Tecnologia | `[Alto/Médio/Baixo]` | `[resumo]` |
| Equipe | `[Alto/Médio/Baixo]` | `[resumo]` |
| Regulatório | `[Alto/Médio/Baixo]` | `[resumo]` |
| Infraestrutura | `[Alto/Médio/Baixo]` | `[resumo]` |

## Exemplo de Preenchimento

### 4. Restrições Tecnológicas
| Restrição | Descrição | Motivo | Alternativa |
|-----------|-----------|--------|------------|
| Deve usar PostgreSQL | Banco relacional já em uso | Equipe de DBA só suporta Postgres | Nenhuma viável no prazo |
| Proibido usar serviços fora do Brasil | Dados devem ficar em território nacional | LGPD e política interna | Usar região sa-east-1 da AWS |

### 6. Restrições Regulatórias e de Compliance
| Regulação | Requisito | Impacto Técnico | Validação |
|-----------|-----------|----------------|-----------|
| LGPD | Dados pessoais criptografados em repouso | Encryption at rest obrigatório no banco | Relatório de auditoria trimestral |

## Dicas de Qualidade
- **Diferencie restrições de preferências:** Restrição é inegociável; preferência pode ser discutida.
- **Verifique a origem:** Toda restrição deve ter uma fonte identificável e verificável.
- **Questione restrições antigas:** Restrições de projetos anteriores podem não se aplicar mais.
- **Mapeie dependências entre restrições:** Uma restrição pode amplificar o impacto de outra.
- **Atualize regularmente:** Restrições podem mudar — mantenha o mapa atualizado.
