import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import os
from sys import argv

class ProfilePage(tk.Tk):
    def __init__(self, email):
        super().__init__()

        self.title("Perfil do Usuário")
        self.geometry("1400x900")
        self.config(bg="white")

        self.email = email
        self.profile_picture_path = tk.StringVar()

        print(email)

        self.create_widgets()

    def create_widgets(self):
        file_path = "Files/categorias.txt"

        with open(file_path, "r") as f:
            categories = [line.strip() for line in f.readlines()]

        cmb = ttk.Combobox(self, values=categories, width=20)
        cmb.place(x=900, y=220)
        cmb.set("Seleciona Categoria")

        button_myprofile = tk.Button(self, text="My Profile", font=('Arial', 10), padx=30, pady=30, command=self.clique_profile)
        button_myprofile.place(x=1200, y=50)

        title = tk.Label(self, text='Latest Álbuns/Most Popular:', font=('Arial', 15))
        title.place(x=300, y=210)
        title.config(bg='white')

        title_filtrar = tk.Label(self, text="Filtrar:", font=("Arial", 10))
        title_filtrar.place(x=850, y=218)
        title_filtrar.config(bg='white')

        lblback = tk.Label(self, padx=400, pady=250)
        lblback.place(x=300, y=250)
        lblback.config(bg='grey')

        button_viewmore = tk.Button(self, text="Vsualizar Mais", font=('Arial'))
        button_viewmore.place(x=650, y=770)

    def clique_profile(self):
        self.destroy()
        caminho_arquivo_perfil = os.path.abspath("Code/perfil.py")
        print(f'python "{caminho_arquivo_perfil}" "{self.email}"')
        os.system(f'python "{caminho_arquivo_perfil}" "{self.email}"')


if __name__ == "__main__":
    # Certificar-se de que há argumentos suficientes
    if len(argv) == 2:
        # Chamar a classe ProfilePage com o argumento adequado
        app = ProfilePage(argv[1])
        app.mainloop()
    else:
        print("Número incorreto de argumentos. Forneça o endereço de e-mail.")
