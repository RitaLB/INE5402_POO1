n = int(input())

#defino variável vazia p presentes:
presentes = 0
#defino um avariável vazia para hpras de trabalho emm cada grupo:
bonecos = 0
arquitetos = 0
musicos = 0
desenhistas = 0
#para cada elfo, vejo quantos presentes serão feitos:
    
for i in range (n):
    e,g,h = input().split()
    h = int(h)
    
    if g == "bonecos":
        bonecos += h
        
    elif g == "arquitetos":
        arquitetos += h
        
    elif g == "musicos":
        musicos += h
        
    elif g == "desenhistas":
        desenhistas += h
        
  #adiciono os presentes feitos na variavel presentes:      
presentes += bonecos//8
presentes += arquitetos//4
presentes += musicos//6
presentes += desenhistas//12
        
#imprimo o total:
print (presentes)