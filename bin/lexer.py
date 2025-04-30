import re

def lexer(code):
    token_patterns = [
        ('STRING', r'"[^"]*"'),
        ('FLOAT', r'\d+\.\d+'),     # <-- ¡Primero va FLOAT!
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
