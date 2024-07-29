while True:
    try:
        #lendo n:
        n = input()
        mf = frequencia[0]
        frequencia = [None]* len(n)
        for i in range (0,len(n)+1):
            for a in range(1, len(n)+1):
                if n[i] == n[a]:
                    frequencia[i] += 1

        for i in range (0,len(frequencia)+1):
            for a in range(1, len(frequencia)+1):
                if frequencia[a] > frequencia[i]:
                    mf = frequencia[a]

        print(mf)
    except EOFError:
        break