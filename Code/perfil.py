# perfil.py

import tkinter as tk
from sys import argv

def exibir_perfil(email, password):
    perfil_janela = tk.Tk()
    perfil_janela.geometry("500x300")
    perfil_janela.title("Perfil")

    # Adicionar Text widgets para exibir as informações de login
    text_email = tk.Text(perfil_janela, height=1, width=40)
    text_email.insert(tk.END, f"Email: {email}")
    text_email.pack(pady=10)

    text_password = tk.Text(perfil_janela, height=1, width=40)
    text_password.insert(tk.END, f"Password: {password}")
    text_password.pack(pady=10)

    # Adicionar mais Text widgets ou outros elementos conforme necessário

    perfil_janela.mainloop()

# Verificar se a função está sendo chamada como script principal
if __name__ == "__main__":
    # Certificar-se de que a quantidade correta de argumentos está presente
    if len(argv) == 3:
        # Chamar a função exibir_perfil com os argumentos adequados
        exibir_perfil(argv[1], argv[2])
    else:
        print("Usage: python perfil.py <email> <password>")
