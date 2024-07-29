n= int(input())
v = 0
g = 0
for i in range (n):
    t, c = input().split()
    t = str(t)
    c = int(c)
    if t == "V":
        v+= c
    elif t == "G":
        g+= c
if v>=g:
    print("A greve vai parar.")
elif g>v:
    print("NAO VAI TER CORTE, VAI TER LUTA!")