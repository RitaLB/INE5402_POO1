from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Ritinha's game")
root.iconbitmap("images\\logo_Rj.ico")


#creating open function:
def open():
    #creating global to the image:
    global my_img
    #creating a new window:
    swind = Toplevel()

    swind.title("My second window")
    swind.iconbitmap("images\\logo_Rj.ico")

    #putting things inside the swind:
    my_img = ImageTk.PhotoImage(Image.open("images\\img_1.jpg"))
    lbl = Label(swind, text = "This is a text").pack()
    my_label = Label(swind,image= my_img ).pack()
    btn2 = Button(swind, text = "close window",command = swind.destroy ).pack()

    
#creating a button to activate the swind:
btn = Button(root, text= "Open Second Window", command = open).pack()



mainloop()