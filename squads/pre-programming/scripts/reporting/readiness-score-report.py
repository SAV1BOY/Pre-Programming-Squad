#!/usr/bin/env python3
"""
Relatório de Score de Prontidão.

Este script gera um relatório detalhado do score de prontidão de um projeto,
avaliando múltiplas dimensões como completude de artefatos, qualidade da
documentação, cobertura de riscos e preparação técnica.

Dimensões avaliadas:
  - Completude de artefatos (peso: 25%)
  - Clareza de requisitos (peso: 20%)
  - Cobertura de riscos (peso: 15%)
  - Qualidade arquitetural (peso: 15%)
  - Preparação de testes (peso: 10%)
  - Plano de rollout (peso: 10%)
  - Aprovações e sign-offs (peso: 5%)

Uso:
  python readiness-score-report.py <caminho_dados> [--format text|json|html] [--threshold N]
"""

import argparse
import json
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

DIMENSOES = {
    "completude_artefatos": {"peso": 0.25, "nome": "Completude de Artefatos"},
    "clareza_requisitos": {"peso": 0.20, "nome": "Clareza de Requisitos"},
    "cobertura_riscos": {"peso": 0.15, "nome": "Cobertura de Riscos"},
    "qualidade_arquitetural": {"peso": 0.15, "nome": "Qualidade Arquitetural"},
    "preparacao_testes": {"peso": 0.10, "nome": "Preparação de Testes"},
    "plano_rollout": {"peso": 0.10, "nome": "Plano de Rollout"},
    "aprovacoes": {"peso": 0.05, "nome": "Aprovações e Sign-offs"},
}

CLASSIFICACOES = [
    (90, "Excelente", "Projeto pronto para iniciar desenvolvimento."),
    (75, "Bom", "Projeto pode iniciar com ressalvas menores."),
    (60, "Regular", "Necessita melhorias antes de iniciar desenvolvimento."),
    (40, "Insuficiente", "Lacunas significativas precisam ser endereçadas."),
    (0, "Crítico", "Projeto não está pronto. Revisão completa necessária."),
]


# ---------------------------------------------------------------------------
# Carregamento de dados
# ---------------------------------------------------------------------------

def carregar_dados(caminho: str) -> dict:
    """Carrega dados do projeto de um arquivo YAML ou JSON."""
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
# Cálculo de métricas
# ---------------------------------------------------------------------------

def calcular_completude_artefatos(dados: dict) -> tuple[float, list[str]]:
    """Calcula score de completude de artefatos (0-100)."""
    artefatos_esperados = [
        "project_brief", "architecture_notes", "risk_register",
        "test_plan", "api_contracts", "acceptance_criteria",
        "decision_log", "dependency_map",
    ]
    artefatos = dados.get("artefatos", {})
    detalhes = []
    presentes = 0

    for art in artefatos_esperados:
        if art in artefatos and artefatos[art]:
            presentes += 1
            detalhes.append(f"  [OK] {art}")
        else:
            detalhes.append(f"  [--] {art}")

    score = (presentes / len(artefatos_esperados)) * 100
    return score, detalhes


def calcular_clareza_requisitos(dados: dict) -> tuple[float, list[str]]:
    """Calcula score de clareza dos requisitos (0-100)."""
    requisitos = dados.get("requisitos", dados.get("requirements", []))
    detalhes = []

    if not requisitos:
        return 0.0, ["  Nenhum requisito encontrado."]

    total = len(requisitos)
    claros = 0

    for req in requisitos:
        if isinstance(req, dict):
            tem_descricao = bool(req.get("descricao", "").strip())
            tem_criterio = bool(req.get("criterio_aceite") or req.get("acceptance_criteria"))
            tem_prioridade = bool(req.get("prioridade") or req.get("priority"))

            pontos = sum([tem_descricao, tem_criterio, tem_prioridade])
            if pontos >= 2:
                claros += 1
        elif isinstance(req, str) and len(req.strip()) > 20:
            claros += 0.5

    score = (claros / total) * 100 if total > 0 else 0
    detalhes.append(f"  Total de requisitos: {total}")
    detalhes.append(f"  Requisitos claros: {int(claros)}")
    detalhes.append(f"  Percentual de clareza: {score:.1f}%")
    return score, detalhes


def calcular_cobertura_riscos(dados: dict) -> tuple[float, list[str]]:
    """Calcula score de cobertura de riscos (0-100)."""
    riscos = dados.get("riscos", dados.get("risk_register", {}).get("riscos", []))
    detalhes = []

    if not riscos:
        return 0.0, ["  Nenhum risco documentado."]

    total = len(riscos)
    com_mitigacao = 0
    com_responsavel = 0

    for risco in riscos:
        if isinstance(risco, dict):
            if risco.get("mitigacao") or risco.get("plano_mitigacao"):
                com_mitigacao += 1
            if risco.get("responsavel"):
                com_responsavel += 1

    score_mitigacao = (com_mitigacao / total) * 60
    score_responsavel = (com_responsavel / total) * 20
    score_quantidade = min(total / 5, 1.0) * 20  # 5+ riscos = pontuação máxima

    score = score_mitigacao + score_responsavel + score_quantidade
    detalhes.append(f"  Total de riscos: {total}")
    detalhes.append(f"  Com mitigação: {com_mitigacao}")
    detalhes.append(f"  Com responsável: {com_responsavel}")
    return score, detalhes


def calcular_qualidade_arquitetural(dados: dict) -> tuple[float, list[str]]:
    """Calcula score de qualidade arquitetural (0-100)."""
    arquitetura = dados.get("architecture_notes", dados.get("arquitetura", {}))
    detalhes = []
    pontos = 0
    max_pontos = 5

    checks = {
        "Decisões documentadas": bool(arquitetura.get("decisoes") or arquitetura.get("decisions")),
        "Diagramas presentes": bool(arquitetura.get("diagramas") or arquitetura.get("diagrams")),
        "Componentes listados": bool(arquitetura.get("componentes") or arquitetura.get("components")),
        "Integrações mapeadas": bool(arquitetura.get("integracoes") or arquitetura.get("integrations")),
        "Restrições definidas": bool(arquitetura.get("restricoes") or arquitetura.get("constraints")),
    }

    for nome, resultado in checks.items():
        if resultado:
            pontos += 1
            detalhes.append(f"  [OK] {nome}")
        else:
            detalhes.append(f"  [--] {nome}")

    score = (pontos / max_pontos) * 100
    return score, detalhes


def calcular_preparacao_testes(dados: dict) -> tuple[float, list[str]]:
    """Calcula score de preparação de testes (0-100)."""
    testes = dados.get("test_plan", dados.get("plano_testes", {}))
    detalhes = []
    pontos = 0
    max_pontos = 4

    checks = {
        "Estratégia definida": bool(testes.get("estrategia") or testes.get("strategy")),
        "Cenários documentados": bool(testes.get("cenarios") or testes.get("scenarios")),
        "Dados de teste": bool(testes.get("dados_teste") or testes.get("test_data")),
        "Critérios de cobertura": bool(testes.get("cobertura") or testes.get("coverage")),
    }

    for nome, resultado in checks.items():
        if resultado:
            pontos += 1
            detalhes.append(f"  [OK] {nome}")
        else:
            detalhes.append(f"  [--] {nome}")

    score = (pontos / max_pontos) * 100
    return score, detalhes


def calcular_plano_rollout(dados: dict) -> tuple[float, list[str]]:
    """Calcula score do plano de rollout (0-100)."""
    rollout = dados.get("rollout_plan", dados.get("plano_rollout", {}))
    detalhes = []
    pontos = 0
    max_pontos = 4

    checks = {
        "Estratégia de deploy": bool(rollout.get("estrategia") or rollout.get("strategy")),
        "Plano de rollback": bool(rollout.get("rollback")),
        "Feature flags": bool(rollout.get("feature_flags")),
        "Monitoramento definido": bool(rollout.get("monitoramento") or rollout.get("monitoring")),
    }

    for nome, resultado in checks.items():
        if resultado:
            pontos += 1
            detalhes.append(f"  [OK] {nome}")
        else:
            detalhes.append(f"  [--] {nome}")

    score = (pontos / max_pontos) * 100
    return score, detalhes


def calcular_aprovacoes(dados: dict) -> tuple[float, list[str]]:
    """Calcula score de aprovações (0-100)."""
    aprovacoes = dados.get("aprovacoes", dados.get("approvals", []))
    detalhes = []

    if not aprovacoes:
        return 0.0, ["  Nenhuma aprovação registrada."]

    total = len(aprovacoes)
    aprovados = sum(
        1 for a in aprovacoes
        if isinstance(a, dict) and a.get("status", "").lower() in ("aprovado", "approved")
    )

    score = (aprovados / total) * 100 if total > 0 else 0
    detalhes.append(f"  Total de aprovações necessárias: {total}")
    detalhes.append(f"  Aprovadas: {aprovados}")
    return score, detalhes


# ---------------------------------------------------------------------------
# Geração do relatório
# ---------------------------------------------------------------------------

def calcular_score_total(dados: dict) -> dict:
    """Calcula o score total de prontidão com detalhamento por dimensão."""
    calculadoras = {
        "completude_artefatos": calcular_completude_artefatos,
        "clareza_requisitos": calcular_clareza_requisitos,
        "cobertura_riscos": calcular_cobertura_riscos,
        "qualidade_arquitetural": calcular_qualidade_arquitetural,
        "preparacao_testes": calcular_preparacao_testes,
        "plano_rollout": calcular_plano_rollout,
        "aprovacoes": calcular_aprovacoes,
    }

    resultados = {}
    score_ponderado = 0.0

    for dimensao, calc in calculadoras.items():
        score, detalhes = calc(dados)
        peso = DIMENSOES[dimensao]["peso"]
        nome = DIMENSOES[dimensao]["nome"]
        contribuicao = score * peso

        resultados[dimensao] = {
            "nome": nome,
            "score": round(score, 1),
            "peso": peso,
            "contribuicao": round(contribuicao, 1),
            "detalhes": detalhes,
        }
        score_ponderado += contribuicao

    score_final = round(score_ponderado, 1)

    # Classificação
    classificacao = "Desconhecido"
    recomendacao = ""
    for limiar, classe, rec in CLASSIFICACOES:
        if score_final >= limiar:
            classificacao = classe
            recomendacao = rec
            break

    return {
        "score_total": score_final,
        "classificacao": classificacao,
        "recomendacao": recomendacao,
        "dimensoes": resultados,
        "data_geracao": datetime.now().isoformat(),
    }


def gerar_relatorio(dados: dict, limiar: int) -> dict:
    """Gera o relatório completo de prontidão."""
    resultado = calcular_score_total(dados)
    resultado["limiar"] = limiar
    resultado["aprovado"] = resultado["score_total"] >= limiar

    # Identificar dimensões críticas
    criticas = []
    for dim, info in resultado["dimensoes"].items():
        if info["score"] < 50:
            criticas.append(info["nome"])
    resultado["dimensoes_criticas"] = criticas

    return resultado


# ---------------------------------------------------------------------------
# Formatação de saída
# ---------------------------------------------------------------------------

def formatar_texto(relatorio: dict) -> str:
    """Formata o relatório como texto."""
    linhas = []
    linhas.append("=" * 60)
    linhas.append("  RELATÓRIO DE SCORE DE PRONTIDÃO")
    linhas.append("=" * 60)
    linhas.append(f"\nData de geração: {relatorio['data_geracao']}")
    linhas.append(f"\nScore Total: {relatorio['score_total']}%")
    linhas.append(f"Classificação: {relatorio['classificacao']}")
    linhas.append(f"Limiar mínimo: {relatorio['limiar']}%")
    status = "APROVADO" if relatorio["aprovado"] else "REPROVADO"
    linhas.append(f"Status: {status}")
    linhas.append(f"\nRecomendação: {relatorio['recomendacao']}")

    linhas.append(f"\n{'-' * 60}")
    linhas.append("DETALHAMENTO POR DIMENSÃO")
    linhas.append("-" * 60)

    for dim_key, dim in relatorio["dimensoes"].items():
        barra = "#" * int(dim["score"] / 5) + "." * (20 - int(dim["score"] / 5))
        linhas.append(f"\n{dim['nome']} (peso: {dim['peso']*100:.0f}%)")
        linhas.append(f"  Score: {dim['score']}% [{barra}]")
        linhas.append(f"  Contribuição: {dim['contribuicao']}%")
        for detalhe in dim["detalhes"]:
            linhas.append(f"  {detalhe}")

    if relatorio["dimensoes_criticas"]:
        linhas.append(f"\n{'=' * 60}")
        linhas.append("DIMENSÕES CRÍTICAS (score < 50%):")
        for d in relatorio["dimensoes_criticas"]:
            linhas.append(f"  * {d}")

    linhas.append(f"\n{'=' * 60}")
    return "\n".join(linhas)


def formatar_html(relatorio: dict) -> str:
    """Formata o relatório como HTML simples."""
    html_parts = [
        "<!DOCTYPE html>",
        "<html lang='pt-BR'><head><meta charset='utf-8'>",
        "<title>Relatório de Prontidão</title>",
        "<style>body{font-family:sans-serif;max-width:800px;margin:auto;padding:20px}",
        ".score{font-size:2em;font-weight:bold}",
        ".ok{color:green}.warn{color:orange}.fail{color:red}",
        "table{border-collapse:collapse;width:100%}",
        "td,th{border:1px solid #ddd;padding:8px;text-align:left}",
        "th{background:#f4f4f4}</style></head><body>",
        "<h1>Relatório de Score de Prontidão</h1>",
        f"<p>Data: {relatorio['data_geracao']}</p>",
    ]

    css_class = "ok" if relatorio["aprovado"] else "fail"
    html_parts.append(
        f"<p class='score {css_class}'>{relatorio['score_total']}% - {relatorio['classificacao']}</p>"
    )
    html_parts.append(f"<p><strong>Recomendação:</strong> {relatorio['recomendacao']}</p>")

    html_parts.append("<h2>Dimensões</h2><table><tr><th>Dimensão</th><th>Score</th><th>Peso</th><th>Contribuição</th></tr>")
    for dim in relatorio["dimensoes"].values():
        html_parts.append(
            f"<tr><td>{dim['nome']}</td><td>{dim['score']}%</td>"
            f"<td>{dim['peso']*100:.0f}%</td><td>{dim['contribuicao']}%</td></tr>"
        )
    html_parts.append("</table></body></html>")
    return "\n".join(html_parts)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def criar_parser() -> argparse.ArgumentParser:
    """Cria o parser de argumentos."""
    parser = argparse.ArgumentParser(
        description="Gera relatório de score de prontidão do projeto.",
    )
    parser.add_argument("arquivo", help="Caminho para dados do projeto (YAML/JSON).")
    parser.add_argument(
        "--format", choices=["text", "json", "html"], default="text",
        help="Formato de saída (padrão: text).",
    )
    parser.add_argument(
        "--threshold", type=int, default=70,
        help="Limiar mínimo de aprovação (padrão: 70).",
    )
    parser.add_argument("--output-file", default=None, help="Arquivo de saída.")
    return parser


def main():
    """Ponto de entrada principal."""
    parser = criar_parser()
    args = parser.parse_args()

    dados = carregar_dados(args.arquivo)
    relatorio = gerar_relatorio(dados, args.threshold)

    if args.format == "json":
        saida = json.dumps(relatorio, indent=2, ensure_ascii=False)
    elif args.format == "html":
        saida = formatar_html(relatorio)
    else:
        saida = formatar_texto(relatorio)

    if args.output_file:
        Path(args.output_file).write_text(saida, encoding="utf-8")
        print(f"Relatório salvo em: {args.output_file}")
    else:
        print(saida)

    sys.exit(0 if relatorio["aprovado"] else 1)


if __name__ == "__main__":
    main()
