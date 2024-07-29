#importar tkinter:
from tkinter import *

#root : a janela principal do programa
root = Tk()

#criar uma label widget:
#(define it)

mylabel = Label(root, text="hello world")

# putting the label widget on the root window (shoving it onto the screen):
#pack it in some how
mylabel.pack()

#criate a loop that keep the screen showing
root.mainloop()

