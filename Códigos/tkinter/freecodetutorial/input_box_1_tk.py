#creating a button:
#importar tkinter:
from tkinter import *

#root : a janela principal do programa
root = Tk()

#crating a entry:
#width = size of the entry
#borderwidth = size of the border
e = Entry(root, width = 50)

#packing it
e.pack()

#e.insert() = defines something to be already inside the entry 
e.insert(0, "Enter Your Name: ")

#e.get =  colects what have been ritten inside the entry

# creating a function to define what the button will do:

def myClick():
    hello = "Hello" + e.get()
    myLabel = Label(root, text = hello)
    myLabel.pack()


#creating a button
myButton = Button(root, text= "click me!", command = myClick, fg = "#000000", bg = "blue")

#putting it uo on the screen
myButton.pack()

#criate a loop that keeps the screen showing
root.mainloop()

