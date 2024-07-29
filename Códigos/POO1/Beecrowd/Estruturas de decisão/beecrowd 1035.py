'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
a,b,c,d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

if (b >c) and (d>a) and (c+d)>(a+b) and c >0 and d >0 and  a%2==0 :
    print("Valores aceitos")
else : 
    print("Valores nao aceitos")
    
