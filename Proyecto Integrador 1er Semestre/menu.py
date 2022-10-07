from tkinter import *
from PIL import ImageTk, Image
from tkinter import font

root = Tk()
root.title("Menú Principal")
root.resizable(FALSE, FALSE)
root.geometry('1000x700+300+50')
root.option_add('*tearOff', FALSE)

# win = Toplevel(root)
# Menu Bar
menubar = Menu(root)
root['menu'] = menubar
menu_options = Menu(menubar)
menu_extra = Menu(menubar)
menu_tutorial = Menu(menubar)

# Pestaña Opciones
menubar.add_cascade(menu=menu_options, label='Opciones')
menu_options.add_command(label='Salir', command=root.quit)

# Pestaña Tutorial
menubar.add_cascade(menu= menu_tutorial, label= 'Ayuda')
menu_tutorial.add_command(label='Video Tutorial')
menu_tutorial.add_command(label='Preguntas Frecuentes')

# Pestaña Otros
menubar.add_cascade(menu=menu_extra, label= 'Otros')

welcome_lbl = Label(root, text="Iniciemos un entrenamiento", font=("Yu Gothic UI Semibold", 30)).pack(pady=10)

button_start_training = Button(root, text="Iniciar", width=20, height=5, background='#56ab2f', foreground= 'white', font=("Segoe UI Black", 20)).pack(pady=20)

training = IntVar()
three_minutes = Radiobutton(root, text="3 Minutos", variable=training, value= 3, font=("Yu Gothic", 15)).pack()
five_minutes = Radiobutton(root, text="5 Minutos", variable=training, value= 5, font=("Yu Gothic", 15)).pack()
seven_minutes = Radiobutton(root, text="7 Minutos", variable=training, value= 7, font=("Yu Gothic", 15)).pack()




root.mainloop()