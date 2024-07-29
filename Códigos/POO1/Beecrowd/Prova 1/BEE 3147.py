h,e,a,o,w,x = input().split()
h = int(h)
e = int(e)
a = int(a)
o = int(o)
w = int(w)
x = int(x)
# exercito bom = a soma de h, e, a e x
#exercito do mal = a soma de 0, w
eb = h+e+a+x
er = o+w
''''
 se a soma dos exercitos bons for maior que a dos mals, exerc. bom ganha. se Exe. mal for maior, ele ganha. 
 EM caso de empate, o hobbit irá desempatá e fazer o exer. bom ganhar'''
if eb>er:
    print("Middle-earth is safe.")
elif er>eb:
    print("Sauron has returned.")
elif er== eb:
    print("Middle-earth is safe.")