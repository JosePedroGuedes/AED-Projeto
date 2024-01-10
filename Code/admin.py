import tkinter as tk
import os
from tkinter import font

def categorias(pagina):
    pagina += "_accounts"
    janela.destroy()
    caminho_arquivo = os.path.abspath(f"AED-Projeto/Code/{pagina}.py")
    print(caminho_arquivo)
    os.system(f'python "{caminho_arquivo}"')

def utilizadores(pagina):
    pagina += "_categorias"
    janela.destroy()
    caminho_arquivo = os.path.abspath(f"AED-Projeto/Code/{pagina}.py")
    print(caminho_arquivo)
    os.system(f'python "{caminho_arquivo}"')

janela = tk.Tk()
janela.title("Página Admin")

fonte_titulo = font.Font(size=35)
titulo = tk.Label(janela, text="Página de admin", font=fonte_titulo)
titulo.pack(padx=20, pady=10)

fonte_titulo_categoria= font.Font(size=20)
fonte_titulo_categoria = tk.Label(janela, text="Categorias", font=fonte_titulo_categoria)
fonte_titulo_categoria.pack(padx=20, pady=20)

# Botão de Adicionar Categorias
botao_adicionar_categorias = tk.Button(janela, text="Adicionar Categoria", command=lambda:categorias("adicionar"))
botao_adicionar_categorias.pack(pady=10)

# Botão de Remover Categorias
botao_remover_categorias = tk.Button(janela, text="Remover Categoria", command=lambda:categorias("eliminar"))
botao_remover_categorias.pack(pady=10)

# Botão de Editar Categorias
botao_editar_categorias = tk.Button(janela, text="Editar Categoria", command=lambda:categorias("editar"))
botao_editar_categorias.pack(pady=10)


fonte_titulo_utilizadores= font.Font(size=20)
fonte_titulo_utilizadores = tk.Label(janela, text="Utilizadores", font=fonte_titulo_utilizadores)
fonte_titulo_utilizadores.pack(padx=20, pady=20)

# Botão de Adicionar Utilizadores
botao_editar_utilizadores = tk.Button(janela, text="Editar Utilizador", command=lambda:utilizadores("editar"))
botao_editar_utilizadores.pack(pady=10)

# Botão de Remover Utilizadores
botao_remover_utilizadores = tk.Button(janela, text="Remover Utilizador", command=lambda:utilizadores("eliminar"))
botao_remover_utilizadores.pack(pady=10)

janela.mainloop()