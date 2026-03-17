# Healthcare - Readiness Primer

## Contexto da Industria

Healthtech e health IT abrangem prontuarios eletronicos (PEP/EHR), telemedicina, agendamento, gestao hospitalar, wearables de saude, clinical decision support e pesquisa clinica. No Brasil, o setor e regulado pela ANVISA, CFM, ANS e opera sob a LGPD com restricoes especiais para dados sensiveis de saude. A pandemia acelerou a adocao de telemedicina e digitalizacao, mas os desafios de interoperabilidade e seguranca permanecem.

## Desafios Especificos de Pre-Programacao

### Dados Sensiveis de Saude
Dados de saude sao classificados como dados sensiveis pela LGPD (art. 11), exigindo protecao adicional. Prontuarios medicos tem sigilo profissional protegido por lei. Na pre-programacao, o mapeamento de dados sensiveis e as bases legais de tratamento devem ser o ponto de partida.

### Interoperabilidade e Padroes
O setor de saude tem padroes complexos: HL7 FHIR para troca de dados clinicos, DICOM para imagens medicas, TISS (Troca de Informacao em Saude Suplementar) para operadoras de saude no Brasil, ICD-10/CID-10 para classificacao de diagnosticos. Na pre-programacao, identificar quais padroes se aplicam e planejar conformidade.

### Disponibilidade Critica
Em saude, indisponibilidade pode ter consequencias para a vida do paciente. Sistemas de emergencia, UTI e centro cirurgico exigem disponibilidade maxima. Na pre-programacao, classificar criticidade por contexto de uso clinico.

### Validacao Clinica
Funcionalidades que influenciam decisoes clinicas (dosagem de medicamentos, alertas de interacao, suporte a diagnostico) requerem validacao com profissionais de saude e, em alguns casos, aprovacao regulatoria (ANVISA classe de risco).

### Rastreabilidade e Auditoria
Quem acessou qual prontuario, quando, por que. Modificacoes devem ser rastreaveis e nao deletaveis. Na pre-programacao, audit log imutavel e requisito fundamental.

## Regulacoes Relevantes

| Regulacao | Escopo | Impacto no Design |
|---|---|---|
| LGPD (dados sensiveis) | Dados de saude | Consentimento especifico, encriptacao, DPO |
| CFM Res. 1821/2007 | Prontuario eletronico | Retencao 20 anos, sigilo, assinatura digital |
| CFM Res. 2314/2022 | Telemedicina | Requisitos de conectividade, consentimento, registro |
| ANVISA | Software como dispositivo medico | Classificacao de risco, registro, validacao |
| ANS/TISS | Saude suplementar | Formato de troca de dados, autorizacoes |
| HL7 FHIR / RNDS | Interoperabilidade | APIs padronizadas, Rede Nacional de Dados em Saude |

## Padroes de Readiness

### Checklist de Pre-Programacao para Healthcare

**Regulatorio:**
- [ ] Classificacao ANVISA do software definida (se aplicavel).
- [ ] Requisitos de CFM para prontuario eletronico mapeados.
- [ ] LGPD: dados sensiveis de saude mapeados com bases legais.
- [ ] Requisitos de TISS/ANS mapeados (se saude suplementar).

**Interoperabilidade:**
- [ ] Padroes aplicaveis identificados (FHIR, TISS, DICOM, CID-10).
- [ ] Integracao com RNDS planejada (se aplicavel).
- [ ] Formatos de troca de dados definidos.

**Seguranca e Privacidade:**
- [ ] Controle de acesso baseado em papel clinico (RBAC).
- [ ] Audit log imutavel para acesso a prontuarios.
- [ ] Encriptacao de dados de saude em transito e repouso.
- [ ] Consentimento do paciente gerenciado.
- [ ] Backup e retencao de prontuarios por 20 anos.

**Disponibilidade:**
- [ ] Criticidade clinica de cada funcionalidade classificada.
- [ ] Modo offline para funcionalidades criticas (emergencia).
- [ ] SLOs definidos por nivel de criticidade clinica.
- [ ] Plano de contingencia manual documentado.

**Validacao Clinica:**
- [ ] Funcionalidades de suporte a decisao clinica validadas com medicos.
- [ ] Calculo de dosagem revisado por farmaceuticos.
- [ ] Alertas clinicos (interacoes, alergias) validados.

## Riscos Tipicos

1. **Risco a vida do paciente:** Dado incorreto, sistema indisponivel em emergencia, dosagem errada.
2. **Vazamento de dados de saude:** LGPD agravada, dano irreparavel ao paciente, processos.
3. **Nao conformidade regulatoria:** ANVISA, CFM, ANS podem suspender operacao.
4. **Interoperabilidade falha:** Dados nao chegam ao medico no momento critico.
5. **Perda de prontuario:** Violacao de retencao obrigatoria de 20 anos.
6. **Fadiga de alertas clinicos:** Excesso de alertas falsos leva profissionais a ignorar alertas reais.
