import tkinter as tk
from tkinter import filedialog
import sys

from roupycore import run_roupy_code

# Paleta de colores estilo VSCode
bg_main = "#1e1e2e"           # Fondo principal (oscuro, con toque azul)
bg_text = "#252526"           # Área de texto fondo (gris oscuro azulado)
fg_text = "#d4d4d4"           # Texto (gris claro)
fg_accent = "#00ff88"         # Verde neón para botones y resaltado
font_family = "Courier"

# Interpretar código Roupy
def run_code():
    code = text_editor.get("1.0", tk.END)
    try:
        result = run_roupy_code(code)
    except Exception as e:
        result = f"Error al interpretar el código: {str(e)}"
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

# Guardar archivo .rp
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".rp", filetypes=[("Roupy Files", "*.rp")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_editor.get("1.0", tk.END))

# Abrir archivo .rp
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".rp", filetypes=[("Roupy Files", "*.rp")])
    if file_path:
        with open(file_path, "r") as file:
            file_content = file.read()
            text_editor.delete("1.0", tk.END)
            text_editor.insert(tk.END, file_content)

# Ventana principal
root = tk.Tk()
root.title("RoupyIDE")
root.geometry("800x600")
root.configure(bg=bg_main)

# Área de texto para escribir
text_editor = tk.Text(
    root,
    height=15,
    bg=bg_text,
    fg=fg_text,
    insertbackground=fg_text,
    font=(font_family, 12)
)
text_editor.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Botón Run
run_button = tk.Button(
    root,
    text="Run",
    command=run_code,
    bg=bg_main,
    fg=fg_accent,
    font=(font_family, 10),
    activebackground="#333344",
    activeforeground=fg_accent
)
run_button.pack(pady=2)

# Botón Save
save_button = tk.Button(
    root,
    text="Save",
    command=save_file,
    bg=bg_main,
    fg=fg_accent,
    font=(font_family, 10),
    activebackground="#333344",
    activeforeground=fg_accent
)
save_button.pack(pady=2)

# Botón Open
open_button = tk.Button(
    root,
    text="Open",
    command=open_file,
    bg=bg_main,
    fg=fg_accent,
    font=(font_family, 10),
    activebackground="#333344",
    activeforeground=fg_accent
)
open_button.pack(pady=2)

# Área de resultados
output_text = tk.Text(
    root,
    height=10,
    bg=bg_text,
    fg=fg_text,
    insertbackground=fg_text,
    font=(font_family, 12)
)
output_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

root.mainloop()

