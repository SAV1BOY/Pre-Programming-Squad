# Brasil e America Latina - Contexto de Readiness

## Contexto Regional

O desenvolvimento de software no Brasil e America Latina opera em um contexto unico que combina: complexidade tributaria extrema, infraestrutura de internet heterogenea, diversidade de dispositivos e conectividade, regulamentacoes em rapida evolucao (Pix, Open Finance, LGPD), e particularidades culturais e operacionais que impactam decisoes de design. Ignorar esse contexto na pre-programacao e receita para fracasso.

## Desafios Especificos de Pre-Programacao

### 1. Complexidade Tributaria Brasileira
O sistema tributario brasileiro e um dos mais complexos do mundo. ICMS varia por estado e tipo de produto, com substituicao tributaria. ISS varia por municipio. PIS/COFINS com regimes cumulativo e nao-cumulativo. IPI por NCM. Reforma tributaria em andamento (IBS, CBS) adiciona incerteza.

**Impacto no design:**
- Motor de calculo tributario deve ser flexivel e atualizavel sem deploy.
- Tabelas de aliquotas devem ser configuráveis, nao hard-coded.
- Integracoes com SEFAZ para NF-e, NFS-e, CT-e.
- Planejar para mudancas frequentes na legislacao fiscal.

### 2. Pix e Meios de Pagamento Locais
Pix e o meio de pagamento dominante no Brasil. Boleto bancario ainda e relevante. Parcelamento sem juros e expectativa cultural. Diferentes adquirentes e bandeiras.

**Impacto no design:**
- Integrar Pix como metodo primario, nao como alternativa.
- Suportar boleto com tratamento de vencimento e baixa.
- Motor de parcelamento com regras flexiveis.
- Integracao com multiplos PSPs (Payment Service Providers).
- Pix Cobranca, Pix Garantido (quando disponivel), QR Code.

### 3. Infraestrutura de Internet Heterogenea
Conexoes variam de fibra 500Mbps em capitais a 3G instavel em areas rurais. Mobile-first: ~60% do trafego brasileiro e mobile. Pacotes de dados limitados sao comuns.

**Impacto no design:**
- Progressive Web Apps e offline-first para cenarios de conectividade ruim.
- Otimizacao de payload (compressao, lazy loading, image optimization).
- Considerar uso de dados moveis (evitar downloads desnecessarios).
- Testar em condicoes de rede degradada (3G, alta latencia).

### 4. Diversidade de Dispositivos
Predominancia de Android (85%+ no Brasil). Dispositivos de entrada com pouca memoria e processamento limitado. Telas de diversos tamanhos.

**Impacto no design:**
- Testar em dispositivos Android de entrada (2GB RAM, processador lento).
- Responsividade real, nao apenas para desktop e iPhone.
- Considerar limites de armazenamento local.

### 5. LGPD (Lei Geral de Protecao de Dados)
A LGPD (Lei 13.709/2018) e a regulamentacao brasileira de protecao de dados, similar ao GDPR europeu. Exige bases legais para tratamento de dados, consentimento quando necessario, direitos do titular (acesso, correcao, exclusao, portabilidade), e reportagem de incidentes a ANPD.

**Impacto no design:**
- Mapeamento de dados pessoais no design doc.
- Consentimento gerenciado por sistema.
- Mecanismos de anonimizacao e pseudonimizacao.
- Direito ao esquecimento implementavel (soft delete ou hard delete conforme base legal).
- Data residency: dados no Brasil quando exigido.

### 6. Fusos Horarios e Regionalizacao
Brasil tem 4 fusos horarios. Horario de verao foi extinto mas sistemas legados ainda podem referencia-lo. Formatacao de datas (DD/MM/YYYY), moeda (R$ com virgula decimal), enderecos (CEP, logradouro, bairro).

**Impacto no design:**
- Armazenar timestamps em UTC, converter para exibicao.
- Formatacao de moeda brasileira (R$ 1.234,56).
- Validacao de CEP e integracao com APIs de endereco (ViaCEP).
- Validacao de CPF/CNPJ com algoritmo de verificacao.

### 7. Open Finance Brasil
Regulado pelo Banco Central, o Open Finance permite compartilhamento de dados financeiros entre instituicoes com consentimento do cliente. APIs padronizadas, certificacoes obrigatorias, jornada de consentimento regulamentada.

**Impacto no design:**
- APIs conforme especificacao do Open Finance Brasil.
- Gerenciamento de consentimento conforme regulacao.
- Certificados de segurança (mTLS, FAPI).
- Monitoramento de SLAs regulatorios.

## Padroes de Readiness para Brasil/LATAM

### Checklist de Pre-Programacao

**Fiscal e Tributario:**
- [ ] Regras tributarias aplicaveis mapeadas (ICMS, ISS, PIS/COFINS, IPI).
- [ ] Motor de calculo tributario planejado (configuravel, atualizavel).
- [ ] Integracao com SEFAZ para documentos fiscais.
- [ ] Plano para mudancas na reforma tributaria.

**Pagamentos:**
- [ ] Pix integrado como metodo primario.
- [ ] Boleto com tratamento de vencimento e baixa.
- [ ] Parcelamento sem juros no cartao.
- [ ] Integracao com PSP definida.

**Conectividade e Dispositivos:**
- [ ] Performance testada em 3G e dispositivos de entrada.
- [ ] Estrategia offline-first definida (se aplicavel).
- [ ] Otimizacao de payloads e imagens.
- [ ] Android como plataforma primaria de teste.

**LGPD:**
- [ ] Dados pessoais mapeados com bases legais.
- [ ] Consentimento gerenciado por sistema.
- [ ] Direitos do titular implementaveis (acesso, exclusao, portabilidade).
- [ ] Data residency no Brasil quando exigido.

**Localizacao:**
- [ ] Formatacao brasileira (datas, moeda, enderecos).
- [ ] Validacao de CPF/CNPJ.
- [ ] Integracao com ViaCEP ou equivalente.
- [ ] Timestamps em UTC com conversao para fusos brasileiros.

## Riscos Tipicos da Regiao

1. **Nao conformidade fiscal:** Multa da Receita Federal, bloqueio de operacao.
2. **LGPD violation:** Multas de ate 2% do faturamento, limitado a R$50M por infracao.
3. **Exclusao de usuarios com conectividade ruim:** Perda de mercado significativa.
4. **Erro tributario:** Calculo incorreto de impostos, passivo fiscal.
5. **Nao suportar Pix:** Perda de conversao (Pix e preferencia de 70%+ dos brasileiros).
6. **Ignorar Android de entrada:** Experiencia degradada para maioria dos usuarios.
