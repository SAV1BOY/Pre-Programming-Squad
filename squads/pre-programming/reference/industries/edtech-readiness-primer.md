# EdTech - Readiness Primer

## Contexto da Industria

EdTech abrange tecnologia para educacao: plataformas de ensino online (LMS), cursos online, EdTech K-12, ensino superior digital, educacao corporativa (L&D), tutoring, assessment e certificacao. No Brasil, o mercado cresceu significativamente com EAD regulamentado, ENADE digital, e demanda corporativa por upskilling. O setor combina requisitos pedagogicos com desafios tecnicos de escala e acessibilidade.

## Desafios Especificos de Pre-Programacao

### Picos de Acesso Simultaneo
Aulas ao vivo, provas e entregas de trabalho geram picos previsíveis mas intensos. Uma turma de 500 alunos acessando prova as 8h gera spike concentrado. Na pre-programacao, modelar picos por tipo de evento educacional.

### Conteudo Multimidia
Video (aulas gravadas, lives), audio, documentos, quizzes interativos, simulacoes. Armazenamento, transcoding, CDN, streaming adaptativo. Na pre-programacao, a estrategia de conteudo multimidia impacta custo e experiencia.

### Acessibilidade
Educacao deve ser inclusiva. WCAG 2.1 AA como minimo: leitores de tela, legendas em videos, contraste adequado, navegacao por teclado. No Brasil, a Lei Brasileira de Inclusao (13.146/2015) exige acessibilidade digital.

### Integridade Academica
Prevencao de cola em avaliacoes online: proctoring, randomizacao de questoes, time limits, deteccao de plagio. Na pre-programacao, a estrategia de integridade academica afeta o design de assessment.

### Rastreabilidade de Progresso
Horas de estudo, conclusao de modulos, notas, certificacao. Padroes como xAPI (Experience API) e LTI (Learning Tools Interoperability) para integracao entre sistemas educacionais.

## Regulacoes Relevantes

| Regulacao | Escopo | Impacto no Design |
|---|---|---|
| MEC / Portarias EAD | Ensino a distancia | Requisitos de polos, avaliacao presencial, carga horaria |
| LGPD | Dados de alunos (menores inclusos) | Consentimento parental para menores, dados escolares |
| Lei de Inclusao (13.146/2015) | Acessibilidade | WCAG 2.1 AA, conteudo acessivel |
| ENADE/INEP | Avaliacao institucional | Integracao com sistemas do MEC |
| LTI / xAPI / SCORM | Interoperabilidade | Padroes de integracao entre ferramentas educacionais |

## Padroes de Readiness

### Checklist de Pre-Programacao para EdTech

**Experiencia de Aprendizagem:**
- [ ] Fluxo pedagogico mapeado com educadores.
- [ ] Tipos de conteudo definidos (video, texto, quiz, simulacao).
- [ ] Estrategia de gamificacao definida (se aplicavel).
- [ ] Metricas de engajamento e aprendizagem definidas.

**Conteudo e Midia:**
- [ ] Estrategia de armazenamento e CDN para video.
- [ ] Transcoding e streaming adaptativo planejados.
- [ ] Legendas e transcricoes para acessibilidade.
- [ ] Limites de upload e formatos suportados definidos.

**Escalabilidade:**
- [ ] Picos de acesso modelados por tipo de evento (prova, aula, entrega).
- [ ] Estrategia de streaming para aulas ao vivo (WebRTC, HLS).
- [ ] Auto-scaling para periodos de prova/matricula.

**Assessment e Integridade:**
- [ ] Estrategia de avaliacao definida (quizzes, provas, projetos).
- [ ] Randomizacao de questoes e alternativas planejada.
- [ ] Proctoring remoto avaliado (se necessario).
- [ ] Deteccao de plagio planejada (se aplicavel).

**Acessibilidade:**
- [ ] WCAG 2.1 AA como requisito de design.
- [ ] Acessibilidade de player de video (legendas, controle por teclado).
- [ ] Testes de acessibilidade planejados com leitores de tela.

**Interoperabilidade:**
- [ ] Padroes LTI/xAPI/SCORM avaliados.
- [ ] Integracao com LMS existentes planejada (se B2B).
- [ ] Export de dados academicos (boletins, certificados).

## Riscos Tipicos

1. **Plataforma indisponivel durante prova:** Alunos perdem avaliacao, crise institucional.
2. **Falha em streaming de aula ao vivo:** Perda de aula, insatisfacao massiva.
3. **Vazamento de dados de menores:** LGPD agravada, repercussao publica severa.
4. **Fraude em avaliacao:** Desvalorizacao de certificacoes, perda de credibilidade.
5. **Inacessibilidade:** Exclusao de alunos com deficiencia, violacao legal.
6. **Perda de conteudo:** Professor perde material criado ao longo de anos.
