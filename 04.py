m = int(input().strip())
while m > 0:
    num = list(map(int, input().split()))
    M = num[0]
    N = num[1]
    arr1 = list(map(int, input().split()))
    arr1.sort()
    arr2 = list(map(int, input().split()))
    arr = []
    for i in range(N):
        for j in range(M):
            if arr2[i] == arr1[j]:
                arr.append(arr1[j])
                #arr1.remove(arr1[j])
    for i in range(M):
        for j in range(N):
            if arr1.__contains__(arr2[j]):
                arr1.remove(arr2[j])
    arr = arr + arr1
    s = ""
    for i in range(len(arr)):
        s = s + str(arr[i]) + " "
    print(s)
    m -= 1
