def bubble_sort(array):
    n = len(array)
    for j in range(n - 1):
        count = 0
        for i in range(0, n-1-j):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                count += 1
        if count == 0:
            break
    return array

while True:
    try:
        list_input = list(map(int, input().split()))
        N = list_input[0]
        array = list_input[1:]
        result = bubble_sort(array)
        s = ''
        for i in range(N):
            s = s + str(result[i]) + ' '
        print(s.strip())
    except EOFError:
        break