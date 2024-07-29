while True:
    n = int(input())
    if n == 0:
        break
    for f in range (0,n):
        a =  list(map(int,input().split()))
        q = '*'
        for i in range (0,5):
            if a[i] > 127:
              a[i] = 'branco'
            else:
             a[i] = 'preto'

        for i in range (1,4):
            if ((a[i] == 'preto') and (a[i] != a[i-1]) and (a[i] != a[i+1])):
                q = i

        for i in range (1,5):
            if a[0] == 'preto' and a[0] != a[i]:
                q = 'A'
        for i in range (0,4):
            if a[4] == 'preto' and a[4] != a[i]:
                q = 'E'

        if q == 1 :
            q = 'B'

        if q == 2:
            q = 'C'
        if q == 3:
            q = 'D'

        print(q)
