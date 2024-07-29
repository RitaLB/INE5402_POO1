from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Ritinha's game")
root.iconbitmap("images\\logo_Rj.ico")


#creating the slider widger ( called scale widget)
vertical = Scale(root, from_=0 , to= 200)
# it's important to pack it in another line
vertical.pack()

def slide(xvar):

    my_label= Label(root, text= horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x400") 

#horizontal slider:
horizontal = Scale(root, from_=0 , to= 400, orient = HORIZONTAL, command = slide )
horizontal.pack()




my_btn = Button(root, text= "I prefer you don't click me", command = slide).pack()
mainloop() 