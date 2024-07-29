soma = 0
qtde = 0
n = float ( input ())
while n != 0:
    soma += n
    qtde += 1
    n = float ( input ())
print ("{:.2f}".format( soma / qtde ))
