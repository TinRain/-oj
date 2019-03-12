import math

T = int(input())
while T > 0:
    try:
        P = int(input())

        sum = 0
        i = 1
        while i*i <= P:
            sum += 1
            P -= i*i
            i += 1

        print(sum)
        T = T - 1
    except EOFError:
        break