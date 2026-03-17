# Integration Pressure Map

## Título e Propósito

O **Integration Pressure Map** é um framework para visualizar e gerenciar as pressões de integração entre sistemas — internos e externos. O propósito é antecipar pontos de tensão nas integrações antes que se tornem gargalos ou pontos de falha, mapeando onde a "pressão" (volume, complexidade, acoplamento, fragilidade) é maior e projetando alívio.

## Quando Usar

- Ao projetar sistema que se integra com múltiplos serviços externos
- Quando integrações existentes estão causando instabilidade
- Na avaliação de arquitetura de sistemas distribuídos
- Ao adicionar nova integração a um sistema existente
- Em revisões de incidentes causados por falhas de integração

## Conceitos-Chave

1. **Pressão de Integração**: A combinação de fatores que tornam uma integração problemática: volume, latência, confiabilidade, complexidade de dados, frequência de mudanças.
2. **Ponto de Pressão**: Local onde múltiplas integrações convergem ou onde a pressão é desproporcionalmente alta.
3. **Contrapressão (Backpressure)**: A capacidade de um sistema comunicar ao chamador que está sobrecarregado e pedir redução de carga.
4. **Acoplamento Temporal**: Quando dois sistemas precisam estar disponíveis ao mesmo tempo para funcionar. Quanto mais síncrono, mais acoplado.
5. **Tolerância a Falha**: A capacidade de uma integração continuar funcionando (degradada) quando o outro lado falha.

## Processo / Passos

### Passo 1 — Mapear Todas as Integrações
Liste todas as integrações do sistema: APIs consumidas, APIs expostas, bancos compartilhados, filas, webhooks, arquivos, ETL.

### Passo 2 — Para Cada Integração, Avaliar Pressões
Avalie cada fator de 1 (baixo) a 5 (crítico):
- Volume de chamadas
- Sensibilidade a latência
- Confiabilidade do parceiro
- Complexidade de dados
- Frequência de mudanças do contrato
- Criticidade para o negócio

### Passo 3 — Identificar Pontos de Pressão
Onde a soma das pressões é mais alta? Onde múltiplas integrações convergem? Esses são os pontos que precisam de atenção.

### Passo 4 — Avaliar Mecanismos de Alívio Existentes
Para cada ponto de pressão, verifique: há retry? Circuit breaker? Timeout? Cache? Fila? Fallback? O que falta?

### Passo 5 — Projetar Alívio para Pontos Críticos
Para pontos de pressão sem alívio adequado, projete: desacoplamento temporal (fila), cache de respostas, circuit breaker, fallback, bulkhead.

### Passo 6 — Definir Contratos e SLAs
Para cada integração crítica, defina: SLA esperado, timeout, retry policy, formato de dados, versionamento.

### Passo 7 — Monitorar Pressão
Instrumente cada integração para medir: latência, taxa de erro, throughput, disponibilidade. Detecte aumento de pressão antes da falha.

## Perguntas de Ativação

- "Se essa integração cair por 1 hora, o que para de funcionar?"
- "Quantas chamadas por segundo fazemos para esse sistema? E ele aguenta?"
- "Temos backpressure implementado ou vamos sobrecarregar o parceiro?"
- "Qual integração nos causou mais incidentes nos últimos 6 meses?"
- "Se o formato dos dados dessa API mudar sem aviso, estamos protegidos?"
- "Podemos funcionar (degradado) se essa integração estiver indisponível?"

## Output Esperado

| Integração | Direção | Volume | Latência | Confiabilidade | Complexidade | Mudanças | Criticidade | Pressão Total | Alívio |
|---|---|---|---|---|---|---|---|---|---|
| Gateway Pagamento | Outbound | 4 | 5 | 3 | 3 | 2 | 5 | **22** | Circuit breaker + retry + fallback para fila |
| API de CEP | Outbound | 3 | 2 | 2 | 1 | 1 | 2 | **11** | Cache local de 7 dias |
| Webhook de parceiro | Inbound | 4 | 3 | 2 | 4 | 4 | 3 | **20** | Validação + idempotência + fila de processamento |
| ERP Legado | Bidirectional | 2 | 4 | 1 | 5 | 3 | 4 | **19** | ACL + retry + monitoramento específico |

**Pontos de pressão críticos**: Gateway Pagamento (22), Webhook parceiro (20), ERP Legado (19).

## Armadilhas Comuns

1. **Integração como detalhe**: Tratar integrações como "detalhes de implementação" quando são frequentemente os pontos mais frágeis do sistema.
2. **Confiança no parceiro**: Assumir que a API externa "sempre funciona" sem projetar para falha.
3. **Sem contrapressão**: Enviar carga máxima sem considerar se o parceiro aguenta. Pode causar throttling ou blacklist.
4. **Acoplamento síncrono desnecessário**: Fazer chamada síncrona quando assíncrona seria mais resiliente.
5. **Não versionar contratos**: Mudanças no contrato quebram integrações. Versione desde o início.
6. **Monitorar apenas o próprio sistema**: Se a integração falha no lado do parceiro, seus dashboards não vão mostrar — monitore a interface.
