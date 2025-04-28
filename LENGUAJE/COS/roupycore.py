# roupycore.py

import sys
import re

# EL LEXER: CONVIERTE EL CODIGO FUENTE EN UNA LISTA DE TOKENS
def lexer(code):
    token_patterns = [
        ('STRING', r'"[^"]*"'),
        ('ID', r'[A-Za-z_][A-Za-z0-9_]*'),
        ('ASSIGN', r'='),
        ('NEWLINE', r'\n'),
        ('SKIP', r'[ \t]+'),
        ('MISMATCH', r'.'),
    ]
    
    token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_patterns)
    
    for mo in re.finditer(token_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f"Caracter inesperado: {value!r}")
        else:
            yield kind, value

# Función que interpreta una lista de tokens y devuelve el resultado como string
def interpret_tokens(tokens):
    if tokens and tokens[0][0] == 'ID' and tokens[0][1] == 'show' and tokens[1][0] == 'ASSIGN':
        if tokens[2][0] == 'STRING':
            text = tokens[2][1][1:-1]  # Eliminar las comillas
            return text
        else:
            return "Syntax Error: Expected a string value enclosed in double quotes."
    else:
        return "Syntax Error: Invalid assignment."

# ✅ Nueva función para que el IDE pueda usar
def run_roupy_code(code):
    lines = code.strip().split('\n')
    output = []
    
    for line in lines:
        if not line.strip():
            continue  # Saltar líneas vacías
        tokens = list(lexer(line.strip()))
        result = interpret_tokens(tokens)
        output.append(result)
    
    return "\n".join(output)

# Puntos de entrada si se ejecuta desde consola
def run_roupy_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            tokens = list(lexer(line.strip()))
            print(interpret_tokens(tokens))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python roupycore.py <file.rp>")
    else:
        filename = sys.argv[1]
        run_roupy_file(filename)

