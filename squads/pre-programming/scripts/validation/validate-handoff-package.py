#!/usr/bin/env python3
"""
Validador de Pacote de Handoff.

Este script valida a completude de um pacote de handoff (transição) entre a
fase de pré-programação e a fase de desenvolvimento, garantindo que todos os
artefatos necessários estejam presentes e bem documentados.

Regras de Validação:
  - Artefatos obrigatórios: project_brief, architecture_notes, risk_register,
    test_plan, api_contracts, acceptance_criteria
  - Cada artefato deve ter caminho válido ou conteúdo inline
  - O resumo executivo deve estar presente
  - Decisões técnicas devem estar documentadas
  - Critérios de aceite devem ser testáveis
  - Score de prontidão deve atingir limiar mínimo
  - Checklist de handoff deve estar completo

Uso:
  python validate-handoff-package.py <caminho_do_pacote> [--min-score N] [--strict]
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

ARTEFATOS_OBRIGATORIOS = [
    "project_brief",
    "architecture_notes",
    "risk_register",
    "test_plan",
    "api_contracts",
    "acceptance_criteria",
]

ARTEFATOS_RECOMENDADOS = [
    "decision_log",
    "dependency_map",
    "rollout_plan",
    "monitoring_plan",
    "runbook",
    "glossario",
    "diagramas",
]

SECOES_RESUMO_EXECUTIVO = [
    "objetivo",
    "escopo",
    "decisoes_chave",
    "riscos_principais",
    "proximos_passos",
]

SCORE_MINIMO_PADRAO = 70


# ---------------------------------------------------------------------------
# Funções auxiliares
# ---------------------------------------------------------------------------

def carregar_pacote(caminho: str) -> dict:
    """Carrega o pacote de handoff de um arquivo ou diretório."""
    caminho = Path(caminho)

    if not caminho.exists():
        raise FileNotFoundError(f"Caminho não encontrado: {caminho}")

    # Se for diretório, buscar arquivo de manifesto
    if caminho.is_dir():
        for nome in ["handoff.yaml", "handoff.yml", "handoff.json", "manifest.yaml", "manifest.json"]:
            manifesto = caminho / nome
            if manifesto.exists():
                return _carregar_arquivo(manifesto), caminho
        raise FileNotFoundError(
            f"Manifesto de handoff não encontrado no diretório: {caminho}"
        )

    return _carregar_arquivo(caminho), caminho.parent


def _carregar_arquivo(caminho: Path) -> dict:
    """Carrega YAML ou JSON."""
    conteudo = caminho.read_text(encoding="utf-8")
    if caminho.suffix in (".yaml", ".yml"):
        if yaml is None:
            raise ImportError("PyYAML necessário.")
        return yaml.safe_load(conteudo) or {}
    if caminho.suffix == ".json":
        return json.loads(conteudo)
    raise ValueError(f"Formato não suportado: {caminho.suffix}")


# ---------------------------------------------------------------------------
# Regras de validação
# ---------------------------------------------------------------------------

def validar_artefatos_obrigatorios(dados: dict, base_dir: Path) -> tuple[list, list]:
    """Verifica presença de todos os artefatos obrigatórios."""
    erros = []
    avisos = []

    artefatos = dados.get("artefatos", dados)

    for artefato in ARTEFATOS_OBRIGATORIOS:
        if artefato not in artefatos:
            erros.append(f"Artefato obrigatório ausente: '{artefato}'")
            continue

        valor = artefatos[artefato]
        if valor is None:
            erros.append(f"Artefato obrigatório vazio: '{artefato}'")
        elif isinstance(valor, str):
            # Verificar se é caminho para arquivo
            caminho_artefato = base_dir / valor
            if not caminho_artefato.exists() and not valor.startswith("http"):
                avisos.append(
                    f"Artefato '{artefato}': arquivo não encontrado em '{valor}'"
                )
        elif isinstance(valor, dict):
            if "caminho" in valor:
                caminho_artefato = base_dir / valor["caminho"]
                if not caminho_artefato.exists():
                    avisos.append(
                        f"Artefato '{artefato}': arquivo não encontrado em "
                        f"'{valor['caminho']}'"
                    )
            elif "conteudo" not in valor and "url" not in valor:
                erros.append(
                    f"Artefato '{artefato}': deve ter 'caminho', 'conteudo' ou 'url'."
                )

    for artefato in ARTEFATOS_RECOMENDADOS:
        if artefato not in artefatos:
            avisos.append(f"Artefato recomendado ausente: '{artefato}'")

    return erros, avisos


def validar_resumo_executivo(dados: dict) -> list[str]:
    """Valida a presença e qualidade do resumo executivo."""
    erros = []
    resumo = dados.get("resumo_executivo", dados.get("resumo", None))

    if resumo is None:
        erros.append("Resumo executivo ausente. É obrigatório para o handoff.")
        return erros

    if isinstance(resumo, dict):
        for secao in SECOES_RESUMO_EXECUTIVO:
            if secao not in resumo:
                erros.append(f"Resumo executivo: seção '{secao}' ausente.")
    elif isinstance(resumo, str):
        if len(resumo.strip()) < 200:
            erros.append(
                "Resumo executivo muito curto (mínimo 200 caracteres)."
            )
    return erros


def validar_decisoes_tecnicas(dados: dict) -> list[str]:
    """Valida que decisões técnicas estejam documentadas."""
    erros = []
    decisoes = dados.get("decisoes_tecnicas", dados.get("decision_log", []))

    if not decisoes:
        erros.append(
            "Decisões técnicas não documentadas. "
            "Use 'decisoes_tecnicas' ou 'decision_log'."
        )
        return erros

    if isinstance(decisoes, list):
        for i, dec in enumerate(decisoes):
            if isinstance(dec, dict):
                if "decisao" not in dec and "titulo" not in dec:
                    erros.append(
                        f"Decisão #{i+1}: deve conter 'decisao' ou 'titulo'."
                    )
                if "justificativa" not in dec and "razao" not in dec:
                    erros.append(
                        f"Decisão #{i+1}: deve conter 'justificativa'."
                    )
    return erros


def validar_criterios_aceite(dados: dict) -> list[str]:
    """Valida que critérios de aceite sejam testáveis."""
    erros = []
    artefatos = dados.get("artefatos", dados)
    criterios = artefatos.get("acceptance_criteria", [])

    if isinstance(criterios, list):
        for i, criterio in enumerate(criterios):
            texto = str(criterio.get("descricao", criterio) if isinstance(criterio, dict) else criterio)
            # Verificar se é testável (contém condição verificável)
            palavras_testaveis = [
                "deve", "quando", "então", "dado", "se",
                "retorna", "exibe", "calcula", "valida",
                "menor que", "maior que", "igual", "contém",
            ]
            if not any(p in texto.lower() for p in palavras_testaveis):
                erros.append(
                    f"Critério de aceite #{i+1} pode não ser testável: "
                    f"'{texto[:60]}...'"
                )
    return erros


def validar_score_prontidao(dados: dict, score_minimo: int) -> list[str]:
    """Valida o score de prontidão."""
    erros = []
    score = dados.get("readiness_score", dados.get("score_prontidao"))

    if score is None:
        erros.append("Score de prontidão não informado.")
        return erros

    if isinstance(score, (int, float)):
        if score < score_minimo:
            erros.append(
                f"Score de prontidão ({score}) abaixo do mínimo ({score_minimo})."
            )
        if score < 0 or score > 100:
            erros.append(f"Score de prontidão deve estar entre 0 e 100: {score}")
    return erros


def validar_checklist_handoff(dados: dict) -> tuple[list, list]:
    """Valida o checklist de handoff."""
    erros = []
    avisos = []
    checklist = dados.get("checklist", [])

    if not checklist:
        avisos.append("Checklist de handoff não encontrado.")
        return erros, avisos

    itens_incompletos = []
    for i, item in enumerate(checklist):
        if isinstance(item, dict):
            concluido = item.get("concluido", item.get("done", False))
            if not concluido:
                nome = item.get("nome", item.get("item", f"Item #{i+1}"))
                itens_incompletos.append(nome)
        elif isinstance(item, str):
            # Formato simples: "[ ] item" ou "[x] item"
            if item.strip().startswith("[ ]"):
                itens_incompletos.append(item.strip()[3:].strip())

    if itens_incompletos:
        erros.append(
            f"Checklist incompleto ({len(itens_incompletos)} itens pendentes): "
            + ", ".join(itens_incompletos[:5])
            + ("..." if len(itens_incompletos) > 5 else "")
        )

    return erros, avisos


def validar_aprovacoes(dados: dict) -> list[str]:
    """Valida que aprovações necessárias estejam registradas."""
    avisos = []
    aprovacoes = dados.get("aprovacoes", [])
    if not aprovacoes:
        avisos.append("Nenhuma aprovação registrada. Considere obter sign-off formal.")
    return avisos


# ---------------------------------------------------------------------------
# Função principal
# ---------------------------------------------------------------------------

def validar_handoff_package(
    caminho: str,
    score_minimo: int = SCORE_MINIMO_PADRAO,
    modo_estrito: bool = False,
) -> dict:
    """
    Valida um pacote de handoff.

    Args:
        caminho: Caminho para o arquivo ou diretório do pacote.
        score_minimo: Score mínimo de prontidão (0-100).
        modo_estrito: Se True, avisos viram erros.

    Returns:
        Dicionário com 'valido', 'erros', 'avisos', 'completude'.
    """
    resultado = {"valido": True, "erros": [], "avisos": [], "completude": {}}

    try:
        dados, base_dir = carregar_pacote(caminho)
    except Exception as e:
        resultado["valido"] = False
        resultado["erros"].append(f"Erro ao carregar pacote: {e}")
        return resultado

    # Executar validações
    erros_art, avisos_art = validar_artefatos_obrigatorios(dados, base_dir)
    resultado["erros"].extend(erros_art)
    resultado["avisos"].extend(avisos_art)

    resultado["erros"].extend(validar_resumo_executivo(dados))
    resultado["erros"].extend(validar_decisoes_tecnicas(dados))
    resultado["erros"].extend(validar_criterios_aceite(dados))
    resultado["erros"].extend(validar_score_prontidao(dados, score_minimo))

    erros_ck, avisos_ck = validar_checklist_handoff(dados)
    resultado["erros"].extend(erros_ck)
    resultado["avisos"].extend(avisos_ck)

    avisos_aprov = validar_aprovacoes(dados)
    if modo_estrito:
        resultado["erros"].extend(avisos_aprov)
    else:
        resultado["avisos"].extend(avisos_aprov)

    # Calcular completude
    artefatos = dados.get("artefatos", dados)
    total_obrig = len(ARTEFATOS_OBRIGATORIOS)
    presentes = sum(1 for a in ARTEFATOS_OBRIGATORIOS if a in artefatos and artefatos[a])
    resultado["completude"] = {
        "artefatos_obrigatorios": f"{presentes}/{total_obrig}",
        "percentual": round((presentes / total_obrig) * 100, 1) if total_obrig > 0 else 0,
    }

    resultado["valido"] = len(resultado["erros"]) == 0
    return resultado


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def criar_parser() -> argparse.ArgumentParser:
    """Cria o parser de argumentos."""
    parser = argparse.ArgumentParser(
        description="Valida completude do pacote de handoff.",
    )
    parser.add_argument("caminho", help="Caminho para o pacote (arquivo ou diretório).")
    parser.add_argument(
        "--min-score", type=int, default=SCORE_MINIMO_PADRAO,
        help=f"Score mínimo de prontidão (padrão: {SCORE_MINIMO_PADRAO}).",
    )
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

    comp = resultado.get("completude", {})
    if comp:
        linhas.append(f"\nCompletude:")
        linhas.append(f"  Artefatos obrigatórios: {comp.get('artefatos_obrigatorios', 'N/A')}")
        linhas.append(f"  Percentual: {comp.get('percentual', 0)}%")

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
    resultado = validar_handoff_package(args.caminho, args.min_score, args.strict)
    print(formatar_saida(resultado, args.output))
    sys.exit(0 if resultado["valido"] else 1)


if __name__ == "__main__":
    main()
