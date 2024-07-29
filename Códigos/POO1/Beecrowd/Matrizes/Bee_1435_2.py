while True:
    n= int(input())
    if n ==0:
        break

    Ma= []
    for i in range(n):
        Ma.append([1]*n)

    for k in range (1, n-1):
        for i in range (k, n-k):
            for j in range(k, n-k):
                Ma[i][j] += 1 

    for i in range(n):
        for j in range(n - 1):
            print('%3d' % Ma[i][j], end=' ')
        print('%3d' % Ma[i][n-1])
    print('')