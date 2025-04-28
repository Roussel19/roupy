# roupycore.py

import sys
import re

# EL LEXER: CONVIERTE EL CODIGO FUENTE EN UNA LISTA DE TOKENS
def lexer(code):
    # PATRONES PARA RECONOCER LOS TIPOS DE TOKENS
    token_patterns = [
        ('STRING', r'"[^"]*"'),  # CADENAS ENTRE COMILLAS DOBLES
        ('ID', r'[A-Za-z_][A-Za-z0-9_]*'),  # IDENTIFICADORES (NOMBRES DE VARIABLES)
        ('ASSIGN', r'='),  # OPERADOR DE ASIGNACION
        ('NEWLINE', r'\n'),  # SALTO DE LINEA
        ('SKIP', r'[ \t]+'),  # ESPACIOS Y TABULACIONES IGNORAMOS
        ('MISMATCH', r'.'),  # cualquier cosa que no sea un token valido
    ]
    
    # UNIR TODOS LOS PATRONES EN UNA SOLA EXPRESION REGULAR
    token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_patterns)
    
    # GENERAR LOS TOKENS CON re.finditer, que nos permite encontrar coincidencias
    for mo in re.finditer(token_regex, code):
        kind = mo.lastgroup  # EL TIPO DE TOKEN ENCONTRADO
        value = mo.group()  # EL VALOR DEL TOKEN
        if kind == 'SKIP':
            continue  # IGNORAR ESPACIOS Y TABULACIONES
        elif kind == 'MISMATCH':
            raise RuntimeError(f"Caracter inesperado: {value!r}")
        else:
            yield kind, value  # GENERAR EL TIPO DE TOKEN Y SU VALOR

			
def interpret_tokens(tokens):
    # COMPROBAR SI LA LÍNEA ES UNA ASIGNACIÓN DE LA FORMA 'show = "texto"'
    if tokens[0][0] == 'ID' and tokens[0][1] == 'show' and tokens[1][0] == 'ASSIGN':
        if tokens[2][0] == 'STRING':  # Si el token es de tipo STRING (es decir, entre comillas)
            text = tokens[2][1][1:-1]  # Eliminar las comillas
            print(text)
        else:
            print("Syntax Error: Expected a string value enclosed in double quotes.")  # Mensaje de error cuando no es una cadena
    else:
        print("Syntax Error: Invalid assignment.")


# 1. Leer el archivo Roupy (.rp)
def run_rouy_file(file_path):
	with open(file_path, 'r') as file:
		lines = file.readlines()
		
		for line in lines:
			tokens = list(lexer(line.strip())) #TOKENIZAMOS LA LINEA
			interpret_tokens(tokens) #INTERPRETAMOS LA LISTA DE TOKENS
			

# 3. Puntos de entrada
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: python roupycore.py <file.rp>")
	else:
		filename = sys.argv[1]
		run_rouy_file(filename)
