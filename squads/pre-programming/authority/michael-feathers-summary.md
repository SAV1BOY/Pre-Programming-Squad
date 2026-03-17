# Michael Feathers — Resumo de Autoridade

## Autor

**Nome**: Michael Feathers
**Afiliação**: Consultor de software, ex-Object Mentor (com Robert Martin)
**Obra Principal**: "Working Effectively with Legacy Code" (Prentice Hall, 2004)
**Área de Expertise**: Código legado, refactoring sob restrições, estratégias de teste para código existente

---

## Tese Central

**Código legado é código sem testes.** Não importa se foi escrito ontem ou há 20 anos — se não tem testes, é legado. O desafio central de trabalhar com código legado é que para refatorar com segurança você precisa de testes, mas para adicionar testes você frequentemente precisa refatorar. Feathers fornece técnicas práticas para quebrar esse ciclo e introduzir mudanças seguras em código aparentemente intocável.

---

## Conceitos-Chave

### 1. O Dilema do Legado
Para mudar código com segurança, precisamos de testes. Para colocar testes, frequentemente precisamos mudar o código. Feathers oferece técnicas para fazer mudanças mínimas e seguras que permitem adicionar testes sem alterar comportamento.

### 2. Seams (Costuras)
Um seam é um ponto no código onde você pode alterar o comportamento sem modificar o código em si. Tipos:
- **Object Seam**: Substituir implementação via polimorfismo ou injeção de dependência
- **Preprocessor Seam**: Compilação condicional
- **Link Seam**: Substituir implementação no nível de linking

Identificar seams é o primeiro passo para testabilidade.

### 3. Characterization Tests
Testes que documentam o comportamento atual do código — não o comportamento desejado. São a rede de segurança que permite refatoração. "O que o código faz?" em vez de "O que o código deveria fazer?"

### 4. Sprout Method/Class
Quando não é seguro alterar código existente, criar novo código (method ou class) ao lado. O código existente delega para o novo. O novo é testável desde o início.

### 5. The Seam Model
Modelo mental para identificar onde é possível inserir testes em código acoplado. Toda base de código, por mais acoplada que seja, tem seams que podem ser explorados.

---

## Aplicação ao Squad

- **Avaliação de legado como etapa da pré-programação**: Antes de planejar integração com código existente, o squad deve avaliar: tem testes? Onde estão os seams? Qual o custo de torná-lo testável?

- **Characterization tests antes de mudanças**: Quando o projeto envolve modificar código existente, o plano de testes deve incluir uma fase de characterization tests — documentar o comportamento atual antes de alterá-lo.

- **Mapa de seams no design doc**: Para projetos que integram com legado, identificar seams disponíveis e documentá-los. Isso informa o time de dev sobre onde é seguro fazer mudanças.

- **Estratégia de sprout no handoff**: Quando a integração com legado é arriscada, recomendar sprout method/class como padrão — novo código testável ao lado do legado, com mínima modificação do existente.

- **Registro de impacto em legado**: Usar o legacy-impact-registry para documentar cada ponto de contato com código legado, incluindo presença/ausência de testes e seams identificados.

---

## Citações Relevantes

> "To me, legacy code is simply code without tests."

> "Code without tests is bad code. It doesn't matter how well written it is; it doesn't matter how pretty or object-oriented or well-encapsulated it is."

> "When we change code, we should have tests in place. To put tests in place, we often have to change code."

> "A seam is a place where you can alter behavior in your program without editing in that place."

> "The first step to making legacy code manageable is to understand it. The second step is to get it under test. Everything else follows."
