fpn= float(input())
if fpn>=  0 and fpn <=25 :
    print("Intervalo [0,25]")
elif fpn>25 and fpn<=50 :
    print("Intervalo (25,50]")
elif fpn >50 and fpn <=75 :
    print("(50,75]")
elif fpn >75 and fpn<=100 :
    print("(75,100]")
else :
    print ("Fora de intervalo")
