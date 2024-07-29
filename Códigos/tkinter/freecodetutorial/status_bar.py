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
my_imag0 = ImageTk.PhotoImage(Image.open("images\\espiral_1.jpg"))
my_imag1 = ImageTk.PhotoImage(Image.open("images\\img_1.jpg"))
my_imag2 = ImageTk.PhotoImage(Image.open("images\\img_2.jpg"))
my_imag3 = ImageTk.PhotoImage(Image.open("images\\img_3.jpg"))
my_imag4 = ImageTk.PhotoImage(Image.open("images\\img_4.jpg"))
my_imag5 = ImageTk.PhotoImage(Image.open("images\\img_5.jpg"))
my_imag6 = ImageTk.PhotoImage(Image.open("images\\img_6.jpg"))
my_imag7 = ImageTk.PhotoImage(Image.open("images\\img_7.jpg"))
my_imag8 = ImageTk.PhotoImage(Image.open("images\\img_8.jpg"))

#creating a list to being able to scroll trought the images
image_list = [my_imag0, my_imag1, my_imag2, my_imag3, my_imag4, my_imag5, my_imag6, my_imag7, my_imag8]

#crating a label to the status bar:
#bd=  size of the edge
# achor = anchor the status bar on the east side of the screen
status = Label(root, text= "Image 1 of " + str(len(image_list)), bd=1, relief= SUNKEN, anchor=E )

#putting it into the screen:
status.grid(row=2, column=0, columnspan=3, sticky= W+E)

#creating a label to the image
my_label = Label(image = my_imag0)
my_label.grid(row = 0, column=0, columnspan=3)

#creating functions to define the functionality of the buttons:

def foward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    #label receives the next image:
    my_label = Label(image= image_list[image_number-1])
    # the parametre of the buttons receive new values:
    button_forward = Button(root, text = ">>", command = lambda: foward(image_number+1) )
    button_back = Button(root, text = "<<", command= lambda: back(image_number-1))

    #creating a condition to the last image:
    if image_number== len(image_list):
        button_forward = Button(root, text = ">>", state = DISABLED )
    #putting the new buttons into the screen:
    button_back.grid(row = 1, column = 0)
    button_forward.grid( row = 1, column = 2)

    #putting the label into the screen:
    my_label.grid(row = 0, column=0, columnspan=3)

    # each time we move to the next iamge, we need to update the status bar:
    status = Label(root, text= "Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief= SUNKEN, anchor=E )
    status.grid(row=2, column=0, columnspan=3, sticky= W+E)


def back(image_number):

    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()

    #label receives the next image:
    my_label = Label(image= image_list[image_number-1])
    # the parametre of the buttons receive new values:
    button_forward = Button(root, text = ">>", command = lambda: foward(image_number+1) )
    button_back = Button(root, text = "<<", command= lambda: back(image_number-1))

    #creating a condition to the first image:
    if image_number == 1:
        button_back = Button(root, text = "<<", state = DISABLED)

    #putting the new buttons into the screen:
    button_back.grid(row = 1, column = 0)
    button_forward.grid( row = 1, column = 2)

    #putting the label into the screen:
    my_label.grid(row = 0, column=0, columnspan=3)

    # each time we move to the next iamge, we need to update the status bar:
    status = Label(root, text= "Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief= SUNKEN, anchor=E )
    status.grid(row=2, column=0, columnspan=3, sticky= W+E)

    

#criating the buttons we will use:
button_back = Button(root, text = "<<", state = DISABLED)
button_exit = Button(root, text= "Exit Program", command = root.quit)
button_forward = Button(root, text = ">>", command = lambda: foward(2) )

button_back.grid(row = 1, column = 0)
button_exit.grid( row =1, column= 1, pady= 10  )
button_forward.grid( row = 1, column = 2)

#criate a loop that keeps the screen showing
root.mainloop()