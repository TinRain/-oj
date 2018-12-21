#将每一列的1逐行相加
#转化为求每一行最大直方图面积求解
#最大直方图面积即为所求
matrix = []
while True:
    try:
        line = input().strip().split()
        line = [int(i) for i in line]
        matrix.append(line)
    except Exception as e:
        break
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]==1:
            for m in range(j+1,len(matrix[0])):
                matrix[i][j] += matrix[i][m]

print(matrix)








