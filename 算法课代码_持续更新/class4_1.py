def result(N, H, P, marks, time):
    dp = [[0 for i in range(H+1)] for j in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, H+1):
            if j >= time[i-1]:
                dp[i][j] = max(marks[i-1] + dp[i-1][j-time[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    ti = 0
    i = N
    j = H
    while i != 0 and j != 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            ti += time[i-1]
            j = j - time[i-1]
            i -= 1
    if dp[N][H] >= P:
        return 'YES ' + (str)(ti)
    return 'NO'


T = int(input())
for _ in range(T):
    first_line = list(map(int, input().split()))
    N = first_line[0]
    H = first_line[1]
    P = first_line[2]

    time = [0 for i in range(N)]
    marks = [0 for i in range(N)]

    for i in range(N):
        line = list(map(int, input().split()))
        time[i] = line[0]
        marks[i] = line[1]

    print(result(N, H, P, marks, time))
