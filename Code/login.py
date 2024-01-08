import tkinter
import os
from tkinter import messagebox

janela = tkinter.Tk()
janela.geometry("500x300")
janela.title("My Photos Login")
janela.config(bg="white")


def button_login():
    
    email_info = email.get()
    password_info = password_entry.get()

    # Verificar se algum dos campos estÃ¡ vazio
    if not (email_info and password_info):  
        messagebox.showwarning("Empty Fields", "Please fill in all the fields.")
        return

    with open ("AED-Projeto/Files/accounts.txt", "r") as f:
        existing_data = f.read()
        print(existing_data)

        if f"Email: {email_info}\nPassword: {password_info}\n" in existing_data:
            messagebox.showinfo("Info", "You have successfully login.")

        else:
            messagebox.showwarning("Warning", "This account doesn't exist. Register First.")
            return


    print("Fazer Login")


def clique_register():
    janela.destroy()
    print("Fazer Registo")
    caminho_arquivo2 = os.path.abspath("AED-Projeto/Code/register.py")  
    os.system(f'python "{caminho_arquivo2}"')


def limpar_email(event):
    if email.get() == "Your E-mail":
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
email.pack(padx=10, pady=10)
email.bind("<FocusIn>", limpar_email)

lblPassword = tkinter.Label(janela, text="Password:")
lblPassword.place(x=111, y=138)
lblPassword.config(bg='white')

password_entry = tkinter.Entry(janela)
password_entry.pack(padx=10, pady=10)
password_entry.bind("<FocusIn>", limpar_password)  

button_login = tkinter.Button(janela, text="Login", command=button_login)
button_login.pack(padx=4, pady=10)

button_register = tkinter.Button(janela, text="Register", command=clique_register)
button_register.pack(padx=7, pady=10)

janela.mainloop()