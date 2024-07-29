while True:
    total = 0
    diferentes_tipos = int(input())
    if diferentes_tipos == 0:
        break
    for i in range(diferentes_tipos):
        comprimento, quantidade = [int(x) for x in(input().split())]
        total += (quantidade - quantidade%2)
    print(int(total/4))