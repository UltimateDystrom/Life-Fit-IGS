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

# Pestaña Opciones
menubar.add_cascade(menu=menu_options, label='Opciones')
menu_options.add_command(label='Salir', command=root.quit)

# Pestaña Otros
menubar.add_cascade(menu=menu_extra, label= 'Otros')

welcome_lbl = Label(root, text="Iniciemos un entrenamiento", font=("Yu Gothic UI Semibold", 30)).grid(row=0, column=1)

button_start_training = Button(root, text="Iniciar").grid(row=1, column=1)



root.mainloop()