while True:
    try:
        n,m = input().split()
        n = int(n)
        m = int(m)
        
        casa = [None] * n
        for i in range (n):
            casa[i] = input().split()

        tab = [0] * n
        for i in range (n):
            for j in range (m):
                if casa[i][j] == 1:
                    tab[i][j] += 9
                else:
                    for k in range (i,n+1):
                        for l in range (j, m+1):
                            if casa[k][l] == 1:
                                tab[i][j] += 1
                    for a in range (i, -1, -1):
                        for b in range (j, -1, -1):
                            if casa[a][b] == 1:
                                tab[i][j] += 1

        print(tab)
    except EOFError:
        break