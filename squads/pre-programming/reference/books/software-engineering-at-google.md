# Software Engineering at Google

## Informações Gerais

- **Titulo:** Software Engineering at Google: Lessons Learned from Programming Over Time
- **Autores:** Titus Winters, Tom Manshreck, Hyrum Wright
- **Ano:** 2020

## Tese Central

Engenharia de software e programacao integrada ao longo do tempo. A diferenca entre "programacao" e "engenharia de software" e a dimensao temporal: engenharia de software deve considerar as mudancas que o codigo sofrera ao longo de anos ou decadas. Decisoes de design, processos e ferramentas devem ser avaliados pelo custo total ao longo do tempo, nao apenas pelo custo imediato.

## Conceitos-Chave para Pre-Programacao

### 1. Software Engineering vs. Programming
Programacao e escrever codigo. Engenharia de software e escrever codigo + tempo + escala + trade-offs. Na pre-programacao, essa distinção e fundamental: estamos avaliando se as decisoes de design sobreviverao ao tempo.

### 2. A Lei de Hyrum (Hyrum's Law)
"Com um numero suficiente de usuarios de uma API, todos os comportamentos observaveis do sistema serao dependidos por alguem." Na pre-programacao, isso significa que contratos de API devem ser definidos com extremo cuidado, pois qualquer comportamento implícito se torna um contrato de fato.

### 3. Shifting Left
Mover a detecção de problemas para o inicio do ciclo de desenvolvimento. A pre-programacao e, por definicao, a aplicacao maxima do shifting left: identificar problemas antes de escrever qualquer codigo.

### 4. Code Review como Pilar
Code review nao e apenas sobre encontrar bugs, mas sobre disseminar conhecimento, manter consistencia e garantir legibilidade. Na pre-programacao, design reviews cumprem papel analogo.

### 5. Deprecation e Gerenciamento de Mudanca
Sistemas precisam evoluir. A capacidade de deprecar e remover funcionalidades e tao importante quanto a capacidade de adiciona-las. Na pre-programacao, planejar a evolucao e deprecacao futura.

### 6. Testing em Escala
O Google testa em multiplos niveis: unitario, integracao, end-to-end. A piramide de testes e rigorosamente mantida. Na pre-programacao, a estrategia de testes deve ser definida antes da implementacao.

### 7. Documentacao como Codigo
Tratar documentacao com o mesmo rigor do codigo: versionada, revisada, testada. Design docs sao artefatos de primeira classe.

## Como Aplicar no Squad

### Na Cultura de Design Docs
- Adotar o formato de design doc do Google como template base.
- Incluir secoes obrigatorias: Contexto, Objetivos, Design, Alternativas, Riscos.
- Exigir revisao por pares de todos os design docs.
- Tratar design docs como documentos vivos que evoluem.

### Na Avaliacao de Trade-offs Temporais
- Para cada decisao de design, perguntar: "Como isso se comporta em 2 anos? Em 5 anos?"
- Aplicar a Lei de Hyrum: "Quais comportamentos implicitos podem se tornar dependencias?"
- Avaliar o custo de mudanca futura de cada decisao.

### Na Definicao de Processos
- Estabelecer design review como gate obrigatorio antes da implementacao.
- Definir niveis de revisao baseados no impacto da mudanca (similar ao sistema de design doc levels do Google).
- Implementar mecanismos de feedback loop entre design e implementacao.

### Na Estrategia de Testes
- Definir a estrategia de testes na fase de pre-programacao.
- Especificar quais tipos de testes sao necessarios para cada componente.
- Planejar infraestrutura de testes como parte do design.

## Citacoes Importantes

> "Software engineering is programming integrated over time."

> "With a sufficient number of users of an API, it does not matter what you promise in the contract: all observable behaviors of your system will be depended on by somebody."

> "The most important decisions in software engineering are not technical decisions, they are social ones."

> "We've found that expertise and shared communication forums offer great value as a way to manage complexity."

> "If you liked it, you should have put a test on it."

## Relacao com Outros Livros de Referencia

- **Accelerate:** Complementa com metricas quantitativas (DORA) que validam as praticas do Google.
- **Continuous Delivery:** As praticas de CI/CD do Google sao uma implementacao em escala dos principios de Humble/Farley.
- **Team Topologies:** A organizacao de equipes do Google pode ser analisada pelo framework de topologias.
