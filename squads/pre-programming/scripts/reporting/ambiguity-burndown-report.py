#!/usr/bin/env python3
"""
Relatório de Burndown de Ambiguidades.

Este script rastreia a redução de ambiguidades ao longo do tempo durante
a fase de pré-programação, gerando visualizações e métricas de progresso
na resolução de incertezas do projeto.

Métricas calculadas:
  - Total de ambiguidades identificadas por período
  - Taxa de resolução de ambiguidades
  - Ambiguidades restantes por categoria
  - Velocidade de resolução (ambiguidades/dia)
  - Projeção de data de conclusão
  - Tendência de novas ambiguidades descobertas

Uso:
  python ambiguity-burndown-report.py <dados> [--format text|json|csv] [--period daily|weekly]
"""

import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------

CATEGORIAS_AMBIGUIDADE = [
    "requisito", "tecnica", "escopo", "integracao",
    "performance", "seguranca", "ux", "negocio",
]

STATUS_AMBIGUIDADE = ["aberta", "em_analise", "resolvida", "aceita", "descartada"]


# ---------------------------------------------------------------------------
# Carregamento de dados
# ---------------------------------------------------------------------------

def carregar_dados(caminho: str) -> dict:
    """Carrega dados de ambiguidades de um arquivo YAML ou JSON."""
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


def extrair_ambiguidades(dados: dict) -> list[dict]:
    """Extrai lista de ambiguidades dos dados carregados."""
    return dados.get("ambiguidades", dados.get("ambiguities", []))


# ---------------------------------------------------------------------------
# Cálculo de métricas
# ---------------------------------------------------------------------------

def calcular_metricas_burndown(ambiguidades: list[dict], periodo: str = "weekly") -> dict:
    """
    Calcula métricas de burndown de ambiguidades.

    Args:
        ambiguidades: Lista de registros de ambiguidade.
        periodo: Agrupamento temporal ('daily' ou 'weekly').

    Returns:
        Dicionário com métricas e série temporal.
    """
    if not ambiguidades:
        return {
            "total_identificadas": 0,
            "total_resolvidas": 0,
            "total_abertas": 0,
            "taxa_resolucao": 0.0,
            "velocidade_resolucao": 0.0,
            "serie_temporal": [],
            "por_categoria": {},
            "projecao_conclusao": None,
        }

    # Classificar por status
    total = len(ambiguidades)
    resolvidas = sum(
        1 for a in ambiguidades
        if isinstance(a, dict) and a.get("status", "").lower() in ("resolvida", "resolved", "descartada")
    )
    abertas = total - resolvidas

    # Agrupar por período
    serie_temporal = _calcular_serie_temporal(ambiguidades, periodo)

    # Por categoria
    por_categoria = defaultdict(lambda: {"total": 0, "resolvidas": 0, "abertas": 0})
    for amb in ambiguidades:
        if isinstance(amb, dict):
            cat = amb.get("categoria", "nao_classificada").lower()
            por_categoria[cat]["total"] += 1
            if amb.get("status", "").lower() in ("resolvida", "resolved", "descartada"):
                por_categoria[cat]["resolvidas"] += 1
            else:
                por_categoria[cat]["abertas"] += 1

    # Velocidade de resolução
    datas_resolucao = []
    for amb in ambiguidades:
        if isinstance(amb, dict) and amb.get("data_resolucao"):
            try:
                dt = datetime.fromisoformat(str(amb["data_resolucao"]))
                datas_resolucao.append(dt)
            except (ValueError, TypeError):
                pass

    datas_criacao = []
    for amb in ambiguidades:
        if isinstance(amb, dict) and amb.get("data_criacao"):
            try:
                dt = datetime.fromisoformat(str(amb["data_criacao"]))
                datas_criacao.append(dt)
            except (ValueError, TypeError):
                pass

    velocidade = 0.0
    if datas_resolucao and datas_criacao:
        data_inicio = min(datas_criacao)
        data_fim = max(datas_resolucao)
        dias = (data_fim - data_inicio).days or 1
        velocidade = round(resolvidas / dias, 2)

    # Projeção
    projecao = None
    if velocidade > 0 and abertas > 0:
        dias_restantes = int(abertas / velocidade)
        projecao = (datetime.now() + timedelta(days=dias_restantes)).strftime("%Y-%m-%d")

    taxa_resolucao = round((resolvidas / total) * 100, 1) if total > 0 else 0.0

    return {
        "total_identificadas": total,
        "total_resolvidas": resolvidas,
        "total_abertas": abertas,
        "taxa_resolucao": taxa_resolucao,
        "velocidade_resolucao": velocidade,
        "serie_temporal": serie_temporal,
        "por_categoria": dict(por_categoria),
        "projecao_conclusao": projecao,
    }


def _calcular_serie_temporal(ambiguidades: list[dict], periodo: str) -> list[dict]:
    """Gera a série temporal de burndown."""
    eventos = []
    for amb in ambiguidades:
        if not isinstance(amb, dict):
            continue
        if amb.get("data_criacao"):
            try:
                dt = datetime.fromisoformat(str(amb["data_criacao"]))
                eventos.append(("criada", dt))
            except (ValueError, TypeError):
                pass
        if amb.get("data_resolucao"):
            try:
                dt = datetime.fromisoformat(str(amb["data_resolucao"]))
                eventos.append(("resolvida", dt))
            except (ValueError, TypeError):
                pass

    if not eventos:
        return []

    eventos.sort(key=lambda e: e[1])
    data_inicio = eventos[0][1].date()
    data_fim = eventos[-1][1].date()

    # Agrupar por período
    delta = timedelta(days=7 if periodo == "weekly" else 1)
    serie = []
    data_atual = data_inicio
    abertas_acumuladas = 0
    resolvidas_acumuladas = 0

    while data_atual <= data_fim + delta:
        proxima = data_atual + delta
        novas = sum(
            1 for tipo, dt in eventos
            if tipo == "criada" and data_atual <= dt.date() < proxima
        )
        fechadas = sum(
            1 for tipo, dt in eventos
            if tipo == "resolvida" and data_atual <= dt.date() < proxima
        )

        abertas_acumuladas += novas - fechadas
        resolvidas_acumuladas += fechadas

        serie.append({
            "periodo": data_atual.isoformat(),
            "novas": novas,
            "resolvidas_periodo": fechadas,
            "abertas_acumuladas": max(0, abertas_acumuladas),
            "resolvidas_acumuladas": resolvidas_acumuladas,
        })
        data_atual = proxima

    return serie


def calcular_tendencia(serie: list[dict]) -> str:
    """Calcula a tendência de resolução."""
    if len(serie) < 2:
        return "insuficiente"

    ultimos = serie[-3:] if len(serie) >= 3 else serie
    abertas = [p["abertas_acumuladas"] for p in ultimos]

    if all(abertas[i] >= abertas[i + 1] for i in range(len(abertas) - 1)):
        return "decrescente"
    elif all(abertas[i] <= abertas[i + 1] for i in range(len(abertas) - 1)):
        return "crescente"
    return "estavel"


# ---------------------------------------------------------------------------
# Formatação de saída
# ---------------------------------------------------------------------------

def formatar_texto(metricas: dict) -> str:
    """Formata o relatório como texto."""
    linhas = []
    linhas.append("=" * 60)
    linhas.append("  RELATÓRIO DE BURNDOWN DE AMBIGUIDADES")
    linhas.append("=" * 60)
    linhas.append(f"\nData: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    linhas.append(f"\nResumo:")
    linhas.append(f"  Total identificadas:    {metricas['total_identificadas']}")
    linhas.append(f"  Resolvidas:             {metricas['total_resolvidas']}")
    linhas.append(f"  Abertas:                {metricas['total_abertas']}")
    linhas.append(f"  Taxa de resolução:      {metricas['taxa_resolucao']}%")
    linhas.append(f"  Velocidade:             {metricas['velocidade_resolucao']} amb/dia")

    if metricas["projecao_conclusao"]:
        linhas.append(f"  Projeção de conclusão:  {metricas['projecao_conclusao']}")

    tendencia = calcular_tendencia(metricas["serie_temporal"])
    linhas.append(f"  Tendência:              {tendencia}")

    # Por categoria
    if metricas["por_categoria"]:
        linhas.append(f"\n{'-' * 60}")
        linhas.append("POR CATEGORIA:")
        linhas.append(f"{'Categoria':<20} {'Total':>6} {'Resolvidas':>11} {'Abertas':>8}")
        linhas.append("-" * 50)
        for cat, info in sorted(metricas["por_categoria"].items()):
            linhas.append(
                f"{cat:<20} {info['total']:>6} {info['resolvidas']:>11} {info['abertas']:>8}"
            )

    # Série temporal (resumida)
    serie = metricas["serie_temporal"]
    if serie:
        linhas.append(f"\n{'-' * 60}")
        linhas.append("BURNDOWN (série temporal):")
        linhas.append(f"{'Período':<12} {'Novas':>6} {'Resolv':>7} {'Abertas':>8}")
        linhas.append("-" * 40)
        for ponto in serie[-10:]:  # Últimos 10 períodos
            linhas.append(
                f"{ponto['periodo']:<12} {ponto['novas']:>6} "
                f"{ponto['resolvidas_periodo']:>7} {ponto['abertas_acumuladas']:>8}"
            )

    linhas.append(f"\n{'=' * 60}")
    return "\n".join(linhas)


def formatar_csv(metricas: dict) -> str:
    """Formata a série temporal como CSV."""
    linhas = ["periodo,novas,resolvidas_periodo,abertas_acumuladas,resolvidas_acumuladas"]
    for ponto in metricas["serie_temporal"]:
        linhas.append(
            f"{ponto['periodo']},{ponto['novas']},{ponto['resolvidas_periodo']},"
            f"{ponto['abertas_acumuladas']},{ponto['resolvidas_acumuladas']}"
        )
    return "\n".join(linhas)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def criar_parser() -> argparse.ArgumentParser:
    """Cria o parser de argumentos."""
    parser = argparse.ArgumentParser(
        description="Gera relatório de burndown de ambiguidades.",
    )
    parser.add_argument("arquivo", help="Dados de ambiguidades (YAML/JSON).")
    parser.add_argument(
        "--format", choices=["text", "json", "csv"], default="text",
        help="Formato de saída.",
    )
    parser.add_argument(
        "--period", choices=["daily", "weekly"], default="weekly",
        help="Período de agrupamento.",
    )
    parser.add_argument("--output-file", default=None, help="Arquivo de saída.")
    return parser


def main():
    """Ponto de entrada principal."""
    parser = criar_parser()
    args = parser.parse_args()

    dados = carregar_dados(args.arquivo)
    ambiguidades = extrair_ambiguidades(dados)
    metricas = calcular_metricas_burndown(ambiguidades, args.period)

    if args.format == "json":
        saida = json.dumps(metricas, indent=2, ensure_ascii=False)
    elif args.format == "csv":
        saida = formatar_csv(metricas)
    else:
        saida = formatar_texto(metricas)

    if args.output_file:
        Path(args.output_file).write_text(saida, encoding="utf-8")
        print(f"Relatório salvo em: {args.output_file}")
    else:
        print(saida)


if __name__ == "__main__":
    main()
