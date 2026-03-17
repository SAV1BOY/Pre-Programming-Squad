#!/usr/bin/env python3
"""
Construtor de Matriz de Testes.

Este script gera uma matriz de testes a partir de requisitos do projeto,
mapeando cada requisito aos tipos de teste necessários, cenários de teste
e critérios de cobertura.

Funcionalidades:
  - Geração de matriz requisito-teste
  - Classificação automática de tipos de teste necessários
  - Estimativa de esforço de teste por requisito
  - Identificação de lacunas de cobertura
  - Exportação em múltiplos formatos (texto, JSON, CSV)

Uso:
  python test-matrix-builder.py <requisitos> [--format text|json|csv] [--coverage-target N]
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

TIPOS_TESTE = {
    "unitario": {
        "nome": "Teste Unitário",
        "descricao": "Testa componentes individuais isoladamente",
        "keywords": ["calcular", "converter", "validar", "formatar", "parser", "transformar"],
    },
    "integracao": {
        "nome": "Teste de Integração",
        "descricao": "Testa a interação entre componentes",
        "keywords": ["integrar", "api", "endpoint", "serviço", "banco", "fila", "mensagem"],
    },
    "e2e": {
        "nome": "Teste End-to-End",
        "descricao": "Testa fluxos completos do usuário",
        "keywords": ["fluxo", "jornada", "usuário", "tela", "página", "formulário"],
    },
    "performance": {
        "nome": "Teste de Performance",
        "descricao": "Testa requisitos não-funcionais de desempenho",
        "keywords": ["performance", "latência", "throughput", "carga", "tempo", "resposta", "simultâneo"],
    },
    "seguranca": {
        "nome": "Teste de Segurança",
        "descricao": "Testa vulnerabilidades e conformidade",
        "keywords": ["segurança", "autenticação", "autorização", "token", "criptografia", "owasp"],
    },
    "acessibilidade": {
        "nome": "Teste de Acessibilidade",
        "descricao": "Testa conformidade com WCAG e usabilidade",
        "keywords": ["acessibilidade", "wcag", "leitor", "contraste", "navegação", "teclado"],
    },
    "regressao": {
        "nome": "Teste de Regressão",
        "descricao": "Garante que mudanças não quebrem funcionalidades existentes",
        "keywords": ["migração", "atualização", "refatoração", "legado", "compatibilidade"],
    },
}

PRIORIDADES = {"critica": 4, "alta": 3, "media": 2, "baixa": 1}

ESFORCO_BASE = {"unitario": 1, "integracao": 2, "e2e": 3, "performance": 2, "seguranca": 2, "acessibilidade": 1, "regressao": 2}


# ---------------------------------------------------------------------------
# Carregamento
# ---------------------------------------------------------------------------

def carregar_dados(caminho: str) -> dict:
    """Carrega requisitos de YAML ou JSON."""
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


def extrair_requisitos(dados: dict) -> list[dict]:
    """Extrai lista de requisitos."""
    return dados.get("requisitos", dados.get("requirements", []))


# ---------------------------------------------------------------------------
# Classificação e geração
# ---------------------------------------------------------------------------

def classificar_tipos_teste(requisito: dict) -> list[str]:
    """Classifica quais tipos de teste são necessários para um requisito."""
    texto = " ".join([
        str(requisito.get("descricao", "")),
        str(requisito.get("titulo", "")),
        str(requisito.get("criterio_aceite", "")),
        " ".join(str(t) for t in requisito.get("tags", [])),
    ]).lower()

    tipos_necessarios = []

    for tipo_id, tipo_info in TIPOS_TESTE.items():
        for keyword in tipo_info["keywords"]:
            if keyword in texto:
                tipos_necessarios.append(tipo_id)
                break

    # Todo requisito funcional deve ter ao menos teste unitário
    if not tipos_necessarios:
        tipos_necessarios.append("unitario")

    # Se tem integração, também precisa de regressão
    if "integracao" in tipos_necessarios and "regressao" not in tipos_necessarios:
        tipos_necessarios.append("regressao")

    return list(set(tipos_necessarios))


def gerar_cenarios(requisito: dict, tipos_teste: list[str]) -> list[dict]:
    """Gera cenários de teste para um requisito."""
    cenarios = []
    titulo = requisito.get("titulo", requisito.get("descricao", "Requisito"))[:50]

    for tipo in tipos_teste:
        nome_tipo = TIPOS_TESTE.get(tipo, {}).get("nome", tipo)

        # Cenário positivo
        cenarios.append({
            "id": f"TC-{tipo[:3].upper()}-POS",
            "tipo": tipo,
            "nome": f"{nome_tipo}: Cenário positivo - {titulo}",
            "descricao": f"Verificar comportamento esperado para {titulo}",
            "prioridade": "alta",
        })

        # Cenário negativo
        cenarios.append({
            "id": f"TC-{tipo[:3].upper()}-NEG",
            "tipo": tipo,
            "nome": f"{nome_tipo}: Cenário negativo - {titulo}",
            "descricao": f"Verificar tratamento de erros para {titulo}",
            "prioridade": "media",
        })

        # Cenário de borda para tipos específicos
        if tipo in ("unitario", "integracao"):
            cenarios.append({
                "id": f"TC-{tipo[:3].upper()}-BRD",
                "tipo": tipo,
                "nome": f"{nome_tipo}: Caso de borda - {titulo}",
                "descricao": f"Verificar limites e valores extremos para {titulo}",
                "prioridade": "media",
            })

    return cenarios


def estimar_esforco(tipos_teste: list[str], prioridade: str) -> dict:
    """Estima o esforço de teste em story points."""
    mult_prioridade = {"critica": 1.5, "alta": 1.2, "media": 1.0, "baixa": 0.8}
    mult = mult_prioridade.get(prioridade.lower(), 1.0)

    esforco_total = sum(ESFORCO_BASE.get(t, 1) for t in tipos_teste)
    esforco_ajustado = round(esforco_total * mult, 1)

    return {
        "story_points": esforco_ajustado,
        "horas_estimadas": esforco_ajustado * 2,  # 2h por story point
        "detalhamento": {t: ESFORCO_BASE.get(t, 1) for t in tipos_teste},
    }


def construir_matriz(requisitos: list[dict], meta_cobertura: int = 80) -> dict:
    """
    Constrói a matriz de testes completa.

    Args:
        requisitos: Lista de requisitos.
        meta_cobertura: Meta de cobertura percentual.

    Returns:
        Matriz com mapeamento requisito-teste.
    """
    entradas = []
    esforco_total = 0
    total_cenarios = 0

    for i, req in enumerate(requisitos):
        if not isinstance(req, dict):
            continue

        req_id = req.get("id", f"REQ-{i+1:03d}")
        titulo = req.get("titulo", req.get("descricao", "Sem título"))
        prioridade = req.get("prioridade", req.get("priority", "media"))

        tipos = classificar_tipos_teste(req)
        cenarios = gerar_cenarios(req, tipos)
        esforco = estimar_esforco(tipos, prioridade)

        entrada = {
            "requisito_id": req_id,
            "titulo": titulo,
            "prioridade": prioridade,
            "tipos_teste": tipos,
            "cenarios": cenarios,
            "esforco": esforco,
            "cobertura": {t: True for t in tipos},
        }
        entradas.append(entrada)
        esforco_total += esforco["story_points"]
        total_cenarios += len(cenarios)

    # Análise de cobertura
    todos_tipos = set()
    for e in entradas:
        todos_tipos.update(e["tipos_teste"])

    cobertura_por_tipo = {}
    for tipo in TIPOS_TESTE:
        reqs_com_tipo = sum(1 for e in entradas if tipo in e["tipos_teste"])
        cobertura_por_tipo[tipo] = {
            "requisitos_cobertos": reqs_com_tipo,
            "percentual": round((reqs_com_tipo / len(entradas)) * 100, 1) if entradas else 0,
        }

    # Lacunas
    lacunas = []
    for tipo, info in cobertura_por_tipo.items():
        if info["percentual"] < meta_cobertura and tipo in ("unitario", "integracao"):
            lacunas.append(
                f"Cobertura de {TIPOS_TESTE[tipo]['nome']} ({info['percentual']}%) "
                f"abaixo da meta de {meta_cobertura}%."
            )

    return {
        "matriz": entradas,
        "resumo": {
            "total_requisitos": len(entradas),
            "total_cenarios": total_cenarios,
            "esforco_total_sp": esforco_total,
            "esforco_total_horas": esforco_total * 2,
            "tipos_teste_utilizados": list(todos_tipos),
        },
        "cobertura_por_tipo": cobertura_por_tipo,
        "lacunas": lacunas,
        "meta_cobertura": meta_cobertura,
    }


# ---------------------------------------------------------------------------
# Formatação
# ---------------------------------------------------------------------------

def formatar_texto(resultado: dict) -> str:
    """Formata a matriz como texto."""
    linhas = []
    linhas.append("=" * 70)
    linhas.append("  MATRIZ DE TESTES")
    linhas.append("=" * 70)

    r = resultado["resumo"]
    linhas.append(f"\nRequisitos: {r['total_requisitos']}")
    linhas.append(f"Cenários: {r['total_cenarios']}")
    linhas.append(f"Esforço estimado: {r['esforco_total_sp']} SP ({r['esforco_total_horas']}h)")

    linhas.append(f"\n{'-' * 70}")
    linhas.append("MAPEAMENTO REQUISITO -> TESTES:")
    linhas.append(f"{'Requisito':<15} {'Título':<30} {'Tipos de Teste':<25}")
    linhas.append("-" * 70)

    for entrada in resultado["matriz"]:
        tipos = ", ".join(entrada["tipos_teste"])
        titulo = entrada["titulo"][:28]
        linhas.append(f"{entrada['requisito_id']:<15} {titulo:<30} {tipos:<25}")

    linhas.append(f"\n{'-' * 70}")
    linhas.append("COBERTURA POR TIPO:")
    for tipo, info in resultado["cobertura_por_tipo"].items():
        nome = TIPOS_TESTE.get(tipo, {}).get("nome", tipo)
        barra = "#" * int(info["percentual"] / 5) + "." * (20 - int(info["percentual"] / 5))
        linhas.append(f"  {nome:<25} {info['percentual']:>5.1f}% [{barra}]")

    if resultado["lacunas"]:
        linhas.append(f"\nLACUNAS:")
        for lac in resultado["lacunas"]:
            linhas.append(f"  * {lac}")

    linhas.append(f"\n{'=' * 70}")
    return "\n".join(linhas)


def formatar_csv(resultado: dict) -> str:
    """Formata a matriz como CSV."""
    linhas = ["requisito_id,titulo,prioridade,tipos_teste,cenarios,story_points"]
    for e in resultado["matriz"]:
        tipos = "|".join(e["tipos_teste"])
        linhas.append(
            f"{e['requisito_id']},{e['titulo']},{e['prioridade']},"
            f"{tipos},{len(e['cenarios'])},{e['esforco']['story_points']}"
        )
    return "\n".join(linhas)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def criar_parser() -> argparse.ArgumentParser:
    """Cria o parser de argumentos."""
    parser = argparse.ArgumentParser(
        description="Gera matriz de testes a partir de requisitos.",
    )
    parser.add_argument("arquivo", help="Arquivo de requisitos (YAML/JSON).")
    parser.add_argument(
        "--format", choices=["text", "json", "csv"], default="text",
        help="Formato de saída.",
    )
    parser.add_argument(
        "--coverage-target", type=int, default=80,
        help="Meta de cobertura em percentual (padrão: 80).",
    )
    parser.add_argument("--output-file", default=None, help="Arquivo de saída.")
    return parser


def main():
    """Ponto de entrada principal."""
    parser = criar_parser()
    args = parser.parse_args()

    dados = carregar_dados(args.arquivo)
    requisitos = extrair_requisitos(dados)
    resultado = construir_matriz(requisitos, args.coverage_target)

    if args.format == "json":
        saida = json.dumps(resultado, indent=2, ensure_ascii=False)
    elif args.format == "csv":
        saida = formatar_csv(resultado)
    else:
        saida = formatar_texto(resultado)

    if args.output_file:
        Path(args.output_file).write_text(saida, encoding="utf-8")
        print(f"Matriz salva em: {args.output_file}")
    else:
        print(saida)


if __name__ == "__main__":
    main()
