#lendo n
n = int(input())

for a in range (n):

    ko = input().split()
    for i in range (len(ko)):
        ko[i]= int(ko[i])
        
    k = ko[0]
    #calcular num aparelhos:
    o = 0
    for b in range (1 , k+1):
        o += ko[b]

    aparelhos = o - (k-1)
    
    print(aparelhos)