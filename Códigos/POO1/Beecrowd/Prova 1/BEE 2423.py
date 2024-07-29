a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
ta = a//2
tb = b//3
tc = c//5
if (ta<=tb) and (ta<=tc):
    print(ta)
elif (tb<=ta) and (tb<=tc):
    print(tb)
elif (tc<=ta) and (tc<=tb):
    print(tc)
