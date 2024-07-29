from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Ritinha's game")
root.iconbitmap("images\\logo_Rj.ico")
#designate hoe big the original window is:
root.geometry("400x400")


#creting the comand to the button:
def open():
    global my_image
    #create the open file dialog box:
    #*.filename returns the file name ( including the path)
    # initialdir = directory that will be opened initially
    # filetypes--> ("text that describes the type" , "type of file that will be shown")
    root.filename = filedialog.askopenfilename(initialdir= "images", title = " Select a file my babe", filetypes = (("The png ones" , "*.png"),("Any kind", "*.*" )))
    my_label = Label(root, text = root.filename).pack()

    #opening the image selected at the open file dialox box:
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label= Label(image = my_image).pack()


#crating a button to call dial box:
my_btn = Button(root, text = "Wanna open a picture? click here", command = open).pack()

mainloop() 