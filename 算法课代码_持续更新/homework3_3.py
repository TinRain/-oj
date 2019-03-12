def shell_sort(array, gaps):
    n = len(array)
    for g in range(len(gaps)):
        gap = gaps[g]
        for j in range(gaps[g], n):
            i = j
            while(i-gap) >= 0:
                if array[i] < array[i-gap]:
                    array[i], array[i-gap] = array[i-gap], array[i]
                    i -= gap
                else:
                    break
    return array

N = int(input())
while N > 0:
    try:
        array = list(map(int, input().split()))
        gaps = list(map(int, input().split()))
        result = shell_sort(array, gaps)
        s = ''
        for i in range(len(array)):
            s = s + str(result[i]) + ' '
        print(s.strip())
        N -= 1
    except EOFError:
        break