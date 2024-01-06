import tkinter
import os
from tkinter import messagebox


janela = tkinter.Tk()
janela.geometry("500x300")
janela.title("My Photos Login")
janela.config(bg="white")

file = open("accounts.txt", "w")
file.writ


def button_save():
    print("Account created")
    res= messagebox.showinfo(title="", message="Your account have been successfully created.")


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

username = tkinter.Entry(janela,)
username.insert(0, "Your Name")
username.pack(padx=10, pady=10)
username.bind("<FocusIn>", limpar_username)

lblEmail = tkinter.Label(janela, text="Email:")
lblEmail.place(x=135, y=140)
lblEmail.config(bg='white')

email_entry = tkinter.Entry(janela)
email_entry.insert(0, "Your Email")
email_entry.pack(padx=10, pady=10)
email_entry.bind("<FocusIn>", limpar_email)  

lblPassword = tkinter.Label(janela, text="Password:")
lblPassword.place(x=113, y=180)
lblPassword.config(bg='white')

password_entry = tkinter.Entry(janela)
password_entry.insert(0, "Your Password")
password_entry.pack(padx=10, pady=10)
password_entry.bind("<FocusIn>", limpar_password) 

button_save = tkinter.Button(janela, text="Save", command=button_save)
button_save.pack(padx=4, pady=10)

janela.mainloop()
