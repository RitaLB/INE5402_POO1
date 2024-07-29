from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Ritinha's program")
root.iconbitmap("C:\\Users\\win_r\\Documents\\Programação\\POO1\\Códigos\\tkinter\\freecodetutorial\\images\\logo_Rj.ico")

#defining the tkinter variable:
r = IntVar()
# setting a initial value to the variable. 2 -> it initiates at the button 2 so
r.set("2")

#creating a label to define usuability to the buttons:
def clicked(value):
    mylabel = Label(root, text = value)
    mylabel.pack()


#creating the button:
#command = lambda: clicked(r.get()) = colects the value of "value"  
Radiobutton(root, text= "Option 1", variable= r, value = 1, command = lambda: clicked(r.get())).pack()

Radiobutton(root, text= "Option 2", variable= r, value = 2, command = lambda: clicked(r.get())).pack()

#creating a new label to sow the result of the click on the button choosen:
mylabel = Label(root, text = r.get())
mylabel.pack()

#creating a button 
mybutton = Button(root, text = "Click Me!", command = lambda: clicked(r.get()) )
mybutton.pack()

root.mainloop()
