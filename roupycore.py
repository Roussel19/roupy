# roupycore.py

import sys
import re

variables = {}
# EL LEXER: CONVIERTE EL CODIGO FUENTE EN UNA LISTA DE TOKENS
def lexer(code):
    token_patterns = [
        ('STRING', r'"[^"]*"'),
        ('NUMBER', r'\d+'),
        ('ID', r'[A-Za-z_][A-Za-z0-9_]*'),
        ('ASSIGN', r'='),
        ('COMMA', r','),
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
    if not tokens:
        return ""

    if tokens[0][0] == 'ID' and tokens[1][0] == 'ASSIGN':
        var_name = tokens[0][1]
        value_tokens = tokens[2:]  # Todos los tokens después del '='

        if var_name == 'show':
            parts = []
            expecting_value = True  # esperamos un valor, no una coma

            for token in value_tokens:
                if expecting_value:
                    if token[0] == 'STRING':
                        parts.append(token[1][1:-1])  # Agregar texto (sin comillas)
                    elif token[0] == 'ID':
                        if token[1] in variables:
                            parts.append(str(variables[token[1]]))  # Agregar valor de variable
                        else:
                            return f"Name Error: Variable '{token[1]}' not found."
                    else:
                        return "Syntax Error: show must have strings or variable names."
                    expecting_value = False
                else:
                    if token[0] != 'COMMA':
                        return "Syntax Error: Expected a comma between values."
                    expecting_value = True

            if expecting_value:
                return "Syntax Error: Trailing comma at the end."

            return " ".join(parts)  # Unir las partes con espacio
        else:
            # Asignar variables
            if len(value_tokens) != 1:
                return "Syntax Error: Only one value can be assigned to a variable."
            
            value_token = value_tokens[0]
            if value_token[0] == 'STRING':
                variables[var_name] = value_token[1][1:-1]
            elif value_token[0] == 'NUMBER':
                variables[var_name] = int(value_token[1])
            else:
                return "Syntax Error: Only strings and integers can be assigned."
            return ""
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

