# import turtle library:
import turtle 

#creating a class:
# things inside the "()": parametros
# size = 100 --> deffout argument. if a value to the parametre isn't provided, 
# this will be the value to size
class Polygon:
    def __init__(self, sides, name, size = 100, color = "black", line_thickness = 3):
        self.sides = sides    
        self.name = name
        self.size = size
        self.color = color
        self.line_thickness = line_thickness
        self.interior_angles = (self.sides - 2)*180
        self.angle = self.interior_angles/ self.sides

    def draw(self):
        turtle.color(self.color)
        turtle.pensize(self.line_thickness)
        for i in range(self.sides):
            turtle.forward(self.size)
            turtle.right(180-self.angle)
        turtle.done


#now you can create objects that uses the polygon class as structure:
square = Polygon(4, "square", 100 )
pentagon = Polygon(5, "pentagon", color = "red")

#you can request specific information about the objects also:
print(square.sides)
print(square.name)

#you can use functions of the class above the objects:
pentagon.draw()

#creating a subclass:
#Square class ultilise the inialization method from the Polygon class 
class Square(Polygon):
    def __init__(self, size = 100, color = "black", line_thickness = 3 ):
        #super() --> take anythinf from the superclass (Polygon)
        # defining the parametres:
        super().__init__(4, square, size, color, line_thickness)

    def draw(self):
        turtle.begin_fill()
        #importing draw function from the Polygon class:
        super().draw()

        turtle.end_fill()


square = Square()
print(square.draw())

turtle.done()