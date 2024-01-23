import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

def eliminar_conta():
    username_a_eliminar = combo_username.get()
    frase = "Escolha o usuário que deseja eliminar"

    if username_a_eliminar != frase:
        with open('Files/accounts.txt', 'r') as f:
            linhas = f.readlines()

        novas_linhas = []
        capturando_conta = False
        for linha in linhas:
            if f"Username: {username_a_eliminar}" in linha:
                capturando_conta = True
            if not capturando_conta:
                novas_linhas.append(linha)
            if linha.strip() == "":
                capturando_conta = False

        with open('Files/accounts.txt', 'w') as f:
            f.writelines(novas_linhas)

        atualizar_combobox()

        mensagem = f"A conta do usuário {username_a_eliminar} foi eliminada com sucesso"
        messagebox.showinfo("Mensagem", mensagem)
    else:
        messagebox.showinfo("Mensagem", "Selecione um usuário")

def atualizar_combobox():
    frase = "Escolha o usuário que deseja eliminar"
    with open('Files/accounts.txt', 'r') as f:
        usuarios = [linha.split(": ")[1].strip() for linha in f.readlines() if "Username: " in linha]

    combo_username['values'] = usuarios
    combo_username.set(frase)

    exibir_ficheiro()

def exibir_ficheiro():
    with open('Files/accounts.txt', 'r') as f:
        conteudo = f.read()
        conteudo = conteudo[:-2]
        print(conteudo)
        caixa_texto.config(state='normal')
        caixa_texto.delete('1.0', tk.END)
        caixa_texto.insert(tk.END, conteudo)
        caixa_texto.config(state='disabled')

def voltar():
    janela.destroy()
    caminho_arquivo = os.path.abspath("Code/admin.py")
    os.system(f'python "{caminho_arquivo}"')

janela = tk.Tk()
janela.title("Eliminar Conta de Usuário")

titulo = tk.Label(janela, text="Escolha o usuário que quer apagar:")
titulo.pack(padx=20, pady=5)

combo_username = ttk.Combobox(janela, state='readonly', width=40)
combo_username.pack(pady=10)

usuarios_label = tk.Label(janela, text="Usuários:")
usuarios_label.pack(padx=20, pady=5)

caixa_texto = tk.Text(janela, wrap=tk.WORD, width=40, height=15, state='disabled')
caixa_texto.pack(padx=10, pady=10)

botao_eliminar = tk.Button(janela, text="Eliminar Conta", command=eliminar_conta)
botao_eliminar.pack(pady=10)

botao_voltar = tk.Button(janela, text="Voltar", command=voltar)
botao_voltar.pack(pady=10)

atualizar_combobox()
janela.mainloop()
