a = [int(x) for x in input().split()]
k = int(input())

a.sort()
dic = {}
s = 0
begin = 0
end = len(a) - 1
while begin < end:
    currSum = a[begin]+a[end]
    if currSum == k:
        kv = {begin: end}
        dic.update(kv)
        begin += 1
        end -= 1
        continue
    else:
        if currSum < k:
            begin += 1
        else:
            end -= 1

print(dic.__len__())