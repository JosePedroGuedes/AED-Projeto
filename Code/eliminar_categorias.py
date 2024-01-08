import tkinter as tk

def eliminar_linha():
    linha_a_eliminar = entrada_linha.get()

    with open('Files/categorias.txt', 'r') as f:
        linhas = f.readlines()

    linhas = [linha for linha in linhas if linha.strip() != linha_a_eliminar.strip()]

    with open('Files/categorias.txt', 'w') as f:
        f.writelines(linhas)

    # Atualiza a entrada para refletir a eliminação
    entrada_linha.delete(0, tk.END)

# Criar a janela
janela = tk.Tk()
janela.title("Eliminar Linha")

# Adicionar uma entrada para o usuário inserir a linha a ser eliminada
entrada_linha = tk.Entry(janela, width=30)
entrada_linha.pack(pady=10)

# Adicionar um botão para iniciar o processo de eliminação
botao_eliminar = tk.Button(janela, text="Eliminar Linha", command=eliminar_linha)
botao_eliminar.pack(pady=10)

# Iniciar o loop principal da interface gráfica
janela.mainloop()
