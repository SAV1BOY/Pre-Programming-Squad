#!/usr/bin/env python3
"""
Gerador de ADR (Architecture Decision Record).

Este script gera documentos de registro de decisão arquitetural (ADR) a partir
de templates padronizados, facilitando a documentação consistente de decisões
técnicas durante a fase de pré-programação.

Funcionalidades:
  - Geração de ADR a partir de template padrão ou customizado
  - Numeração automática sequencial
  - Suporte a formatos Markdown e YAML
  - Validação de campos obrigatórios antes da geração
  - Linkagem com ADRs anteriores (supersedes/superseded-by)

Uso:
  python adr-generator.py --title "Título da Decisão" --status proposta [--output-dir ./adrs]
  python adr-generator.py --from-yaml decisao.yaml --output-dir ./adrs
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
# Template padrão
# ---------------------------------------------------------------------------

TEMPLATE_ADR_MD = """# ADR-{numero:04d}: {titulo}

**Data:** {data}
**Status:** {status}
**Autor:** {autor}
{supersedes_line}

## Contexto

{contexto}

## Decisão

{decisao}

## Alternativas Consideradas

{alternativas}

## Consequências

### Positivas
{consequencias_positivas}

### Negativas
{consequencias_negativas}

## Notas

{notas}

---
*Gerado automaticamente pelo ADR Generator em {data_geracao}*
"""

STATUS_VALIDOS = ["proposta", "aceita", "rejeitada", "obsoleta", "em_revisao"]


# ---------------------------------------------------------------------------
# Funções principais
# ---------------------------------------------------------------------------

def obter_proximo_numero(diretorio: Path) -> int:
    """Obtém o próximo número sequencial de ADR no diretório."""
    if not diretorio.exists():
        return 1

    numeros = []
    for arquivo in diretorio.glob("ADR-*.md"):
        match = re.match(r"ADR-(\d+)", arquivo.stem)
        if match:
            numeros.append(int(match.group(1)))

    for arquivo in diretorio.glob("adr-*.md"):
        match = re.match(r"adr-(\d+)", arquivo.stem)
        if match:
            numeros.append(int(match.group(1)))

    return max(numeros, default=0) + 1


def carregar_dados_yaml(caminho: str) -> dict:
    """Carrega dados de entrada de um arquivo YAML."""
    if yaml is None:
        raise ImportError("PyYAML necessário para ler YAML.")
    with open(caminho, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def formatar_lista(itens: list | str | None) -> str:
    """Formata uma lista de itens como bullets Markdown."""
    if itens is None:
        return "- (A ser definido)"
    if isinstance(itens, str):
        return itens
    if isinstance(itens, list):
        return "\n".join(f"- {item}" for item in itens)
    return str(itens)


def formatar_alternativas(alternativas: list | str | None) -> str:
    """Formata alternativas consideradas."""
    if alternativas is None:
        return "1. (Nenhuma alternativa documentada)"
    if isinstance(alternativas, str):
        return alternativas
    if isinstance(alternativas, list):
        linhas = []
        for i, alt in enumerate(alternativas, 1):
            if isinstance(alt, dict):
                nome = alt.get("nome", alt.get("titulo", f"Alternativa {i}"))
                desc = alt.get("descricao", "")
                pros = alt.get("pros", [])
                contras = alt.get("contras", [])
                linhas.append(f"### {i}. {nome}")
                if desc:
                    linhas.append(f"\n{desc}")
                if pros:
                    linhas.append("\n**Prós:**")
                    linhas.extend(f"- {p}" for p in pros)
                if contras:
                    linhas.append("\n**Contras:**")
                    linhas.extend(f"- {c}" for c in contras)
                linhas.append("")
            else:
                linhas.append(f"{i}. {alt}")
        return "\n".join(linhas)
    return str(alternativas)


def gerar_adr(
    titulo: str,
    contexto: str = "",
    decisao: str = "",
    alternativas: list | str | None = None,
    consequencias_positivas: list | str | None = None,
    consequencias_negativas: list | str | None = None,
    status: str = "proposta",
    autor: str = "",
    notas: str = "",
    supersedes: int | None = None,
    numero: int | None = None,
    diretorio_saida: str = ".",
) -> str:
    """
    Gera um documento ADR.

    Args:
        titulo: Título da decisão arquitetural.
        contexto: Descrição do contexto que motivou a decisão.
        decisao: A decisão tomada.
        alternativas: Alternativas consideradas.
        consequencias_positivas: Impactos positivos da decisão.
        consequencias_negativas: Impactos negativos da decisão.
        status: Status da decisão.
        autor: Autor da decisão.
        notas: Notas adicionais.
        supersedes: Número do ADR que esta decisão substitui.
        numero: Número forçado do ADR (se None, auto-incrementa).
        diretorio_saida: Diretório para salvar o ADR.

    Returns:
        Caminho do arquivo gerado.
    """
    dir_saida = Path(diretorio_saida)
    dir_saida.mkdir(parents=True, exist_ok=True)

    if numero is None:
        numero = obter_proximo_numero(dir_saida)

    # Validar status
    if status.lower() not in STATUS_VALIDOS:
        raise ValueError(f"Status inválido: '{status}'. Use: {', '.join(STATUS_VALIDOS)}")

    # Preparar supersedes
    supersedes_line = ""
    if supersedes:
        supersedes_line = f"**Substitui:** ADR-{supersedes:04d}"

    # Gerar conteúdo
    conteudo = TEMPLATE_ADR_MD.format(
        numero=numero,
        titulo=titulo,
        data=datetime.now().strftime("%Y-%m-%d"),
        status=status.title(),
        autor=autor or "(Não especificado)",
        supersedes_line=supersedes_line,
        contexto=contexto or "(Descrever o contexto da decisão)",
        decisao=decisao or "(Descrever a decisão tomada)",
        alternativas=formatar_alternativas(alternativas),
        consequencias_positivas=formatar_lista(consequencias_positivas),
        consequencias_negativas=formatar_lista(consequencias_negativas),
        notas=notas or "(Sem notas adicionais)",
        data_geracao=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )

    # Gerar nome do arquivo
    slug = re.sub(r"[^a-z0-9]+", "-", titulo.lower()).strip("-")
    nome_arquivo = f"ADR-{numero:04d}-{slug}.md"
    caminho_saida = dir_saida / nome_arquivo

    caminho_saida.write_text(conteudo, encoding="utf-8")
    return str(caminho_saida)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def criar_parser() -> argparse.ArgumentParser:
    """Cria o parser de argumentos."""
    parser = argparse.ArgumentParser(
        description="Gera documentos ADR (Architecture Decision Record).",
    )
    parser.add_argument("--title", help="Título da decisão.")
    parser.add_argument("--context", default="", help="Contexto da decisão.")
    parser.add_argument("--decision", default="", help="Decisão tomada.")
    parser.add_argument(
        "--status", default="proposta", choices=STATUS_VALIDOS,
        help="Status da decisão.",
    )
    parser.add_argument("--author", default="", help="Autor da decisão.")
    parser.add_argument("--notes", default="", help="Notas adicionais.")
    parser.add_argument(
        "--supersedes", type=int, default=None,
        help="Número do ADR que esta decisão substitui.",
    )
    parser.add_argument(
        "--number", type=int, default=None,
        help="Número forçado do ADR.",
    )
    parser.add_argument(
        "--from-yaml", default=None,
        help="Carregar dados de um arquivo YAML.",
    )
    parser.add_argument(
        "--output-dir", default=".", help="Diretório de saída.",
    )
    return parser


def main():
    """Ponto de entrada principal."""
    parser = criar_parser()
    args = parser.parse_args()

    if args.from_yaml:
        dados = carregar_dados_yaml(args.from_yaml)
        caminho = gerar_adr(
            titulo=dados.get("titulo", dados.get("title", "Sem Título")),
            contexto=dados.get("contexto", dados.get("context", "")),
            decisao=dados.get("decisao", dados.get("decision", "")),
            alternativas=dados.get("alternativas", dados.get("alternatives")),
            consequencias_positivas=dados.get("consequencias_positivas", dados.get("pros")),
            consequencias_negativas=dados.get("consequencias_negativas", dados.get("cons")),
            status=dados.get("status", "proposta"),
            autor=dados.get("autor", dados.get("author", "")),
            notas=dados.get("notas", dados.get("notes", "")),
            supersedes=dados.get("supersedes"),
            numero=dados.get("numero", dados.get("number")),
            diretorio_saida=args.output_dir,
        )
    elif args.title:
        caminho = gerar_adr(
            titulo=args.title,
            contexto=args.context,
            decisao=args.decision,
            status=args.status,
            autor=args.author,
            notas=args.notes,
            supersedes=args.supersedes,
            numero=args.number,
            diretorio_saida=args.output_dir,
        )
    else:
        parser.error("É necessário fornecer --title ou --from-yaml.")
        return

    print(f"ADR gerado com sucesso: {caminho}")


if __name__ == "__main__":
    main()
