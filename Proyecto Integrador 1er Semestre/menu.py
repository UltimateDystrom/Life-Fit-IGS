from tkinter import *
from PIL import ImageTk, Image
from tkinter import font

root = Tk()
root.title("Menú Principal")
root.resizable(FALSE, FALSE)
root.geometry('1000x700+300+50')
root.option_add('*tearOff', FALSE)
root.configure(background='#6dd5ed')
# win = Toplevel(root)
# Menu Bar
# bg_image = ImageTk.PhotoImage(Image.open("images/Background Menu.png"))
# bg_frame = Frame(root, bg_image)

menubar = Menu(root, bg='#56ab2f')
root['menu'] = menubar
menu_options = Menu(menubar, bg='#56ab2f', fg='white')
menu_extra = Menu(menubar, bg='#56ab2f', fg='white')
menu_tutorial = Menu(menubar, bg='#56ab2f', fg='white')

# Pestaña Opciones
menubar.add_cascade(menu=menu_options, label='Opciones')
menu_options.add_command(label='Salir', command=root.quit)

# Pestaña Tutorial
menubar.add_cascade(menu= menu_tutorial, label= 'Ayuda')
menu_tutorial.add_command(label='Video Tutorial')
menu_tutorial.add_command(label='Preguntas Frecuentes')

# Pestaña Otros
menubar.add_cascade(menu=menu_extra, label= 'Otros')

welcome_lbl = Label(root, text="Iniciemos un entrenamiento", font=("Yu Gothic UI Semibold", 30), background='#6dd5ed').pack(pady=10)

button_start_training = Button(root, text="Iniciar", width=20, height=5, background='#56ab2f', foreground= 'white', font=("Segoe UI Black", 20), state= DISABLED)
button_start_training.pack(pady=20)

def choose_training(value):
    if value > 0:
        button_start_training["state"] = NORMAL

training = IntVar()
three_minutes = Radiobutton(root, text="3 Minutos", variable=training, value= 1, font=("Yu Gothic", 15), command= lambda: choose_training(training.get()), bg= '#6dd5ed').pack()
five_minutes = Radiobutton(root, text="5 Minutos", variable=training, value= 2, font=("Yu Gothic", 15), command= lambda: choose_training(training.get()), bg= '#6dd5ed').pack()
seven_minutes = Radiobutton(root, text="7 Minutos", variable=training, value= 3, font=("Yu Gothic", 15), command= lambda: choose_training(training.get()), bg= '#6dd5ed').pack()




root.mainloop()