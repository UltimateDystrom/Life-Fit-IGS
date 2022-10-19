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
root.configure(background='cyan')
#
my_img = ImageTk.PhotoImage(Image.open('Menu1.png'))
my_lable = Label(image=my_img)

my_lable.pack()

# Menu Bar
menubar = Menu(root, bg='#56ab2f')
root['menu'] = menubar
menu_options = Menu(menubar, bg='#000000', fg='black')
menu_extra = Menu(menubar, bg='#000000', fg='black')
menu_tutorial = Menu(menubar, bg='#000000', fg='black')

# Pestaña Opciones
menubar.add_cascade(menu=menu_options, label='Opciones')
menu_options.add_command(label='Salir', command=root.quit)

# Pestaña Tutorial
menubar.add_cascade(menu= menu_tutorial, label= 'Ayuda')
menu_tutorial.add_command(label='Video Tutorial')
menu_tutorial.add_command(label='Preguntas Frecuentes')

# Pestaña Otros
menubar.add_cascade(menu=menu_extra, label= 'Otros')

welcome_lbl = Label(root, text="Iniciemos un entrenamiento", font=("Yu Gothic UI Semibold", 30), background='cyan').pack(pady=10)
button_start_training = Button(root, text="Iniciar", width=20, height=5, background='#56ab2f', foreground= 'white', font=("Segoe UI Black", 20), state= DISABLED)
button_start_training.pack(pady=20)

def choose_training(value):
    if value > 0:
        button_start_training["state"] = NORMAL

training = IntVar()
three_minutes = Radiobutton(root, text="3 Minutos", variable=training, value= 1, font=("Yu Gothic", 15), command= lambda: choose_training(training.get()), bg= 'cyan').pack()
five_minutes = Radiobutton(root, text="5 Minutos", variable=training, value= 2, font=("Yu Gothic", 15), command= lambda: choose_training(training.get()), bg= 'cyan').pack()
seven_minutes = Radiobutton(root, text="7 Minutos", variable=training, value= 3, font=("Yu Gothic", 15), command= lambda: choose_training(training.get()), bg= 'cyan').pack()



root.mainloop()