import tkinter
from tkinter import ttk
from PIL import ImageTk, Image
import os

janela = tkinter.Tk()   

janela.geometry(f"1400x900")
janela.title("My Photos")
janela.config(bg="white")


def login_info():
    caminho_arquivo_perfil = os.path.abspath("/Code/login.py")
    os.system(f'python "{variavel1}" "{variavel2}"')


def clique_profile():
    janela.destroy()
    print("Go to Profile")
    caminho_arquivo2 = os.path.abspath("Code/perfil.py")


file_path = "Files/categorias.txt"

with open(file_path, "r") as f:
    categories = [line.strip() for line in f.readlines()]

cmb = ttk.Combobox(janela, values=categories, width=20)
cmb.place(x=900, y=220)
cmb.set("Seleciona Categoria")


button_myprofile = tkinter.Button(janela, text="My Profile", font=('Arial', 10), padx=30, pady=30, command=clique_profile)
button_myprofile.place(x=1200, y=50)

title = tkinter.Label(janela, text='Latest Álbuns/Most Popular:', font=('Arial', 15))
title.place(x=300, y=210)
title.config(bg='white')

title_filtrar = tkinter.Label(janela, text="Filtrar:", font=("Arial", 10))
title_filtrar.place(x=850, y=218)
title_filtrar.config(bg='white')

lblback = tkinter.Label(janela, padx=400, pady=250)
lblback.place(x=300, y=250)
lblback.config(bg='grey')


button_viewmore = tkinter.Button(janela, text="Vsualizar Mais", font=('Arial'))
button_viewmore.place(x=650, y=770)

janela.mainloop()