while True:
    n = int(input())
    # n é o número de diferentes comprimentos das varetas

    if n == 0:
        break
    qpares = 0

    for i in range(n):
        # ci = comprimento das varetas  e vi = número de varetas com esse comprimento
        ci, vi = map(int, input().split())

        # formo pares com as varetas de cada comprimento
        qpares += vi // 2

    '''para descobrir o número de retângulos, vejo quantos pares de pares consigo formar 
    ( um retâng. usa 4 varetas, ou seja, 2 pares)'''

    qretangulos = qpares // 2
    print(qretangulos)

