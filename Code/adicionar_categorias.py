import tkinter as tk
from tkinter import messagebox
import os

def categoria_existe(texto):
    with open('AED-Projeto/Files/categorias.txt', 'r') as arquivo:
        categorias_existentes = [linha.strip() for linha in arquivo.readlines()]
    return texto in categorias_existentes

def salvar_texto():
    texto = caixa_texto.get("1.0", "end-1c").strip()

    if texto != "":
        if categoria_existe(texto):
            messagebox.showinfo("Mensagem", f"A categoria {texto} já existe.")
        else:
            with open("AED-Projeto/Files/categorias.txt", "a") as arquivo:
                arquivo.write("\n" + texto)
                print("Texto salvo com sucesso!")

            caixa_texto.delete("1.0", "end")

            exibir_ficheiro()
            
            categoria = f"A categoria '{texto}' foi criada com sucesso"
            messagebox.showinfo("Mensagem", categoria)
    
    else:
        messagebox.showinfo("Mensagem", "Não deixe a categoria em branco")

def exibir_ficheiro():
    with open('AED-Projeto/Files/categorias.txt', 'r') as arquivo:
        conteudo = arquivo.read()

        categorias.config(state='normal')
        categorias.delete('1.0', tk.END)  # Limpa o conteúdo atual
        categorias.insert(tk.END, conteudo)
        categorias.config(state='disabled')

def voltar():
    janela.destroy()
    caminho_arquivo = os.path.abspath("AED-Projeto/Code/admin.py")
    os.system(f'python "{caminho_arquivo}"')

janela = tk.Tk()
janela.title("Adicionar Categoria")

titulo = tk.Label(janela, text="Categorias existentes")
titulo.pack(padx=20, pady=5)

categorias = tk.Text(wrap=tk.WORD, width=40, height=10, state='disabled')
categorias.pack(padx=10, pady=10)

titulo = tk.Label(janela, text="Adicionar nova categoria:")
titulo.pack(padx=20, pady=5)

caixa_texto = tk.Text(janela, height=1, width=40)
caixa_texto.pack(padx=10, pady=10)

botao_salvar = tk.Button(janela, text="Salvar Texto", command=salvar_texto)
botao_salvar.pack(pady=10)

botao_voltar = tk.Button(janela, text="Voltar", command=voltar)
botao_voltar.pack(pady=10)

exibir_ficheiro()
janela.mainloop()
