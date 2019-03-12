import collections

def solution(arr, qr):
    dicC = collections.Counter(arr)
    mx = max(arr)
    res = []
    for r in qr:
        j = 1
        c = 0
        while j * r <= mx:
            if j * r in dicC:
                c += dicC[j * r]
            j += 1
        res.append(c)

    return ' '.join(map(str, res))

# Driver code
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        numbers = list(map(int, input().split()))
        N = numbers[0]
        M = numbers[1]
        A = list(map(int, input().split()))
        K = list(map(int, input().split()))
        print(solution(A, K))

