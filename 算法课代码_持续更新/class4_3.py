T = int(input())
for _ in range(T):
    n = int(input())
    ct = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            r = (i*j) % 7
            r = (r*r*r) % 7
            if r != 1 and r != 5:
                ct += 1
    print(ct)


