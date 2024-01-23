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
        username_entry.insert(tk.END, "Nome de Exemplo")
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

        # Exibir a foto de perfil inicial
        self.show_profile_picture()

    def change_profile_picture(self):
        file_path = filedialog.askopenfilename(title="Escolher Foto de Perfil", filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])

        if file_path:
            # Define o caminho de destino
            destination_directory = os.path.join("AED-Projeto", "Imagens", "Perfil")
            
            # Cria o diretório de destino se não existir
            os.makedirs(destination_directory, exist_ok=True)

            # Constrói o caminho completo para a imagem de perfil
            destination_path = os.path.join(destination_directory, "perfil_image.png")

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

        if image_path:
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
    print("Olá")
    # Certificar-se de que há argumentos suficientes
    if len(argv) == 2:
        # Chamar a classe ProfilePage com o argumento adequado
        app = ProfilePage(argv[1])
        app.mainloop()
    else:
        print("Só a partir do login")
