a,b,c = input ().split()
a= float(a)
b= float(b)
c = float(c)
pi= 3.14159
triangulo= (a*c)/2
circle = pi * c * c
trapezio = ((a + b)/2 )* c
square = b*b
retangulo = a*b
print("TRIANGULO: {:.3f}".format(triangulo))
print("CIRCULO: {:.3f}".format(circle))
print("TRAPEZIO: {:.3f}".format(trapezio))
print("QUADRADO: {:.3f}" .format(square))
print("RETANGULO: {:.3f}".format(retangulo))
