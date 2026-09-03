"""Analizador léxico independiente para el IMP básico de Winskel."""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

from lark import Lark, Token
from lark.exceptions import UnexpectedCharacters

from tabla_simbolos import TablaSimbolos


RUTA_GRAMATICA = Path(__file__).with_name("imp.lark")


@dataclass
class ResultadoLexico:
    """Productos observables de la fase léxica."""

    tokens: list[Token]
    tabla: TablaSimbolos


def construir_lexer() -> Lark:
    """Construye el lexer a partir de la especificación local."""
    gramatica = RUTA_GRAMATICA.read_text(encoding="utf-8")
    return Lark(
        gramatica,
        parser=None,
        lexer="basic",
        propagate_positions=True,
    )


def analizar(codigo_fuente: str) -> ResultadoLexico:
    """Tokeniza el código y registra las apariciones de cada localidad."""
    tokens = list(construir_lexer().lex(codigo_fuente))
    tabla = TablaSimbolos()
    for token in tokens:
        if token.type == "LOC":
            tabla.registrar(token)
    return ResultadoLexico(tokens, tabla)


def mostrar_resultado(resultado: ResultadoLexico) -> None:
    """Muestra tokens y tabla léxica en un formato legible."""
    print(f"{'TIPO':<10} {'LEXEMA':<16} POSICION")
    for token in resultado.tokens:
        print(
            f"{token.type:<10} {str(token)!r:<16} "
            f"{token.line}:{token.column}"
        )

    print("\nTABLA DE LOCALIDADES")
    for entrada in resultado.tabla.entradas():
        posiciones = ", ".join(
            f"{item.linea}:{item.columna}" for item in entrada.apariciones
        )
        print(f"{entrada.indice:<4} {entrada.lexema:<16} {posiciones}")


def leer_argumentos() -> argparse.Namespace:
    """Lee la ruta del programa IMP que se analizará."""
    parser = argparse.ArgumentParser(description="Lexer de IMP")
    parser.add_argument("archivo", type=Path, help="archivo fuente de IMP")
    return parser.parse_args()


def main() -> int:
    argumentos = leer_argumentos()
    codigo = argumentos.archivo.read_text(encoding="utf-8")

    try:
        mostrar_resultado(analizar(codigo))
    except UnexpectedCharacters as error:
        print(
            f"Error lexico en linea {error.line}, "
            f"columna {error.column}: {error.char!r}",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
