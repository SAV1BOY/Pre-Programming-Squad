#!/usr/bin/env python3
"""
Validador de Notas de Arquitetura.

Este script valida documentos de notas de arquitetura nos formatos YAML ou
Markdown, garantindo que decisões arquiteturais estejam documentadas de forma
completa e consistente.

Regras de Validação:
  - Campos obrigatórios: titulo, contexto, decisao, consequencias, status
  - O contexto deve ter no mínimo 100 caracteres
  - A decisão deve referenciar pelo menos uma alternativa considerada
  - Consequências devem listar impactos positivos e negativos
  - O status deve ser um dos valores válidos (proposta, aceita, rejeitada, obsoleta)
  - Deve conter data de criação e autor

Uso:
  python validate-architecture-note.py <caminho_do_arquivo> [--schema <caminho>] [--strict]
"""

import argparse
import json
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
    "contexto",
    "decisao",
    "consequencias",
    "status",
]

CAMPOS_OPCIONAIS = [
    "autor",
    "data_criacao",
    "data_revisao",
    "alternativas",
    "justificativa",
    "restricoes",
    "dependencias",
    "componentes_afetados",
    "diagramas",
    "referencias",
    "revisores",
    "tags",
]

STATUS_VALIDOS = ["proposta", "aceita", "rejeitada", "obsoleta", "em_revisao"]

TAMANHO_MINIMO_CONTEXTO = 100


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
            raise ImportError("PyYAML é necessário. Instale com: pip install pyyaml")
        dados = yaml.safe_load(conteudo)
        if not isinstance(dados, dict):
            raise ValueError("O YAML deve conter um mapeamento raiz.")
        return dados

    if caminho.suffix == ".md":
        return _parse_markdown(conteudo)

    raise ValueError(f"Formato não suportado: {caminho.suffix}")


def _parse_markdown(conteudo: str) -> dict:
    """Extrai frontmatter YAML e seções de um Markdown."""
    if yaml is None:
        raise ImportError("PyYAML é necessário para processar frontmatter.")

    dados = {}
    padrao = re.match(r"^---\s*\n(.*?)\n---", conteudo, re.DOTALL)
    if padrao:
        dados = yaml.safe_load(padrao.group(1)) or {}

    # Extrair seções do corpo do Markdown
    secoes = re.findall(r"^##\s+(.+?)\n(.*?)(?=^##\s|\Z)", conteudo, re.MULTILINE | re.DOTALL)
    mapa_secoes = {
        "contexto": "contexto",
        "decisão": "decisao",
        "decisao": "decisao",
        "consequências": "consequencias",
        "consequencias": "consequencias",
        "alternativas": "alternativas",
    }
    for titulo_secao, corpo in secoes:
        chave = mapa_secoes.get(titulo_secao.strip().lower())
        if chave and chave not in dados:
            dados[chave] = corpo.strip()

    return dados


# ---------------------------------------------------------------------------
# Regras de validação
# ---------------------------------------------------------------------------

def validar_campos_obrigatorios(dados: dict) -> list[str]:
    """Verifica presença de todos os campos obrigatórios."""
    erros = []
    for campo in CAMPOS_OBRIGATORIOS:
        if campo not in dados or dados[campo] is None:
            erros.append(f"Campo obrigatório ausente: '{campo}'")
        elif isinstance(dados[campo], str) and not dados[campo].strip():
            erros.append(f"Campo obrigatório vazio: '{campo}'")
    return erros


def validar_contexto(dados: dict) -> list[str]:
    """Valida que o contexto tenha tamanho mínimo adequado."""
    erros = []
    contexto = dados.get("contexto", "")
    if isinstance(contexto, str) and 0 < len(contexto.strip()) < TAMANHO_MINIMO_CONTEXTO:
        erros.append(
            f"O campo 'contexto' deve ter no mínimo {TAMANHO_MINIMO_CONTEXTO} "
            f"caracteres (atual: {len(contexto.strip())})."
        )
    return erros


def validar_status(dados: dict) -> list[str]:
    """Valida que o status seja um dos valores permitidos."""
    erros = []
    status = dados.get("status", "")
    if isinstance(status, str) and status.strip():
        if status.strip().lower() not in STATUS_VALIDOS:
            erros.append(
                f"Status inválido: '{status}'. "
                f"Valores permitidos: {', '.join(STATUS_VALIDOS)}"
            )
    return erros


def validar_alternativas(dados: dict) -> list[str]:
    """Valida que alternativas foram consideradas."""
    erros = []
    alternativas = dados.get("alternativas", [])
    decisao = dados.get("decisao", "")

    if not alternativas and isinstance(decisao, str):
        # Verificar se a decisão menciona alternativas no texto
        palavras_alternativa = ["alternativa", "opção", "considerad", "avaliad"]
        texto = decisao.lower()
        if not any(p in texto for p in palavras_alternativa):
            erros.append(
                "A nota deve documentar alternativas consideradas. "
                "Use o campo 'alternativas' ou mencione-as na decisão."
            )

    if isinstance(alternativas, list):
        for i, alt in enumerate(alternativas):
            if isinstance(alt, dict):
                if "descricao" not in alt and "nome" not in alt:
                    erros.append(
                        f"Alternativa #{i+1}: deve conter 'descricao' ou 'nome'."
                    )
            elif isinstance(alt, str) and len(alt.strip()) < 10:
                erros.append(
                    f"Alternativa #{i+1}: descrição muito curta (mínimo 10 caracteres)."
                )
    return erros


def validar_consequencias(dados: dict) -> list[str]:
    """Valida que consequências incluam impactos positivos e negativos."""
    erros = []
    consequencias = dados.get("consequencias")

    if isinstance(consequencias, dict):
        if "positivas" not in consequencias and "positivos" not in consequencias:
            erros.append("Consequências devem listar impactos positivos.")
        if "negativas" not in consequencias and "negativos" not in consequencias:
            erros.append("Consequências devem listar impactos negativos.")
    elif isinstance(consequencias, str):
        texto = consequencias.lower()
        tem_positivo = any(p in texto for p in ["positiv", "benefício", "vantagem", "ganho"])
        tem_negativo = any(p in texto for p in ["negativ", "desvantagem", "risco", "custo", "trade-off"])
        if not tem_positivo:
            erros.append("Consequências devem mencionar impactos positivos.")
        if not tem_negativo:
            erros.append("Consequências devem mencionar impactos negativos ou trade-offs.")
    elif isinstance(consequencias, list):
        if len(consequencias) < 2:
            erros.append(
                "Deve haver pelo menos 2 consequências listadas "
                "(impactos positivos e negativos)."
            )
    return erros


def validar_metadados(dados: dict) -> list[str]:
    """Valida metadados como autor e data."""
    avisos = []
    if "autor" not in dados:
        avisos.append("Recomendado: adicionar campo 'autor'.")
    if "data_criacao" not in dados:
        avisos.append("Recomendado: adicionar campo 'data_criacao'.")
    return avisos


def validar_componentes(dados: dict) -> list[str]:
    """Valida que componentes afetados estejam listados."""
    avisos = []
    if "componentes_afetados" not in dados:
        avisos.append(
            "Recomendado: listar componentes afetados em 'componentes_afetados'."
        )
    return avisos


# ---------------------------------------------------------------------------
# Função principal
# ---------------------------------------------------------------------------

def validar_architecture_note(
    caminho: str,
    caminho_schema: str | None = None,
    modo_estrito: bool = False,
) -> dict:
    """
    Valida um arquivo de nota de arquitetura.

    Args:
        caminho: Caminho para o arquivo.
        caminho_schema: Caminho opcional para JSON Schema.
        modo_estrito: Se True, avisos viram erros.

    Returns:
        Dicionário com 'valido', 'erros', 'avisos'.
    """
    resultado = {"valido": True, "erros": [], "avisos": []}

    try:
        dados = carregar_arquivo(caminho)
    except Exception as e:
        resultado["valido"] = False
        resultado["erros"].append(f"Erro ao carregar arquivo: {e}")
        return resultado

    # Schema externo
    if caminho_schema:
        try:
            import jsonschema
            with open(caminho_schema, "r", encoding="utf-8") as f:
                schema = json.load(f)
            jsonschema.validate(instance=dados, schema=schema)
        except ImportError:
            resultado["avisos"].append("Módulo jsonschema não disponível.")
        except Exception as e:
            resultado["erros"].append(f"Erro no schema: {e}")

    # Validações
    for validador in [
        validar_campos_obrigatorios,
        validar_contexto,
        validar_status,
        validar_alternativas,
        validar_consequencias,
    ]:
        resultado["erros"].extend(validador(dados))

    # Avisos
    avisos_meta = validar_metadados(dados) + validar_componentes(dados)
    if modo_estrito:
        resultado["erros"].extend(avisos_meta)
    else:
        resultado["avisos"].extend(avisos_meta)

    resultado["valido"] = len(resultado["erros"]) == 0
    return resultado


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def criar_parser() -> argparse.ArgumentParser:
    """Cria o parser de argumentos."""
    parser = argparse.ArgumentParser(
        description="Valida notas de arquitetura contra regras predefinidas.",
    )
    parser.add_argument("arquivo", help="Caminho para o arquivo (YAML/Markdown).")
    parser.add_argument("--schema", default=None, help="JSON Schema externo.")
    parser.add_argument("--strict", action="store_true", help="Modo estrito.")
    parser.add_argument(
        "--output", choices=["text", "json"], default="text", help="Formato de saída."
    )
    return parser


def formatar_saida(resultado: dict, formato: str) -> str:
    """Formata o resultado para exibição."""
    if formato == "json":
        return json.dumps(resultado, indent=2, ensure_ascii=False)

    linhas = []
    status = "VÁLIDO" if resultado["valido"] else "INVÁLIDO"
    linhas.append(f"Resultado: {status}")
    if resultado["erros"]:
        linhas.append(f"\nErros ({len(resultado['erros'])}):")
        for e in resultado["erros"]:
            linhas.append(f"  - {e}")
    if resultado["avisos"]:
        linhas.append(f"\nAvisos ({len(resultado['avisos'])}):")
        for a in resultado["avisos"]:
            linhas.append(f"  - {a}")
    return "\n".join(linhas)


def main():
    """Ponto de entrada principal."""
    parser = criar_parser()
    args = parser.parse_args()
    resultado = validar_architecture_note(args.arquivo, args.schema, args.strict)
    print(formatar_saida(resultado, args.output))
    sys.exit(0 if resultado["valido"] else 1)


if __name__ == "__main__":
    main()
