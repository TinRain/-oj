arr = [int(x) for x in input().split()]

# 从左往右递增
b = [[[str(x)]] for x in arr]
c = [[[str(x)]] for x in arr]
for i in range(len(arr)):
    j = 0
    while j < i:
        if arr[j] <= arr[i] and len(b[j][0]) == len(b[i][0]) - 1:
            tmp = []
            tmp.extend(b[j][0])
            tmp.append(str(arr[i]))
            b[i].append(tmp)
        if arr[j] <= arr[i] and len(b[j][0]) > len(b[i][0]) - 1:
            b[i] = [[]]
            b[i][0].extend(b[j][0])
            b[i][0].append(str(arr[i]))
        j = j + 1

# 从右往左增
i = len(arr) - 1
while i >= 0:
    j = i + 1
    while j < len(arr):
        if arr[j] <= arr[i] and len(c[j][0]) == len(c[i][0]) - 1:
            tmp = []
            tmp.append(str(arr[i]))
            tmp.extend(c[j][0])
            c[i].append(tmp)
        if arr[j] <= arr[i] and len(c[j][0]) > len(c[i][0]) - 1:
            c[i] = [[]]
            c[i][0].append(str(arr[i]))
            c[i][0].extend(c[j][0])
        j = j + 1
    i = i - 1

sub = []
t = -1
for i in range(len(arr)):
    if len(b[i][0]) + len(c[i][0]) - 1 > len(sub):
        len_b = len(b[i][0])
        sub = b[i][0][:len_b - 1] + c[i][0]
        t = i

for i in range(len(b[t])):
    b[t][i] = b[t][i][:len(b[t][i]) - 1]
    for j in range(len(c[t])):
        sub = b[t][i] + c[t][j]
        print(' '.join(sub))