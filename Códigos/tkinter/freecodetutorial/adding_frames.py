from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Ritinha's program")
root.iconbitmap("C:\\Users\\win_r\\Documents\\Programação\\POO1\\Códigos\\tkinter\\freecodetutorial\\images\\logo_Rj.ico")

# creating a frame widget:

frame = LabelFrame(root, text= "this is my frame", padx= 5, pady=5)
frame.pack(padx=10, pady=10)

#creating a button insite the frame:
#obs: we can use pack sistem to the frame at the same time we use grid sistem inside the frame

b = Button(frame, text = "don't click here")
b.grid(row = 0, column =0 )
b2 = Button(frame, text = "... or here")
b2.grid(row = 1, column =0 )


root.mainloop()
