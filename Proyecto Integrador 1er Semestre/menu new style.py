from cProfile import label
from lib2to3.pgen2.token import LBRACE
from modulefinder import IMPORT_NAME
import posixpath
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image


root = Tk()
root.title("Menú Principal")
root.resizable(FALSE, FALSE)
root.geometry('1000x700+300+50')
root.option_add('*tearOff', FALSE)

# Images
img_bg = ImageTk.PhotoImage(Image.open('images/fondo.png'))
lbl_bg = Label(root, image=img_bg)
lbl_bg.place(x = 0, y = 0)


img_rb = ImageTk.PhotoImage(Image.open('images/radio button image.png'))
lbl_rb = Label(root, image=img_rb)

img_btn = ImageTk.PhotoImage(Image.open('images/boton menu.png'))

# Menu Bar
menubar = Menu(root, bg='#56ab2f')
root['menu'] = menubar
menu_options = Menu(menubar, bg='#000000', fg='black', foreground='white')
menu_extra = Menu(menubar, bg='#000000', fg='black', foreground='white')
menu_tutorial = Menu(menubar, bg='#000000', fg='black', foreground='white')

# Pestaña Opciones
menubar.add_cascade(menu=menu_options, label='Opciones')
menu_options.add_command(label='Salir', command=root.quit)

# Pestaña Tutorial
menubar.add_cascade(menu= menu_tutorial, label= 'Ayuda', foreground='white')
menu_tutorial.add_command(label='Video Tutorial', foreground='white')
menu_tutorial.add_command(label='Preguntas Frecuentes', foreground='white')

# Pestaña Otros
menubar.add_cascade(menu=menu_extra, label= 'Otros', foreground='white')

#welcome_lbl = Label(root, text="Iniciemos un entrenamiento", font=("Yu Gothic UI Semibold", 30), background='cyan').pack(pady=10)
# button_start_training = Button(root, text="Iniciar", width=15, height=5, background='#56ab2f', foreground= 'white', font=("Segoe UI Black", 20), state= DISABLED)
button_start_training = Button(root, image=img_btn, state= DISABLED, bg='#f5c814', borderwidth=0)
button_start_training.place(x=380, y=160)

def choose_training(value):
    if value > 0:
        button_start_training["state"] = NORMAL

training = IntVar()
three_minutes = Radiobutton(root, text="3 Minutos", variable=training, value= 1, font=("Yu Gothic Semibold", 30), command= lambda: choose_training(training.get()), bg= '#f5c814', fg='white')
five_minutes = Radiobutton(root, text="5 Minutos", variable=training, value= 2, font=("Yu Gothic Semibold", 30), command= lambda: choose_training(training.get()), bg= '#f5c814', fg='white')
seven_minutes = Radiobutton(root, text="7 Minutos", variable=training, value= 3, font=("Yu Gothic Semibold", 30), command= lambda: choose_training(training.get()), bg= '#f5c814', fg='white')
three_minutes.place(x = 390, y = 400)
five_minutes.place(x=390, y=460)
seven_minutes.place(x=390, y=520)

root.mainloop()