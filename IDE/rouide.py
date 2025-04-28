import tkinter as tk
from tkinter import filedialog
import sys

#Interpretar codigo Roupy
def run_roupy_code(code):
    lines = code.strip().split("\n")
    output = ""
    for line in lines:
        line = line.strip()
        if line.startswith("show = "):
            text_to_show = line.split("=", 1)[1].strip()

            # Verificar si el texto está entre comillas
            if text_to_show.startswith('"') and text_to_show.endswith('"'):
                text_to_show = text_to_show[1:-1]  # Eliminar las comillas
                output += text_to_show + "\n"
            else:
                output += "Syntax Error: Expected text in double quotes.\n"
    return output

	
#Funcion CUAndo PRESIONAS RUN

def run_code():
	code = text_editor.get("1.0", tk.END)
	result = run_roupy_code(code)
	output_text.delete("1.0", tk.END)
	output_text.insert(tk.END, result)
	
# FUNCION PARA GUARDAR ARCHIVOS

def save_file():
	file_path = filedialog.asksaveasfilename(defaultextension=".rp", filetypes =[("Roupy Files", "*.rp")])
	if file_path:
		with open(file_path, "w") as file:
			file.write(text_editor.get("1.0", tk.END))

def open_file():
	file_path = filedialog.askopenfilename(defaultextension=".rp", filetypes=[("Roupy Files", "*.rp")])
	if file_path:
		with open(file_path, "r") as file:
			file_content = file.read()
			text_editor.delete("1.0", tk.END) #BORRAR EL CONTENIDO ACTUAL
			text_editor.insert(tk.END, file_content) #INSERTAR EL CONENIDO DEL ARCHIVO
# CREAR VENTANA PRINCIPAL
root = tk.Tk()
root.title("RoupyIDE")
root.geometry("800x600")

#AREA DE TEXTO PARA ESCRIBIR
text_editor = tk.Text(root, height=15, bg="black", fg="lime", insertbackground="white", font=("Courier", 12))
text_editor.pack(fill=tk.BOTH, expand=True)

#BOTON RUN
run_button = tk.Button(root, text="Run", command=run_code, bg="black", fg="lime", font=("Courier", 10))
run_button.pack()

#BOTON SAVE
save_button = tk.Button(root, text="Save", command=save_file, bg="black", fg="lime", font=("Courier", 10))
save_button.pack()

#BOTON OPEN
open_button = tk.Button(root, text="Open", command=open_file, bg="black", fg="lime", font=("Courier", 10))
open_button.pack()
#AREA DE RESULTADOS
output_text = tk.Text(root, height=10, bg="black", fg="lime", insertbackground="white", font=("Courier", 12))
output_text.pack(fill=tk.BOTH, expand=True)

root.mainloop()
	
