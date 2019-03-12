num_tests = int(input())

while num_tests > 0:
    array_size = int(input())
    list_input = list(map(int,input().split()))
    a = {}
    for i in list_input:
        a[i]= list_input.count(i)
    b = sorted(a.items(),key=lambda item:(-item[1],item[0]))
    c = []
    for j in b:
        c += [str(j[0])] * j[1]
    print(' '.join(c))
    num_tests -=1