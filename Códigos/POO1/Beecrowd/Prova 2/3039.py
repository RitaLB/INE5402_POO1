n = int(input())
#crio variáveis para carrinhos e bonecas:
carrinhos = 0
bonecas = 0

#para cada criança vejo se será feito carrinho ou boneca:
for i in range (n):
    nome,letra = str(input()).split()
    if letra == "F":
        bonecas +=1
    else:
        carrinhos +=1 

#imprimo os resultados:
print(carrinhos,"carrinhos")
print(bonecas,"bonecas")
