import sys
from parser import run_roupy_file

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <archivo.rp>")
    else:
        run_file(sys.argv[1])
