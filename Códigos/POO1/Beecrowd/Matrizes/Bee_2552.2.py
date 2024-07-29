# -*- coding: utf-8 -*-
while True:
    try:
        n, m = map(int, input().split())
        mat = [None] * n
        for i in range(n):
            mat[i] = input().split()
                    
        for i in range (n):
            resp = ''
            j = 0
            for j in range(m):
                vI = i
                vJ = j
                p = 0
                p = int(p)
                if mat[i][j] == '1':
                    resp += '9'
                else:
                    if vI > 0 and mat[i-1][j] == '1':
                        p += 1
                    if vI < n-1 and mat[i+1][j] == '1':
                        p += 1
                    if vJ > 0 and mat[i][j-1] == '1':
                        p += 1
                    if vJ < m-1 and mat[i][j+1] == '1':
                        p += 1
                    p = str(p)
                    resp += p
            print(resp)

    except EOFError:
        break