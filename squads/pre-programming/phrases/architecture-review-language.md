# Frases: Revisão de Arquitetura

## Contexto
Usar durante sessões de revisão de arquitetura para promover discussão construtiva, questionar decisões de forma respeitosa e garantir que o design é robusto.

## Frases-Modelo

1. "O que acontece quando esse componente fica fora do ar? Como o sistema se comporta?"

2. "Qual é o ponto único de falha nessa arquitetura? Podemos eliminá-lo ou precisamos de um plano de contingência?"

3. "Essa decisão é facilmente reversível ou estamos nos comprometendo a longo prazo? Se é longo prazo, vamos documentar bem o porquê."

4. "Como essa arquitetura se comporta com 10x o volume atual? Não que precisemos disso agora, mas quero entender o teto."

5. "Qual é o custo operacional dessa escolha? Quem vai monitorar, manter e dar suporte a isso em produção?"

6. "Se um desenvolvedor novo entrar no projeto amanhã, quanto tempo leva para entender essa arquitetura?"

7. "Estou vendo 3 decisões implícitas nesse desenho. Vamos torná-las explícitas e documentá-las."

8. "Essa é a arquitetura mais simples que resolve o problema? Se não, o que estamos ganhando com a complexidade adicional?"

9. "Já vimos esse padrão funcionar em escala similar na nossa organização, ou é a primeira vez?"

## Quando Usar
- Em sessões de revisão de arquitetura.
- Quando decisões técnicas significativas estão sendo tomadas.
- Quando o design parece complexo demais ou simples demais.

## Quando NÃO Usar
- Para microgerenciar decisões de implementação de baixo nível.
- Para criticar sem oferecer alternativas ou questionamentos construtivos.
- Quando a arquitetura já foi aprovada e está em implementação (foco em feedback para próxima vez).

## Tom Recomendado
Curioso e respeitoso. Revisão de arquitetura é um exercício colaborativo, não um tribunal. As perguntas devem ser genuínas e orientadas a melhorar o design, não a provar que está errado. Se encontrar um problema, proponha alternativas.
