#!/usr/bin/env python3
"""
Relatório de Origem de Defeitos.

Este script mapeia defeitos encontrados durante o desenvolvimento à sua fase
de origem no planejamento, permitindo identificar padrões e melhorar o processo
de pré-programação.

Análises realizadas:
  - Distribuição de defeitos por fase de origem (requisitos, arquitetura, design, etc.)
  - Custo relativo de correção por fase
  - Tipos de defeito mais frequentes por origem
  - Correlação entre qualidade do planejamento e defeitos
  - Recomendações de melhoria no processo

Uso:
  python defect-origin-report.py <dados_defeitos> [--format text|json|html] [--include-recommendations]
"""

import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------

FASES_ORIGEM = {
    "requisitos": {"nome": "Requisitos", "multiplicador_custo": 1.0},
    "arquitetura": {"nome": "Arquitetura", "multiplicador_custo": 1.5},
    "design": {"nome": "Design Detalhado", "multiplicador_custo": 2.0},
    "implementacao": {"nome": "Implementação", "multiplicador_custo": 5.0},
    "integracao": {"nome": "Integração", "multiplicador_custo": 8.0},
    "teste": {"nome": "Teste", "multiplicador_custo": 10.0},
    "producao": {"nome": "Produção", "multiplicador_custo": 30.0},
}

TIPOS_DEFEITO = [
    "ambiguidade", "incompletude", "inconsistencia", "incorreto",
    "performance", "seguranca", "usabilidade", "integracao",
]

SEVERIDADES = {
    "critica": 4,
    "alta": 3,
    "media": 2,
    "baixa": 1,
}


# ---------------------------------------------------------------------------
# Carregamento de dados
# ---------------------------------------------------------------------------

def carregar_dados(caminho: str) -> dict:
    """Carrega dados de defeitos."""
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


def extrair_defeitos(dados: dict) -> list[dict]:
    """Extrai lista de defeitos dos dados."""
    return dados.get("defeitos", dados.get("defects", []))


# ---------------------------------------------------------------------------
# Cálculo de métricas
# ---------------------------------------------------------------------------

def analisar_distribuicao_por_fase(defeitos: list[dict]) -> dict:
    """Analisa distribuição de defeitos por fase de origem."""
    contagem = Counter()
    for defeito in defeitos:
        if isinstance(defeito, dict):
            fase = defeito.get("fase_origem", defeito.get("origin_phase", "desconhecida"))
            contagem[fase.lower()] += 1

    total = sum(contagem.values()) or 1
    distribuicao = {}
    for fase, qtd in contagem.most_common():
        info_fase = FASES_ORIGEM.get(fase, {"nome": fase.title(), "multiplicador_custo": 1.0})
        distribuicao[fase] = {
            "nome": info_fase["nome"],
            "quantidade": qtd,
            "percentual": round((qtd / total) * 100, 1),
        }
    return distribuicao


def calcular_custo_relativo(defeitos: list[dict]) -> dict:
    """Calcula custo relativo de correção por fase de origem."""
    custos_por_fase = defaultdict(float)
    contagem_por_fase = defaultdict(int)

    for defeito in defeitos:
        if not isinstance(defeito, dict):
            continue
        fase = defeito.get("fase_origem", "desconhecida").lower()
        fase_deteccao = defeito.get("fase_deteccao", "implementacao").lower()
        severidade = defeito.get("severidade", "media").lower()

        mult_origem = FASES_ORIGEM.get(fase, {}).get("multiplicador_custo", 1.0)
        mult_deteccao = FASES_ORIGEM.get(fase_deteccao, {}).get("multiplicador_custo", 5.0)
        peso_severidade = SEVERIDADES.get(severidade, 2)

        custo = mult_deteccao / mult_origem * peso_severidade
        custos_por_fase[fase] += custo
        contagem_por_fase[fase] += 1

    resultado = {}
    for fase in custos_por_fase:
        info_fase = FASES_ORIGEM.get(fase, {"nome": fase.title()})
        resultado[fase] = {
            "nome": info_fase.get("nome", fase.title()),
            "custo_total_relativo": round(custos_por_fase[fase], 1),
            "custo_medio": round(
                custos_por_fase[fase] / contagem_por_fase[fase], 1
            ) if contagem_por_fase[fase] > 0 else 0,
            "quantidade": contagem_por_fase[fase],
        }
    return resultado


def analisar_tipos_por_fase(defeitos: list[dict]) -> dict:
    """Analisa tipos de defeito mais frequentes por fase de origem."""
    tipos_por_fase = defaultdict(Counter)

    for defeito in defeitos:
        if not isinstance(defeito, dict):
            continue
        fase = defeito.get("fase_origem", "desconhecida").lower()
        tipo = defeito.get("tipo", defeito.get("type", "nao_classificado")).lower()
        tipos_por_fase[fase][tipo] += 1

    resultado = {}
    for fase, counter in tipos_por_fase.items():
        resultado[fase] = [
            {"tipo": tipo, "quantidade": qtd}
            for tipo, qtd in counter.most_common(5)
        ]
    return resultado


def calcular_metricas_resumo(defeitos: list[dict]) -> dict:
    """Calcula métricas resumidas do relatório."""
    total = len(defeitos)
    if total == 0:
        return {
            "total_defeitos": 0,
            "defeitos_planejamento": 0,
            "percentual_planejamento": 0.0,
            "severidade_media": 0.0,
            "fase_mais_problematica": "N/A",
        }

    fases_planejamento = {"requisitos", "arquitetura", "design"}
    defeitos_plan = sum(
        1 for d in defeitos
        if isinstance(d, dict) and d.get("fase_origem", "").lower() in fases_planejamento
    )

    severidades_num = [
        SEVERIDADES.get(d.get("severidade", "media").lower(), 2)
        for d in defeitos if isinstance(d, dict)
    ]

    contagem_fases = Counter(
        d.get("fase_origem", "desconhecida").lower()
        for d in defeitos if isinstance(d, dict)
    )
    fase_pior = contagem_fases.most_common(1)[0][0] if contagem_fases else "N/A"

    return {
        "total_defeitos": total,
        "defeitos_planejamento": defeitos_plan,
        "percentual_planejamento": round((defeitos_plan / total) * 100, 1),
        "severidade_media": round(sum(severidades_num) / len(severidades_num), 2) if severidades_num else 0,
        "fase_mais_problematica": FASES_ORIGEM.get(fase_pior, {}).get("nome", fase_pior),
    }


def gerar_recomendacoes(distribuicao: dict, tipos_por_fase: dict) -> list[str]:
    """Gera recomendações baseadas na análise de defeitos."""
    recomendacoes = []

    for fase, info in distribuicao.items():
        if info["percentual"] > 30 and fase == "requisitos":
            recomendacoes.append(
                "Alta concentração de defeitos originados em requisitos. "
                "Recomenda-se: revisão por pares de requisitos, workshops de "
                "elicitação mais frequentes e uso de templates padronizados."
            )
        elif info["percentual"] > 25 and fase == "arquitetura":
            recomendacoes.append(
                "Muitos defeitos com origem arquitetural. Recomenda-se: "
                "provas de conceito para decisões críticas, revisão arquitetural "
                "formal e documentação de trade-offs."
            )
        elif info["percentual"] > 20 and fase == "design":
            recomendacoes.append(
                "Quantidade significativa de defeitos de design. Recomenda-se: "
                "design reviews mais rigorosos, protótipos e validação antecipada."
            )

    # Recomendações por tipo
    todos_tipos = Counter()
    for fase_tipos in tipos_por_fase.values():
        for item in fase_tipos:
            todos_tipos[item["tipo"]] += item["quantidade"]

    tipo_pior = todos_tipos.most_common(1)
    if tipo_pior:
        tipo, qtd = tipo_pior[0]
        if tipo == "ambiguidade":
            recomendacoes.append(
                f"O tipo mais frequente é 'ambiguidade' ({qtd} ocorrências). "
                "Invista em detecção precoce de ambiguidades e clarificação de requisitos."
            )
        elif tipo == "incompletude":
            recomendacoes.append(
                f"O tipo mais frequente é 'incompletude' ({qtd} ocorrências). "
                "Use checklists de completude e revise critérios de aceite."
            )
        elif tipo == "inconsistencia":
            recomendacoes.append(
                f"O tipo mais frequente é 'inconsistência' ({qtd} ocorrências). "
                "Implemente rastreabilidade bidirecional entre artefatos."
            )

    if not recomendacoes:
        recomendacoes.append("Distribuição dentro dos parâmetros esperados. Manter práticas atuais.")

    return recomendacoes


# ---------------------------------------------------------------------------
# Geração do relatório
# ---------------------------------------------------------------------------

def gerar_relatorio(dados: dict, incluir_recomendacoes: bool = True) -> dict:
    """Gera o relatório completo de origem de defeitos."""
    defeitos = extrair_defeitos(dados)

    distribuicao = analisar_distribuicao_por_fase(defeitos)
    custos = calcular_custo_relativo(defeitos)
    tipos = analisar_tipos_por_fase(defeitos)
    resumo = calcular_metricas_resumo(defeitos)

    relatorio = {
        "data_geracao": datetime.now().isoformat(),
        "resumo": resumo,
        "distribuicao_por_fase": distribuicao,
        "custo_relativo": custos,
        "tipos_por_fase": tipos,
    }

    if incluir_recomendacoes:
        relatorio["recomendacoes"] = gerar_recomendacoes(distribuicao, tipos)

    return relatorio


# ---------------------------------------------------------------------------
# Formatação
# ---------------------------------------------------------------------------

def formatar_texto(relatorio: dict) -> str:
    """Formata o relatório como texto."""
    linhas = []
    linhas.append("=" * 65)
    linhas.append("  RELATÓRIO DE ORIGEM DE DEFEITOS")
    linhas.append("=" * 65)
    linhas.append(f"\nData: {relatorio['data_geracao']}")

    r = relatorio["resumo"]
    linhas.append(f"\nResumo:")
    linhas.append(f"  Total de defeitos:             {r['total_defeitos']}")
    linhas.append(f"  Originados no planejamento:    {r['defeitos_planejamento']} ({r['percentual_planejamento']}%)")
    linhas.append(f"  Severidade média:              {r['severidade_media']}")
    linhas.append(f"  Fase mais problemática:        {r['fase_mais_problematica']}")

    linhas.append(f"\n{'-' * 65}")
    linhas.append("DISTRIBUIÇÃO POR FASE DE ORIGEM:")
    linhas.append(f"{'Fase':<25} {'Qtd':>5} {'%':>7}")
    linhas.append("-" * 40)
    for fase, info in relatorio["distribuicao_por_fase"].items():
        barra = "#" * int(info["percentual"] / 3)
        linhas.append(f"{info['nome']:<25} {info['quantidade']:>5} {info['percentual']:>6.1f}% {barra}")

    linhas.append(f"\n{'-' * 65}")
    linhas.append("CUSTO RELATIVO POR FASE:")
    linhas.append(f"{'Fase':<25} {'Custo Total':>12} {'Custo Médio':>12}")
    linhas.append("-" * 52)
    for fase, info in sorted(
        relatorio["custo_relativo"].items(),
        key=lambda x: x[1]["custo_total_relativo"],
        reverse=True,
    ):
        linhas.append(
            f"{info['nome']:<25} {info['custo_total_relativo']:>12.1f} {info['custo_medio']:>12.1f}"
        )

    if "recomendacoes" in relatorio:
        linhas.append(f"\n{'-' * 65}")
        linhas.append("RECOMENDAÇÕES:")
        for i, rec in enumerate(relatorio["recomendacoes"], 1):
            linhas.append(f"\n  {i}. {rec}")

    linhas.append(f"\n{'=' * 65}")
    return "\n".join(linhas)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def criar_parser() -> argparse.ArgumentParser:
    """Cria o parser de argumentos."""
    parser = argparse.ArgumentParser(
        description="Gera relatório de origem de defeitos.",
    )
    parser.add_argument("arquivo", help="Dados de defeitos (YAML/JSON).")
    parser.add_argument(
        "--format", choices=["text", "json"], default="text",
        help="Formato de saída.",
    )
    parser.add_argument(
        "--include-recommendations", action="store_true", default=True,
        help="Incluir recomendações (padrão: True).",
    )
    parser.add_argument("--output-file", default=None, help="Arquivo de saída.")
    return parser


def main():
    """Ponto de entrada principal."""
    parser = criar_parser()
    args = parser.parse_args()

    dados = carregar_dados(args.arquivo)
    relatorio = gerar_relatorio(dados, args.include_recommendations)

    if args.format == "json":
        saida = json.dumps(relatorio, indent=2, ensure_ascii=False)
    else:
        saida = formatar_texto(relatorio)

    if args.output_file:
        Path(args.output_file).write_text(saida, encoding="utf-8")
        print(f"Relatório salvo em: {args.output_file}")
    else:
        print(saida)


if __name__ == "__main__":
    main()
