from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Ritinha's game")
root.iconbitmap("images\\logo_Rj.ico")

#dropdown is kinda option menu

def show():
    mylabel = Label(root, text= clicked.get()).pack()
    
#create a variable to carry the value of the option clicked:
clicked = StringVar()
#set the initial value:
clicked.set("Monday")

#creat the option menu:
# clicked -> the variable ,
#  "monday"... "friday" --> the options
drop = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday", "Thursday", "friday")
drop.pack()

myButton = Button(root, text = "Show Selection", command = show).pack()
mainloop() 