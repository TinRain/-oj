m = int(input().strip())
sum = 0
while m>0:
    n = int(input().strip())
    arr = input().strip().split()
    arr = [int(i) for i in arr]
    for i in range(n):
        for j in range(n):
            if i<j and arr[i]>arr[j]:
                sum+=1
    m-=1
print(sum)

