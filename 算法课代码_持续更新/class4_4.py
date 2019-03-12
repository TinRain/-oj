def minInitialPoints(points, R, C):
    dp = [[0 for x in range(C + 1)]
          for y in range(R + 1)]
    m, n = R, C

    if points[m - 1][n - 1] > 0:
        dp[m - 1][n - 1] = 1
    else:
        dp[m - 1][n - 1] = abs(points[m - 1][n - 1]) + 1

    for i in range(m - 2, -1, -1):
        dp[i][n - 1] = max(dp[i + 1][n - 1] -
                           points[i][n - 1], 1)
    for i in range(2, -1, -1):
        dp[m - 1][i] = max(dp[m - 1][i + 1] -
                           points[m - 1][i], 1)

    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            min_points_on_exit = min(dp[i + 1][j],
                                     dp[i][j + 1])
            dp[i][j] = max(min_points_on_exit -
                           points[i][j], 1)

    return dp[0][0]


T = int(input())
for _ in range(T):
    line = list(map(int, input().split()))
    R = line[0]
    C = line[1]
    arr = list(map(int, input().split()))
    points = [[0 for i in range(C)] for j in range(R)]
    for i in range(R):
        for j in range(C):
            points[i][j] = arr[i*R+j]
    print(minInitialPoints(points, R, C))
