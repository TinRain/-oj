def counting_sort(a, k):  # k = max(a)
    n = len(a)  # 计算a序列的长度
    b = [0 for i in range(n)]  # 设置输出序列并初始化为0
    c = [0 for i in range(k + 1)]  # 设置计数序列并初始化为0，
    for j in a:
        c[j] = c[j] + 1
    for i in range(1, len(c)):
        c[i] = c[i] + c[i-1]
    for j in a:
        b[c[j] - 1] = j
        c[j] = c[j] - 1
    return b

def get_max(array):
    max = array[0]
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
    return max


while True:
    try:
        list_input = list(map(int, input().split()))
        N = list_input[0]
        array = list_input[1:]
        result = counting_sort(array, get_max(array))
        s = ''
        for i in range(N):
            s = s + str(result[i]) + ' '
        print(s.strip())
    except EOFError:
        break