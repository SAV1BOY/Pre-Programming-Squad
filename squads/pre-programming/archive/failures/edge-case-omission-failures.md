# Falhas por Omissão de Edge Cases

## Objetivo

Catalogar casos onde edge cases não identificados na fase de pré-programação causaram bugs em produção, incidentes ou retrabalho. A identificação precoce de edge cases é uma das atividades mais valiosas do Pre-Programming Squad.

---

## Caso 1: Fuso Horário na Virada do Dia

### O Que Aconteceu
Sistema de agendamento permitia marcar compromissos para "amanhã". Um usuário em Fernando de Noronha (UTC-2) agendou às 23:30 para "amanhã". O servidor em São Paulo (UTC-3) interpretou "amanhã" como o dia seguinte de São Paulo, que ainda era "hoje" em Fernando de Noronha. O compromisso apareceu no dia errado.

### O Que Deu Errado
- "Amanhã" foi calculado no timezone do servidor, não do usuário
- Testes usavam apenas um timezone
- Requisito não mencionava comportamento multi-timezone
- Nenhum agente questionou como datas relativas seriam tratadas

### Causa Raiz
**Edge case temporal não explorado.** Operações com datas relativas ("amanhã", "próxima semana") são notoriamente perigosas em sistemas multi-timezone. O design não definiu timezone de referência.

### Como Prevenir
1. Para qualquer funcionalidade envolvendo datas/horas, criar matrix de cenários com pelo menos 3 timezones
2. Testar explicitamente: virada do dia, horário de verão, UTC offset fracionário
3. Definir no design: "todas as datas relativas são calculadas no timezone do ___"

### Checklist Atualizado
- [ ] Funcionalidades com data/hora foram testadas com múltiplos timezones?
- [ ] Datas relativas têm timezone de referência definido?
- [ ] Transição de horário de verão foi considerada?

---

## Caso 2: Usuário com Email Duplicado após Merge de Contas

### O Que Aconteceu
Feature de merge de contas corporativas: quando empresa A compra empresa B, contas dos usuários são unificadas. Um usuário tinha conta nas duas empresas com o mesmo email. O merge tentou criar uma entrada duplicada, violou unique constraint e a transação falhou silenciosamente, deixando o usuário sem acesso.

### O Que Deu Errado
- Merge assumia que emails eram únicos entre empresas
- Constraint de unicidade existia no banco mas o código não tratava a violação
- Nenhum cenário de teste cobria usuário com conta em ambas as empresas
- Erro silencioso (catch genérico) impediu detecção rápida

### Causa Raiz
**Premissa incorreta não validada.** A premissa "emails são únicos entre empresas" era verdadeira em 99.7% dos casos mas falsa para ~200 usuários. O design não questionou premissas sobre unicidade.

### Como Prevenir
1. Listar todas as premissas do design e validar cada uma com dados reais
2. Para operações de merge/migração, executar dry-run com dados de produção antes
3. Nunca usar catch genérico em operações de dados — cada erro deve ter tratamento específico

### Checklist Atualizado
- [ ] Premissas sobre unicidade de dados foram validadas com dados reais?
- [ ] Operações de merge/migração têm modo dry-run?
- [ ] Violações de constraint têm tratamento específico (não catch genérico)?

---

## Caso 3: Campo de Texto com Emoji de Múltiplos Code Points

### O Que Aconteceu
Campo de nome de usuário tinha limite de 50 caracteres validado no frontend com `.length`. Emojis compostos (como bandeiras e emojis com tom de pele) usam múltiplos code points. Um nome com 10 caracteres visíveis excedeu o limite de 50 no backend (que contava bytes UTF-8), causando erro 500 na API.

### O Que Deu Errado
- Frontend e backend usavam métricas diferentes para "comprimento"
- Validação de comprimento não considerava Unicode multi-byte
- Testes usavam apenas caracteres ASCII
- Sem contrato explícito sobre como medir comprimento de strings

### Causa Raiz
**Contrato de validação inconsistente.** Frontend e backend não concordavam sobre como medir comprimento de strings. Edge case de Unicode é previsível e recorrente.

### Como Prevenir
1. Definir no design doc como strings são medidas (code points, grapheme clusters ou bytes)
2. Validação deve ser idêntica em frontend e backend — idealmente compartilhar a lógica
3. Incluir emojis compostos e caracteres multi-byte em dados de teste

### Checklist Atualizado
- [ ] Validações de string definem unidade de medida (bytes, code points, graphemes)?
- [ ] Validações são consistentes entre frontend e backend?
- [ ] Dados de teste incluem Unicode multi-byte e emojis compostos?

---

## Caso 4: Carrinho de Compras com Produto Removido do Catálogo

### O Que Aconteceu
Usuário adicionou produto ao carrinho. Entre a adição e o checkout (3 dias depois), o produto foi removido do catálogo. No checkout, o sistema tentou ler o preço do produto inexistente, retornou null, e o cálculo de total gerou NaN, que foi salvo como valor do pedido.

### O Que Deu Errado
- Nenhum cenário cobria produto sendo removido entre adição ao carrinho e checkout
- O carrinho referenciava o produto por ID sem snapshot dos dados
- Operação de cálculo não validava inputs null
- NaN foi aceito como valor válido pela camada de persistência

### Causa Raiz
**Janela temporal não considerada.** O design assumia que o estado entre carrinho e checkout era estável. Em sistemas assíncronos, qualquer entidade referenciada pode mudar ou desaparecer entre operações.

### Como Prevenir
1. Para qualquer referência entre entidades, definir: "o que acontece se a entidade referenciada muda ou desaparece?"
2. Implementar snapshot de dados críticos (preço, disponibilidade) no momento da adição
3. Validar invariantes antes de operações críticas (checkout, pagamento)

### Checklist Atualizado
- [ ] Referências entre entidades têm tratamento para entidade removida/modificada?
- [ ] Dados críticos são snapshotted em operações de longa duração?
- [ ] Cálculos validam inputs antes de operar (null checks, range checks)?

---

## Caso 5: Upload de Arquivo com Tamanho Zero

### O Que Aconteceu
Endpoint de upload de documentos aceitava qualquer arquivo. Um script automatizado enviou arquivo de 0 bytes. O processador de documentos entrou em loop infinito tentando extrair texto de arquivo vazio, consumindo 100% de CPU do worker por 12 horas até ser detectado.

### O Que Deu Errado
- Nenhuma validação de tamanho mínimo no upload
- Processador não tratava arquivo vazio como edge case
- Sem timeout no processamento de documentos
- Monitoramento de CPU não tinha alerta configurado

### Causa Raiz
**Inputs degenerados não testados.** Arquivo vazio, string vazia, lista vazia, zero, null — inputs degenerados são edge cases universais que deveriam estar em todo checklist de testes.

### Como Prevenir
1. Toda validação de input deve considerar: vazio, null, zero, negativo, máximo e acima do máximo
2. Todo processamento deve ter timeout explícito
3. Incluir inputs degenerados no plano de testes desde o design

### Checklist Atualizado
- [ ] Inputs degenerados (vazio, null, zero, máximo) estão no plano de testes?
- [ ] Processamentos têm timeout explícito?
- [ ] Validação rejeita inputs inválidos antes do processamento?

---

## Resumo de Padrões

| Padrão | Frequência | Impacto Médio |
|--------|------------|---------------|
| Edge case temporal (timezone, DST) | Alta | Bug recorrente, difícil de reproduzir |
| Premissa de unicidade não validada | Média | Corrupção de dados |
| Encoding/Unicode inconsistente | Média | Erros 500 esporádicos |
| Entidade referenciada desaparece | Alta | Dados inválidos em produção |
| Input degenerado não tratado | Alta | Loops, crashes, consumo de recursos |

---

## Checklist Consolidado — Identificação de Edge Cases

- [ ] Cenários temporais (timezone, DST, virada de dia/mês/ano) foram mapeados?
- [ ] Premissas sobre dados (unicidade, existência, formato) foram validadas?
- [ ] Validações são consistentes entre camadas (frontend, backend, banco)?
- [ ] Referências entre entidades tratam mudança e remoção?
- [ ] Inputs degenerados estão no plano de testes?
- [ ] Processamentos assíncronos têm timeout?
- [ ] Operações numéricas tratam null, NaN, overflow e underflow?
- [ ] Cenários de concorrência foram considerados (dois usuários, mesmo recurso)?
