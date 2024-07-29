# x é o código do produto  e y é o número de ítens
x,y = input().split()
x = int(x)
y = int(y)
if x == 1:
    total = y*4
if x == 2:
    total = y*4.5
if x == 3:
    total = y*5
if x == 4:
    total = y*2
if x == 5:
    total = y*1.5

print("Total: R$ {:.2f}".format(total))
