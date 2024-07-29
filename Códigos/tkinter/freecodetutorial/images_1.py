#importar tkinter:
from tkinter import *

# importing mudule to be able to deal with images
from PIL import ImageTk , Image

#root : a janela principal do programa
root = Tk()

#root.title() gives a title for the program
root.title("ritinha's program" )

#putting a icon on the top of the program
#obs: its important the image to be in .ico formt
root.iconbitmap("C:\\Users\\win_r\\Documents\\Programação\\POO1\\Códigos\\tkinter\\freecodetutorial\\images\\logo_Rj.ico")


#creating a image
#obs: if the image is at the same directory as your code, you don't need to especify all the path
my_imag = ImageTk.PhotoImage(Image.open("images\\espiral_1.jpg"))

#creating a label to the image
my_label = Label(image = my_imag)
my_label.pack()

#criate a exit button:
button_quit = Button(root, text= "Exit Program", command = root.quit)
button_quit.pack()

#criate a loop that keeps the screen showing
root.mainloop()
