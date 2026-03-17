#!/usr/bin/env python3
"""
Construtor de Mapa de Dependências.

Este script constrói um mapa de dependências entre componentes do projeto
a partir de definições em YAML, gerando visualizações e análises de
acoplamento, ciclos e caminhos críticos.

Funcionalidades:
  - Parsing de dependências de YAML/JSON
  - Detecção de ciclos de dependência
  - Cálculo de ordem topológica
  - Identificação de componentes críticos (alto fan-in/fan-out)
  - Geração de mapa em formato DOT (Graphviz), JSON ou texto
  - Análise de impacto de mudanças

Uso:
  python dependency-map-builder.py <arquivo_deps> [--format text|json|dot] [--analyze]
"""

import argparse
import json
import sys
from collections import defaultdict, deque
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


# ---------------------------------------------------------------------------
# Carregamento
# ---------------------------------------------------------------------------

def carregar_dados(caminho: str) -> dict:
    """Carrega definições de dependências."""
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


def extrair_dependencias(dados: dict) -> dict[str, list[str]]:
    """
    Extrai o grafo de dependências dos dados.

    Aceita formatos:
      - {"componentes": [{"nome": "A", "depende_de": ["B", "C"]}]}
      - {"dependencias": {"A": ["B", "C"]}}
      - {"A": {"depends_on": ["B"]}}
    """
    deps = {}

    if "componentes" in dados:
        for comp in dados["componentes"]:
            if isinstance(comp, dict):
                nome = comp.get("nome", comp.get("name", ""))
                dep_list = comp.get("depende_de", comp.get("depends_on", []))
                if isinstance(dep_list, str):
                    dep_list = [dep_list]
                deps[nome] = dep_list

    elif "dependencias" in dados or "dependencies" in dados:
        raw = dados.get("dependencias", dados.get("dependencies", {}))
        if isinstance(raw, dict):
            for chave, valor in raw.items():
                if isinstance(valor, list):
                    deps[chave] = valor
                elif isinstance(valor, str):
                    deps[chave] = [valor]

    else:
        for chave, valor in dados.items():
            if isinstance(valor, dict):
                dep_list = valor.get("depende_de", valor.get("depends_on", []))
                if isinstance(dep_list, str):
                    dep_list = [dep_list]
                deps[chave] = dep_list
            elif isinstance(valor, list):
                deps[chave] = valor

    # Garantir que todos os nós referenciados existam
    todos_nos = set(deps.keys())
    for dep_list in deps.values():
        todos_nos.update(dep_list)
    for no in todos_nos:
        if no not in deps:
            deps[no] = []

    return deps


# ---------------------------------------------------------------------------
# Análise do grafo
# ---------------------------------------------------------------------------

def detectar_ciclos(deps: dict[str, list[str]]) -> list[list[str]]:
    """Detecta ciclos no grafo de dependências usando DFS."""
    ciclos = []
    visitados = set()
    em_pilha = set()
    caminho = []

    def dfs(no: str):
        visitados.add(no)
        em_pilha.add(no)
        caminho.append(no)

        for vizinho in deps.get(no, []):
            if vizinho not in visitados:
                dfs(vizinho)
            elif vizinho in em_pilha:
                idx = caminho.index(vizinho)
                ciclo = caminho[idx:] + [vizinho]
                ciclos.append(ciclo)

        caminho.pop()
        em_pilha.discard(no)

    for no in deps:
        if no not in visitados:
            dfs(no)

    return ciclos


def ordenacao_topologica(deps: dict[str, list[str]]) -> list[str] | None:
    """Retorna a ordem topológica ou None se houver ciclos."""
    grau_entrada = defaultdict(int)
    for no in deps:
        if no not in grau_entrada:
            grau_entrada[no] = 0
        for dep in deps[no]:
            grau_entrada[dep] += 0  # Garantir que existe
    for no, dep_list in deps.items():
        for dep in dep_list:
            grau_entrada[no] += 0  # O nó depende de dep, não o contrário

    # Recalcular: grau de entrada = quantos dependem deste nó
    grau = defaultdict(int)
    grafo_reverso = defaultdict(list)
    for no, dep_list in deps.items():
        for dep in dep_list:
            grafo_reverso[dep].append(no)
            grau[no] += 1
        if no not in grau:
            grau[no] = 0

    fila = deque(no for no in deps if grau[no] == 0)
    ordem = []

    while fila:
        no = fila.popleft()
        ordem.append(no)
        for vizinho in grafo_reverso.get(no, []):
            grau[vizinho] -= 1
            if grau[vizinho] == 0:
                fila.append(vizinho)

    if len(ordem) != len(deps):
        return None  # Ciclo detectado
    return ordem


def calcular_metricas(deps: dict[str, list[str]]) -> dict:
    """Calcula métricas do grafo de dependências."""
    fan_out = {}  # Quantas dependências cada componente tem
    fan_in = defaultdict(int)  # Quantos componentes dependem deste

    for no, dep_list in deps.items():
        fan_out[no] = len(dep_list)
        for dep in dep_list:
            fan_in[dep] += 1

    # Garantir todos os nós
    for no in deps:
        if no not in fan_in:
            fan_in[no] = 0

    total_arestas = sum(fan_out.values())
    total_nos = len(deps)
    densidade = (total_arestas / (total_nos * (total_nos - 1))) if total_nos > 1 else 0

    # Componentes críticos (alto fan-in ou fan-out)
    limiar = max(2, total_nos * 0.3)
    criticos = [
        no for no in deps
        if fan_in.get(no, 0) >= limiar or fan_out.get(no, 0) >= limiar
    ]

    # Componentes isolados
    isolados = [no for no in deps if fan_in.get(no, 0) == 0 and fan_out.get(no, 0) == 0]

    # Folhas (sem dependentes)
    folhas = [no for no in deps if fan_in.get(no, 0) == 0 and fan_out.get(no, 0) > 0]

    return {
        "total_componentes": total_nos,
        "total_dependencias": total_arestas,
        "densidade": round(densidade, 4),
        "fan_in": dict(fan_in),
        "fan_out": fan_out,
        "componentes_criticos": criticos,
        "componentes_isolados": isolados,
        "folhas": folhas,
    }


def analise_impacto(deps: dict[str, list[str]], componente: str) -> dict:
    """Calcula o impacto de mudança em um componente."""
    # BFS reverso: quem depende deste componente (direta e transitivamente)
    grafo_reverso = defaultdict(list)
    for no, dep_list in deps.items():
        for dep in dep_list:
            grafo_reverso[dep].append(no)

    impactados = set()
    fila = deque([componente])
    while fila:
        atual = fila.popleft()
        for dependente in grafo_reverso.get(atual, []):
            if dependente not in impactados:
                impactados.add(dependente)
                fila.append(dependente)

    return {
        "componente": componente,
        "impacto_direto": grafo_reverso.get(componente, []),
        "impacto_transitivo": list(impactados),
        "total_impactados": len(impactados),
    }


# ---------------------------------------------------------------------------
# Construção do mapa
# ---------------------------------------------------------------------------

def construir_mapa(caminho: str, analisar: bool = True, componente_impacto: str | None = None) -> dict:
    """
    Constrói o mapa de dependências completo.

    Args:
        caminho: Caminho para o arquivo de dependências.
        analisar: Se True, inclui análises detalhadas.
        componente_impacto: Componente para análise de impacto.

    Returns:
        Mapa completo com dependências, análises e métricas.
    """
    dados = carregar_dados(caminho)
    deps = extrair_dependencias(dados)

    mapa = {
        "componentes": list(deps.keys()),
        "dependencias": deps,
        "total_componentes": len(deps),
    }

    if analisar:
        ciclos = detectar_ciclos(deps)
        ordem = ordenacao_topologica(deps)
        metricas = calcular_metricas(deps)

        mapa["ciclos"] = ciclos
        mapa["tem_ciclos"] = len(ciclos) > 0
        mapa["ordem_topologica"] = ordem
        mapa["metricas"] = metricas

    if componente_impacto and componente_impacto in deps:
        mapa["analise_impacto"] = analise_impacto(deps, componente_impacto)

    return mapa


# ---------------------------------------------------------------------------
# Formatação
# ---------------------------------------------------------------------------

def formatar_texto(mapa: dict) -> str:
    """Formata o mapa como texto."""
    linhas = []
    linhas.append("=" * 60)
    linhas.append("  MAPA DE DEPENDÊNCIAS")
    linhas.append("=" * 60)
    linhas.append(f"\nTotal de componentes: {mapa['total_componentes']}")

    linhas.append(f"\n{'-' * 60}")
    linhas.append("DEPENDÊNCIAS:")
    for comp, deps in sorted(mapa["dependencias"].items()):
        if deps:
            linhas.append(f"  {comp} -> {', '.join(deps)}")
        else:
            linhas.append(f"  {comp} (sem dependências)")

    if "metricas" in mapa:
        m = mapa["metricas"]
        linhas.append(f"\n{'-' * 60}")
        linhas.append("MÉTRICAS:")
        linhas.append(f"  Total dependências: {m['total_dependencias']}")
        linhas.append(f"  Densidade do grafo: {m['densidade']}")
        if m["componentes_criticos"]:
            linhas.append(f"  Componentes críticos: {', '.join(m['componentes_criticos'])}")
        if m["componentes_isolados"]:
            linhas.append(f"  Componentes isolados: {', '.join(m['componentes_isolados'])}")

    if "ciclos" in mapa and mapa["ciclos"]:
        linhas.append(f"\n{'-' * 60}")
        linhas.append("CICLOS DETECTADOS:")
        for i, ciclo in enumerate(mapa["ciclos"], 1):
            linhas.append(f"  {i}. {' -> '.join(ciclo)}")

    if "ordem_topologica" in mapa and mapa["ordem_topologica"]:
        linhas.append(f"\n{'-' * 60}")
        linhas.append("ORDEM TOPOLÓGICA (ordem de build):")
        for i, comp in enumerate(mapa["ordem_topologica"], 1):
            linhas.append(f"  {i}. {comp}")

    if "analise_impacto" in mapa:
        ai = mapa["analise_impacto"]
        linhas.append(f"\n{'-' * 60}")
        linhas.append(f"ANÁLISE DE IMPACTO: {ai['componente']}")
        linhas.append(f"  Impacto direto: {', '.join(ai['impacto_direto']) or 'nenhum'}")
        linhas.append(f"  Total impactados: {ai['total_impactados']}")

    linhas.append(f"\n{'=' * 60}")
    return "\n".join(linhas)


def formatar_dot(mapa: dict) -> str:
    """Formata o mapa como DOT (Graphviz)."""
    linhas = ["digraph DependencyMap {", '  rankdir=LR;', '  node [shape=box, style=filled, fillcolor=lightblue];']

    criticos = set(mapa.get("metricas", {}).get("componentes_criticos", []))

    for comp in mapa["componentes"]:
        cor = "salmon" if comp in criticos else "lightblue"
        linhas.append(f'  "{comp}" [fillcolor={cor}];')

    for comp, deps in mapa["dependencias"].items():
        for dep in deps:
            linhas.append(f'  "{comp}" -> "{dep}";')

    linhas.append("}")
    return "\n".join(linhas)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def criar_parser() -> argparse.ArgumentParser:
    """Cria o parser de argumentos."""
    parser = argparse.ArgumentParser(
        description="Constrói mapa de dependências a partir de YAML/JSON.",
    )
    parser.add_argument("arquivo", help="Arquivo de dependências.")
    parser.add_argument(
        "--format", choices=["text", "json", "dot"], default="text",
        help="Formato de saída.",
    )
    parser.add_argument("--analyze", action="store_true", default=True, help="Incluir análise.")
    parser.add_argument("--impact", default=None, help="Componente para análise de impacto.")
    parser.add_argument("--output-file", default=None, help="Arquivo de saída.")
    return parser


def main():
    """Ponto de entrada principal."""
    parser = criar_parser()
    args = parser.parse_args()

    mapa = construir_mapa(args.arquivo, args.analyze, args.impact)

    if args.format == "json":
        saida = json.dumps(mapa, indent=2, ensure_ascii=False)
    elif args.format == "dot":
        saida = formatar_dot(mapa)
    else:
        saida = formatar_texto(mapa)

    if args.output_file:
        Path(args.output_file).write_text(saida, encoding="utf-8")
        print(f"Mapa salvo em: {args.output_file}")
    else:
        print(saida)


if __name__ == "__main__":
    main()
