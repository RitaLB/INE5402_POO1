#creating a button:
#importar tkinter:
from tkinter import *

#root : a janela principal do programa
root = Tk()

# creating a function to define what the button will do:

def myClick():
    myLabel = Label(root, text= "look! i clicked a Button!!!")
    myLabel.pack()


#creating a button
# state: state = DISABLED if i put it next to thext, it disable the button 
# padx= n defines the size of the butto in the x dimention
# pady= n defines the size of the butto in the y dimention
# command = define what the button will do
# fg =  letters color
# bg = background color
myButton = Button(root, text= "click me!", command = myClick, fg = "#000000", bg = "blue")

#putting it uo on the screen
myButton.pack()

#criate a loop that keeps the screen showing
root.mainloop()

