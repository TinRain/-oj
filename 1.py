arr = input().strip().split()
arr = [int(i) for i in arr]
n = int(input().strip())
sum = 0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if abs(arr[i]-arr[j]) > n:
            sum+=1
print(sum*2)
