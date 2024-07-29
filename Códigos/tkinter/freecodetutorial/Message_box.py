from tkinter import *
from PIL import ImageTk, Image
#import a module for message box creation
from tkinter import messagebox

# obs: there are several kinds of popups: 
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

root = Tk()
root.title("ritinha's message box")
root.iconbitmap("images\\logo_Rj.ico")

#creating the popup function:
def popup(): 
#creating a message box
    messagebox.askokcancel("This is my Popup!", "Hello world!")

#creating a button:
Button(root, text= "POpup", command= popup).pack()

mainloop()
