soma= 0
quantidade = 0
n = float(input())
while n != 0:
    soma += n
    quantidade += 1

    n = float(input())

print("{}".format(soma/quantidade))
