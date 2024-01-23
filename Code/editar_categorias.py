import tkinter as tk
import os
from tkinter import messagebox

def carregar_categorias():
    try:
        with open('Files/categorias.txt', 'r') as arquivo:
            categorias = [linha.strip() for linha in arquivo.readlines()]
        return categorias
    except FileNotFoundError:
        return []

def salvar_categorias(categorias):
    with open('Files/categorias.txt', 'w') as arquivo:
        arquivo.write('\n'.join(categorias))

def selecionar_categoria(event):
    index = lista_categorias.curselection()
    if index:
        categoria_selecionada = lista_categorias.get(index)
        caixa_edicao.delete(1.0, tk.END)
        caixa_edicao.insert(tk.END, categoria_selecionada)

def editar_categoria():
    index = lista_categorias.curselection()
    if index:
        nova_categoria = caixa_edicao.get("1.0", "end-1c").strip()
        if nova_categoria:
            categorias[index[0]] = nova_categoria
            salvar_categorias(categorias)
            atualizar_lista_categorias()
            messagebox.showinfo("Mensagem", "Categoria editada com sucesso.")
            caixa_edicao.delete(1.0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Por favor, insira um nome de categoria válido.")

def atualizar_lista_categorias():
    lista_categorias.delete(0, tk.END)
    for categoria in categorias:
        lista_categorias.insert(tk.END, categoria)

def voltar():
    janela.destroy()
    caminho_arquivo = os.path.abspath("Code/admin.py")
    os.system(f'python "{caminho_arquivo}"')

categorias = carregar_categorias()

janela = tk.Tk()
janela.title("Editar Categoria")

frame_principal = tk.Frame(janela)
frame_principal.pack(padx=10, pady=10)

frame_lista = tk.Frame(frame_principal)
frame_lista.pack(side=tk.LEFT, padx=10)

frame_edicao = tk.Frame(frame_principal)
frame_edicao.pack(side=tk.LEFT, padx=10)

lista_categorias = tk.Listbox(frame_lista, selectmode=tk.SINGLE, height=10, width=20)
lista_categorias.pack(pady=10)
lista_categorias.bind('<ButtonRelease-1>', selecionar_categoria)

atualizar_lista_categorias()

caixa_edicao = tk.Text(frame_edicao, height=1, width=20)
caixa_edicao.pack(pady=10)

botao_editar = tk.Button(frame_edicao, text="Editar Categoria", command=editar_categoria)
botao_editar.pack(pady=10)

botao_voltar = tk.Button(janela, text="Voltar", command=voltar)
botao_voltar.pack(pady=10)

janela.mainloop()
