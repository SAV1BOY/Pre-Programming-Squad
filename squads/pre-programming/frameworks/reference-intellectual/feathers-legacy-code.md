# Feathers: Trabalhar com Legado sem Medo

## Título e Propósito

Framework baseado no trabalho de **Michael Feathers** (*Working Effectively with Legacy Code*). A tese central: **legacy code é simplesmente código sem testes** — e a habilidade mais importante é criar pontos de entrada para testes em código existente sem quebrá-lo. O propósito é desmistificar o trabalho com legado e torná-lo metódico em vez de aterrorizante.

## Quando Usar

- Quando a equipe precisa modificar código que não tem testes
- Em projetos de refatoração ou modernização de sistemas existentes
- Quando há medo de "mexer" em código antigo por falta de confiança
- Para planejar como tornar código legado testável incrementalmente
- Ao estimar esforço de mudanças em código desconhecido

## Conceitos-Chave

1. **Legado = Código sem Testes**: Não é sobre idade ou tecnologia. É sobre ausência de rede de segurança.
2. **Seam (Costura)**: Ponto no código onde comportamento pode ser alterado sem modificar o código em si. Essencial para injetar testes.
3. **Characterization Test**: Teste que documenta o comportamento atual, mesmo que "errado". É a rede de segurança para mudanças.
4. **Sprout Method/Class**: Técnica para adicionar novo comportamento em código novo e testável, conectando ao legado com mínima alteração.
5. **Edit and Pray vs. Cover and Modify**: Sem testes, mudanças são "edit and pray" (rezar para não quebrar). Com testes, são "cover and modify" (cobrir e modificar com confiança).

## Processo / Passos

### Passo 1 — Identificar o Que Precisa Mudar
Defina com precisão qual comportamento vai ser alterado, adicionado ou removido.

### Passo 2 — Encontrar Seams
Identifique pontos onde testes podem ser injetados: interfaces, pontos de injeção de dependência, métodos que podem ser overridden.

### Passo 3 — Escrever Characterization Tests
Antes de mudar qualquer coisa, escreva testes que capturam o comportamento atual. Se o teste falhar, você sabe que algo mudou.

### Passo 4 — Fazer a Mudança com Segurança
Com testes de caracterização como rede de segurança, faça a mudança. Se testes de caracterização falharem inesperadamente, investigue.

### Passo 5 — Adicionar Testes para o Novo Comportamento
O novo comportamento deve ter seus próprios testes. Isso melhora a cobertura incrementalmente.

## Perguntas de Ativação

- "Esse código tem testes? Se não, qual é o primeiro passo antes de mudá-lo?"
- "Onde estão os seams nesse código? Podemos injetar testes?"
- "Se eu mudar isso e algo quebrar, como vou saber?"
- "Quais testes de caracterização precisamos antes de tocar nesse código?"
- "Estamos fazendo 'edit and pray' ou 'cover and modify'?"

## Output Esperado

Mapeamento de seams no código legado, plano de characterization tests, estratégia de modificação segura, estimativa de esforço para tornar o código testável.

## Armadilhas Comuns

1. **Mudar sem testar**: A tentação de "só fazer a mudança" sem testes. Funciona até quebrar algo invisível.
2. **Rewrite em vez de refactor**: A tentação de reescrever do zero em vez de melhorar incrementalmente. Quase sempre mais arriscado.
3. **Testes de caracterização ignorados**: "Vou testar depois" — depois nunca chega.
4. **Seams forçados**: Criar seams que distorcem o código em vez de encontrar pontos naturais.
5. **Medo paralisante**: O código é tão frágil que ninguém quer tocá-lo. Characterization tests são o antídoto.
