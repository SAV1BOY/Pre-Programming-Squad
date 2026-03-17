# Legacy Boundary Isolation Framework

## Título e Propósito

O **Legacy Boundary Isolation Framework** é um sistema para definir e manter fronteiras claras entre código novo e sistemas legados. O propósito é permitir que novo desenvolvimento avance sem ser contaminado pela complexidade do legado, enquanto mantém interoperabilidade funcional — criando uma "zona de quarentena" controlada.

## Quando Usar

- Quando novo desenvolvimento precisa coexistir com sistemas legados
- Em projetos de modernização incremental (strangler fig pattern)
- Quando a equipe precisa integrar com sistemas que não pode modificar
- Quando bugs do legado começam a contaminar código novo
- Na definição de estratégia de migração gradual

## Conceitos-Chave

1. **Fronteira do Legado**: O ponto exato onde código novo encontra código legado. Deve ser explícita, documentada e estreita.
2. **Anti-Corruption Layer (ACL)**: Camada de tradução entre o modelo novo e o modelo do legado. Protege o código novo de conceitos e formatos do legado.
3. **Strangler Fig Pattern**: Estratégia de substituir o legado gradualmente, redirecionando funcionalidades uma a uma para o sistema novo.
4. **Contrato de Interface**: Acordo explícito sobre formato, protocolo e comportamento na fronteira. Mudanças no contrato requerem acordo das duas partes.
5. **Dívida de Integração**: Complexidade acumulada em adaptadores, conversores e workarounds necessários para manter a ponte com o legado.

## Processo / Passos

### Passo 1 — Mapear o Legado
Identifique: quais sistemas legados existem, quais funcionalidades proveem, quais dados possuem, quais interfaces expõem.

### Passo 2 — Identificar Pontos de Contato
Liste todos os pontos onde o novo sistema precisa interagir com o legado: APIs, banco de dados compartilhado, arquivos, filas, eventos.

### Passo 3 — Definir a Fronteira
Para cada ponto de contato, decida: onde exatamente a fronteira será traçada? O que fica de cada lado?

### Passo 4 — Projetar a Anti-Corruption Layer
Para cada fronteira, projete a camada de tradução. Ela deve:
- Converter formatos de dados do legado para o modelo novo
- Isolar erros e falhas do legado
- Ser substituível quando o legado for aposentado

### Passo 5 — Definir Contratos
Documente o contrato em cada fronteira: formato de dados, protocolo, SLA, tratamento de erros, versionamento.

### Passo 6 — Estabelecer Monitoramento na Fronteira
Instrumentar a fronteira para detectar: mudanças de comportamento do legado, aumento de erros, degradação de performance.

### Passo 7 — Planejar Migração Gradual
Defina a sequência de funcionalidades que serão migradas do legado para o novo sistema, e como o tráfego será redirecionado.

## Perguntas de Ativação

- "Onde exatamente o nosso código novo encontra o legado?"
- "Se o legado mudar sem avisar, o código novo quebra?"
- "Estamos importando conceitos do legado para o modelo novo?"
- "A ACL está fina o suficiente para ser mantida sem esforço desproporcional?"
- "Podemos testar o código novo sem o legado disponível?"
- "Quando o legado for aposentado, quanto do nosso código precisará mudar?"

## Output Esperado

| Ponto de Contato | Sistema Legado | Interface Atual | ACL Projetada | Contrato | Risco | Plano de Migração |
|---|---|---|---|---|---|---|
| Dados de cliente | ERP Mainframe | Arquivo CSV diário | Adapter que lê CSV e converte para domínio novo | Schema JSON validado | Formato muda sem aviso | Fase 2: API REST substituirá CSV |
| Autenticação | LDAP corporativo | Bind direto | Provider de autenticação com interface abstrata | Token JWT na saída | Indisponibilidade LDAP | Fase 3: migrar para identity provider moderno |
| Catálogo de produtos | Banco Oracle compartilhado | Query direta | Repository com read model próprio | Contrato de colunas usadas | Schema muda em deploys do legado | Fase 1: criar API dedicada sobre Oracle |

## Armadilhas Comuns

1. **Banco compartilhado como integração**: Acessar direto o banco do legado acopla fortemente. Prefira APIs ou eventos.
2. **ACL ausente**: Consumir dados do legado diretamente no código novo espalha conceitos legados por toda a base nova.
3. **ACL que cresce demais**: Se a ACL se torna tão complexa quanto o próprio legado, a fronteira falhou.
4. **Fronteira ambígua**: Não saber exatamente onde termina o legado e começa o novo gera zona cinzenta problemática.
5. **Migração infinita**: Sem plano explícito de migração, o legado persiste indefinidamente e a ACL vira permanente.
6. **Testar apenas o happy path da fronteira**: O legado vai enviar dados inesperados, falhar silenciosamente e mudar comportamento. Teste para isso.
