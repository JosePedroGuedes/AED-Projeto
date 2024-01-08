import tkinter
from tkinter import messagebox

janela = tkinter.Tk()
janela.geometry("500x300")
janela.title("My Photos Login")
janela.config(bg="white")

def button_save():
    username_info = username.get()
    email_info = email_entry.get()
    password_info = password_entry.get()

    # Verificar se algum dos campos está vazio
    if not (username_info and email_info and password_info):
        messagebox.showwarning("Empty Fields", "Please fill in all the fields.")
        return

    with open ("AED-Projeto/Files/accounts.txt", "r") as f:
        existing_data = f.read()

    if f"Username: {username_info}\nEmail: {email_info}\nPassword: {password_info}\n" in existing_data:
        messagebox.showwarning("Duplicate Entry", "This account already exists.")
        return

    # Escrever as informações no arquivo
    with open("AED-Projeto/Files/accounts.txt", "a") as f:
        f.write(f"Username: {username_info}\nEmail: {email_info}\nPassword: {password_info}\n\n")

    print("Account created")
    messagebox.showinfo("", "Your account has been successfully created.")


def limpar_username(event):
    if username.get() == "Your Name":
        username.delete(0, tkinter.END)


def limpar_email(event):
    if email_entry.get() == "Your Email":
        email_entry.delete(0, tkinter.END)


def limpar_password(event):
    if password_entry.get() == "Your Password":
        password_entry.delete(0, tkinter.END)
        password_entry.config(show="*")


title = tkinter.Label(janela, text='My Photos', font=('Arial', 18))
title.pack(padx=8, pady=8)
title.config(bg='white')

texto = tkinter.Label(janela, text="Register", font=(12))
texto.pack(padx=10, pady=10)
texto.config(bg='white')

lblUsername = tkinter.Label(janela, text="Username:")
lblUsername.place(x=111, y=100)
lblUsername.config(bg='white')

username = tkinter.Entry(janela)
username.pack(padx=10, pady=10)
username.bind("<FocusIn>", limpar_username)

lblEmail = tkinter.Label(janela, text="Email:")
lblEmail.place(x=135, y=140)
lblEmail.config(bg='white')

email_entry = tkinter.Entry(janela)
email_entry.pack(padx=10, pady=10)
email_entry.bind("<FocusIn>", limpar_email)

lblPassword = tkinter.Label(janela, text="Password:")
lblPassword.place(x=113, y=180)
lblPassword.config(bg='white')

password_entry = tkinter.Entry(janela)
password_entry.pack(padx=10, pady=10)
password_entry.bind("<FocusIn>", limpar_password)

button_save = tkinter.Button(janela, text="Save", command=button_save)
button_save.pack(padx=4, pady=10)

janela.mainloop()