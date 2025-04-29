import sys
from roupycore import run_roupy_file

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: Python main.py <archivo.rp>")
	else:
		run_roupy_file(sys.argv[1])
