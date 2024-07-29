while True:
    n = int(input())
    if n== 0:
        break
    p = 0
    h= list(map(int,input().split()))
    for i in range(1, n-1):
        if (h[i] > h[i+1]) and (h[i]> h[i-1]):
            p += 1
        elif (h[i] < h[i+1]) and (h[i]<h[i-1]):
            p+= 1
    if (h[0] > h[1]) and (h[0]> h[n-1]):
        p += 1
    elif (h[0] < h[1]) and (h[0] < h[n-1]):
        p+= 1
    if (h[n-1] > h[0]) and (h[n-1]> h[n-2]):
        p += 1
    elif (h[n-1] < h[0]) and (h[n-1] < h[n-2]):
        p+= 1
    print(p)

