from tkinter import *
from PIL import ImageTk, Image
from tkinter import font

# Ventana
root = Tk()
root.title("Formulario")
root.resizable(FALSE, FALSE)
root.geometry('650x700+300+50')

# Labels
welcome_lbl = Label(root, text="Permítenos conocerte.", font=("Yu Gothic UI Semibold", 30)).grid(row=0, column=1, columnspan=2)

name_lbl = Label(root, text="Nombre:", font=("Yu Gothic UI Light", 20)).grid(row=1, column=0)

sex_lbl = Label(root, text="Sexo:", font=("Yu Gothic UI Light", 20)).grid(row=2, column=0)

age_lbl = Label(root, text="Edad:", font=("Yu Gothic UI Light", 20)).grid(row=3, column=0)

lifestyle_lbl = Label(root, text="Tipo de Vida:", font=("Yu Gothic UI Light", 20)).grid(row=3, column=0)





root.mainloop()

