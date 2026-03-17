# Task: Analisar Sistema Existente

## Objetivo
Compreender o sistema legado que será afetado pelo projeto, documentando sua arquitetura, dependências, estado atual e riscos associados à mudança.

## Input Necessário
- Identificação do(s) sistema(s) legado(s) impactados.
- Documentação existente (se houver).
- Acesso ao código-fonte e infraestrutura.
- Contato com a equipe que mantém o legado.

## Agentes Envolvidos
- **Agente de Legado:** Conduz a análise.
- **Equipe do sistema legado:** Fornece conhecimento institucional.
- **Agente de Arquitetura:** Avalia aspectos técnicos.
- **DBA:** Analisa estrutura de dados do legado.

## Passos

### 1. Coletar Documentação Existente
- Reunir toda documentação disponível (diagramas, specs, runbooks).
- Avaliar a qualidade e atualidade da documentação.
- Identificar gaps de documentação.

### 2. Mapear Arquitetura Atual
- Identificar componentes e tecnologias.
- Mapear fluxos de dados e comunicação.
- Documentar infraestrutura (servidores, banco, redes).

### 3. Identificar Dependências
- Quais sistemas dependem do legado?
- De quais sistemas o legado depende?
- Quais interfaces são expostas (APIs, arquivos, banco direto)?

### 4. Avaliar Estado de Saúde
- Métricas operacionais (uptime, incidentes, performance).
- Qualidade do código (cobertura de testes, dívida técnica).
- Frequência de mudanças e problemas recentes.

### 5. Entrevistar a Equipe
- Perguntar sobre pontos de dor, riscos conhecidos, áreas frágeis.
- Documentar conhecimento que não está escrito em lugar nenhum.
- Identificar "minas terrestres" que a equipe conhece.

### 6. Documentar
- Preencher o template `legacy-impact-template.md`.
- Criar diagrama atualizado do sistema legado.

## Output Esperado
- Documentação atualizada do sistema legado.
- Mapa de dependências bidirecional.
- Avaliação de saúde do sistema.
- Lista de riscos e "minas terrestres" identificadas.

## Checklist de Validação
- [ ] A arquitetura do legado está documentada.
- [ ] Dependências bidirecionais estão mapeadas.
- [ ] Interfaces expostas pelo legado estão documentadas.
- [ ] Estado de saúde foi avaliado com dados.
- [ ] A equipe do legado foi entrevistada.
- [ ] Conhecimento institucional foi capturado.
- [ ] Riscos e áreas frágeis estão identificados.
- [ ] Diagrama atualizado foi produzido.
