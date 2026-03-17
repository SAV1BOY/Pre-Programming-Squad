#!/usr/bin/env python3
"""
Gerador de Memorando de Decisão.

Este script gera memorandos de decisão padronizados a partir de templates,
documentando decisões técnicas e de negócio tomadas durante a fase de
pré-programação com rastreabilidade e justificativas.

Funcionalidades:
  - Geração de memo a partir de template padrão ou customizado
  - Suporte a múltiplos formatos de saída (Markdown, YAML)
  - Numeração sequencial automática
  - Registro de participantes e votos
  - Linkagem com ADRs e outros artefatos
  - Seção de análise de impacto

Uso:
  python decision-memo-generator.py --title "Título" --type tecnica [--output-dir ./memos]
  python decision-memo-generator.py --from-yaml decisao.yaml
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
# Templates
# ---------------------------------------------------------------------------

TEMPLATE_MEMO_MD = """# Memorando de Decisão #{numero:04d}

**Título:** {titulo}
**Data:** {data}
**Tipo:** {tipo}
**Status:** {status}
**Autor:** {autor}
**Urgência:** {urgencia}

---

## 1. Resumo Executivo

{resumo}

## 2. Contexto e Motivação

{contexto}

## 3. Opções Consideradas

{opcoes}

## 4. Decisão Tomada

{decisao}

## 5. Justificativa

{justificativa}

## 6. Análise de Impacto

### Impacto Técnico
{impacto_tecnico}

### Impacto no Cronograma
{impacto_cronograma}

### Impacto no Custo
{impacto_custo}

## 7. Riscos da Decisão

{riscos}

## 8. Plano de Ação

{plano_acao}

## 9. Participantes e Aprovações

{participantes}

## 10. Artefatos Relacionados

{artefatos_relacionados}

---

*Memorando gerado em {data_geracao}*
"""

TIPOS_DECISAO = [
    "tecnica", "arquitetural", "processo", "ferramenta",
    "infraestrutura", "seguranca", "negocio", "design",
]

STATUS_VALIDOS = ["rascunho", "em_revisao", "aprovada", "rejeitada", "implementada"]

URGENCIAS = ["baixa", "media", "alta", "critica"]


# ---------------------------------------------------------------------------
# Funções auxiliares
# ---------------------------------------------------------------------------

def obter_proximo_numero(diretorio: Path) -> int:
    """Obtém próximo número sequencial de memo."""
    if not diretorio.exists():
        return 1

    numeros = []
    for arquivo in diretorio.glob("DM-*.md"):
        match = re.match(r"DM-(\d+)", arquivo.stem)
        if match:
            numeros.append(int(match.group(1)))
    return max(numeros, default=0) + 1


def carregar_yaml(caminho: str) -> dict:
    """Carrega dados de YAML."""
    if yaml is None:
        raise ImportError("PyYAML necessário.")
    with open(caminho, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def formatar_opcoes(opcoes: list | str | None) -> str:
    """Formata opções consideradas."""
    if opcoes is None:
        return "*(Nenhuma opção documentada)*"
    if isinstance(opcoes, str):
        return opcoes
    if isinstance(opcoes, list):
        linhas = []
        for i, opcao in enumerate(opcoes, 1):
            if isinstance(opcao, dict):
                nome = opcao.get("nome", opcao.get("titulo", f"Opção {i}"))
                desc = opcao.get("descricao", "")
                pros = opcao.get("pros", [])
                contras = opcao.get("contras", [])
                escolhida = opcao.get("escolhida", False)

                marcador = " **(ESCOLHIDA)**" if escolhida else ""
                linhas.append(f"### Opção {i}: {nome}{marcador}")
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
                linhas.append(f"### Opção {i}: {opcao}\n")
        return "\n".join(linhas)
    return str(opcoes)


def formatar_lista(itens: list | str | None, prefixo: str = "-") -> str:
    """Formata uma lista como bullets Markdown."""
    if itens is None:
        return "*(A ser definido)*"
    if isinstance(itens, str):
        return itens
    if isinstance(itens, list):
        return "\n".join(f"{prefixo} {item}" for item in itens)
    return str(itens)


def formatar_participantes(participantes: list | None) -> str:
    """Formata lista de participantes."""
    if not participantes:
        return "*(Nenhum participante registrado)*"

    linhas = ["| Participante | Papel | Voto | Data |", "|---|---|---|---|"]
    for p in participantes:
        if isinstance(p, dict):
            nome = p.get("nome", "N/A")
            papel = p.get("papel", "N/A")
            voto = p.get("voto", "pendente")
            data = p.get("data", "N/A")
            linhas.append(f"| {nome} | {papel} | {voto} | {data} |")
        else:
            linhas.append(f"| {p} | - | pendente | - |")
    return "\n".join(linhas)


def formatar_artefatos(artefatos: list | None) -> str:
    """Formata artefatos relacionados."""
    if not artefatos:
        return "*(Nenhum artefato relacionado)*"

    linhas = []
    for art in artefatos:
        if isinstance(art, dict):
            tipo = art.get("tipo", "documento")
            ref = art.get("referencia", art.get("caminho", "N/A"))
            desc = art.get("descricao", "")
            linhas.append(f"- **[{tipo}]** {ref}" + (f" - {desc}" if desc else ""))
        else:
            linhas.append(f"- {art}")
    return "\n".join(linhas)


# ---------------------------------------------------------------------------
# Geração do memo
# ---------------------------------------------------------------------------

def gerar_memo(
    titulo: str,
    tipo: str = "tecnica",
    contexto: str = "",
    decisao: str = "",
    justificativa: str = "",
    opcoes: list | None = None,
    riscos: list | None = None,
    plano_acao: list | None = None,
    participantes: list | None = None,
    artefatos_relacionados: list | None = None,
    resumo: str = "",
    impacto_tecnico: str = "",
    impacto_cronograma: str = "",
    impacto_custo: str = "",
    status: str = "rascunho",
    autor: str = "",
    urgencia: str = "media",
    numero: int | None = None,
    diretorio_saida: str = ".",
) -> str:
    """
    Gera um memorando de decisão.

    Args:
        titulo: Título da decisão.
        tipo: Tipo de decisão.
        contexto: Contexto e motivação.
        decisao: Decisão tomada.
        justificativa: Justificativa da decisão.
        opcoes: Opções consideradas.
        riscos: Riscos da decisão.
        plano_acao: Plano de ação para implementar.
        participantes: Participantes e aprovadores.
        artefatos_relacionados: Documentos e artefatos vinculados.
        resumo: Resumo executivo.
        impacto_tecnico: Impacto técnico esperado.
        impacto_cronograma: Impacto no cronograma.
        impacto_custo: Impacto no custo.
        status: Status da decisão.
        autor: Autor do memo.
        urgencia: Nível de urgência.
        numero: Número forçado do memo.
        diretorio_saida: Diretório de saída.

    Returns:
        Caminho do arquivo gerado.
    """
    dir_saida = Path(diretorio_saida)
    dir_saida.mkdir(parents=True, exist_ok=True)

    if numero is None:
        numero = obter_proximo_numero(dir_saida)

    conteudo = TEMPLATE_MEMO_MD.format(
        numero=numero,
        titulo=titulo,
        data=datetime.now().strftime("%Y-%m-%d"),
        tipo=tipo.title(),
        status=status.title(),
        autor=autor or "(Não especificado)",
        urgencia=urgencia.title(),
        resumo=resumo or "(Resumo a ser preenchido)",
        contexto=contexto or "(Contexto a ser descrito)",
        opcoes=formatar_opcoes(opcoes),
        decisao=decisao or "(Decisão a ser documentada)",
        justificativa=justificativa or "(Justificativa a ser adicionada)",
        impacto_tecnico=impacto_tecnico or "*(A ser avaliado)*",
        impacto_cronograma=impacto_cronograma or "*(A ser avaliado)*",
        impacto_custo=impacto_custo or "*(A ser avaliado)*",
        riscos=formatar_lista(riscos),
        plano_acao=formatar_lista(plano_acao, "1."),
        participantes=formatar_participantes(participantes),
        artefatos_relacionados=formatar_artefatos(artefatos_relacionados),
        data_geracao=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )

    slug = re.sub(r"[^a-z0-9]+", "-", titulo.lower()).strip("-")
    nome_arquivo = f"DM-{numero:04d}-{slug}.md"
    caminho_saida = dir_saida / nome_arquivo

    caminho_saida.write_text(conteudo, encoding="utf-8")
    return str(caminho_saida)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def criar_parser() -> argparse.ArgumentParser:
    """Cria o parser de argumentos."""
    parser = argparse.ArgumentParser(
        description="Gera memorandos de decisão padronizados.",
    )
    parser.add_argument("--title", help="Título da decisão.")
    parser.add_argument(
        "--type", default="tecnica", choices=TIPOS_DECISAO,
        help="Tipo de decisão.",
    )
    parser.add_argument("--context", default="", help="Contexto.")
    parser.add_argument("--decision", default="", help="Decisão tomada.")
    parser.add_argument("--justification", default="", help="Justificativa.")
    parser.add_argument(
        "--status", default="rascunho", choices=STATUS_VALIDOS,
        help="Status.",
    )
    parser.add_argument("--author", default="", help="Autor.")
    parser.add_argument(
        "--urgency", default="media", choices=URGENCIAS,
        help="Urgência.",
    )
    parser.add_argument("--number", type=int, default=None, help="Número forçado.")
    parser.add_argument("--from-yaml", default=None, help="Carregar de YAML.")
    parser.add_argument("--output-dir", default=".", help="Diretório de saída.")
    return parser


def main():
    """Ponto de entrada principal."""
    parser = criar_parser()
    args = parser.parse_args()

    if args.from_yaml:
        dados = carregar_yaml(args.from_yaml)
        caminho = gerar_memo(
            titulo=dados.get("titulo", dados.get("title", "Sem Título")),
            tipo=dados.get("tipo", dados.get("type", "tecnica")),
            contexto=dados.get("contexto", dados.get("context", "")),
            decisao=dados.get("decisao", dados.get("decision", "")),
            justificativa=dados.get("justificativa", dados.get("justification", "")),
            opcoes=dados.get("opcoes", dados.get("options")),
            riscos=dados.get("riscos", dados.get("risks")),
            plano_acao=dados.get("plano_acao", dados.get("action_plan")),
            participantes=dados.get("participantes", dados.get("participants")),
            artefatos_relacionados=dados.get("artefatos", dados.get("artifacts")),
            resumo=dados.get("resumo", dados.get("summary", "")),
            impacto_tecnico=dados.get("impacto_tecnico", ""),
            impacto_cronograma=dados.get("impacto_cronograma", ""),
            impacto_custo=dados.get("impacto_custo", ""),
            status=dados.get("status", "rascunho"),
            autor=dados.get("autor", dados.get("author", "")),
            urgencia=dados.get("urgencia", dados.get("urgency", "media")),
            numero=dados.get("numero"),
            diretorio_saida=args.output_dir,
        )
    elif args.title:
        caminho = gerar_memo(
            titulo=args.title,
            tipo=args.type,
            contexto=args.context,
            decisao=args.decision,
            justificativa=args.justification,
            status=args.status,
            autor=args.author,
            urgencia=args.urgency,
            numero=args.number,
            diretorio_saida=args.output_dir,
        )
    else:
        parser.error("Forneça --title ou --from-yaml.")
        return

    print(f"Memorando gerado: {caminho}")


if __name__ == "__main__":
    main()
