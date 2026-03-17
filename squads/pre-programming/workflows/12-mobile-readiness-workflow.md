# Workflow 12: Prontidão Mobile

## Objetivo
Garantir que projetos mobile tenham plataformas-alvo definidas, guidelines de cada store atendidos, offline-first considerado e pipeline de build/deploy configurado.

## Trigger
- Projeto classificado com componente mobile (iOS, Android, cross-platform).

## Agentes Envolvidos
- Agente de Arquitetura (Mobile)
- Designer de UI/UX Mobile
- Agente de Qualidade
- Equipe de DevOps Mobile

## Passos

### 1. Definir Plataformas e Abordagem
- Plataformas-alvo (iOS, Android, ambos).
- Abordagem (Nativa, React Native, Flutter, PWA).
- Versões mínimas de OS suportadas.
- **Output:** Decisão de plataforma documentada.

### 2. Validar Guidelines das Stores
- Revisar Apple Human Interface Guidelines (se iOS).
- Revisar Material Design Guidelines (se Android).
- Verificar requisitos de submissão (permissões, privacidade).
- **Output:** Conformidade com guidelines verificada.

### 3. Planejar Offline-First (se aplicável)
- Definir quais funcionalidades funcionam offline.
- Estratégia de sincronização de dados.
- Resolução de conflitos.
- **Output:** Estratégia offline documentada.

### 4. Configurar Pipeline Mobile
- Build automatizado para cada plataforma.
- Distribuição para testes (TestFlight, Firebase App Distribution).
- Assinatura de código configurada.
- **Output:** Pipeline mobile funcional.

### 5. Planejar Push Notifications (se aplicável)
- Provedor de push (FCM, APNs).
- Permissões e opt-in do usuário.
- Conteúdo e gatilhos de notificação.
- **Output:** Estratégia de push definida.

### 6. Planejar Testes Mobile
- Dispositivos de teste (físicos e emuladores).
- Testes de diferentes tamanhos de tela.
- Testes de performance em dispositivos de baixo recurso.
- **Output:** Estratégia de testes mobile.

### 7. Planejar Release Mobile
- Processo de submissão nas stores.
- Staged rollout (rollout gradual).
- Estratégia de atualizações forçadas e opcionais.
- **Output:** Plano de release mobile.

## Gates de Qualidade
- [ ] Plataformas e abordagem estão definidas e justificadas.
- [ ] Guidelines das stores foram revisadas.
- [ ] Estratégia offline está definida (se aplicável).
- [ ] Pipeline de build e distribuição está funcional.
- [ ] Dispositivos de teste estão disponíveis.
- [ ] Estratégia de push está definida (se aplicável).
- [ ] Plano de release nas stores está definido.

## Output
- Mobile pronto para implementação.
- Pipeline configurado.
- Estratégias definidas (offline, push, release).

## Próximo Workflow
→ Retorna ao workflow principal (06-test-design-to-readiness).
