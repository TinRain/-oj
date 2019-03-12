def insert_sort(lst):
    n = len(lst)
    if n == 1:
        return lst
    for i in range(1,n):
        # range(start, stop[, step])
        # step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
        for j in range(i, 0, -1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
            else:
                break
    return lst


while True:
    try:
        list_input = list(map(int, input().split()))
        N = list_input[0]
        array = list_input[1:]
        result = insert_sort(array)
        s = ''
        for i in range(N):
            s = s + str(result[i]) + ' '
        print(s.strip())
    except EOFError:
        break