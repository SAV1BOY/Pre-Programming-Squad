# Feature Mobile — Fase 06: Testes

## Objetivo da Fase

Definir estratégia de testes mobile abrangendo: testes em dispositivos reais, cenários de conectividade, lifecycle, performance e acessibilidade.

## Agentes Envolvidos

- **Agente de Testes** (líder da fase) — Desenha estratégia de testes mobile
- **Agente de Riscos** — Garante cobertura de cenários de risco mobile

## Inputs

- Arquitetura mobile (Fase 04)
- Device matrix (Fase 05)
- Performance targets (Fase 03)
- Cenários de conectividade (Fase 02)

## Atividades

1. **Definir testes unitários e de integração** — Business logic testada com testes unitários. Integração com camada de dados local. Mock de networking para testes rápidos.
2. **Planejar testes de dispositivo** — Selecionar device matrix (mínimo 10 dispositivos): iPhones (SE, padrão, Pro Max), Android (Samsung, Pixel, Xiaomi, low-end). Testcontainers ou farm de dispositivos.
3. **Planejar testes de conectividade** — Cenários: online → offline → online (sync), início offline (cache), 3G lento (timeout handling), perda de conexão durante operação.
4. **Planejar testes de lifecycle** — App backgrounds durante operação, app é terminada pelo OS, rotação de tela, split screen, picture-in-picture. Estado é preservado?
5. **Planejar testes de performance** — App launch cold/warm, time to interactive, scroll performance (60fps), memória peak, tamanho do app. Comparar com targets.
6. **Planejar testes de acessibilidade** — VoiceOver (iOS), TalkBack (Android), texto grande, modo de alto contraste. Elementos interativos têm labels acessíveis?
7. **Planejar testes de push notification** — Permissão concedida/negada, app em foreground/background/terminated, deep link funciona, payload grande/malformado.
8. **Definir testes de UI automatizados** — XCTest (iOS), Espresso (Android), ou Appium (cross-platform). Fluxos críticos automatizados para regressão.

## Outputs

- Suite de testes unitários e integração
- Device matrix com plano de execução
- Cenários de teste de conectividade
- Cenários de teste de lifecycle
- Benchmark de performance vs. targets
- Checklist de acessibilidade
- Testes de push notification
- Suite de UI tests automatizados para fluxos críticos

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Device matrix testada | Top 10 dispositivos validados | Sim |
| Conectividade testada | Online, offline, transição cobertos | Sim |
| Lifecycle testado | Background, termination, rotação | Sim |
| Performance validada | Métricas dentro dos targets | Sim |
| Acessibilidade verificada | VoiceOver/TalkBack funcionando | Sim |

## Próxima Fase

→ [07-readiness.md](./07-readiness.md) — Avaliação de prontidão para submissão à app store
