# 先将原序列排序，然后从排完序的数组中取出最小的，
# 它在原数组中的位置表示有多少比它大的数在它前面，
# 每取出一个在原数组中删除该元素，保证后面取出的元素在原数组中是最小的，
# 这样其位置才能表示有多少比它大的数在它前面，即逆序对数。

T = int(input())
def func(arr):
    count = 0
    copy = []
    for i in arr:
        copy.append(i)
    copy.sort()
    for i in range(len(copy)):
        count += arr.index(copy[i])
        arr.remove(copy[i])
    return count

while T > 0:
    N = int(input())
    list_input = list(map(int, input().split()))
    print(func(list_input))
    T -= 1