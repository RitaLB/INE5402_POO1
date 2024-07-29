money=float(input())

notas100= money//100
notas50= (money%100)//50
notas20= ((money%100)%50)//20 
notas10= (((money%100)%50)%20)//10
notas5= ((((money%100)%50)%20)%10)//5
notas2= (((((money%100)%50)%20)%10)%5)//2
moeda1= ((((((money%100)%50)%20)%10)%5)%2)//1

money = int(money*100)

moeda050= (((((((money%10000)%5000)%2000)%1000)%500)%200)%100)//50
moeda025= ((((((((money%10000)%5000)%2000)%1000)%500)%200)%100)%50)//25 
moeda010 = (((((((((money%10000)%5000)%2000)%1000)%500)%200)%100)%50)%25)//10
moeda005= ((((((((((money%10000)%5000)%2000)%1000)%500)%200)%100)%50)%25)%10)//5
moeda001= (((((((((((money%10000)%5000)%2000)%1000)%500)%200)%100)%50)%25)%10)%5)//1 

print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(int(notas100)))
print("{} nota(s) de R$ 50.00".format(int(notas50)))
print("{} nota(s) de R$ 20.00".format(int(notas20)))
print("{} nota(s) de R$ 10.00".format(int(notas10)))
print("{} nota(s) de R$ 5.00".format(int(notas5)))
print("{} nota(s) de R$ 2.00".format(int(notas2)))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(int(moeda1)))
print("{} moeda(s) de R$ 0.50".format(int(moeda050)))
print("{} moeda(s) de R$ 0.25".format(int(moeda025)))
print("{} moeda(s) de R$ 0.10".format(int(moeda010)))
print("{} moeda(s) de R$ 0.05".format(int(moeda005)))
print("%d moeda(s) de R$ 0.01" % moeda001)