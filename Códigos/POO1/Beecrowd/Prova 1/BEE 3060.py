v = int(input())
p = int(input())
'''Se o resto da divisão do valor e das parcelas for igual a zer, todas as parcelas serão iguais'''
if v%p == 0:
    for i in range (p):
        print(int(v/p))
'''Se o resto da divisão do valor e das parcelas for diferente de zero, será acrescentado 1 para as "n" parcelas iniciais, 
sendo n o valor do resto da divisão. As outras parcels ficarão com o valor original da divisão inteira
'''
elif v%p != 0:
    for i in range (v%p):
        print(int((v//p)+1))
    for i in range (p- (v%p)):
        print(int(v//p))
