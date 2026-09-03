# IMP Compiler 01 — Lexical Analysis

**Status:** complete.

This is the first phase of the **IMP compiler in Python** for Winskel's basic
language. It implements lexical analysis: it receives source text and produces
a sequence of tokens containing type, lexeme, line, and column information. It
also builds a lexical table that collects every occurrence of each location
(`LOC`).

The table in this version does not check declarations, types, or scopes. Those
responsibilities will be introduced during the semantic analysis phase.

## Requirements

- Python 3.10 or later.
- Lark 1.2.2.

Using a virtual environment is recommended:

```bash
python -m venv .venv
python -m pip install -r requirements.txt
```

## Usage

From this directory, run:

```bash
python lexer.py ejemplos/ciclo.imp
```

The output displays the tokens in order, followed by the location table. The
example should produce 14 tokens and one entry for `X` with four occurrences.

To see a lexical error:

```bash
python lexer.py ejemplos/error_lexico.imp
```

The program exits with status code 1 and reports the first unrecognized
character together with its line and column.

## Tests

```bash
python -m unittest -v
```

The tests cover IMP recognition, the conflict between reserved words and
locations, Boolean operators, token positions, table entry reuse, and
unrecognized characters.

## Files

- `imp.lark`: token specification and ignored whitespace rules.
- `lexer.py`: driver, analysis interface, and command-line program.
- `tabla_simbolos.py`: lexical table for locations.
- `ejemplos/`: valid input and an input containing a lexical error.
- `tests/`: automated tests.
- `requirements.txt`: required Lark version.
