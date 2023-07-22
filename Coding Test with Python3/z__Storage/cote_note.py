from collections import deque

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(m, n)
print(matrix)

res = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

queue = deque([])
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])
print(queue)