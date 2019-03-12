def result(n, arr):
    res = []
    for i in range(0, n - 1):
        start = arr[i]
        end = arr[i + 1]

        while True:
            mid = float(start + end) / 2
            k = 0
            for j in range(0, n):
                k += 1 / (mid - arr[j])

            if abs(k) < 0.00001 / 2:
                res.append('%.2f' % mid)
                break

            elif k > 0:
                start = mid

            else:
                end = mid
    return res


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(x) for x in input().split(' ') if x != '']
        print(*result(n, arr))