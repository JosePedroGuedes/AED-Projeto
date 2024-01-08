import tkinter as tk

# Criar a janela
janela = tk.Tk()
janela.title("Exemplo de Rótulo")

# Criar um rótulo
rotulo = tk.Label(janela, text="Editar Categorias!")
rotulo.pack(padx=20, pady=20)

# Iniciar o loop principal da interface gráfica
janela.mainloop()
