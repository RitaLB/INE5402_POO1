while True:
    # n é o número de bilhetes originais e m é o número de pessoas que foram pra festa
    n, m = map(int, input().split())
    if (n == 0) and (m == 0):
        break

    # b é o  número total de bilhetes e r é o número de bilhetes que contém outro igual
    b = list(map(int, input().split()))
    b.sort()

    # lista.sort() deixa os elementos da lista em ordem crescente
    r = 0
    for i in range(1, len(b) - 1):
        if (b[i] == b[i + 1]) and (b[i] != b[i - 1]):
            r += 1
        else:
            r += 0
    if b[0] == b[1]:
        r += 1
    print(r)





