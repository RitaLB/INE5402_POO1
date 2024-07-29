r=int(input())

while r!=0:
    for i in range (r):
        a,b= input().split()
        a = int(a)
        b = int(b)
        a+=a
        b+=b
    if (a>b):
        print("Teste {}".format(i))
        print("Aldo")
    if (b>a):
        print("Teste {}".format(i))
        print("Beto")
    r = int(input())