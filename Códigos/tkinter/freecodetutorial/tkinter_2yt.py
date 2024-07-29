#importar tkinter:
from tkinter import *

#root : a janela principal do programa
root = Tk()

""" every thing in tkinter has 2 process:
- creating it
- putting it on the screen"""

#criar uma label widget:
#(define it)

mylabel1 = Label(root, text= "hello world")
mylabel2 = Label(root, text= "my name is Rita")

# showing it onto the screen and defining it position 
# the position is createde using a grid sismem of rows and columns
mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=0)

#criate a loop that keep the screen showing
root.mainloop()

