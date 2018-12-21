arr1 = input().strip().split()
arr1 = [int(i) for i in arr1]
arr2 = input().strip().split()
arr2 = [int(i) for i in arr2]
print(arr1)
print(arr2)
sum_arr1 = sum(arr1)
sum_arr2 = sum(arr2)
diff = sum_arr1 - sum_arr2
while abs(diff) > 0 :
    swap1,swap2 = 0,0
    swap_diff = 0
    for i in range (len(arr1)):
        for j in range(len(arr2)):
            if abs(diff- 2 * (arr1[i]-arr2[j]))<abs(diff- 2 * swap_diff):
                swap_diff = arr1[i]-arr2[j]
                swap1,swap2 = i,j
    if swap_diff==0:
        break
    arr1[swap1], arr2[swap2] = arr2[swap2], arr1[swap1]
    print(arr1)
    sum_arr1 = sum(arr1)
    sum_arr2 = sum(arr2)
    diff = sum_arr1-sum_arr2
print(diff)

