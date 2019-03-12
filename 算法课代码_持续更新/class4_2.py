output = 0


def check(arr, element):
    for j in range(len(arr)):
        string = str(arr[j])
        for k in range(len(string)):
            if string[k] not in str(element):
                continue
            else:
                return False
    return True


def subSequence(arr, pat, start):
    global output
    for j in range(start, len(arr)):
        if check(pat, arr[j]):
            output = max(output, sum(pat) + arr[j])
            subSequence(arr, pat+[arr[j]], j+1)


T = int(input())
for _ in range(T):
    output = 0
    N = int(input())
    arr = list(map(int, input().split()))
    subSequence(arr, [], 0)
    print(output)


