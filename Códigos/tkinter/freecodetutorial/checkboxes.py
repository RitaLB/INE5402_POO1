from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Ritinha's game")
root.iconbitmap("images\\logo_Rj.ico")

def show():
    #creating a label to see the value inside the option clicked:
    mylabel = Label(root, text = var.get()).pack()

# it's important to create a variable to cary the value of the action of click or not
var = StringVar() 

#creating the checkbox:
#check boxes are binary stated. we can set the states to be called what ever we want with 
#onvalue and offvalue. 
c = Checkbutton(root, text = "Don't check this box!", variable = var, onvalue= "on", offvalue = "off")
c.deselect()
c.pack()

#if you work with var = IntVar(), you don't have to atribute a value to the options, it is pre-atributed as 0 and 1. 
# you don't need to c.deselect ether. 

myButton = Button(root, text = "Show selection", command = show).pack()
mainloop() 