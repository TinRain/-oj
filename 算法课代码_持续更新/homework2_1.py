def solveLCS(a, b):
    aLen = len(a)
    bLen = len(b)
    array = [[0 for i in range(aLen+1)] for j in range(bLen+1)]

    for i in range(1, aLen+1):
        for j in range(1, bLen+1):
            if a[i-1] == b[j-1]:
                array[i][j] = array[i-1][j-1]+1
            elif array[i][j-1] >= array[i-1][j]:
                array[i][j] = array[i][j-1]
            else:
                array[i][j] = array[i-1][j]
    printLCSImpl(array, a, b, aLen, bLen)
    return array[aLen][bLen]


def printLCSImpl(array, a, b, i, j):
    result = set()
    if i == 0 or j == 0:
        result = set()
        result.add(list())
        return result
    if a[i-1] == b[j-1]:
        result = printLCSImpl(array, a, b, i-1, j-1)
        for res in result:
            res.__add__(a[i-1])
    else:
        if array[i][j-1] > array[i-1][j]:
            set - printLCSImpl(array, a, b, i, j-1)
        elif array[i][j-1] == array[i-1][j]:
            set1 = printLCSImpl(array, a, b, i, j-1)
            set2 = printLCSImpl(array, a, b, i-1, j)
            set1.add(set2)
            result = set(set1)
        else:
            result = printLCSImpl(array, a, b, i-1, j)
    return result


a = '1A2BD3G4H56JK'
b = '23EFG4I5J6K7'
solveLCS(a, b)