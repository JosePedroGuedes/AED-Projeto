import tkinter as tk
from tkinter import ttk, filedialog
import os
import shutil
from sys import argv

class ProfilePage(tk.Tk):
    def __init__(self, email):
        super().__init__()

        self.title("Perfil do Usuário")
        self.geometry("800x600")

        self.email = email
        self.profile_picture_path = tk.StringVar()

        self.username = self.nome_usuario(email)

        self.create_widgets()

    def create_widgets(self):
        # Cabeçalho
        header_label = tk.Label(self, text="Perfil do Usuário", font=("Helvetica", 16))
        header_label.pack(pady=10)

        # Informações do Usuário
        user_frame = ttk.LabelFrame(self, text="Informações do Usuário")
        user_frame.pack(padx=10, pady=10, fill="both", expand=True)

        username_label = ttk.Label(user_frame, text="Nome de Usuário:")
        username_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        username_entry = ttk.Entry(user_frame)
        username_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        email_label = ttk.Label(user_frame, text="E-mail:")
        email_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        email_entry = ttk.Entry(user_frame)
        email_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Preencher informações do usuário
        username_entry.insert(tk.END, self.username)
        email_entry.insert(tk.END, self.email)

        # Foto de Perfil
        profile_picture_label = ttk.Label(user_frame, text="Foto de Perfil:")
        profile_picture_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.profile_picture_display = ttk.Label(user_frame)
        self.profile_picture_display.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Botão para Mudar Foto de Perfil
        change_picture_button = ttk.Button(user_frame, text="Mudar Foto de Perfil", command=self.change_profile_picture)
        change_picture_button.grid(row=3, column=0, columnspan=2, pady=5)

        # Álbuns
        albums_frame = ttk.LabelFrame(self, text="Álbuns")
        albums_frame.pack(padx=10, pady=10, fill="both", expand=True)

        albums_listbox = tk.Listbox(albums_frame, selectmode=tk.SINGLE)
        albums_listbox.pack(pady=10, fill="both", expand=True)

        add_album_button = ttk.Button(albums_frame, text="Adicionar Álbum", command=self.add_album)
        add_album_button.pack(pady=5)

        view_album_button = ttk.Button(albums_frame, text="Ver Álbum Selecionado", command=self.view_album)
        view_album_button.pack(pady=5)

        # Notificações
        notifications_frame = ttk.LabelFrame(self, text="Notificações")
        notifications_frame.pack(padx=10, pady=10, fill="both", expand=True)

        notifications_text = tk.Text(notifications_frame, height=10, width=50)
        notifications_text.pack(pady=10, fill="both", expand=True)

        self.show_profile_picture()

    def nome_usuario(self, email):
        try:
            with open('AED-Projeto/Files/accounts.txt', 'r') as f:
                linhas = f.readlines()

            for i, linha in enumerate(linhas):
                if f"Email: {email}" in linha:
                    # Imprime a linha anterior (sem a parte "Username: ")
                    if i > 0:
                        previous_line = linhas[i - 1].replace("Username: ", "").strip()
                        print(previous_line)
                    # Extrai o nome de usuário da linha atual
                    username = previous_line
                    return username
        except Exception as e:
            print(f"Erro ao ler o arquivo de contas: {e}")



    def change_profile_picture(self):
        file_path = filedialog.askopenfilename(title="Escolher Foto de Perfil", filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])

        if file_path:
            # Define o caminho de destino
            destination_directory = os.path.join("AED-Projeto", "Images", "Perfil")
            
            # Obtém o nome do arquivo a partir do self.username
            username_filename = self.username.replace(" ", "_")  # Substitui espaços por underscores para evitar problemas no nome do arquivo
            destination_path = os.path.join(destination_directory, f"{username_filename}_perfil.png")

            # Cria o diretório de destino se não existir
            os.makedirs(destination_directory, exist_ok=True)

            # Verifica se o arquivo de destino já existe
            if os.path.exists(destination_path):
                # Se existir, exclui-o antes de copiar
                os.remove(destination_path)

            # Move (renomeia) o arquivo para o destino
            shutil.copy(file_path, destination_path)

            # Atualiza o caminho da imagem de perfil
            self.profile_picture_path.set(destination_path)

            # Exibe a imagem
            self.show_profile_picture()


    def show_profile_picture(self):
        image_path = self.profile_picture_path.get()
        print("Imagem: ", image_path)

        if not image_path:
            # Se não houver um caminho definido, procura uma imagem específica na pasta
            username_filename = self.username.replace(" ", "_")
            candidate_path = os.path.join("AED-Projeto", "Images", "Perfil", f"{username_filename}_perfil.png")
            print(candidate_path + " ww")
            
            # Verifica se o arquivo candidato existe
            if os.path.exists(candidate_path):
                image_path = candidate_path
            else:
                # Se não existir, usa a imagem padrão
                image_path = "AED-Projeto/Images/Perfil/semfoto.png"

        # Cria o objeto PhotoImage e configura a exibição
        photo = tk.PhotoImage(file=image_path)
        self.profile_picture_display.config(image=photo)
        self.profile_picture_display.image = photo


    def add_album(self):
        # Função para adicionar um álbum à lista
        pass

    def view_album(self):
        # Função para visualizar o álbum selecionado
        pass

if __name__ == "__main__":
    # Certificar-se de que há argumentos suficientes
    if len(argv) == 2:
        # Chamar a classe ProfilePage com o argumento adequado
        app = ProfilePage(argv[1])
        app.mainloop()
    else:
        print("Número incorreto de argumentos. Forneça o endereço de e-mail.")
