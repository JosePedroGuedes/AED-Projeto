import tkinter as tk
import os

def salvar_texto():
    texto = caixa_texto.get("1.0", "end-1c")  # Caixa de texto

    if (texto != ""):
        with open("Files/categorias.txt", "a") as arquivo:
            arquivo.write("\n" + texto)  # Adicionar o texto

        print("Texto salvo com sucesso!")
        
        caixa_texto.delete("1.0", "end") # Limpa o conteúdo da caixa de texto

def voltar():
    janela.destroy()
    caminho_arquivo = os.path.abspath("Code/admin.py")
    os.system(f'python "{caminho_arquivo}"')

# Janela principal
janela = tk.Tk()
janela.title("Adicionar Categoria")

# Caixa de texto
caixa_texto = tk.Text(janela, height=10, width=40)
caixa_texto.pack(padx=10, pady=10)

# Botão de salvar
botao_salvar = tk.Button(janela, text="Salvar Texto", command=salvar_texto)
botao_salvar.pack(pady=10)

# Botão de voltar
botao_voltar = tk.Button(janela, text="Voltar", command=voltar)
botao_voltar.pack(pady=10)

janela.mainloop()
