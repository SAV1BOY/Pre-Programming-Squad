#!/usr/bin/env python3
"""
Validador de Plano de Rollout.

Este script valida a completude e qualidade de um plano de rollout (implantação),
verificando que todos os elementos críticos estejam definidos antes do início
do desenvolvimento.

Verificações realizadas:
  - Estratégia de deploy (blue-green, canary, rolling, big-bang)
  - Plano de rollback com critérios de ativação
  - Feature flags e controles de lançamento
  - Critérios de go/no-go
  - Plano de monitoramento pós-deploy
  - Comunicação e notificações
  - Janela de manutenção e cronograma
  - Checklist pré-deploy

Uso:
  python rollout-checker.py <plano_rollout> [--format text|json] [--strict]
"""

import argparse
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------

ESTRATEGIAS_VALIDAS = [
    "blue-green", "canary", "rolling", "big-bang",
    "feature-flag", "a-b-test", "shadow",
]

SECOES_OBRIGATORIAS = [
    "estrategia_deploy",
    "plano_rollback",
    "criterios_go_nogo",
    "monitoramento",
]

SECOES_RECOMENDADAS = [
    "feature_flags",
    "comunicacao",
    "janela_manutencao",
    "checklist_pre_deploy",
    "responsaveis",
    "dependencias_externas",
    "plano_dados",
    "metricas_sucesso",
]


# ---------------------------------------------------------------------------
# Carregamento
# ---------------------------------------------------------------------------

def carregar_dados(caminho: str) -> dict:
    """Carrega plano de rollout."""
    caminho = Path(caminho)
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    conteudo = caminho.read_text(encoding="utf-8")
    if caminho.suffix in (".yaml", ".yml"):
        if yaml is None:
            raise ImportError("PyYAML necessário.")
        return yaml.safe_load(conteudo) or {}
    if caminho.suffix == ".json":
        return json.loads(conteudo)
    raise ValueError(f"Formato não suportado: {caminho.suffix}")


# ---------------------------------------------------------------------------
# Regras de validação
# ---------------------------------------------------------------------------

def verificar_estrategia_deploy(dados: dict) -> tuple[list, list]:
    """Verifica a estratégia de deploy."""
    erros = []
    avisos = []

    estrategia = dados.get("estrategia_deploy", dados.get("deploy_strategy"))
    if not estrategia:
        erros.append("Estratégia de deploy não definida.")
        return erros, avisos

    if isinstance(estrategia, dict):
        tipo = estrategia.get("tipo", estrategia.get("type", ""))
    else:
        tipo = str(estrategia)

    if tipo.lower() not in ESTRATEGIAS_VALIDAS:
        avisos.append(
            f"Estratégia '{tipo}' não é padrão. "
            f"Estratégias conhecidas: {', '.join(ESTRATEGIAS_VALIDAS)}"
        )

    if isinstance(estrategia, dict):
        if not estrategia.get("descricao") and not estrategia.get("detalhes"):
            avisos.append("Estratégia de deploy sem descrição detalhada.")
        if not estrategia.get("etapas") and not estrategia.get("steps"):
            avisos.append("Estratégia de deploy sem etapas definidas.")

    return erros, avisos


def verificar_plano_rollback(dados: dict) -> tuple[list, list]:
    """Verifica o plano de rollback."""
    erros = []
    avisos = []

    rollback = dados.get("plano_rollback", dados.get("rollback_plan", dados.get("rollback")))
    if not rollback:
        erros.append("Plano de rollback não definido.")
        return erros, avisos

    if isinstance(rollback, dict):
        if not rollback.get("criterios_ativacao") and not rollback.get("triggers"):
            erros.append("Plano de rollback sem critérios de ativação.")
        if not rollback.get("procedimento") and not rollback.get("steps"):
            erros.append("Plano de rollback sem procedimento definido.")
        if not rollback.get("tempo_estimado") and not rollback.get("estimated_time"):
            avisos.append("Plano de rollback sem tempo estimado de execução.")
        if not rollback.get("responsavel"):
            avisos.append("Plano de rollback sem responsável definido.")
        if not rollback.get("verificacao_pos_rollback"):
            avisos.append("Plano de rollback sem verificação pós-execução.")
    elif isinstance(rollback, str) and len(rollback.strip()) < 50:
        erros.append("Plano de rollback muito superficial (mínimo 50 caracteres).")

    return erros, avisos


def verificar_criterios_go_nogo(dados: dict) -> tuple[list, list]:
    """Verifica critérios de go/no-go."""
    erros = []
    avisos = []

    criterios = dados.get("criterios_go_nogo", dados.get("go_nogo_criteria"))
    if not criterios:
        erros.append("Critérios de go/no-go não definidos.")
        return erros, avisos

    if isinstance(criterios, list):
        if len(criterios) < 3:
            avisos.append("Recomendado ter pelo menos 3 critérios de go/no-go.")
        for i, c in enumerate(criterios):
            if isinstance(c, dict):
                if not c.get("criterio") and not c.get("descricao"):
                    erros.append(f"Critério #{i+1}: sem descrição.")
                if not c.get("metrica") and not c.get("como_verificar"):
                    avisos.append(f"Critério #{i+1}: sem forma de verificação.")
    elif isinstance(criterios, dict):
        if "go" not in criterios and "no_go" not in criterios:
            avisos.append("Critérios devem separar condições de 'go' e 'no-go'.")

    return erros, avisos


def verificar_monitoramento(dados: dict) -> tuple[list, list]:
    """Verifica o plano de monitoramento."""
    erros = []
    avisos = []

    monitor = dados.get("monitoramento", dados.get("monitoring"))
    if not monitor:
        erros.append("Plano de monitoramento pós-deploy não definido.")
        return erros, avisos

    if isinstance(monitor, dict):
        checks = {
            "Métricas": bool(monitor.get("metricas") or monitor.get("metrics")),
            "Alertas": bool(monitor.get("alertas") or monitor.get("alerts")),
            "Dashboards": bool(monitor.get("dashboards")),
            "Logs": bool(monitor.get("logs")),
            "SLAs/SLOs": bool(monitor.get("slas") or monitor.get("slos")),
        }
        for nome, presente in checks.items():
            if not presente:
                avisos.append(f"Monitoramento: '{nome}' não definido.")

        if not any(checks.values()):
            erros.append("Plano de monitoramento sem nenhum elemento definido.")

    return erros, avisos


def verificar_feature_flags(dados: dict) -> list[str]:
    """Verifica configuração de feature flags."""
    avisos = []
    flags = dados.get("feature_flags", dados.get("flags"))
    if not flags:
        avisos.append("Feature flags não configurados. Considere usar para lançamento gradual.")
    elif isinstance(flags, list):
        for i, flag in enumerate(flags):
            if isinstance(flag, dict):
                if not flag.get("nome") and not flag.get("name"):
                    avisos.append(f"Feature flag #{i+1}: sem nome.")
                if not flag.get("valor_padrao") and flag.get("default") is None:
                    avisos.append(f"Feature flag #{i+1}: sem valor padrão.")
    return avisos


def verificar_comunicacao(dados: dict) -> list[str]:
    """Verifica plano de comunicação."""
    avisos = []
    comunicacao = dados.get("comunicacao", dados.get("communication"))
    if not comunicacao:
        avisos.append("Plano de comunicação não definido. Quem será notificado?")
    return avisos


def verificar_checklist_pre_deploy(dados: dict) -> list[str]:
    """Verifica checklist pré-deploy."""
    avisos = []
    checklist = dados.get("checklist_pre_deploy", dados.get("pre_deploy_checklist"))
    if not checklist:
        avisos.append("Checklist pré-deploy não definido.")
    elif isinstance(checklist, list) and len(checklist) < 5:
        avisos.append("Checklist pré-deploy com poucos itens (recomendado: 5+).")
    return avisos


# ---------------------------------------------------------------------------
# Função principal
# ---------------------------------------------------------------------------

def verificar_rollout(caminho: str, modo_estrito: bool = False) -> dict:
    """
    Valida completude do plano de rollout.

    Args:
        caminho: Caminho para o arquivo do plano.
        modo_estrito: Se True, avisos viram erros.

    Returns:
        Relatório de validação.
    """
    resultado = {"valido": True, "erros": [], "avisos": [], "score": 0}

    try:
        dados = carregar_dados(caminho)
    except Exception as e:
        resultado["valido"] = False
        resultado["erros"].append(f"Erro ao carregar: {e}")
        return resultado

    # Verificações obrigatórias
    verificacoes = [
        verificar_estrategia_deploy,
        verificar_plano_rollback,
        verificar_criterios_go_nogo,
        verificar_monitoramento,
    ]

    for verificacao in verificacoes:
        erros, avisos = verificacao(dados)
        resultado["erros"].extend(erros)
        if modo_estrito:
            resultado["erros"].extend(avisos)
        else:
            resultado["avisos"].extend(avisos)

    # Verificações recomendadas
    avisos_extras = []
    avisos_extras.extend(verificar_feature_flags(dados))
    avisos_extras.extend(verificar_comunicacao(dados))
    avisos_extras.extend(verificar_checklist_pre_deploy(dados))

    if modo_estrito:
        resultado["erros"].extend(avisos_extras)
    else:
        resultado["avisos"].extend(avisos_extras)

    # Calcular score
    total_checks = len(SECOES_OBRIGATORIAS) + len(SECOES_RECOMENDADAS)
    presentes = 0
    for secao in SECOES_OBRIGATORIAS + SECOES_RECOMENDADAS:
        if dados.get(secao):
            presentes += 1
    resultado["score"] = round((presentes / total_checks) * 100, 1) if total_checks > 0 else 0

    resultado["valido"] = len(resultado["erros"]) == 0
    return resultado


# ---------------------------------------------------------------------------
# Formatação
# ---------------------------------------------------------------------------

def formatar_texto(resultado: dict) -> str:
    """Formata o resultado como texto."""
    linhas = []
    linhas.append("=" * 60)
    linhas.append("  VALIDAÇÃO DO PLANO DE ROLLOUT")
    linhas.append("=" * 60)

    status = "APROVADO" if resultado["valido"] else "REPROVADO"
    linhas.append(f"\nStatus: {status}")
    linhas.append(f"Score de completude: {resultado['score']}%")

    if resultado["erros"]:
        linhas.append(f"\nErros ({len(resultado['erros'])}):")
        for e in resultado["erros"]:
            linhas.append(f"  [XX] {e}")
    if resultado["avisos"]:
        linhas.append(f"\nAvisos ({len(resultado['avisos'])}):")
        for a in resultado["avisos"]:
            linhas.append(f"  [!!] {a}")

    if not resultado["erros"] and not resultado["avisos"]:
        linhas.append("\nPlano de rollout completo e sem problemas detectados.")

    linhas.append(f"\n{'=' * 60}")
    return "\n".join(linhas)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def criar_parser() -> argparse.ArgumentParser:
    """Cria o parser de argumentos."""
    parser = argparse.ArgumentParser(
        description="Valida completude do plano de rollout.",
    )
    parser.add_argument("arquivo", help="Plano de rollout (YAML/JSON).")
    parser.add_argument("--strict", action="store_true", help="Modo estrito.")
    parser.add_argument(
        "--format", choices=["text", "json"], default="text",
        help="Formato de saída.",
    )
    parser.add_argument("--output-file", default=None, help="Arquivo de saída.")
    return parser


def main():
    """Ponto de entrada principal."""
    parser = criar_parser()
    args = parser.parse_args()

    resultado = verificar_rollout(args.arquivo, args.strict)

    if args.format == "json":
        saida = json.dumps(resultado, indent=2, ensure_ascii=False)
    else:
        saida = formatar_texto(resultado)

    if args.output_file:
        Path(args.output_file).write_text(saida, encoding="utf-8")
        print(f"Relatório salvo em: {args.output_file}")
    else:
        print(saida)

    sys.exit(0 if resultado["valido"] else 1)


if __name__ == "__main__":
    main()
