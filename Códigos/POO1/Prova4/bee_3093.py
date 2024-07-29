n = int(input())
for i in range (n):
    monte = str(input())

    q = False
    j = False
    k = False
    a = False

    for a in range (len(monte)):
        if monte[a] == 'Q':
            q =True
        elif monte[a] == 'J':
            j = True
        elif monte[a] == 'K':
            k = True
        elif monte[a] == 'A':
            a = True

    if q and j and k and a:
        print("Aaah muleke")

    else: 
        print("Ooo raca viu")