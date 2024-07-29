# -*- coding: utf-8 -*-
while True:
    a = 0
    n = int(input())
    if n == 0:
        break
    for i in range(1, n + 1):
        v = input().split()
        a = 0
        for j in range(0, len(v)):
            v[j] = int(v[j])
            if v[j] <= 127:
                a += 1
                c = j
        if a == 1:
            if c == 0:
                print('A')
            elif c == 1:
                print('B')
            elif c == 2:
                print('C')
            elif c == 3:
                print('D')
            else:
                print('E')
        else:
            print('*')