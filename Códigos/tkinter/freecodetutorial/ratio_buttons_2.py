from tkinter import *
from PIL import ImageTk, Image

# in this file we improve the ratio_button by creating a loop to create the ratio buttons

root = Tk()
root.title("Ritinha's program")
root.iconbitmap("C:\\Users\\win_r\\Documents\\Programação\\POO1\\Códigos\\tkinter\\freecodetutorial\\images\\logo_Rj.ico")

#creating a list:
# ("x", "y") --> x = (text) what will show up on the screen, 
# y = (mode) the actual value the click will atribute to some variable 
MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushrom", "Mushrom"),
    ("onion", "onion"),
]

#creatinga tkinter variable:
pizza = StringVar()
# setting it a initial value:
pizza.set("Pepperoni")

#loop throught all this things and put them all on the screen:
for text, mode in MODES:
    Radiobutton(root, text = text, variable= pizza, value = mode).pack(anchor=W)

#creating a label to define usuability to the buttons:
def clicked(value):
    mylabel = Label(root, text = value)
    mylabel.pack()


#creating a button 
mybutton = Button(root, text = "Click Me!", command = lambda: clicked(pizza.get()) )
mybutton.pack()

root.mainloop()
