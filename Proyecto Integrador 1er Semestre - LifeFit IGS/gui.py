from tkinter import *
from PIL import ImageTk, Image, ImageSequence
from tkinter import font
from tkinter import messagebox
import os
import random

root = Tk()
root.title("Menú Principal")
root.resizable(FALSE, FALSE)
root.geometry('1000x700+300+50')
root.option_add('*tearOff', FALSE)

icon = ImageTk.PhotoImage(Image.open('images/logo-life-fit.png'))
root.wm_iconphoto(False, icon)

# Images
img_bg = ImageTk.PhotoImage(Image.open('images/fondo.png'))
lbl_bg = Label(root, image=img_bg)
lbl_bg.place(x = 0, y = 0)

img_bg2 = ImageTk.PhotoImage(Image.open('images/fondo entrenamiento.png'))
img_bg3 = ImageTk.PhotoImage(Image.open('images/fondo entrenamiento.png'))

img_btn = ImageTk.PhotoImage(Image.open('images/boton menu.png'))
img_btn_play = ImageTk.PhotoImage(Image.open('images/boton play.png'))
img_btn_next = ImageTk.PhotoImage(Image.open('images/boton next.png'))
img_btn_back = ImageTk.PhotoImage(Image.open('images/boton back.png'))

img_btn_play1 = ImageTk.PhotoImage(Image.open('images/boton play.png'))
img_btn_next1 = ImageTk.PhotoImage(Image.open('images/boton next.png'))
img_btn_back1 = ImageTk.PhotoImage(Image.open('images/boton back.png'))
img_ergonomia_window = ImageTk.PhotoImage(Image.open('images/ergonomia window.png'))

# Menu Bar
menubar = Menu(root)
root['menu'] = menubar
menu_options = Menu(menubar, bg='#010039', foreground='#f5c814')
menu_extra = Menu(menubar, bg='#010039', foreground='#f5c814')
menu_tutorial = Menu(menubar, bg='#010039', foreground='#f5c814')

# Pestaña Opciones
menubar.add_cascade(menu=menu_options, label='Opciones')
def acerca_de():
    messagebox.showinfo("Acerca de", "Integrantes del equipo:\n -Gilberto\n-Dylan\n-Juan\n-Hugo")
menu_options.add_command(label='Acerca de', command=acerca_de)
menu_options.add_command(label='Salir', command=root.quit)

# Variables globales
c = 0
c1 = 0
routine = []
paths_ergonomics = []
descriptions = ["1. Ubique el mouse relativamente cerca al cuerpo y en un\n lugar de fácil ubicación. Se recomienda usar el mouse sobre una superficie, llamada pad mouse con un gel para\n la muñeca.  En caso el pad llegue a presentar alguna deformación debe ser reemplazada  de inmediato.\n\n2. Use la menor cantidad de fuerza posible para mover el\n mouse y hacer clic.\n\n3. Procure mover el mouse con todo el antebrazo y no sólo\n con la muñeca. De esa forma podrás mantener la muñeca\n derecha todo el tiempo.\n\n3. Apoye una parte del antebrazo sobre el escritorio, o\n mesa, al momento de usar el mouse. Pero nunca se debe\n posar el codo, recuérdalo.", "1. El monitor debe estar al frente a la altura de los ojos y a\n una distancia de unos 43 centímetros de tu cuerpo\n\n2. No te excedas con los objetos personales\n\n3. Limpia tu escritorio y haz espacio para lo realmente\n importante."]


def choose_training(value):     
    if value > 0:
        button_start_training["state"] = NORMAL

def open_training():
    window2 = Toplevel()
    window2.title("Entrenamiento")
    window2.resizable(FALSE, FALSE)
    window2.geometry('1000x700+300+50')
    window2.wm_iconphoto(False, icon)
    lbl_bg2 = Label(window2, image=img_bg2)
    lbl_bg2.place(x = 0, y = 0)

    paths = []
    for file in os.listdir('gifs'):
        paths.append("gifs/" + file)

    def delete_duplicates(x):
        return list(dict.fromkeys(x))

    global training
    ex = training.get()
    while len(routine) < ex:
        routine.append(random.choice(paths))
        delete_duplicates(routine)

    lbl = Label(window2, bg='#f5c814')
    lbl.place(x=340, y=150)

        
    def setframe(iterator, img=None):
        global c
        if(img is None):
            img = next(iterator)
    
        img = img.resize((300,300))
        img = ImageTk.PhotoImage(img)
        lbl.config(image = img)
        lbl.image = img

        try:
            img = next(iterator)
            btn_next["state"] = DISABLED
            btn_back["state"] = DISABLED
        except StopIteration:
            if c == len(routine)-1:
                btn_next["state"] = DISABLED
                lbl_sign["text"] = "Entrenamiento terminado."

            else: 
                btn_next["state"] = NORMAL
            if c <= 0:
                btn_back["state"] = DISABLED
            else: 
                btn_back["state"] = NORMAL
            return

        root.after(50, setframe, iterator, img)

    def start_gif():
        lbl_sign["text"] = ""
        try:
            img = Image.open(routine[c])

            iterator = ImageSequence.Iterator(img)
            setframe(iterator)
        except IndexError as e:
            btn_next["state"] = DISABLED

    def next_gif():
        global c, routine
        c += 1
        lbl_count["text"] = "Entrenamiento %d de %d" % (c+1, ex)
        btn_back["state"] = NORMAL
        if c == len(routine)-1:
            btn_next["state"] = DISABLED
        start_gif()

    def back_gif():
        global c, routine
        c -= 1
        lbl_count["text"] = "Entrenamiento %d de %d" % (c+1, ex)
        if c <= 0:
            btn_back["state"] = DISABLED
        start_gif()



    btn_play = Button(window2, image=img_btn_play, command=start_gif, bg='#f5c814', borderwidth=0)
    btn_play.place(x=430, y=500)

    btn_next = Button(window2, image=img_btn_next, command=next_gif, bg='#f5c814', borderwidth=0)
    btn_next.place(x= 570, y=527)

    btn_back = Button(window2, image=img_btn_back, bg='#f5c814', borderwidth=0, command=back_gif, state=DISABLED)
    btn_back.place(x=310, y=525)

    lbl_sign = Label(window2, bg='#f5c814', text= "Presiona Play para iniciar.",font=("Bahnschrift semibold", 16), fg='#010039')
    lbl_sign.place(x=380, y=650)

    lbl_count = Label(window2, bg='#f5c814', text= "Entrenamiento %d de %d" % (c+1, ex), font=("Bahnschrift semibold", 16), fg='#010039')
    lbl_count.place(x=380,y=20)

def open_ergonomics():
    window3 = Toplevel()
    window3.title("Ergonomía")
    window3.resizable(FALSE, FALSE)
    window3.geometry('1000x700+300+50')
    window3.wm_iconphoto(False, icon)

    def show_buttons():
        btn_show_gifs.destroy()
        lbl_bg1["image"] = img_bg3
        lbl1.place(x=100, y=180)
        btn_play1.place(x=430, y=500)
        btn_next1.place(x=570, y=525)
        btn_back1.place(x=310, y=525)
        lbl_sign1.place(x=360, y=650)
        lbl_descriptions.place(x=410, y=200)

    for file in os.listdir('ergonomics'):
        paths_ergonomics.append("ergonomics/" + file)
    paths_ergonomics.sort()

    def setframe(iterator, img=None):
        global c1
        if(img is None):
            img = next(iterator)
    
        img = img.resize((300,300))
        img = ImageTk.PhotoImage(img)
        lbl1.config(image = img)
        lbl1.image = img

        try:
            img = next(iterator)
            btn_next1["state"] = DISABLED
            btn_back1["state"] = DISABLED
        except StopIteration:
            if c1 == len(paths_ergonomics)-1:
                btn_next1["state"] = DISABLED
            else: 
                btn_next1["state"] = NORMAL
            if c1 <= 0:
                btn_back1["state"] = DISABLED
            else: 
                btn_back1["state"] = NORMAL
            return

        root.after(50, setframe, iterator, img)

    def start_gif():
        lbl_sign1["text"] = ""
        try:
            img = Image.open(paths_ergonomics[c1])
            if c1 == 1:
                lbl_descriptions["font"] = ("Bahnschrift semibold", 16)
                lbl_descriptions["text"] = ""
                lbl_descriptions["text"] = descriptions[c1]
            else:
                lbl_descriptions["font"] = ("Bahnschrift semibold", 8)
                lbl_descriptions["text"] = ""
                lbl_descriptions["text"] = descriptions[c1]


            iterator = ImageSequence.Iterator(img)
            setframe(iterator)
        except IndexError as e:
            btn_next1["state"] = DISABLED

    def next_gif():
        global c1, paths_ergonomics, btn_next
        c1 += 1
        btn_back1["state"] = NORMAL
        if c1 == len(paths_ergonomics)-1:
            btn_next1["state"] = DISABLED
        start_gif()

    def back_gif():
        global c1, paths_ergonomics, btn_back
        c1 -= 1
        if c1 <= 0:
            btn_back1["state"] = DISABLED
        start_gif()

    lbl_bg1 = Label(window3, image=img_ergonomia_window)
    lbl_bg1.place(x=0,y=0)
    lbl1 = Label(window3, bg='#f5c814')
    btn_show_gifs = Button(window3, image=img_btn_play1, command=show_buttons, bg='#f5c814', borderwidth=0)
    btn_play1 = Button(window3, image=img_btn_play1, command=start_gif, bg='#f5c814', borderwidth=0)
    btn_next1 = Button(window3, image=img_btn_next1, command=next_gif, bg='#f5c814', borderwidth=0)
    btn_back1 = Button(window3, image=img_btn_back1, bg='#f5c814', borderwidth=0, command=back_gif, state=DISABLED)
    btn_show_gifs.place(x=440, y=520)
    lbl_sign1 = Label(window3, bg='#f5c814', text= "Presiona Play para visualizar.",font=("Bahnschrift semibold", 16), fg='#010039')
    lbl_descriptions = Label(window3, bg='#f5c814', text= "",font=("Bahnschrift semibold", 8), fg='#010039')
    
    
button_start_training = Button(root, image=img_btn, state= DISABLED, bg='#f5c814', borderwidth=0, command=open_training, cursor="hand2")
button_start_training.place(x=390, y=160)
training = IntVar()
three_minutes = Radiobutton(root, text="3 Minutos", variable=training, value= 6, font=("Yu Gothic Semibold", 30), command= lambda: choose_training(training.get()), bg= '#f5c814', fg='white', cursor="hand2")
five_minutes = Radiobutton(root, text="5 Minutos", variable=training, value= 10, font=("Yu Gothic Semibold", 30), command= lambda: choose_training(training.get()), bg= '#f5c814', fg='white', cursor="hand2")
seven_minutes = Radiobutton(root, text="7 Minutos", variable=training, value= 14, font=("Yu Gothic Semibold", 30), command= lambda: choose_training(training.get()), bg= '#f5c814', fg='white', cursor="hand2")
three_minutes.place(x = 390, y = 400)
five_minutes.place(x=390, y=460)
seven_minutes.place(x=390, y=520)
button_ergonomics = Button(root, fg='#f5c814', bg='#010039',font=("Bahnschrift semibold", 16), text="Conoce sobre la ergonomía", cursor="hand2", command=open_ergonomics, borderwidth=0)
button_ergonomics.place(x=365,y=590)

mainloop()

