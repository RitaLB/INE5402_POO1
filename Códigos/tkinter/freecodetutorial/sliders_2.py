from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Ritinha's game")
root.iconbitmap("images\\logo_Rj.ico")


#creating the slider widger ( called scale widget)
vertical = Scale(root, from_=0 , to= 400)
# it's important to pack it in another line
vertical.pack()

def slide():
   
    my_label= Label(root, text= str(horizontal.get()) + "x" + str(vertical.get()) ).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get())) 

#horizontal slider:
horizontal = Scale(root, from_=0 , to= 400, orient = HORIZONTAL )
horizontal.pack()


my_btn = Button(root, text= "I prefer you don't click me", command = slide).pack()
mainloop() 