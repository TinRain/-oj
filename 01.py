n = int(input().strip())
m = int(input().strip())
arr = input().strip().split()
arr = [int(i) for i in arr]
l = []
num = []
while n > 0:
    for i in arr:
        arr.sort()
        l.append(arr.count(i))
        l = list(set(l))
        l.sort(reverse=True)
    for m in l:
        for j in arr:
            if m == arr.count(j):
                num.append(j)

    num1 = " ".join(map(str,num))
    n= n-1
    print(num1)
