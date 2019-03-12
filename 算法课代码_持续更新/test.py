def mf(mid, arr, size):
    ans = 0
    for i in range(size):
        ans += 1 / (mid - arr[i])
    return ans


def zeroPoints(arr, size, left, right):
    while left < right:
        mid = left + (right - left) / 2
        mag = mf(mid, arr, size)
        if abs(mag) < 0.0000000000001:
            return mid
        elif mag > 0:
            return zeroPoints(arr, size, mid, right)
        else:
            return zeroPoints(arr, size, left, mid)


T = int(input())
while T > 0:
    try:
        N = int(input())
        M = list(map(int, input().split()))
        for i in range(1, N):
            if i == N - 1:
                print('%.2f' % zeroPoints(M, N, M[i - 1], M[i]))
            else:
                print('%.2f' % zeroPoints(M, N, M[i - 1], M[i]), end=" ")
        T = T - 1
    except EOFError:
        break

