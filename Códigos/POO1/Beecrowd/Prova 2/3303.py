while True:
    try:
        p = str(input())
    #se o tamanho da string for maior q 10, a palavra é um palavrão
        if len(p) >= 10:
            print("palavrao")
    #se o tamanho de p for menor q 10, é uma palavrinha
        else: 
            print("palavrinha")
    except EOFError:
        break
    