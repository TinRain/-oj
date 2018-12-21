arr = input().strip().split()
arr = [int(i) for i in arr]
arr2 = [int(x) for x in input().strip().split()]
k = int(input())
arr3 = arr[arr2[0]-1: arr2[1]]
print(arr3)
arr3 = sorted(arr3)
print(arr3[k-1])