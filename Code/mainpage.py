import tkinter
from tkinter import ttk
from PIL import ImageTk, Image

janela = tkinter.Tk()   

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

janela.geometry(f"{largura_tela}x{altura_tela}")
janela.title("My Photos")
janela.config(bg="white")



file_path = "Files/categorias.txt"

with open(file_path, "r") as f:
    categories = [line.strip() for line in f.readlines()]

cmb = ttk.Combobox(janela, values=categories, width=20)
cmb.place(x=900, y=210)
cmb.set("Seleciona Categoria")


button_myprofile = tkinter.Button(janela, text="My Profile", font=('Arial', 10), padx=30, pady=30)
button_myprofile.place(x=1200, y=50)

title = tkinter.Label(janela, text='Latest Albums/Most Popular:', font=('Arial', 15))
title.place(x=300, y=200)
title.config(bg='white')

lblback = tkinter.Label(janela, padx=400, pady=250)
lblback.place(x=300, y=250)
lblback.config(bg='grey')

janela.mainloop()
    