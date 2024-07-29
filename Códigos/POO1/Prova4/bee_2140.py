while True:
    #ler n:
    n,m = input().split()
    n = int(n)
    m = int(m)
    
    #caso de parada:
    if n == 0 and m==0:
        break
    
    #calculo de troco:
    troco = m-n
    #trocos possiveis:
    ptroco= [4,10,20,40,100,200,7,12,22,52,102,15,25,55,105,30,60,110,70,120,150]
    possivel = False

    #verificar se é possível:
    for i in range (len(ptroco)):
        if ptroco[i] == troco:
            possivel = True
    if possivel:
        print("possible")
    else: 
        print("impossible")