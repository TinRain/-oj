T = int(input())


def func(arr1, arr2, N, M):
    copy = []
    for i in range(M):
        for j in range(N):
            if arr1[j] == arr2[i]:
                copy.append(arr1[j])
    for i in range(N):
        for j in range(M):
            if arr1.__contains__(arr2[j]):
                arr1.remove(arr2[j])
    arr1.sort()
    for i in range(len(arr1)):
        copy.append(arr1[i])
    return copy


while T > 0:
    num = list(map(int, input().split()))
    N = num[0]
    M = num[1]
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    res = func(arr1, arr2, N, M)
    s = ''
    for i in range(len(res)):
        s = s + str(res[i]) + ' '
    print(s.rstrip())
    T -= 1