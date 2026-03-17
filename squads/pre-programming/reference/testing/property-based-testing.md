# Property-Based Testing

## O que e Property-Based Testing

Property-based testing (PBT) e uma tecnica de teste onde, em vez de especificar exemplos concretos de input/output, voce define propriedades que devem ser verdadeiras para qualquer input valido. O framework gera automaticamente centenas ou milhares de inputs aleatorios e verifica se a propriedade se mantem. Quando encontra uma falha, reduz automaticamente o input ao caso minimo que reproduz o bug (shrinking).

## Diferenca entre Testes Baseados em Exemplos e Propriedades

### Teste Baseado em Exemplo (tradicional)
```
Dado: input = [3, 1, 2]
Quando: sort(input)
Entao: resultado = [1, 2, 3]
```
Testa um caso especifico. O desenvolvedor escolhe os inputs.

### Teste Baseado em Propriedade
```
Para qualquer lista de inteiros 'xs':
  sort(xs) deve ter o mesmo comprimento que xs
  sort(xs) deve ter todos os elementos de xs
  cada elemento de sort(xs) deve ser <= ao proximo
```
Testa propriedades universais. O framework gera inputs.

## Tipos de Propriedades

### 1. Invariantes
Algo que e sempre verdadeiro independente do input.
- "O resultado de sort() sempre esta ordenado."
- "O saldo de uma conta nunca e negativo."
- "O total de um pedido e sempre >= 0."

### 2. Ida e Volta (Round-trip)
serialize(deserialize(x)) == x
- "Codificar e decodificar JSON preserva os dados."
- "Encriptar e decriptar retorna a mensagem original."
- "Converter para moeda e voltar preserva o valor."

### 3. Modelo de Referencia
Comparar implementacao otimizada com implementacao simples de referencia.
- "quicksort(xs) == bubblesort(xs)" (mesmo resultado, performance diferente).
- "cache.get(k) == database.get(k)" (cache consistente com banco).

### 4. Idempotencia
Aplicar a operacao duas vezes produz o mesmo resultado.
- "normalizar um email ja normalizado nao muda nada."
- "aplicar migracao ja aplicada nao altera dados."

### 5. Comutatividade / Associatividade
- "A + B == B + A" (comutatividade).
- "(A + B) + C == A + (B + C)" (associatividade).
- Merge de dois conjuntos de dados independente da ordem.

## Ferramentas por Linguagem

| Linguagem | Frameworks |
|---|---|
| Haskell | QuickCheck (original) |
| Python | Hypothesis |
| JavaScript/TypeScript | fast-check |
| Java/Kotlin | jqwik |
| Scala | ScalaCheck |
| Rust | proptest |
| Go | gopter |
| C# | FsCheck |

## Aplicacao na Pre-Programacao

### Identificar Propriedades no Design
Durante a pre-programacao, ao definir regras de negocio, identificar propriedades que devem ser sempre verdadeiras:

**Exemplo: Sistema de Precificacao**
- "O preco final nunca e negativo."
- "Aplicar desconto X% e depois desconto Y% == aplicar desconto combinado (1-X%)(1-Y%)."
- "O preco com desconto e sempre <= preco original."
- "Frete gratis acima de R$99: se total >= 99, frete == 0."

**Exemplo: Sistema de Permissoes**
- "Um usuario sem role nao tem nenhuma permissao."
- "Adicionar e remover a mesma permissao nao muda nada (round-trip)."
- "Permissoes de admin sao superset de permissoes de usuario."

### Incluir Propriedades nos Criterios de Aceitacao
Em vez de (ou alem de) exemplos concretos, documentar propriedades:
```markdown
## Criterios de Aceitacao: Calculo de Impostos

### Propriedades
- Para qualquer produto e qualquer estado, o imposto e >= 0.
- O imposto nunca excede 50% do valor do produto.
- Para o mesmo produto e estado, o imposto e deterministico.
- Isencao de imposto: se produto.categoria == 'cesta_basica', imposto == 0.
```

### No Design Doc
Incluir secao de propriedades testáveis:
```markdown
## Propriedades do Sistema

### Invariantes de Negocio
- Saldo de conta >= 0 (P0 - critico).
- Soma de parcelas == valor total do pedido (P0 - critico).
- Data de entrega estimada > data do pedido (P0 - critico).

### Round-trips
- Serialize/deserialize de todas as entidades de dominio.
- Encode/decode de tokens de autenticacao.

### Idempotencia
- Processamento de pagamento e idempotente (retry seguro).
- Consumo de eventos e idempotente.
```

## Quando Property-Based Testing e Mais Valioso

- **Parsing/serialização:** Round-trip properties.
- **Calculos financeiros:** Invariantes de nao-negatividade, consistencia.
- **Algoritmos:** Corretude, invariantes de ordenacao, preservacao de dados.
- **Stateful systems:** Model-based testing (comparar com modelo simplificado).
- **Migracoes de dados:** Dados migrados preservam invariantes.

## Quando NAO Usar Property-Based Testing

- **UI testing:** Propriedades de UI sao dificeis de definir automaticamente.
- **Testes de integracao com terceiros:** Inputs aleatorios podem causar problemas.
- **Logica trivial:** Overhead nao justificado para getters/setters simples.
