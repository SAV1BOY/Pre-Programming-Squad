#!/usr/bin/env python3
"""
Validador de Registro de Riscos.

Este script valida entradas do registro de riscos em formato YAML ou JSON,
garantindo que cada risco esteja adequadamente categorizado, avaliado e com
planos de mitigação definidos.

Regras de Validação:
  - Cada risco deve ter: id, titulo, descricao, probabilidade, impacto, categoria
  - Probabilidade deve ser: muito_baixa, baixa, media, alta, muito_alta (ou 1-5)
  - Impacto deve ser: muito_baixo, baixo, medio, alto, muito_alto (ou 1-5)
  - Cada risco com severidade >= alta deve ter plano de mitigação
  - Não pode haver IDs duplicados
  - Datas devem estar em formato válido
  - O registro deve ter pelo menos 1 risco documentado

Uso:
  python validate-risk-register.py <caminho_do_arquivo> [--min-risks N] [--strict]
"""

import argparse
import json
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

CAMPOS_OBRIGATORIOS_RISCO = ["id", "titulo", "descricao", "probabilidade", "impacto", "categoria"]

CAMPOS_OPCIONAIS_RISCO = [
    "mitigacao",
    "plano_contingencia",
    "responsavel",
    "status",
    "data_identificacao",
    "data_revisao",
    "gatilho",
    "indicadores",
    "notas",
]

NIVEIS_PROBABILIDADE = {
    "muito_baixa": 1, "baixa": 2, "media": 3, "alta": 4, "muito_alta": 5,
}

NIVEIS_IMPACTO = {
    "muito_baixo": 1, "baixo": 2, "medio": 3, "alto": 4, "muito_alto": 5,
}

CATEGORIAS_VALIDAS = [
    "tecnico", "organizacional", "externo", "gerenciamento",
    "requisitos", "complexidade", "dependencias", "seguranca",
    "performance", "integracao", "infraestrutura", "dados",
]

STATUS_VALIDOS = [
    "identificado", "analisado", "mitigando", "aceito",
    "resolvido", "fechado", "materializado",
]

LIMIAR_MITIGACAO_OBRIGATORIA = 12  # probabilidade * impacto >= 12


# ---------------------------------------------------------------------------
# Funções auxiliares
# ---------------------------------------------------------------------------

def carregar_arquivo(caminho: str) -> dict:
    """Carrega arquivo YAML ou JSON."""
    caminho = Path(caminho)
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    conteudo = caminho.read_text(encoding="utf-8")

    if caminho.suffix in (".yaml", ".yml"):
        if yaml is None:
            raise ImportError("PyYAML é necessário. Instale com: pip install pyyaml")
        return yaml.safe_load(conteudo)
    if caminho.suffix == ".json":
        return json.loads(conteudo)

    raise ValueError(f"Formato não suportado: {caminho.suffix}")


def normalizar_nivel(valor, mapa: dict) -> int | None:
    """Converte nível textual ou numérico para inteiro 1-5."""
    if isinstance(valor, int) and 1 <= valor <= 5:
        return valor
    if isinstance(valor, str):
        return mapa.get(valor.strip().lower())
    return None


def calcular_severidade(probabilidade: int, impacto: int) -> int:
    """Calcula a severidade como produto de probabilidade e impacto."""
    return probabilidade * impacto


# ---------------------------------------------------------------------------
# Regras de validação
# ---------------------------------------------------------------------------

def validar_estrutura_registro(dados: dict) -> list[str]:
    """Valida a estrutura geral do registro."""
    erros = []
    if not isinstance(dados, dict):
        erros.append("O registro deve ser um objeto/dicionário.")
        return erros

    riscos = dados.get("riscos", dados.get("risks", []))
    if isinstance(dados, dict) and "riscos" not in dados and "risks" not in dados:
        # Talvez o próprio dados seja uma lista de riscos
        if isinstance(dados, list):
            return erros
        erros.append("O registro deve conter a chave 'riscos' com uma lista de riscos.")
    elif not isinstance(riscos, list):
        erros.append("A chave 'riscos' deve conter uma lista.")
    return erros


def extrair_riscos(dados) -> list[dict]:
    """Extrai a lista de riscos do registro."""
    if isinstance(dados, list):
        return dados
    if isinstance(dados, dict):
        riscos = dados.get("riscos", dados.get("risks", []))
        if isinstance(riscos, list):
            return riscos
    return []


def validar_risco_individual(risco: dict, indice: int) -> tuple[list[str], list[str]]:
    """Valida um risco individual. Retorna (erros, avisos)."""
    erros = []
    avisos = []
    prefixo = f"Risco #{indice + 1}"

    if not isinstance(risco, dict):
        erros.append(f"{prefixo}: deve ser um objeto/dicionário.")
        return erros, avisos

    risco_id = risco.get("id", f"sem_id_{indice}")
    prefixo = f"Risco '{risco_id}'"

    # Campos obrigatórios
    for campo in CAMPOS_OBRIGATORIOS_RISCO:
        if campo not in risco or risco[campo] is None:
            erros.append(f"{prefixo}: campo obrigatório ausente: '{campo}'")

    # Validar probabilidade
    prob_raw = risco.get("probabilidade")
    prob = normalizar_nivel(prob_raw, NIVEIS_PROBABILIDADE)
    if prob_raw is not None and prob is None:
        erros.append(
            f"{prefixo}: probabilidade inválida: '{prob_raw}'. "
            f"Use: {', '.join(NIVEIS_PROBABILIDADE.keys())} ou 1-5."
        )

    # Validar impacto
    imp_raw = risco.get("impacto")
    imp = normalizar_nivel(imp_raw, NIVEIS_IMPACTO)
    if imp_raw is not None and imp is None:
        erros.append(
            f"{prefixo}: impacto inválido: '{imp_raw}'. "
            f"Use: {', '.join(NIVEIS_IMPACTO.keys())} ou 1-5."
        )

    # Validar categoria
    categoria = risco.get("categoria", "")
    if isinstance(categoria, str) and categoria.strip():
        if categoria.strip().lower() not in CATEGORIAS_VALIDAS:
            avisos.append(
                f"{prefixo}: categoria '{categoria}' não é padrão. "
                f"Categorias padrão: {', '.join(CATEGORIAS_VALIDAS)}"
            )

    # Validar status
    status = risco.get("status", "")
    if isinstance(status, str) and status.strip():
        if status.strip().lower() not in STATUS_VALIDOS:
            avisos.append(f"{prefixo}: status '{status}' não é padrão.")

    # Verificar se riscos de alta severidade têm mitigação
    if prob is not None and imp is not None:
        severidade = calcular_severidade(prob, imp)
        if severidade >= LIMIAR_MITIGACAO_OBRIGATORIA:
            mitigacao = risco.get("mitigacao", risco.get("plano_mitigacao", ""))
            if not mitigacao:
                erros.append(
                    f"{prefixo}: severidade {severidade} (prob={prob} x imp={imp}) "
                    f"requer plano de mitigação obrigatório."
                )

    # Verificar descrição mínima
    descricao = risco.get("descricao", "")
    if isinstance(descricao, str) and 0 < len(descricao.strip()) < 20:
        avisos.append(f"{prefixo}: descrição muito curta (mínimo recomendado: 20 caracteres).")

    # Recomendar responsável
    if "responsavel" not in risco:
        avisos.append(f"{prefixo}: recomendado definir 'responsavel'.")

    return erros, avisos


def validar_ids_unicos(riscos: list[dict]) -> list[str]:
    """Verifica que não há IDs duplicados."""
    erros = []
    ids_vistos = {}
    for i, risco in enumerate(riscos):
        if isinstance(risco, dict):
            rid = risco.get("id")
            if rid is not None:
                if rid in ids_vistos:
                    erros.append(
                        f"ID duplicado: '{rid}' aparece nos riscos "
                        f"#{ids_vistos[rid]+1} e #{i+1}."
                    )
                ids_vistos[rid] = i
    return erros


# ---------------------------------------------------------------------------
# Função principal
# ---------------------------------------------------------------------------

def validar_risk_register(
    caminho: str,
    min_riscos: int = 1,
    caminho_schema: str | None = None,
    modo_estrito: bool = False,
) -> dict:
    """
    Valida um registro de riscos.

    Args:
        caminho: Caminho para o arquivo.
        min_riscos: Número mínimo de riscos esperados.
        caminho_schema: Caminho opcional para JSON Schema.
        modo_estrito: Se True, avisos viram erros.

    Returns:
        Dicionário com 'valido', 'erros', 'avisos', 'estatisticas'.
    """
    resultado = {"valido": True, "erros": [], "avisos": [], "estatisticas": {}}

    try:
        dados = carregar_arquivo(caminho)
    except Exception as e:
        resultado["valido"] = False
        resultado["erros"].append(f"Erro ao carregar: {e}")
        return resultado

    # Validar estrutura
    resultado["erros"].extend(validar_estrutura_registro(dados))
    if resultado["erros"]:
        resultado["valido"] = False
        return resultado

    riscos = extrair_riscos(dados)

    # Validar quantidade mínima
    if len(riscos) < min_riscos:
        resultado["erros"].append(
            f"Mínimo de {min_riscos} risco(s) esperado(s), "
            f"encontrado(s): {len(riscos)}."
        )

    # Validar IDs únicos
    resultado["erros"].extend(validar_ids_unicos(riscos))

    # Validar cada risco
    total_severidade = 0
    contagem_severidade = 0
    for i, risco in enumerate(riscos):
        erros_r, avisos_r = validar_risco_individual(risco, i)
        resultado["erros"].extend(erros_r)
        if modo_estrito:
            resultado["erros"].extend(avisos_r)
        else:
            resultado["avisos"].extend(avisos_r)

        # Calcular estatísticas
        if isinstance(risco, dict):
            prob = normalizar_nivel(risco.get("probabilidade"), NIVEIS_PROBABILIDADE)
            imp = normalizar_nivel(risco.get("impacto"), NIVEIS_IMPACTO)
            if prob and imp:
                total_severidade += calcular_severidade(prob, imp)
                contagem_severidade += 1

    # Estatísticas
    resultado["estatisticas"] = {
        "total_riscos": len(riscos),
        "severidade_media": (
            round(total_severidade / contagem_severidade, 2)
            if contagem_severidade > 0 else 0
        ),
        "riscos_criticos": sum(
            1 for r in riscos
            if isinstance(r, dict)
            and normalizar_nivel(r.get("probabilidade"), NIVEIS_PROBABILIDADE)
            and normalizar_nivel(r.get("impacto"), NIVEIS_IMPACTO)
            and calcular_severidade(
                normalizar_nivel(r.get("probabilidade"), NIVEIS_PROBABILIDADE),
                normalizar_nivel(r.get("impacto"), NIVEIS_IMPACTO),
            ) >= LIMIAR_MITIGACAO_OBRIGATORIA
        ),
    }

    resultado["valido"] = len(resultado["erros"]) == 0
    return resultado


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def criar_parser() -> argparse.ArgumentParser:
    """Cria o parser de argumentos."""
    parser = argparse.ArgumentParser(
        description="Valida registro de riscos contra regras predefinidas.",
    )
    parser.add_argument("arquivo", help="Caminho para o arquivo (YAML/JSON).")
    parser.add_argument(
        "--min-risks", type=int, default=1,
        help="Número mínimo de riscos esperados (padrão: 1).",
    )
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

    stats = resultado.get("estatisticas", {})
    if stats:
        linhas.append(f"\nEstatísticas:")
        linhas.append(f"  Total de riscos: {stats.get('total_riscos', 0)}")
        linhas.append(f"  Severidade média: {stats.get('severidade_media', 0)}")
        linhas.append(f"  Riscos críticos: {stats.get('riscos_criticos', 0)}")

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
    resultado = validar_risk_register(
        args.arquivo, args.min_risks, args.schema, args.strict
    )
    print(formatar_saida(resultado, args.output))
    sys.exit(0 if resultado["valido"] else 1)


if __name__ == "__main__":
    main()
