# Compilador de IMP 01 — Analizador léxico

**Estado:** funcional.

Esta es la primera fase del **compilador de IMP** básico de Winskel. Implementa
el análisis léxico: recibe texto fuente y produce una secuencia de tokens con
tipo, lexema, línea y columna. También construye una tabla léxica que reúne las
apariciones de cada localidad (`LOC`).

La tabla de esta versión no comprueba declaraciones, tipos ni alcances. Esas
responsabilidades se incorporarán en la fase semántica.

## Requisitos

- Python 3.10 o posterior.
- Lark 1.2.2.

Se recomienda utilizar un entorno virtual:

```bash
$ python -m venv .venv
$ source .venv/bin/activate
$ python -m pip install -r requirements.txt
```

## Ejecución

Desde esta carpeta:

```bash
python lexer.py ejemplos/ciclo.imp
```

La salida muestra los tokens en orden y, al final, la tabla de localidades. El
ejemplo debe producir 14 tokens y una entrada para `X` con cuatro apariciones.

Para observar un error léxico:

```bash
python lexer.py ejemplos/error_lexico.imp
```

El programa termina con código 1 e informa el primer carácter no reconocido,
su línea y su columna.

## Pruebas

```bash
python -m unittest -v
```

Las pruebas comprueban el reconocimiento de IMP, el conflicto entre palabras
reservadas y localidades, los operadores booleanos, la posición de los tokens,
la reutilización de entradas en la tabla y los caracteres no reconocidos.

## Archivos

- `imp.lark`: especificación de tokens y espacios omitidos.
- `lexer.py`: controlador, interfaz de análisis y programa de línea de comandos.
- `tabla_simbolos.py`: tabla léxica de localidades.
- `ejemplos/`: entrada correcta y entrada con error.
- `tests/`: pruebas automatizadas.
- `requirements.txt`: versión de Lark utilizada.
