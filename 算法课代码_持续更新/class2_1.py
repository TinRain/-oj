import sys


def isPossible(A, N, M, curr_min):
    students_required = 1
    curr_sum = 0
    for i in range(N):
        if A[i] > curr_min:
            return False
        if curr_sum + A[i] > curr_min:
            students_required += 1
            curr_sum = A[i]
            if students_required > M:
                return False
        else:
            curr_sum += A[i]
    return True


def find_pages(A, N, M):
    sum = 0
    if N < M:
        return -1

    for i in range(N):
        sum += A[i]

    start = 0
    end = sum
    result = sys.maxsize

    while start <= end:
        mid = int(start+end)/2
        if isPossible(A, N, M, mid):
            result = min(result, mid)
            end = mid - 1
        else:
            start = mid + 1
    return result


T = int(input())


while T > 0:
    try:
        N = int(input())
        A = list(map(int, input().split()))
        M = int(input())

        print(int(find_pages(A, N, M)))
        T -= 1
    except EOFError:
        break
