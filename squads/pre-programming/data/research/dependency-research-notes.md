# Notas de Pesquisa de Dependências

## Propósito

Documentar a análise de todas as dependências externas e internas do projeto — bibliotecas, serviços de terceiros, APIs externas, times internos, fornecedores e qualquer elemento fora do controle direto do squad que afete a entrega. Dependências mal mapeadas são a principal causa de bloqueios inesperados e atrasos em projetos de software.

Este documento serve como inventário vivo de dependências, seus riscos, alternativas e planos de contingência.

---

## Estrutura de Registro

Cada dependência pesquisada deve conter:

- **ID da Dependência**: Identificador único (ex.: `DEP-001`)
- **Data de Identificação**: Quando a dependência foi descoberta
- **Pesquisador**: Membro do squad responsável
- **Tipo**: Classificação da dependência
- **Nome**: Nome da dependência
- **Versão/SLA**: Versão da biblioteca ou SLA do serviço
- **Criticidade**: Quão crítica é para o projeto
- **Proprietário**: Quem mantém a dependência
- **Estado de Saúde**: Avaliação atual da confiabilidade
- **Alternativas**: Opções de fallback ou substituição
- **Plano de Contingência**: O que fazer se a dependência falhar

---

## Campos Detalhados

### Tipo de Dependência
- **Biblioteca/Pacote**: Dependências de código (npm, pip, maven, go modules, etc.)
- **API Externa**: Serviços de terceiros consumidos (pagamento, e-mail, SMS, geolocalização)
- **Serviço Interno**: APIs ou serviços mantidos por outros times da organização
- **Infraestrutura**: Serviços cloud, DNS, CDN, load balancers
- **Dados**: Fontes de dados externas, feeds, data lakes compartilhados
- **Time/Pessoa**: Dependência de aprovação, conhecimento ou ação de outra equipe
- **Fornecedor**: Dependência de entrega de software ou serviço por fornecedor externo
- **Regulatório**: Dependência de aprovação de órgão regulador ou auditoria

### Criticidade
- **Bloqueante**: Sem esta dependência, o projeto não pode ser entregue
- **Alta**: Afeta funcionalidades core, mas existem workarounds parciais
- **Média**: Afeta funcionalidades secundárias, alternativas viáveis existem
- **Baixa**: Nice-to-have, pode ser removida do escopo se necessário

### Estado de Saúde
Avaliar periodicamente com base em:
- **Verde**: Estável, responsivo, sem incidentes recentes, boa documentação
- **Amarelo**: Alguns sinais de alerta (atrasos, incidentes menores, docs desatualizados)
- **Vermelho**: Problemas ativos (indisponibilidade, bugs conhecidos, time não responsivo)
- **Desconhecido**: Ainda não avaliado ou informações insuficientes

### Análise de Risco da Dependência
Para cada dependência crítica, avaliar:
- Probabilidade de indisponibilidade
- Impacto de indisponibilidade
- Tempo médio de resolução do fornecedor/time
- Histórico de incidentes
- Qualidade da documentação e suporte

---

## Template de Entrada

```markdown
### DEP-[NNN] — [Nome da Dependência]

- **Data de Identificação**: AAAA-MM-DD
- **Pesquisador**: [Nome]
- **Tipo**: [Biblioteca | API Externa | Serviço Interno | Infra | Dados | Time | Fornecedor | Regulatório]
- **Versão/SLA**: [Versão ou nível de SLA]
- **Criticidade**: [Bloqueante | Alta | Média | Baixa]
- **Proprietário**: [Time ou organização responsável]
- **Estado de Saúde**: [Verde | Amarelo | Vermelho | Desconhecido]

#### Descrição

[O que é essa dependência, por que o projeto precisa dela, como será utilizada.]

#### Análise de Risco

| Fator | Avaliação |
|-------|-----------|
| Probabilidade de falha | [Baixa | Média | Alta] |
| Impacto de falha | [Baixo | Médio | Alto | Catastrófico] |
| Tempo de resolução típico | [Estimativa] |
| Histórico de incidentes | [Quantidade e gravidade nos últimos 12 meses] |
| Qualidade da documentação | [Excelente | Boa | Regular | Ruim] |
| Responsividade do suporte | [Excelente | Boa | Regular | Ruim] |

#### Alternativas Disponíveis

1. **[Alternativa A]**: [Descrição, prós, contras, custo de migração]
2. **[Alternativa B]**: [Descrição, prós, contras, custo de migração]

#### Plano de Contingência

[O que o squad fará se essa dependência ficar indisponível ou apresentar problemas críticos. Incluir passos específicos, responsáveis e tempos estimados.]

#### Pontos de Contato

- **Técnico**: [Nome — e-mail — canal Slack]
- **Gerencial**: [Nome — e-mail]
- **Emergência**: [Processo de escalação]

#### Próximos Passos

- [ ] [Ação 1 — Responsável — Prazo]
- [ ] [Ação 2 — Responsável — Prazo]
```

---

## Diretrizes de Uso

1. **Mapear cedo**: Identificar dependências nas primeiras fases do projeto. Dependências descobertas tarde são as mais perigosas.
2. **Validar ativamente**: Não confie em documentação antiga. Teste as APIs, verifique as versões, confirme os SLAs.
3. **Manter contato**: Estabeleça canal de comunicação com os proprietários de cada dependência crítica antes de precisar deles.
4. **Monitorar saúde**: Revise o estado de saúde das dependências semanalmente. Degradação gradual é difícil de perceber sem monitoramento ativo.
5. **Ter plano B**: Toda dependência bloqueante deve ter pelo menos uma alternativa identificada, mesmo que seja um workaround temporário.
6. **Versionar com cuidado**: Fixar versões de bibliotecas e documentar política de atualização. Updates automáticos em produção são uma fonte de incidentes.
