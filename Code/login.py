import tkinter
import os

janela = tkinter.Tk()
janela.geometry("500x300")
janela.title("My Photos Login")
janela.config(bg="white")


file = open("AED-Projeto/Files/accounts.txt", "w")

def clique_login():
    print("Fazer Login")


def clique_register():
    janela.destroy()
    print("Fazer Registo")
    caminho_arquivo2 = os.path.abspath("AED-Projeto/Code/register.py")  
    os.system(f'python "{caminho_arquivo2}"')


def limpar_email(event):
    if email.get() == "Seu E-mail":
        email.delete(0, tkinter.END)


def limpar_password(event):
    if password_entry.get() == "Palavra Pass":
        password_entry.delete(0, tkinter.END)


title = tkinter.Label(janela, text='My Photos', font=('Arial', 18))
title.pack(padx=8, pady=8)
title.config(bg='white')

texto = tkinter.Label(janela, text="Login", font=(12))
texto.pack(padx=10, pady=10)
texto.config(bg='white')

lblEmail = tkinter.Label(janela, text="Email:")
lblEmail.place(x=111, y=100)
lblEmail.config(bg='white')

email = tkinter.Entry(janela,)
email.insert(0, "Seu E-mail")
email.pack(padx=10, pady=10)
email.bind("<FocusIn>", limpar_email)

lblPassword = tkinter.Label(janela, text="Password:")
lblPassword.place(x=111, y=138)
lblPassword.config(bg='white')

password_entry = tkinter.Entry(janela)
password_entry.insert(0, "Palavra Pass")
password_entry.pack(padx=10, pady=10)
password_entry.bind("<FocusIn>", limpar_password)  

button = tkinter.Button(janela, text="Login", command=clique_login)
button.pack(padx=4, pady=10)

button_register = tkinter.Button(janela, text="Register", command=clique_register)
button_register.pack(padx=7, pady=10)

janela.mainloop()
