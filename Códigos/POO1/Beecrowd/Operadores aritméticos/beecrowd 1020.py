age= int(input("quantos dias de vida você tem?"))

years = age // 365
a = (age % 365)
months = a // 30
days = a % 30
print ( "{} ano(s)".format(years))
print("{} mes(es)".format(months))
print("{} dia(s)".format(days))
