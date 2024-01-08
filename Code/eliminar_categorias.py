import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

def eliminar_categoria():
    
    categoria_a_eliminar = combo_categoria.get()
    frase = "Escolha a categoria que deseja eliminar"

    if(categoria_a_eliminar != frase):

        with open('AED-Projeto/Files/categorias.txt', 'r') as f:
            linhas = f.readlines()

        linhas = [linha for linha in linhas if linha.strip() != categoria_a_eliminar.strip()]

        with open('AED-Projeto/Files/categorias.txt', 'w') as f:
            f.writelines(linhas)

        atualizar_combobox()

        mensagem = "A categoria " + categoria_a_eliminar + " foi eleminada com sucesso"

        messagebox.showinfo("Mensagem", mensagem)

    else:
        messagebox.showinfo("Mensagem", "Selecione uma categoria")
    

def atualizar_combobox():
    frase = "Escolha a categoria que deseja eliminar"
    with open('AED-Projeto/Files/categorias.txt', 'r') as f:
        categorias = [linha.strip() for linha in f.readlines()]

    combo_categoria['values'] = categorias
    combo_categoria.set(frase)

    exibir_ficheiro()


def exibir_ficheiro():
    with open('AED-Projeto/Files/categorias.txt', 'r') as f:
        conteudo = f.read()
        print(conteudo)
        caixa_texto.config(state='normal')
        caixa_texto.delete('1.0', tk.END)  # Limpa o conteúdo atual
        caixa_texto.insert(tk.END, conteudo)
        caixa_texto.config(state='disabled')


def voltar():
    janela.destroy()
    caminho_arquivo = os.path.abspath("AED-Projeto/Code/admin.py")
    os.system(f'python "{caminho_arquivo}"')


# Criar a janela
janela = tk.Tk()
janela.title("Eliminar Categoria")

# Adicionar um widget para o título
titulo = tk.Label(janela, text="Escolha a categoria que quer apagar:")
titulo.pack(padx=20, pady=20)

# Adicionar um combobox para escolher a categoria
combo_categoria = ttk.Combobox(janela, state='readonly', width=40)
combo_categoria.pack(pady=10)

# Adicionar uma caixa de texto
caixa_texto = tk.Text(janela, wrap=tk.WORD, width=40, height=10, state='disabled')
caixa_texto.pack(padx=10, pady=10)

# Adicionar um botão para iniciar o processo de eliminação
botao_eliminar = tk.Button(janela, text="Eliminar Categoria", command=eliminar_categoria)
botao_eliminar.pack(pady=10)

# Adicionar um botão para iniciar o processo de eliminação
botao_eliminar = tk.Button(janela, text="Voltar", command=voltar)
botao_eliminar.pack(pady=10)

atualizar_combobox()
janela.mainloop()