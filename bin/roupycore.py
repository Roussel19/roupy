from lexer import lexer
from parser import interpret_tokens

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

