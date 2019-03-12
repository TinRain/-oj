arr = [int(x) for x in input().split()]
num = int(input())
arr.sort()

j = 1
c = []
for i in range(len(arr)):
    while j < len(arr) and arr[j] - arr[i] <= num:
        j = j+1
    if j < len(arr):
        c.append([arr[i],arr[j]])

result = 0
t = len(arr)-1
d = []
for a in c:
    if a not in d:
        t = t - c.count(a)
        result = result + 2 ** t
        d.append(a)
print(result)