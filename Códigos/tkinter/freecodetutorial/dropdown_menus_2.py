from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Ritinha's game")
root.iconbitmap("images\\logo_Rj.ico")

#dropdown is kinda option menu

def show():
    mylabel = Label(root, text= clicked.get()).pack()
    
#creating a list to the options:
options = [
     "Monday",
     "Tuesday", 
     "Wednesday", 
     "Thursday", 
     "friday"
]

#create a variable to carry the value of the option clicked:
clicked = StringVar()
#set the initial value:
clicked.set(options[0])


#creat the option menu:
# clicked -> the variable ,
# *options--> create a option to each item at options list

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text = "Show Selection", command = show).pack()
mainloop() 