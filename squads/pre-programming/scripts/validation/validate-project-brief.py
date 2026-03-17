#!/usr/bin/env python3
"""
Validador de Project Brief (Resumo do Projeto).

Este script valida arquivos de project brief nos formatos YAML ou Markdown
contra um schema predefinido, garantindo que todos os campos obrigatórios
estejam presentes e que os valores estejam dentro dos limites esperados.

Regras de Validação:
  - Campos obrigatórios: titulo, objetivo, escopo, stakeholders, prazo_estimado
  - O objetivo deve ter no mínimo 50 caracteres
  - Deve haver pelo menos 1 stakeholder definido
  - O escopo deve conter seções 'incluso' e 'excluso'
  - O prazo estimado deve estar no formato ISO 8601
  - Critérios de sucesso devem ser mensuráveis (conter números ou métricas)

Uso:
  python validate-project-brief.py <caminho_do_arquivo> [--schema <caminho_schema>] [--strict]
"""

import argparse
import json
import os
import re
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

CAMPOS_OBRIGATORIOS = [
    "titulo",
    "objetivo",
    "escopo",
    "stakeholders",
    "prazo_estimado",
]

CAMPOS_OPCIONAIS = [
    "descricao",
    "criterios_sucesso",
    "restricoes",
    "dependencias",
    "riscos_iniciais",
    "premissas",
    "aprovadores",
    "versao",
    "data_criacao",
]

TAMANHO_MINIMO_OBJETIVO = 50


# ---------------------------------------------------------------------------
# Funções auxiliares
# ---------------------------------------------------------------------------

def carregar_arquivo(caminho: str) -> dict:
    """Carrega um arquivo YAML ou Markdown e retorna um dicionário."""
    caminho = Path(caminho)

    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    conteudo = caminho.read_text(encoding="utf-8")

    if caminho.suffix in (".yaml", ".yml"):
        if yaml is None:
            raise ImportError(
                "O módulo PyYAML é necessário para processar arquivos YAML. "
                "Instale com: pip install pyyaml"
            )
        dados = yaml.safe_load(conteudo)
        if not isinstance(dados, dict):
            raise ValueError("O arquivo YAML deve conter um mapeamento raiz.")
        return dados

    if caminho.suffix == ".md":
        return _parse_markdown_frontmatter(conteudo)

    raise ValueError(f"Formato de arquivo não suportado: {caminho.suffix}")


def _parse_markdown_frontmatter(conteudo: str) -> dict:
    """Extrai frontmatter YAML de um arquivo Markdown."""
    if yaml is None:
        raise ImportError("O módulo PyYAML é necessário para processar frontmatter.")

    padrao = re.match(r"^---\s*\n(.*?)\n---", conteudo, re.DOTALL)
    if not padrao:
        raise ValueError(
            "O arquivo Markdown deve conter frontmatter YAML delimitado por '---'."
        )
    return yaml.safe_load(padrao.group(1))


def carregar_schema(caminho_schema: str | None) -> dict | None:
    """Carrega um JSON Schema externo, se fornecido."""
    if caminho_schema is None:
        return None
    with open(caminho_schema, "r", encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# Regras de validação
# ---------------------------------------------------------------------------

def validar_campos_obrigatorios(dados: dict) -> list[str]:
    """Verifica se todos os campos obrigatórios estão presentes."""
    erros = []
    for campo in CAMPOS_OBRIGATORIOS:
        if campo not in dados or dados[campo] is None:
            erros.append(f"Campo obrigatório ausente: '{campo}'")
        elif isinstance(dados[campo], str) and not dados[campo].strip():
            erros.append(f"Campo obrigatório vazio: '{campo}'")
    return erros


def validar_objetivo(dados: dict) -> list[str]:
    """Valida que o objetivo tenha comprimento mínimo."""
    erros = []
    objetivo = dados.get("objetivo", "")
    if isinstance(objetivo, str) and len(objetivo.strip()) < TAMANHO_MINIMO_OBJETIVO:
        erros.append(
            f"O campo 'objetivo' deve ter no mínimo {TAMANHO_MINIMO_OBJETIVO} "
            f"caracteres (atual: {len(objetivo.strip())})."
        )
    return erros


def validar_stakeholders(dados: dict) -> list[str]:
    """Valida que haja pelo menos 1 stakeholder."""
    erros = []
    stakeholders = dados.get("stakeholders", [])
    if not isinstance(stakeholders, list) or len(stakeholders) < 1:
        erros.append("Deve haver pelo menos 1 stakeholder definido.")
    else:
        for i, s in enumerate(stakeholders):
            if isinstance(s, dict):
                if "nome" not in s:
                    erros.append(f"Stakeholder #{i+1}: campo 'nome' ausente.")
                if "papel" not in s:
                    erros.append(f"Stakeholder #{i+1}: campo 'papel' ausente.")
            elif not isinstance(s, str) or not s.strip():
                erros.append(f"Stakeholder #{i+1}: valor inválido.")
    return erros


def validar_escopo(dados: dict) -> list[str]:
    """Valida que o escopo contenha 'incluso' e 'excluso'."""
    erros = []
    escopo = dados.get("escopo")
    if isinstance(escopo, dict):
        if "incluso" not in escopo:
            erros.append("O campo 'escopo' deve conter a chave 'incluso'.")
        if "excluso" not in escopo:
            erros.append("O campo 'escopo' deve conter a chave 'excluso'.")
    elif isinstance(escopo, str):
        texto = escopo.lower()
        if "incluso" not in texto and "incluído" not in texto:
            erros.append(
                "O campo 'escopo' em formato texto deve mencionar o que está incluso."
            )
    return erros


def validar_prazo(dados: dict) -> list[str]:
    """Valida o formato do prazo estimado."""
    erros = []
    prazo = dados.get("prazo_estimado", "")
    if isinstance(prazo, str) and prazo.strip():
        formatos = ["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S"]
        valido = False
        for fmt in formatos:
            try:
                datetime.strptime(prazo.strip(), fmt)
                valido = True
                break
            except ValueError:
                continue
        # Aceita também durações como "3 meses", "6 semanas"
        if not valido and not re.match(
            r"^\d+\s*(dias?|semanas?|meses|mes|anos?|sprints?)$",
            prazo.strip(),
            re.IGNORECASE,
        ):
            erros.append(
                f"O campo 'prazo_estimado' deve estar no formato ISO 8601 "
                f"ou em formato de duração (ex: '3 meses'). Valor: '{prazo}'"
            )
    return erros


def validar_criterios_sucesso(dados: dict) -> list[str]:
    """Valida que critérios de sucesso sejam mensuráveis."""
    erros = []
    criterios = dados.get("criterios_sucesso", [])
    if isinstance(criterios, list):
        for i, criterio in enumerate(criterios):
            texto = str(criterio)
            if not re.search(r"\d+|%|métrica|kpi|sla|tempo|latência|uptime", texto, re.IGNORECASE):
                erros.append(
                    f"Critério de sucesso #{i+1} pode não ser mensurável: '{texto[:80]}'. "
                    "Considere incluir números ou métricas."
                )
    return erros


# ---------------------------------------------------------------------------
# Função principal de validação
# ---------------------------------------------------------------------------

def validar_project_brief(
    caminho: str,
    caminho_schema: str | None = None,
    modo_estrito: bool = False,
) -> dict:
    """
    Valida um arquivo de project brief.

    Args:
        caminho: Caminho para o arquivo YAML ou Markdown.
        caminho_schema: Caminho opcional para um JSON Schema externo.
        modo_estrito: Se True, avisos são tratados como erros.

    Returns:
        Dicionário com 'valido' (bool), 'erros' (list), 'avisos' (list).
    """
    resultado = {"valido": True, "erros": [], "avisos": []}

    try:
        dados = carregar_arquivo(caminho)
    except Exception as e:
        resultado["valido"] = False
        resultado["erros"].append(f"Erro ao carregar arquivo: {e}")
        return resultado

    # Validar com schema externo, se fornecido
    if caminho_schema:
        try:
            import jsonschema  # type: ignore
            schema = carregar_schema(caminho_schema)
            if schema:
                jsonschema.validate(instance=dados, schema=schema)
        except ImportError:
            resultado["avisos"].append(
                "Módulo jsonschema não disponível. Validação por schema ignorada."
            )
        except Exception as e:
            resultado["erros"].append(f"Erro de validação do schema: {e}")

    # Executar regras de validação internas
    validadores = [
        validar_campos_obrigatorios,
        validar_objetivo,
        validar_stakeholders,
        validar_escopo,
        validar_prazo,
    ]

    for validador in validadores:
        resultado["erros"].extend(validador(dados))

    # Critérios de sucesso geram avisos (a menos que em modo estrito)
    avisos_criterios = validar_criterios_sucesso(dados)
    if modo_estrito:
        resultado["erros"].extend(avisos_criterios)
    else:
        resultado["avisos"].extend(avisos_criterios)

    # Verificar campos desconhecidos
    campos_conhecidos = set(CAMPOS_OBRIGATORIOS + CAMPOS_OPCIONAIS)
    for campo in dados:
        if campo not in campos_conhecidos:
            resultado["avisos"].append(f"Campo desconhecido encontrado: '{campo}'")

    resultado["valido"] = len(resultado["erros"]) == 0
    return resultado


# ---------------------------------------------------------------------------
# Interface CLI
# ---------------------------------------------------------------------------

def criar_parser() -> argparse.ArgumentParser:
    """Cria o parser de argumentos da linha de comando."""
    parser = argparse.ArgumentParser(
        description="Valida um arquivo de Project Brief contra regras predefinidas.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  python validate-project-brief.py projeto.yaml
  python validate-project-brief.py projeto.md --strict
  python validate-project-brief.py projeto.yaml --schema schema.json --output json
        """,
    )
    parser.add_argument(
        "arquivo",
        help="Caminho para o arquivo de project brief (YAML ou Markdown).",
    )
    parser.add_argument(
        "--schema",
        dest="schema",
        default=None,
        help="Caminho para um JSON Schema externo para validação adicional.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        default=False,
        help="Modo estrito: trata avisos como erros.",
    )
    parser.add_argument(
        "--output",
        choices=["text", "json"],
        default="text",
        help="Formato de saída (padrão: text).",
    )
    return parser


def formatar_saida(resultado: dict, formato: str) -> str:
    """Formata o resultado da validação para exibição."""
    if formato == "json":
        return json.dumps(resultado, indent=2, ensure_ascii=False)

    linhas = []
    status = "VÁLIDO ✓" if resultado["valido"] else "INVÁLIDO ✗"
    linhas.append(f"Resultado: {status}")
    linhas.append("")

    if resultado["erros"]:
        linhas.append(f"Erros ({len(resultado['erros'])}):")
        for erro in resultado["erros"]:
            linhas.append(f"  - {erro}")
        linhas.append("")

    if resultado["avisos"]:
        linhas.append(f"Avisos ({len(resultado['avisos'])}):")
        for aviso in resultado["avisos"]:
            linhas.append(f"  - {aviso}")
        linhas.append("")

    return "\n".join(linhas)


def main():
    """Ponto de entrada principal do script."""
    parser = criar_parser()
    args = parser.parse_args()

    resultado = validar_project_brief(
        caminho=args.arquivo,
        caminho_schema=args.schema,
        modo_estrito=args.strict,
    )

    print(formatar_saida(resultado, args.output))
    sys.exit(0 if resultado["valido"] else 1)


if __name__ == "__main__":
    main()
