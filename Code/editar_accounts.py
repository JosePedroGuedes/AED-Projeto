import tkinter as tk
from tkinter import messagebox
import os

def atualizar_lista_contas():
    with open('AED-Projeto/Files/accounts.txt', 'r') as arquivo:
        contas = [linha.strip() for linha in arquivo.readlines() if "Username: " in linha]
    
    lista_contas.delete(0, tk.END)
    for conta in contas:
        username = conta.replace('Username: ', '').strip()
        lista_contas.insert(tk.END, username)

def exibir_detalhes_conta(event):
    index = lista_contas.curselection()
    if index:
        username_selecionado = lista_contas.get(index)
        detalhes_conta = obter_detalhes_conta(username_selecionado)
        preencher_campos_detalhes(detalhes_conta)

def obter_detalhes_conta(username):
    with open('AED-Projeto/Files/accounts.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        detalhes_conta = ""
        capturar = False
        for linha in linhas:
            if f"Username: {username}" in linha:
                capturar = True
            if capturar:
                detalhes_conta += linha
                if linha.strip() == "":
                    break
        return detalhes_conta

def preencher_campos_detalhes(detalhes_conta):
    entry_username.config(state='normal')
    entry_email.config(state='normal')
    entry_password.config(state='normal')

    entry_username.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_password.delete(0, tk.END)

    linhas = detalhes_conta.strip().split('\n')
    entry_username.insert(0, linhas[0].replace('Username: ', ''))
    entry_email.insert(0, linhas[1].replace('Email: ', ''))
    entry_password.insert(0, linhas[2].replace('Password: ', ''))

def salvar_alteracoes():
    index = lista_contas.curselection()
    if index:
        username_selecionado = lista_contas.get(index)
        novo_detalhes_conta = (
            f"Username: {entry_username.get()}\n"
            f"Email: {entry_email.get()}\n"
            f"Password: {entry_password.get()}\n\n"
        )
        atualizar_arquivo(username_selecionado, novo_detalhes_conta)
        messagebox.showinfo("Sucesso", "Alterações salvas com sucesso.")
        atualizar_lista_contas()
        limpar_campos()

def atualizar_arquivo(username_antigo, novo_detalhes_conta):
    with open('AED-Projeto/Files/accounts.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    with open('AED-Projeto/Files/accounts.txt', 'w') as arquivo:
        atualizando = False
        for linha in linhas:
            if f"Username: {username_antigo}" in linha:
                atualizando = True
                arquivo.write(novo_detalhes_conta)
            elif atualizando and linha.strip() == "":
                atualizando = False
            elif not atualizando:
                arquivo.write(linha)

def limpar_campos():
    entry_username.config(state='normal')
    entry_email.config(state='normal')
    entry_password.config(state='normal')

    entry_username.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_password.delete(0, tk.END)

    entry_username.config(state='disabled')
    entry_email.config(state='disabled')
    entry_password.config(state='disabled')

    lista_contas.selection_clear(0, tk.END)

def voltar():
    janela.destroy()
    caminho_arquivo = os.path.abspath("AED-Projeto/Code/admin.py")
    os.system(f'python "{caminho_arquivo}"')

janela = tk.Tk()
janela.title("Lista de Usuários")

frame_principal = tk.Frame(janela)
frame_principal.pack(padx=10, pady=10)

frame_lista = tk.Frame(frame_principal)
frame_lista.pack(side=tk.LEFT, padx=10)

label_titulo = tk.Label(frame_lista, text="Lista de Utilizadores")
label_titulo.pack()

lista_contas = tk.Listbox(frame_lista, selectmode=tk.SINGLE, height=10, width=20)
lista_contas.pack(pady=10)
lista_contas.bind('<ButtonRelease-1>', lambda event: exibir_detalhes_conta(event))

frame_detalhes = tk.Frame(frame_principal)
frame_detalhes.pack(side=tk.LEFT, padx=10)

label_username = tk.Label(frame_detalhes, text="Username:")
label_username.grid(row=0, column=0, padx=5, pady=5)

label_email = tk.Label(frame_detalhes, text="Email:")
label_email.grid(row=1, column=0, padx=5, pady=5)

label_password = tk.Label(frame_detalhes, text="Password:")
label_password.grid(row=2, column=0, padx=5, pady=5)

entry_username = tk.Entry(frame_detalhes, width=20, state='disabled')
entry_username.grid(row=0, column=1, padx=5, pady=5)

entry_email = tk.Entry(frame_detalhes, width=20, state='disabled')
entry_email.grid(row=1, column=1, padx=5, pady=5)

entry_password = tk.Entry(frame_detalhes, width=20, state='disabled')
entry_password.grid(row=2, column=1, padx=5, pady=5)

botao_salvar = tk.Button(frame_detalhes, text="Salvar Alterações", command=salvar_alteracoes)
botao_salvar.grid(row=3, column=0, columnspan=2, pady=10)

botao_voltar = tk.Button(janela, text="Voltar", command=voltar)
botao_voltar.pack(pady=10)

atualizar_lista_contas()

janela.mainloop()
