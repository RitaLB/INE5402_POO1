while True:
    try:
        #crio vetores vazios para armazenar números sorteados e depois fazer comparações
        nf = [0]*100
        ns = [0]*100
        #crio variável com num de acertos:
        acertos = 0
       #apostas de flavinho:
        f = input().split()
        for k in range(0, len(f)+1):
            f[k] = int(f[k])
           
       # num sorteados:
        s = input().split()
        for c in range(0, len(s)+1):
            s[c] = int(s[c])
        #atribuo 1 para cada numero escolhido e sorteado:
    
        for i in range (6):
            nf[f[i]] += 1
           
        for b in range(6):
            ns[s[b]] +=1
        
        # comparo os dois vetores:
        for h in range (100):
            if nf[h] == ns[h]:
                acertos += 1
        # imprimo as saídas 
        if acertos == 3:
            print ("terno")
            
        if acertos == 4:
            print ("quadra")
            
        if acertos == 5:
            print ("quina")
            
        if acertos == 6:
            print ("sena")
        
        else:
            print("azar")
        
    except EOFError:
        break
        