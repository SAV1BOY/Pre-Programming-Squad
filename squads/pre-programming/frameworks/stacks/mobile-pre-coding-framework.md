# Mobile Pre-Coding Framework

## Título e Propósito

O **Mobile Pre-Coding Framework** é um checklist para decisões específicas de desenvolvimento mobile que devem ser tomadas antes da implementação. O propósito é endereçar as particularidades do mobile — conectividade intermitente, variedade de dispositivos, gestão de ciclo de vida do app, distribuição via stores — que diferenciam profundamente mobile de web.

## Quando Usar

- Antes de iniciar desenvolvimento de app mobile (nativo ou cross-platform)
- Em features que envolvem funcionalidades offline, push notifications, câmera, GPS
- Ao definir arquitetura de um novo app mobile
- Em migrações de plataforma (nativo → cross-platform ou vice-versa)
- Como checklist de readiness para trabalho mobile

## Conceitos-Chave

1. **Offline-First**: Projetar para funcionar sem internet e sincronizar quando conectar. Não é feature — é requisito em mobile.
2. **Ciclo de Vida do App**: Background, foreground, suspensão, terminação pelo SO. O app precisa lidar com todos os estados.
3. **Fragmentação de Dispositivos**: Telas diferentes, versões de SO diferentes, capacidades diferentes. Testar em dispositivos reais.
4. **Distribuição via Store**: Apple App Store e Google Play têm processos de review. Deploys não são instantâneos como na web.
5. **Performance em Dispositivos Limitados**: Memória, CPU e bateria são recursos escassos. Otimizar é obrigatório, não opcional.

## Processo / Passos

### Passo 1 — Definir Plataformas e Versões Mínimas
iOS mínimo, Android mínimo. Quais dispositivos são prioridade? Isso determina APIs disponíveis e performance esperada.

### Passo 2 — Definir Estratégia Offline
Quais funcionalidades funcionam offline? Como dados são armazenados localmente? Como sincronizar? Conflitos de sincronização?

### Passo 3 — Projetar para Ciclo de Vida
O que acontece quando o app vai para background? E quando volta? Dados são salvos? Sessão expira?

### Passo 4 — Definir Estratégia de Dados Locais
SQLite, Realm, CoreData, MMKV? Cache de API? Armazenamento seguro para tokens e dados sensíveis?

### Passo 5 — Planejar Performance
Startup time, tempo de renderização, uso de memória, consumo de bateria. Defina budgets.

### Passo 6 — Definir Push Notifications
Quais eventos disparam push? Formatação? Deep links? Silent push para sincronização em background?

### Passo 7 — Planejar Distribuição e Atualização
Pipeline de CI/CD para stores. Beta testing (TestFlight/Firebase Distribution). Versioning. Force update para versões críticas.

## Perguntas de Ativação

- "O que o usuário vê quando abre o app sem internet?"
- "Se o SO matar o app em background, dados não salvos são perdidos?"
- "Quais versões de SO e dispositivos precisamos suportar?"
- "Quanto tempo leva para o app iniciar a frio? É aceitável?"
- "Como vamos testar em dispositivos reais, não apenas simuladores?"
- "Qual é o processo de atualização quando encontrarmos um bug crítico em produção?"

## Output Esperado

Checklist cobrindo: plataformas e versões, estratégia offline, ciclo de vida, armazenamento local, performance budgets, push notifications, pipeline de distribuição, testes em dispositivos reais.

## Armadilhas Comuns

1. **Ignorar offline**: Desenvolver como se a internet fosse sempre estável. Em mobile, não é.
2. **Testar só em simulador**: Simuladores não replicam performance real, conectividade e comportamento de hardware.
3. **Startup lento**: App que leva 5+ segundos para abrir perde usuários. Meça e otimize.
4. **Não lidar com background**: App que perde dados ou quebra quando vai para background/foreground.
5. **Deploy como web**: Esperar que atualizações cheguem instantaneamente. Stores têm review de 24h-7 dias.
6. **Permissões agressivas**: Pedir todas as permissões no primeiro uso assusta o usuário. Peça no momento de uso.
