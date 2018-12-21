arr = input().strip().split()
arr = [int(i) for i in arr]
w = int(input().strip())
tmp = []
sum =0
for j in range(len(arr)-w+1):
     tmp = sorted(arr[j: j+w])
     print(tmp)
     sum += tmp[-1]
print(sum)