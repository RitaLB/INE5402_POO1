#ler n e m:
n,m = input().split()
n = int(n)
m = int(m)

#crio dicionario para runas
dicio = {} #Crio meu dicionário vazio
for i in range(n):
    runa, valor = input().split()
    valor = int(valor)
    dicio[runa] = valor

q = int(input())
recitadas = input().split()

#calculo total:
total = 0
for i in range (q):
    total += int(dicio[recitadas[i]])

#vejo quem ganha:
print (total)
if total >= m:
    print("You shall pass!")
else:
    print("My precioooous")