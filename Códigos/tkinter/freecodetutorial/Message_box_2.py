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
    response =  messagebox.askyesno("This is my Popup!", "Are you going to choose the option 'yes'?")
    #Label(root, text= response).pack() 
    if response == 1:
        Label(root, text = "Indeed, you chose the option 'yes'").pack()
    else:
        Label(root, text = "Indeed, you didn't chose the option 'yes'").pack()
#creating a button:
Button(root, text= "POpup", command= popup).pack()

mainloop()
