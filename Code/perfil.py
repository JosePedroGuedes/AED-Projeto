import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import shutil
from sys import argv
from PIL import Image, ImageTk

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

        self.username_label = ttk.Label(user_frame, text="Nome de Usuário:")
        self.username_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.username_entry = ttk.Entry(user_frame)  # Entrada inicialmente não editável
        self.username_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        email_label = ttk.Label(user_frame, text="E-mail:")
        email_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.email_entry = ttk.Entry(user_frame)  # Entrada inicialmente não editável
        self.email_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Preencher informações do usuário
        self.load_user_info()

        # Botões para Editar e Salvar
        edit_button = ttk.Button(user_frame, text="Editar", command=self.enable_edit)
        edit_button.grid(row=3, column=0, pady=5)

        self.save_button = ttk.Button(user_frame, text="Salvar", command=self.save_changes, state='disabled')
        self.save_button.grid(row=3, column=1, pady=5)

        # Foto de Perfil
        profile_picture_label = ttk.Label(user_frame, text="Foto de Perfil:")
        profile_picture_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.profile_picture_display = ttk.Label(user_frame)
        self.profile_picture_display.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Botão para Mudar Foto de Perfil
        change_picture_button = ttk.Button(user_frame, text="Mudar Foto de Perfil", command=self.change_profile_picture)
        change_picture_button.grid(row=4, column=0, columnspan=2, pady=5)

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

        # Agora, chamamos show_profile_picture depois de preencher as entradas
        self.show_profile_picture()

    def nome_usuario(self, email):
        try:
            with open('Files/accounts.txt', 'r') as f:
                linhas = f.readlines()

            for i, linha in enumerate(linhas):
                if f"Email: {email}" in linha:
                    # Imprime a linha anterior (sem a parte "Username: ")
                    if i > 0:
                        previous_line = linhas[i - 1].replace("Username: ", "").strip()
                        return previous_line
        except Exception as e:
            print(f"Erro ao ler o arquivo de contas: {e}")

    def load_user_info(self):
        self.username = self.nome_usuario(self.email)
        self.username_entry.insert(tk.END, self.username)
        self.email_entry.insert(tk.END, self.email)

    def enable_edit(self):
        self.username_entry.config(state='normal')
        self.email_entry.config(state='normal')
        self.save_button['state'] = 'normal'

    def save_changes(self):
        new_username = self.username_entry.get()
        new_email = self.email_entry.get()

        print(new_username + "  " + new_email)

        new_image_path = os.path.join("Images", "Perfil", f"{new_username.replace(' ', '_')}_perfil.png")

        # Obter o caminho antigo do arquivo da imagem
        old_image_path = self.profile_picture_path.get()

        # Renomear o arquivo da imagem antigo para o novo caminho
        if os.path.exists(old_image_path):
            os.rename(old_image_path, new_image_path)

        # Atualizar o caminho da imagem de perfil
        self.profile_picture_path.set(new_image_path)
        
        try:
            with open('Files/accounts.txt', 'r') as f:
                linhas = f.readlines()

            for i, linha in enumerate(linhas):
                if f"Email: {self.email}" in linha:
                    # Atualiza a linha correspondente com as novas informações
                    linhas[i - 1] = f"Username: {new_username}\n"
                    linhas[i] = f"Email: {new_email}\n"
                    print("dd")

            with open('Files/accounts.txt', 'w') as f:
                f.writelines(linhas)
                print(linhas)

            messagebox.showinfo("Salvar", "Alterações salvas com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar as alterações: {e}")

        # Desabilita a edição e desativa o botão de salvar
        self.username_entry['state'] = 'readonly'
        self.email_entry['state'] = 'readonly'
        self.save_button['state'] = 'disabled'

    def change_profile_picture(self):
        file_path = filedialog.askopenfilename(title="Escolher Foto de Perfil", filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])

        if file_path:
            # Define o caminho de destino
            destination_directory = os.path.join("Images", "Perfil")

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
        self.username_entry['state'] = 'readonly'
        self.email_entry['state'] = 'readonly'

        image_path = self.profile_picture_path.get()
        print("Imagem: ", image_path)

        if not image_path:
            # Se não houver um caminho definido, procura uma imagem específica na pasta
            profile_image_filename = self.username.replace(" ", "_")
            candidate_path = os.path.join("Images", "Perfil", f"{profile_image_filename}_perfil.png")
            print(candidate_path)

            # Verifica se o arquivo candidato existe
            if os.path.exists(candidate_path):
                image_path = candidate_path
            else:
                # Se não existir, usa a imagem padrão
                image_path = "Images/Perfil/semfoto.png"
                print("Imagem padrão")

        # Cria o objeto PhotoImage e configura a exibição
        foto = Image.open(image_path)
        foto = foto.resize((50, 50))
        foto = ImageTk.PhotoImage(foto)
        self.profile_picture_display.config(image=foto)
        self.profile_picture_display.image = foto

        

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