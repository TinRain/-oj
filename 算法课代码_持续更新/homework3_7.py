# 广度优先遍历图
def BFS(maze, start, visted):
    queue = []
    visited[start] = True




N = int(input())
while N > 0:
    try:
        line1 = input().split()
        nodes_num = int(line1[0])
        start_node = line1[1]
        nodes = input().split()
        num = 0
        visitedNum = False
        maze = [[num for i in range(nodes_num)] for i in range(nodes_num)]
        visited = [[visitedNum for i in range(nodes_num)] for i in range(nodes_num)]
        for i in range(nodes_num):
            temp = list(map(int, input().split()[1:]))
            maze[i] = temp
        BFS(maze,start_node,visited)
        N -= 1
    except EOFError:
        break