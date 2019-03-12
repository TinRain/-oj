T = int(input())
for _ in range(T):
    N = int(input())
    cow = [1, 1]
    for i in range(2, N + 1):
        cow.append(cow[i-1] + cow[i-2])
    print(int(max(cow)))
