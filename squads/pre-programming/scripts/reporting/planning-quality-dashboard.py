#!/usr/bin/env python3
"""
Dashboard de Qualidade do Planejamento.

Este script gera um dashboard consolidado com os principais KPIs de qualidade
do processo de pré-programação, agregando métricas de múltiplas fontes para
oferecer uma visão holística do estado do planejamento.

KPIs monitorados:
  - Score de prontidão geral
  - Índice de completude de artefatos
  - Taxa de resolução de ambiguidades
  - Cobertura de riscos identificados
  - Qualidade dos requisitos (clareza, testabilidade)
  - Índice de confiança arquitetural
  - Velocidade do ciclo de planejamento
  - Taxa de retrabalho de planejamento

Uso:
  python planning-quality-dashboard.py <diretorio_dados> [--format text|json|html]
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------

LIMIARES_KPI = {
    "score_prontidao": {"verde": 80, "amarelo": 60, "vermelho": 0},
    "completude_artefatos": {"verde": 90, "amarelo": 70, "vermelho": 0},
    "taxa_resolucao_ambiguidades": {"verde": 85, "amarelo": 65, "vermelho": 0},
    "cobertura_riscos": {"verde": 80, "amarelo": 60, "vermelho": 0},
    "qualidade_requisitos": {"verde": 75, "amarelo": 55, "vermelho": 0},
    "confianca_arquitetural": {"verde": 80, "amarelo": 60, "vermelho": 0},
    "velocidade_ciclo": {"verde": 80, "amarelo": 60, "vermelho": 0},
    "taxa_retrabalho": {"verde": 80, "amarelo": 60, "vermelho": 0},
}


# ---------------------------------------------------------------------------
# Carregamento de dados
# ---------------------------------------------------------------------------

def carregar_dados_diretorio(caminho: str) -> dict:
    """Carrega todos os arquivos de dados de um diretório."""
    caminho = Path(caminho)
    dados_agregados = {}

    if caminho.is_file():
        return _carregar_arquivo(caminho)

    if not caminho.is_dir():
        raise FileNotFoundError(f"Caminho não encontrado: {caminho}")

    for arquivo in sorted(caminho.iterdir()):
        if arquivo.suffix in (".yaml", ".yml", ".json"):
            try:
                dados = _carregar_arquivo(arquivo)
                dados_agregados[arquivo.stem] = dados
            except Exception:
                continue

    return dados_agregados


def _carregar_arquivo(caminho: Path) -> dict:
    """Carrega um arquivo individual."""
    conteudo = caminho.read_text(encoding="utf-8")
    if caminho.suffix in (".yaml", ".yml"):
        if yaml is None:
            raise ImportError("PyYAML necessário.")
        return yaml.safe_load(conteudo) or {}
    if caminho.suffix == ".json":
        return json.loads(conteudo)
    raise ValueError(f"Formato não suportado: {caminho.suffix}")


# ---------------------------------------------------------------------------
# Cálculo de KPIs
# ---------------------------------------------------------------------------

def calcular_score_prontidao(dados: dict) -> dict:
    """Calcula o KPI de score de prontidão geral."""
    score = dados.get("readiness_score", dados.get("score_prontidao"))

    if score is None:
        # Tentar calcular a partir dos sub-componentes
        artefatos = dados.get("artefatos", {})
        if artefatos:
            obrig = ["project_brief", "architecture_notes", "risk_register",
                     "test_plan", "api_contracts", "acceptance_criteria"]
            presentes = sum(1 for a in obrig if a in artefatos and artefatos[a])
            score = round((presentes / len(obrig)) * 100, 1)
        else:
            score = 0

    return _criar_kpi("Score de Prontidão", score, "score_prontidao", "%")


def calcular_completude_artefatos(dados: dict) -> dict:
    """Calcula o índice de completude de artefatos."""
    artefatos = dados.get("artefatos", {})
    todos = [
        "project_brief", "architecture_notes", "risk_register",
        "test_plan", "api_contracts", "acceptance_criteria",
        "decision_log", "dependency_map", "rollout_plan", "monitoring_plan",
    ]
    presentes = sum(1 for a in todos if a in artefatos and artefatos[a])
    score = round((presentes / len(todos)) * 100, 1) if todos else 0
    return _criar_kpi("Completude de Artefatos", score, "completude_artefatos", "%")


def calcular_taxa_resolucao_ambiguidades(dados: dict) -> dict:
    """Calcula a taxa de resolução de ambiguidades."""
    ambiguidades = dados.get("ambiguidades", [])
    if not ambiguidades:
        return _criar_kpi("Resolução de Ambiguidades", 100, "taxa_resolucao_ambiguidades", "%")

    total = len(ambiguidades)
    resolvidas = sum(
        1 for a in ambiguidades
        if isinstance(a, dict) and a.get("status", "").lower() in ("resolvida", "descartada")
    )
    score = round((resolvidas / total) * 100, 1) if total > 0 else 0
    return _criar_kpi("Resolução de Ambiguidades", score, "taxa_resolucao_ambiguidades", "%")


def calcular_cobertura_riscos(dados: dict) -> dict:
    """Calcula a cobertura de riscos."""
    riscos = dados.get("riscos", [])
    if not riscos:
        return _criar_kpi("Cobertura de Riscos", 0, "cobertura_riscos", "%")

    total = len(riscos)
    com_mitigacao = sum(
        1 for r in riscos
        if isinstance(r, dict) and (r.get("mitigacao") or r.get("plano_mitigacao"))
    )
    score = round((com_mitigacao / total) * 100, 1) if total > 0 else 0
    return _criar_kpi("Cobertura de Riscos", score, "cobertura_riscos", "%")


def calcular_qualidade_requisitos(dados: dict) -> dict:
    """Calcula a qualidade dos requisitos."""
    requisitos = dados.get("requisitos", [])
    if not requisitos:
        return _criar_kpi("Qualidade de Requisitos", 0, "qualidade_requisitos", "%")

    total = len(requisitos)
    pontuacao_total = 0

    for req in requisitos:
        if not isinstance(req, dict):
            continue
        pontos = 0
        max_pontos = 4
        if req.get("descricao") and len(str(req["descricao"])) > 20:
            pontos += 1
        if req.get("criterio_aceite") or req.get("acceptance_criteria"):
            pontos += 1
        if req.get("prioridade") or req.get("priority"):
            pontos += 1
        if req.get("rastreabilidade") or req.get("traceability"):
            pontos += 1
        pontuacao_total += (pontos / max_pontos) * 100

    score = round(pontuacao_total / total, 1) if total > 0 else 0
    return _criar_kpi("Qualidade de Requisitos", score, "qualidade_requisitos", "%")


def calcular_confianca_arquitetural(dados: dict) -> dict:
    """Calcula o índice de confiança arquitetural."""
    arq = dados.get("architecture_notes", dados.get("arquitetura", {}))
    if not arq:
        return _criar_kpi("Confiança Arquitetural", 0, "confianca_arquitetural", "%")

    pontos = 0
    max_pontos = 6
    checks = [
        bool(arq.get("decisoes") or arq.get("decisions")),
        bool(arq.get("diagramas") or arq.get("diagrams")),
        bool(arq.get("componentes") or arq.get("components")),
        bool(arq.get("integracoes") or arq.get("integrations")),
        bool(arq.get("restricoes") or arq.get("constraints")),
        bool(arq.get("alternativas") or arq.get("alternatives")),
    ]
    pontos = sum(checks)
    score = round((pontos / max_pontos) * 100, 1)
    return _criar_kpi("Confiança Arquitetural", score, "confianca_arquitetural", "%")


def calcular_velocidade_ciclo(dados: dict) -> dict:
    """Calcula a velocidade do ciclo de planejamento."""
    ciclo = dados.get("ciclo_planejamento", {})
    data_inicio = ciclo.get("data_inicio")
    data_fim = ciclo.get("data_fim")
    duracao_planejada = ciclo.get("duracao_planejada_dias", 0)

    if data_inicio and data_fim and duracao_planejada:
        try:
            inicio = datetime.fromisoformat(str(data_inicio))
            fim = datetime.fromisoformat(str(data_fim))
            duracao_real = (fim - inicio).days
            if duracao_real > 0:
                eficiencia = min((duracao_planejada / duracao_real) * 100, 100)
            else:
                eficiencia = 100
        except (ValueError, TypeError):
            eficiencia = 50
    else:
        eficiencia = 50

    return _criar_kpi("Velocidade do Ciclo", round(eficiencia, 1), "velocidade_ciclo", "%")


def calcular_taxa_retrabalho(dados: dict) -> dict:
    """Calcula a taxa de retrabalho no planejamento."""
    revisoes = dados.get("revisoes", dados.get("reviews", []))
    if not revisoes:
        return _criar_kpi("Taxa Sem Retrabalho", 80, "taxa_retrabalho", "%")

    total = len(revisoes)
    aprovados_primeira = sum(
        1 for r in revisoes
        if isinstance(r, dict) and r.get("tentativa", r.get("attempt", 1)) == 1
        and r.get("resultado", r.get("result", "")).lower() in ("aprovado", "approved")
    )
    score = round((aprovados_primeira / total) * 100, 1) if total > 0 else 80
    return _criar_kpi("Taxa Sem Retrabalho", score, "taxa_retrabalho", "%")


def _criar_kpi(nome: str, valor: float, chave: str, unidade: str) -> dict:
    """Cria a estrutura de um KPI."""
    limiares = LIMIARES_KPI.get(chave, {"verde": 80, "amarelo": 60, "vermelho": 0})
    if valor >= limiares["verde"]:
        status = "verde"
    elif valor >= limiares["amarelo"]:
        status = "amarelo"
    else:
        status = "vermelho"

    return {
        "nome": nome,
        "chave": chave,
        "valor": valor,
        "unidade": unidade,
        "status": status,
    }


# ---------------------------------------------------------------------------
# Geração do dashboard
# ---------------------------------------------------------------------------

def gerar_dashboard(dados: dict) -> dict:
    """Gera o dashboard completo de KPIs."""
    # Se dados foram agregados de múltiplos arquivos, mesclar
    dados_flat = {}
    for chave, valor in dados.items():
        if isinstance(valor, dict):
            dados_flat.update(valor)
        else:
            dados_flat[chave] = valor

    calculadoras = [
        calcular_score_prontidao,
        calcular_completude_artefatos,
        calcular_taxa_resolucao_ambiguidades,
        calcular_cobertura_riscos,
        calcular_qualidade_requisitos,
        calcular_confianca_arquitetural,
        calcular_velocidade_ciclo,
        calcular_taxa_retrabalho,
    ]

    kpis = [calc(dados_flat) for calc in calculadoras]

    # Saúde geral
    scores = [kpi["valor"] for kpi in kpis]
    saude_geral = round(sum(scores) / len(scores), 1) if scores else 0

    verdes = sum(1 for k in kpis if k["status"] == "verde")
    amarelos = sum(1 for k in kpis if k["status"] == "amarelo")
    vermelhos = sum(1 for k in kpis if k["status"] == "vermelho")

    return {
        "data_geracao": datetime.now().isoformat(),
        "saude_geral": saude_geral,
        "resumo_status": {
            "verde": verdes,
            "amarelo": amarelos,
            "vermelho": vermelhos,
        },
        "kpis": kpis,
        "alertas": _gerar_alertas(kpis),
    }


def _gerar_alertas(kpis: list[dict]) -> list[str]:
    """Gera alertas para KPIs em estado crítico."""
    alertas = []
    for kpi in kpis:
        if kpi["status"] == "vermelho":
            alertas.append(
                f"ALERTA: '{kpi['nome']}' está em {kpi['valor']}{kpi['unidade']} "
                f"(abaixo do limiar mínimo)."
            )
        elif kpi["status"] == "amarelo":
            alertas.append(
                f"ATENÇÃO: '{kpi['nome']}' está em {kpi['valor']}{kpi['unidade']} "
                f"(zona de atenção)."
            )
    return alertas


# ---------------------------------------------------------------------------
# Formatação
# ---------------------------------------------------------------------------

def formatar_texto(dashboard: dict) -> str:
    """Formata o dashboard como texto."""
    linhas = []
    linhas.append("=" * 65)
    linhas.append("  DASHBOARD DE QUALIDADE DO PLANEJAMENTO")
    linhas.append("=" * 65)
    linhas.append(f"\nData: {dashboard['data_geracao']}")
    linhas.append(f"Saúde Geral: {dashboard['saude_geral']}%")

    rs = dashboard["resumo_status"]
    linhas.append(f"\nStatus dos KPIs: {rs['verde']} OK | {rs['amarelo']} Atenção | {rs['vermelho']} Crítico")

    linhas.append(f"\n{'-' * 65}")
    linhas.append("KPIs:")
    linhas.append(f"{'Indicador':<35} {'Valor':>8} {'Status':>10}")
    linhas.append("-" * 55)

    indicadores_status = {"verde": "[OK]", "amarelo": "[!!]", "vermelho": "[XX]"}
    for kpi in dashboard["kpis"]:
        ind = indicadores_status.get(kpi["status"], "[??]")
        barra_len = int(kpi["valor"] / 5)
        barra = "#" * barra_len + "." * (20 - barra_len)
        linhas.append(
            f"{kpi['nome']:<35} {kpi['valor']:>6.1f}{kpi['unidade']} {ind:>5}"
        )
        linhas.append(f"  [{barra}]")

    if dashboard["alertas"]:
        linhas.append(f"\n{'-' * 65}")
        linhas.append("ALERTAS:")
        for alerta in dashboard["alertas"]:
            linhas.append(f"  * {alerta}")

    linhas.append(f"\n{'=' * 65}")
    return "\n".join(linhas)


def formatar_html(dashboard: dict) -> str:
    """Formata o dashboard como HTML."""
    cores = {"verde": "#28a745", "amarelo": "#ffc107", "vermelho": "#dc3545"}
    html = [
        "<!DOCTYPE html><html lang='pt-BR'><head><meta charset='utf-8'>",
        "<title>Dashboard de Qualidade</title>",
        "<style>body{font-family:sans-serif;max-width:900px;margin:auto;padding:20px}",
        ".kpi{display:inline-block;width:200px;padding:15px;margin:8px;border-radius:8px;text-align:center}",
        ".verde{background:#d4edda;border:2px solid #28a745}",
        ".amarelo{background:#fff3cd;border:2px solid #ffc107}",
        ".vermelho{background:#f8d7da;border:2px solid #dc3545}",
        ".score{font-size:1.8em;font-weight:bold}",
        "table{border-collapse:collapse;width:100%}td,th{padding:8px;border:1px solid #ddd;text-align:left}",
        "th{background:#f4f4f4}</style></head><body>",
        "<h1>Dashboard de Qualidade do Planejamento</h1>",
        f"<p>Gerado em: {dashboard['data_geracao']}</p>",
        f"<p class='score'>Saúde Geral: {dashboard['saude_geral']}%</p>",
        "<div>",
    ]

    for kpi in dashboard["kpis"]:
        html.append(
            f"<div class='kpi {kpi['status']}'>"
            f"<div style='font-size:0.9em'>{kpi['nome']}</div>"
            f"<div class='score'>{kpi['valor']}{kpi['unidade']}</div></div>"
        )

    html.append("</div>")

    if dashboard["alertas"]:
        html.append("<h2>Alertas</h2><ul>")
        for alerta in dashboard["alertas"]:
            html.append(f"<li>{alerta}</li>")
        html.append("</ul>")

    html.append("</body></html>")
    return "\n".join(html)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def criar_parser() -> argparse.ArgumentParser:
    """Cria o parser de argumentos."""
    parser = argparse.ArgumentParser(
        description="Gera dashboard de qualidade do planejamento.",
    )
    parser.add_argument("caminho", help="Diretório ou arquivo de dados.")
    parser.add_argument(
        "--format", choices=["text", "json", "html"], default="text",
        help="Formato de saída.",
    )
    parser.add_argument("--output-file", default=None, help="Arquivo de saída.")
    return parser


def main():
    """Ponto de entrada principal."""
    parser = criar_parser()
    args = parser.parse_args()

    dados = carregar_dados_diretorio(args.caminho)
    dashboard = gerar_dashboard(dados)

    if args.format == "json":
        saida = json.dumps(dashboard, indent=2, ensure_ascii=False)
    elif args.format == "html":
        saida = formatar_html(dashboard)
    else:
        saida = formatar_texto(dashboard)

    if args.output_file:
        Path(args.output_file).write_text(saida, encoding="utf-8")
        print(f"Dashboard salvo em: {args.output_file}")
    else:
        print(saida)


if __name__ == "__main__":
    main()
