a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
k = int(input())

tmp = [1/x for x in a[b[0]-1:b[1]]]
tmp.sort()

print(int(1/tmp[-k]))
