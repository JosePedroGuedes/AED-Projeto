import tkinter as tk
import os

def categorias(pagina):
    pagina += "_categorias"
    janela.destroy()
    caminho_arquivo = os.path.abspath(f"AED-Projeto/Code/{pagina}.py")
    print(caminho_arquivo)
    os.system(f'python "{caminho_arquivo}"')

janela = tk.Tk()
janela.title("Página Admin")

rotulo = tk.Label(janela, text="Página de admin")
rotulo.pack(padx=20, pady=20)

rotulo = tk.Label(janela, text="Categorias")

# Botão de Adicionar
botao_adicionar = tk.Button(janela, text="Adicionar Categoria", command=lambda:categorias("adicionar"))
botao_adicionar.pack(pady=10)

# Botão de Remover
botao_remover = tk.Button(janela, text="Remover Categoria", command=lambda:categorias("eliminar"))
botao_remover.pack(pady=10)

# Botão de Editar
botao_editar = tk.Button(janela, text="Editar Categoria", command=lambda:categorias("editar"))
botao_editar.pack(pady=10)

janela.mainloop()