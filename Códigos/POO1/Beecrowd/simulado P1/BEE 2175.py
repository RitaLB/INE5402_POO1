ot,bt,it = input().split()
ot= float(ot)
bt= float(bt)
it= float(it)

if (ot <bt) and (ot<it):
    print("Otavio")
elif (bt<ot) and (bt<it):
    print("Bruno")
elif (it<ot) and (it<bt):
    print("Ian")
elif (ot==bt) or (ot==it) or (bt==it):
    print("Empate")