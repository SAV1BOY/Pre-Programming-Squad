#!/usr/bin/env python3
"""
Executor de Checklists de Validação.

Este script executa checklists de validação definidos em arquivos YAML ou JSON,
verificando automaticamente itens que podem ser avaliados programaticamente e
reportando o status geral de completude.

Funcionalidades:
  - Carregamento de checklists de múltiplos formatos (YAML, JSON)
  - Verificação automática de itens baseados em regras
  - Suporte a verificações de arquivos (existência, tamanho, conteúdo)
  - Suporte a verificações de campos em documentos
  - Relatório detalhado de itens pendentes, aprovados e reprovados
  - Modo interativo e modo batch

Uso:
  python checklist-runner.py <checklist> [--data <dados_projeto>] [--format text|json]
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------

TIPOS_VERIFICACAO = [
    "arquivo_existe",
    "campo_presente",
    "campo_nao_vazio",
    "campo_minimo",
    "contagem_minima",
    "padrao_regex",
    "manual",
]


# ---------------------------------------------------------------------------
# Carregamento
# ---------------------------------------------------------------------------

def carregar_arquivo(caminho: str) -> dict | list:
    """Carrega um arquivo YAML ou JSON."""
    caminho = Path(caminho)
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    conteudo = caminho.read_text(encoding="utf-8")
    if caminho.suffix in (".yaml", ".yml"):
        if yaml is None:
            raise ImportError("PyYAML necessário.")
        return yaml.safe_load(conteudo)
    if caminho.suffix == ".json":
        return json.loads(conteudo)
    raise ValueError(f"Formato não suportado: {caminho.suffix}")


def extrair_checklist(dados) -> list[dict]:
    """Extrai itens do checklist dos dados carregados."""
    if isinstance(dados, list):
        return dados
    if isinstance(dados, dict):
        return dados.get("checklist", dados.get("itens", dados.get("items", [])))
    return []


# ---------------------------------------------------------------------------
# Motor de verificação
# ---------------------------------------------------------------------------

def executar_verificacao(item: dict, dados_projeto: dict | None, base_dir: Path) -> dict:
    """
    Executa a verificação de um item do checklist.

    Args:
        item: Definição do item do checklist.
        dados_projeto: Dados do projeto para verificação contextual.
        base_dir: Diretório base para resolver caminhos de arquivos.

    Returns:
        Resultado da verificação com status e mensagem.
    """
    tipo = item.get("tipo", item.get("type", "manual"))
    nome = item.get("nome", item.get("name", item.get("descricao", "Item sem nome")))

    resultado = {
        "nome": nome,
        "tipo": tipo,
        "status": "pendente",
        "mensagem": "",
        "categoria": item.get("categoria", item.get("category", "geral")),
        "obrigatorio": item.get("obrigatorio", item.get("required", True)),
    }

    try:
        if tipo == "arquivo_existe":
            caminho = item.get("caminho", item.get("path", ""))
            caminho_completo = base_dir / caminho
            if caminho_completo.exists():
                resultado["status"] = "aprovado"
                resultado["mensagem"] = f"Arquivo encontrado: {caminho}"
            else:
                resultado["status"] = "reprovado"
                resultado["mensagem"] = f"Arquivo não encontrado: {caminho}"

        elif tipo == "campo_presente":
            campo = item.get("campo", item.get("field", ""))
            if dados_projeto and _resolver_campo(dados_projeto, campo) is not None:
                resultado["status"] = "aprovado"
                resultado["mensagem"] = f"Campo '{campo}' presente."
            else:
                resultado["status"] = "reprovado"
                resultado["mensagem"] = f"Campo '{campo}' ausente."

        elif tipo == "campo_nao_vazio":
            campo = item.get("campo", item.get("field", ""))
            valor = _resolver_campo(dados_projeto, campo) if dados_projeto else None
            if valor and (not isinstance(valor, str) or valor.strip()):
                resultado["status"] = "aprovado"
                resultado["mensagem"] = f"Campo '{campo}' preenchido."
            else:
                resultado["status"] = "reprovado"
                resultado["mensagem"] = f"Campo '{campo}' vazio ou ausente."

        elif tipo == "campo_minimo":
            campo = item.get("campo", item.get("field", ""))
            minimo = item.get("minimo", item.get("min", 0))
            valor = _resolver_campo(dados_projeto, campo) if dados_projeto else None
            if isinstance(valor, str) and len(valor.strip()) >= minimo:
                resultado["status"] = "aprovado"
                resultado["mensagem"] = f"Campo '{campo}' atende mínimo de {minimo} caracteres."
            elif isinstance(valor, (int, float)) and valor >= minimo:
                resultado["status"] = "aprovado"
                resultado["mensagem"] = f"Campo '{campo}' = {valor} >= {minimo}."
            else:
                resultado["status"] = "reprovado"
                resultado["mensagem"] = f"Campo '{campo}' não atende mínimo de {minimo}."

        elif tipo == "contagem_minima":
            campo = item.get("campo", item.get("field", ""))
            minimo = item.get("minimo", item.get("min", 1))
            valor = _resolver_campo(dados_projeto, campo) if dados_projeto else None
            if isinstance(valor, (list, tuple)) and len(valor) >= minimo:
                resultado["status"] = "aprovado"
                resultado["mensagem"] = f"Campo '{campo}' tem {len(valor)} itens (mín: {minimo})."
            else:
                qtd = len(valor) if isinstance(valor, (list, tuple)) else 0
                resultado["status"] = "reprovado"
                resultado["mensagem"] = f"Campo '{campo}' tem {qtd} itens (mín: {minimo})."

        elif tipo == "padrao_regex":
            campo = item.get("campo", item.get("field", ""))
            padrao = item.get("padrao", item.get("pattern", ""))
            valor = str(_resolver_campo(dados_projeto, campo) or "")
            if re.search(padrao, valor):
                resultado["status"] = "aprovado"
                resultado["mensagem"] = f"Campo '{campo}' atende padrão."
            else:
                resultado["status"] = "reprovado"
                resultado["mensagem"] = f"Campo '{campo}' não atende padrão: {padrao}"

        elif tipo == "manual":
            # Itens manuais mantêm status conforme definido no checklist
            status_manual = item.get("status", item.get("concluido", False))
            if status_manual is True or str(status_manual).lower() in ("aprovado", "concluido", "done"):
                resultado["status"] = "aprovado"
                resultado["mensagem"] = "Verificação manual: aprovado."
            else:
                resultado["status"] = "pendente"
                resultado["mensagem"] = "Requer verificação manual."

        else:
            resultado["status"] = "pendente"
            resultado["mensagem"] = f"Tipo de verificação desconhecido: {tipo}"

    except Exception as e:
        resultado["status"] = "erro"
        resultado["mensagem"] = f"Erro na verificação: {e}"

    return resultado


def _resolver_campo(dados: dict, caminho_campo: str):
    """Resolve um campo usando notação de ponto (ex: 'artefatos.risk_register')."""
    if not dados or not caminho_campo:
        return None

    partes = caminho_campo.split(".")
    atual = dados
    for parte in partes:
        if isinstance(atual, dict) and parte in atual:
            atual = atual[parte]
        elif isinstance(atual, list):
            try:
                idx = int(parte)
                atual = atual[idx]
            except (ValueError, IndexError):
                return None
        else:
            return None
    return atual


# ---------------------------------------------------------------------------
# Execução do checklist completo
# ---------------------------------------------------------------------------

def executar_checklist(
    caminho_checklist: str,
    caminho_dados: str | None = None,
) -> dict:
    """
    Executa um checklist completo de validação.

    Args:
        caminho_checklist: Caminho para o arquivo de checklist.
        caminho_dados: Caminho opcional para dados do projeto.

    Returns:
        Relatório com resultados de cada item e resumo.
    """
    checklist_raw = carregar_arquivo(caminho_checklist)
    itens = extrair_checklist(checklist_raw)

    dados_projeto = None
    if caminho_dados:
        dados_projeto = carregar_arquivo(caminho_dados)
        if not isinstance(dados_projeto, dict):
            dados_projeto = {}

    base_dir = Path(caminho_checklist).parent

    resultados = []
    for item in itens:
        if isinstance(item, dict):
            resultado = executar_verificacao(item, dados_projeto, base_dir)
            resultados.append(resultado)
        elif isinstance(item, str):
            resultados.append({
                "nome": item,
                "tipo": "manual",
                "status": "pendente",
                "mensagem": "Requer verificação manual.",
                "categoria": "geral",
                "obrigatorio": True,
            })

    # Calcular resumo
    total = len(resultados)
    aprovados = sum(1 for r in resultados if r["status"] == "aprovado")
    reprovados = sum(1 for r in resultados if r["status"] == "reprovado")
    pendentes = sum(1 for r in resultados if r["status"] == "pendente")
    erros = sum(1 for r in resultados if r["status"] == "erro")

    obrig_reprov = sum(
        1 for r in resultados
        if r["status"] == "reprovado" and r.get("obrigatorio", True)
    )

    return {
        "checklist": Path(caminho_checklist).name,
        "resultados": resultados,
        "resumo": {
            "total": total,
            "aprovados": aprovados,
            "reprovados": reprovados,
            "pendentes": pendentes,
            "erros": erros,
            "percentual_aprovado": round((aprovados / total) * 100, 1) if total > 0 else 0,
            "obrigatorios_reprovados": obrig_reprov,
            "status_geral": "aprovado" if obrig_reprov == 0 and erros == 0 else "reprovado",
        },
    }


# ---------------------------------------------------------------------------
# Formatação
# ---------------------------------------------------------------------------

def formatar_texto(relatorio: dict) -> str:
    """Formata o relatório como texto."""
    linhas = []
    linhas.append("=" * 60)
    linhas.append(f"  CHECKLIST: {relatorio['checklist']}")
    linhas.append("=" * 60)

    res = relatorio["resumo"]
    status_geral = "APROVADO" if res["status_geral"] == "aprovado" else "REPROVADO"
    linhas.append(f"\nStatus Geral: {status_geral}")
    linhas.append(f"Aprovados: {res['aprovados']}/{res['total']} ({res['percentual_aprovado']}%)")
    if res["reprovados"]:
        linhas.append(f"Reprovados: {res['reprovados']} ({res['obrigatorios_reprovados']} obrigatórios)")
    if res["pendentes"]:
        linhas.append(f"Pendentes: {res['pendentes']}")

    linhas.append(f"\n{'-' * 60}")
    linhas.append("ITENS:")

    indicadores = {
        "aprovado": "[OK]", "reprovado": "[XX]",
        "pendente": "[..]", "erro": "[ER]",
    }

    # Agrupar por categoria
    categorias = {}
    for r in relatorio["resultados"]:
        cat = r.get("categoria", "geral")
        categorias.setdefault(cat, []).append(r)

    for cat, itens in categorias.items():
        linhas.append(f"\n  [{cat.upper()}]")
        for item in itens:
            ind = indicadores.get(item["status"], "[??]")
            obrig = "*" if item.get("obrigatorio", True) else " "
            linhas.append(f"    {ind}{obrig} {item['nome']}")
            if item["mensagem"]:
                linhas.append(f"         {item['mensagem']}")

    linhas.append(f"\n{'=' * 60}")
    return "\n".join(linhas)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def criar_parser() -> argparse.ArgumentParser:
    """Cria o parser de argumentos."""
    parser = argparse.ArgumentParser(
        description="Executa checklists de validação.",
    )
    parser.add_argument("checklist", help="Caminho para o checklist (YAML/JSON).")
    parser.add_argument("--data", default=None, help="Dados do projeto para validação.")
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

    relatorio = executar_checklist(args.checklist, args.data)

    if args.format == "json":
        saida = json.dumps(relatorio, indent=2, ensure_ascii=False)
    else:
        saida = formatar_texto(relatorio)

    if args.output_file:
        Path(args.output_file).write_text(saida, encoding="utf-8")
        print(f"Relatório salvo em: {args.output_file}")
    else:
        print(saida)

    sys.exit(0 if relatorio["resumo"]["status_geral"] == "aprovado" else 1)


if __name__ == "__main__":
    main()
