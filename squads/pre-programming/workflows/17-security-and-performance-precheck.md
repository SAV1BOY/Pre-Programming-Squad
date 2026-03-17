# Workflow 17: Pré-check de Segurança e Performance

## Objetivo
Executar revisões de segurança e performance antes da implementação, garantindo que o design atende os requisitos não-funcionais e não introduz vulnerabilidades.

## Trigger
- Arquitetura v1 aprovada (pode ser executado em paralelo com workflow 04).

## Agentes Envolvidos
- Agente de Qualidade
- Agente de Arquitetura
- Especialista de Segurança (se disponível)
- DBA

## Passos

### 1. Executar Pré-check de Segurança
- Executar task `run-security-precheck.md`.
- Preencher template `security-review-template.md`.
- **Output:** Revisão de segurança completa.

### 2. Executar Pré-check de Performance
- Executar task `run-performance-precheck.md`.
- Preencher template `performance-plan-template.md`.
- **Output:** Plano de performance completo.

### 3. Cruzar Riscos
- Vincular vulnerabilidades de segurança ao registro de riscos.
- Vincular gargalos de performance ao registro de riscos.
- Priorizar ações combinadas.
- **Output:** Registro de riscos atualizado.

### 4. Definir Ações Prioritárias
- Listar ações de segurança obrigatórias antes do dev (ex: setup de secrets).
- Listar ações de performance obrigatórias (ex: definir índices).
- Listar ações que podem ser feitas durante o dev.
- **Output:** Plano de ação priorizado.

### 5. Validar com Especialistas
- Se disponível, revisão com equipe de segurança da organização.
- Obter aceite ou lista de requisitos adicionais.
- **Output:** Aceite ou plano de adequação.

## Gates de Qualidade
- [ ] OWASP Top 10 foi revisado contra o design.
- [ ] Dados sensíveis estão classificados e protegidos.
- [ ] Metas de performance estão definidas e são atingíveis.
- [ ] Gargalos potenciais foram identificados.
- [ ] Ações de segurança obrigatórias estão listadas.
- [ ] Ações de performance estão priorizadas.
- [ ] Riscos de segurança e performance estão no registro de riscos.

## Output
- Security review completo.
- Performance plan completo.
- Plano de ação priorizado.

## Próximo Workflow
→ Retorna ao workflow principal (05 ou 06).
