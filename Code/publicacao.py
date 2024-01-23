#Menu de publicação de imagem

from tkinter import *
from tkinter import ttk
from tkinter import filedialog 
from PIL import ImageTk, Image
import os

def selecioarFile():

    global image1

    filename =filedialog.askopenfilename(title='Select image', initialdir= './image',
                filetypes = (("png files", "*.png"),("gif files", "*.gif"),("all files", "*.*")))



    
    image = Image.open(filename)
    image1 = ImageTk.PhotoImage(image)#imagem Inicial
    ctnimage.itemconfig(image_id, image=image1)

def char_count(event):
    count = len(comentario.get('1.0', 'end-1c'))
    if count >= char_limit and event.keysym not in{'BackSpace', 'Delete'}:
        return 'break'

def submeter():
    comentario_info = comentario.get("1.0", "end-1c")

    with open('Files/comentarios.txt', 'a') as f:
        f.write(f"Coments:{comentario_info}\n")


    filename = filedialog.asksaveasfilename(defaultextension=".png",
                                              filetypes=(("PNG files", ".png"), ("GIF files", ".gif"),
                                                         ("All files", ".")))


    if not filename:
        return

    image.save(filename)


   

window=Tk()
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))  
window.title('Publicar magem')
char_limit = 150


#buttons
btnSelect = Button(window, text='Selecionar Imagem', command= selecioarFile)
btnSelect.place(x=450, y=640)

btnSubmeter = Button(window, text='Submeter', command= submeter)
btnSubmeter.place(x=665, y=640)

categoria = ttk.Combobox(name="categoria")
categoria ['value'] = ('Paisagem', 'Natureza', 'Animais', 'Comida')
categoria.place(x=520, y=610)

lblCategoria = Label(window, text='Categoria')
lblCategoria.place(x=450, y=610)

#comentario
txtcomentario = Label(window, text='Comentario')
txtcomentario.place(x=450, y=475)

comentario = Text(window, width=30, height=5, font='20')
comentario.place(x=450, y=500)

comentario.bind('<KeyPress>', char_count)
comentario.bind('<KeyRelease>', char_count)


txtcomentario = Label(window, text='Comentario (limite de 150 characteres)')
txtcomentario.place(x=450, y=475)


#canvas
ctnimage = Canvas(window, width=700, height=350)
ctnimage.place(x=450, y=100)



image = Image.open('./images/image1.jpg')
image1 = ImageTk.PhotoImage(image)#imagem Inicial
image_id = ctnimage.create_image(0,0, anchor='nw', image=image1)


window.mainloop()