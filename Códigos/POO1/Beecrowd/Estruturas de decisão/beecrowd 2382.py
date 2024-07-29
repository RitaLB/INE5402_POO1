l,a,p,r = input().split()
l= int(l)
a= int(a)
p= int(p)
r= int(r)
if 2*r>= ((l**2)+(a**2)+(p**2))**(1/2):
    print("S")
else:
    print("N")