while True:
    try:
        #crio variável vazia para má sorte: 
        msorte = 0
        #leio n:
        n = str(input())
        #se na string n houver "1" seguido de "3", má sorte ficará maior que 0
        for i in range(0, len(n)-1):
            if n[i] == '1':
                if n[i+1] == '3':
                    msorte +=1
        #se msorte > 0, o número é de má sorte. Imprimo a frase corresp. ao resultado:
        if msorte >=1:
            print(n,"es de Mala Suerte")
        if msorte == 0:
            print(n,"NO es de Mala Suerte")
        
        
    except EOFError:
        break
        