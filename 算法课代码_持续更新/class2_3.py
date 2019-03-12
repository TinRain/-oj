T = int(input())
while T > 0:
    try:
        n_q = list(map(int, input().split()))
        N = n_q[0]
        Q = n_q[1]
        l_r = list(map(int, input().split()))
        x = list(map(int, input().split()))
        marks_lr = list()
        ranks = list()
        for i in range(0, 2*N, 2):
            marks_lr.append([l_r[i], l_r[i+1]])
        ranks.append(0)
        for i in range(1, N + 1):
            ranks.append(ranks[i - 1] + marks_lr[i - 1][1] - marks_lr[i - 1][0] + 1)

        results = []
        for q in x:
            ind = 0
            if q > max(ranks):
                q -= max(ranks)
                results.append(q + marks_lr[N - 1][1])
            else:
                for i in range(len(ranks) - 1):
                    if q >= ranks[i] and q <= ranks[i + 1]:
                        ind = i
                        break
                q -= ranks[ind]
                results.append(q + marks_lr[ind][0] - 1)
        print(*results)
        T = T - 1
    except EOFError:
        break